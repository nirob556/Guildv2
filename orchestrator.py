# -*- coding: utf-8 -*-
"""
LVL + GLD orchestrator.

Per account, after login:

    level >= lvl_min_level (default 3)            -> LVL   (original level-up logic)
    gld_min_level <= level < lvl_min_level        -> GLD   (solo matches, app.py behaviour)
                                                     until level >= lvl_min_level,
                                                     then hand over to LVL
    level <  gld_min_level                        -> LVL

The GLD phase is the old gld app.py engine (gld_engine.py) running in solo mode.
A monitor re-reads the account level every `level_poll_seconds`; the moment it
reaches the target the GLD tasks are cancelled and the caller (the per-account
worker loop in auth_layer) re-enters, sees level >= 3 and runs LVL.
"""
import asyncio
import re
import time
from typing import Dict, List, Optional, Tuple

import config
import dashboard_server as ds
from console import print  # quiet-mode aware print (see console.py)

bot_state = ds.bot_state

# Admin overrides: account_id -> "gld" | "lvl"  (absent = automatic)
FORCE: Dict[str, str] = {}
# (username, key) -> consecutive login failures
LOGIN_FAILS: Dict[Tuple[str, str], int] = {}

_login_sem: Optional[asyncio.Semaphore] = None
_login_sem_size = 0
_gld = None  # lazily imported gld_engine module


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def _log(msg: str, level: str = "info", uid: Optional[str] = None):
    try:
        bot_state.log(msg, level, uid)
    except Exception:
        pass
    print("[orch] " + msg, flush=True)


def login_semaphore() -> asyncio.Semaphore:
    """Semaphore sized from config (rebuilt if the admin changes the size)."""
    global _login_sem, _login_sem_size
    size = config.get()["max_parallel_logins"]
    if _login_sem is None or size != _login_sem_size:
        _login_sem = asyncio.Semaphore(size)
        _login_sem_size = size
    return _login_sem


def set_phase(acc_id: str, phase: str, note: str = ""):
    acc = bot_state.accounts.get(str(acc_id))
    if acc is not None:
        if acc.get("phase") != phase:
            acc["phase_since"] = time.time()
        acc["phase"] = phase
        acc["phase_note"] = note
        acc["target_level"] = config.get()["lvl_min_level"]
        acc["last_update"] = time.time()


def get_phase(acc_id: str) -> str:
    return (bot_state.accounts.get(str(acc_id)) or {}).get("phase", "PENDING")


def parse_bulk(text: str, max_lines: int = 0):
    """
    Parse a pasted block, one account per line.

      uid:password        -> guest account (split on the FIRST ':')
      <long token>        -> access token (no ':' and >= 16 chars)

    Returns (accounts, errors) where accounts is a list of
    {"type": "guest"|"token", ...} with duplicates inside the paste removed and
    errors is a list of {"line": n, "text": ..., "error": ...}.
    """
    accounts: List[dict] = []
    errors: List[dict] = []
    seen = set()
    n_lines = 0
    for i, raw in enumerate((text or "").splitlines(), start=1):
        line = raw.strip().strip("\ufeff")
        if not line or line.startswith("#"):
            continue
        n_lines += 1
        if max_lines and n_lines > max_lines:
            errors.append({"line": i, "text": _mask(line), "error": "Over bulk line limit (%d)" % max_lines})
            continue
        if ":" in line:
            uid, pw = line.split(":", 1)
            uid, pw = uid.strip(), pw.strip()
            if not uid or not pw:
                errors.append({"line": i, "text": _mask(line), "error": "Expected uid:password"})
                continue
            if not re.fullmatch(r"\d{5,20}", uid):
                errors.append({"line": i, "text": _mask(line), "error": "UID must be numeric"})
                continue
            key = "g:" + uid
            if key in seen:
                errors.append({"line": i, "text": _mask(line), "error": "Duplicate in paste"})
                continue
            seen.add(key)
            accounts.append({"type": "guest", "uid": uid, "password": pw, "line": i})
        elif len(line) >= 16 and re.fullmatch(r"[A-Za-z0-9._\-]+", line):
            key = "t:" + line[:20]
            if key in seen:
                errors.append({"line": i, "text": _mask(line), "error": "Duplicate in paste"})
                continue
            seen.add(key)
            accounts.append({"type": "token", "token": line, "line": i})
        else:
            errors.append({"line": i, "text": _mask(line), "error": "Expected uid:password"})
    return accounts, errors


def _mask(s: str) -> str:
    """Never echo a full password/token back to the browser."""
    if ":" in s:
        uid = s.split(":", 1)[0]
        return uid[:20] + ":***"
    return s[:6] + "***"


# ---------------------------------------------------------------------------
# GLD engine binding
# ---------------------------------------------------------------------------
def _engine(m):
    """Import gld_engine once and bind it to the shared LVL state/cache."""
    global _gld
    if _gld is None:
        import gld_engine as g
        # one shared token cache so a login done by LVL is reused by GLD and back
        g.cache_get = m.cache_get
        g.cache_set = m.cache_set
        g.cache_invalidate = m.cache_invalidate
        g.TEAM_MODE = False
        g.AUTO_JOIN_CLAN = False
        _gld = g
    return _gld


async def get_level(m, ad: dict, fails: Optional[dict] = None) -> Optional[int]:
    """Ask the game server for the account's current level (None on failure)."""
    try:
        res = await m.send_getlogin(
            ad["login_payload_data"], ad["server_url"], ad["token"], ad["release_version"]
        )
        if not res:
            return None
        res_proto, dict_res = res
        level = int(m.get_proto_field(dict_res, 6, 1))
        exp = int(m.get_proto_field(dict_res, 7, 0))
        acc_id = str(ad["account_id"])
        if exp > 0:
            bot_state.update_exp(acc_id, exp, level)
        acc = bot_state.accounts.get(acc_id)
        if acc is not None:
            acc["level"] = level
            acc["last_update"] = time.time()
        return level
    except asyncio.CancelledError:
        raise
    except Exception as e:
        _log("level check failed: %s: %s" % (type(e).__name__, e), "warning")
        return None


def decide_phase(level: int, force: Optional[str] = None) -> str:
    """Pure routing rule (kept separate so it is trivially testable)."""
    cfg = config.get()
    if force in ("gld", "lvl"):
        return force.upper()
    if cfg["gld_min_level"] <= level < cfg["lvl_min_level"]:
        return "GLD"
    return "LVL"


# ---------------------------------------------------------------------------
# GLD phase
# ---------------------------------------------------------------------------
async def run_gld_phase(m, ad: dict, label: str, cap: Optional[int] = None) -> bool:
    """
    Play solo matches with the GLD engine until the account reaches the target
    level. Returns True if the target was reached (or an admin override ended
    the phase), False if the session just dropped and should be re-established.
    """
    g = _engine(m)
    acc_id = str(ad["account_id"])
    region = ad.get("region", "BD")
    cfg = config.get()
    target = cfg["lvl_min_level"]
    if cap:
        target = min(target, cap)

    pkt_online = await g.build_tcp_startup_packet(
        ad["account_id"], ad["token"], ad["server_time"], ad["aes_ak"], ad["iv_i"],
        region=region, typ="OnLine")
    pkt_chat = await g.build_tcp_startup_packet(
        ad["account_id"], ad["token"], ad["server_time"], ad["aes_ak"], ad["iv_i"],
        region=region, typ="ChaT")

    set_phase(acc_id, "GLD", "solo matches until Lv.%d" % target)
    _log("[GLD] %s (%s) starting solo matches until Level %d" % (label, acc_id, target), "info", acc_id)

    info_task = asyncio.create_task(g.informational(
        ad["informational_addrs"], pkt_chat, ad["aes_ak"], ad["iv_i"],
        region=region, account_id=acc_id, account_data=ad))
    func_task = asyncio.create_task(g.functional_lone_wolf(
        ad["functional_addrs"], pkt_online, region, ad["client_version"],
        ad["aes_ak"], ad["iv_i"], account_id=acc_id, account_data=ad))

    reached = False
    bad_checks = 0
    try:
        while True:
            # sleep in small steps so a stop/force change is noticed quickly
            waited = 0.0
            poll = float(config.get()["level_poll_seconds"])
            while waited < poll and not func_task.done():
                await asyncio.sleep(1.0)
                waited += 1.0
                if FORCE.get(acc_id) == "lvl":
                    break
            if func_task.done():
                _log("[GLD] %s session ended early - reconnecting" % acc_id, "warning", acc_id)
                break
            if FORCE.get(acc_id) == "lvl":
                _log("[GLD] %s admin override -> LVL" % acc_id, "info", acc_id)
                reached = True
                break
            level = await get_level(m, ad)
            if level is None:
                bad_checks += 1
                if bad_checks >= 3:
                    _log("[GLD] %s level check failing - refreshing login" % acc_id, "warning", acc_id)
                    break
                continue
            bad_checks = 0
            target = config.get()["lvl_min_level"]
            if cap:
                target = min(target, cap)
            if level >= target:
                _log("[GLD] %s reached Level %d -> handing over to LVL" % (acc_id, level), "success", acc_id)
                reached = True
                break
    finally:
        for t in (func_task, info_task):
            if not t.done():
                t.cancel()
        for t in (func_task, info_task):
            try:
                await t
            except (asyncio.CancelledError, Exception):
                pass
        try:
            bot_state.close_writers_for_account(acc_id)
        except Exception:
            pass
    return reached


# ---------------------------------------------------------------------------
# entry point used by the per-account worker loops
# ---------------------------------------------------------------------------
async def _wait_for_cap(m, ad: dict, cap: int) -> int:
    """System 1 (Limited): poll the account level and return once it reaches `cap`."""
    while True:
        level = await get_level(m, ad)
        if level is not None and level >= cap:
            return level
        # check faster when the account is about to hit the cap, so it stops promptly
        near = level is not None and level >= cap - 1
        await asyncio.sleep(4.0 if near else min(10.0, float(config.get()["level_poll_seconds"])))


async def _run_lvl_limited(m, ad: dict, label: str, cap: int) -> Optional[str]:
    """Run the normal level-up worker, but stop it the moment the cap level is reached."""
    acc_id = str(ad["account_id"])
    work = asyncio.create_task(m.run_account_worker(ad, label))
    watch = asyncio.create_task(_wait_for_cap(m, ad, cap))
    reached = False
    try:
        await asyncio.wait({work, watch}, return_when=asyncio.FIRST_COMPLETED)
        reached = watch.done() and not watch.cancelled() and watch.exception() is None
    finally:
        for t in (work, watch):
            if not t.done():
                t.cancel()
        for t in (work, watch):
            try:
                await t
            except (asyncio.CancelledError, Exception):
                pass
        try:
            bot_state.close_writers_for_account(acc_id)
        except Exception:
            pass
    return "COMPLETED" if reached else None


async def run_account(m, ad: dict, label: str, mode: str = "unlimited") -> Optional[str]:
    """
    One routing pass for a logged-in account. Returns when the phase ends so
    the caller can loop (re-login from cache, then route again).

    mode "unlimited" (System 2): levels up with no limit (the original behaviour).
    mode "limited"   (System 1): same, but stops at config limited_max_level and
                     returns "COMPLETED" so the caller can retire the account.
    """
    acc_id = str(ad["account_id"])
    cap = int(config.get()["limited_max_level"]) if mode == "limited" else None
    level = await get_level(m, ad)
    if level is None:
        level = int(ad.get("level", 1) or 1)

    if cap and level >= cap:
        _log("[LIMITED] %s (%s) is Level %d (limit %d) -> completed" % (label, acc_id, level, cap), "success", acc_id)
        return "COMPLETED"

    phase = decide_phase(level, FORCE.get(acc_id))

    if phase == "GLD":
        reached = await run_gld_phase(m, ad, label, cap=cap)
        if reached:
            # drop the cached (stale-level) login so the next pass starts clean
            set_phase(acc_id, "LVL", "reached target level")
        return None

    set_phase(acc_id, "LVL", "level-up" if not cap else "level-up (stops at Lv.%d)" % cap)
    _log("[LVL] %s (%s) level-up running at Level %d" % (label, acc_id, level), "info", acc_id)
    if cap:
        return await _run_lvl_limited(m, ad, label, cap)
    await m.run_account_worker(ad, label)
    return None
