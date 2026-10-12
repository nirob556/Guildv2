# -*- coding: utf-8 -*-

import os
import json
import time
import asyncio
import hashlib
import secrets
import contextvars
import csv
import io
from typing import Dict, Any

from aiohttp import web

import dashboard_server as ds
from console import print  # quiet-mode aware print (see console.py)
import config as cfgmod
import orchestrator as orch

bot_state = ds.bot_state

from templates import (
    LOGIN_HTML,
    PLANS_HTML,
    DASHBOARD_HTML,
    EXPIRED_HTML,
    ADMIN_LOGIN_HTML,
    ADMIN_PANEL_HTML,
    HOME_HTML,
)

ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "nirob")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "55")
ADMIN_PATH = "/admin/nirob/levelup/adm-dash"

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
SESSIONS_FILE = os.path.join(DATA_DIR, "sessions.json")

SESSION_COOKIE = "vxl_session"
SESSION_TTL = 7 * 24 * 3600

USER_WORKERS: Dict[str, Dict[str, asyncio.Task]] = {}

# System 1 (Limited): accounts that reached the limit level. username -> key -> info.
# Kept in memory as well as in users.json so a stale write can never "un-complete" one.
COMPLETED_INFO: Dict[str, Dict[str, dict]] = {}
USER_PAUSED: Dict[str, set] = {}
USER_DELETED: Dict[str, set] = {}
_LAST_SYNC: Dict[str, float] = {}
_CURRENT_OWNER = contextvars.ContextVar("current_owner", default=None)


async def sync_user_accounts_to_disk(username):
    """Persist live bot_state account data into users.json so logout/login doesn't lose progress."""
    try:
        users = load_users()
        u = users.get(username)
        if not u:
            return
        accounts = u.get("accounts", [])
        if not accounts:
            return
        changed = False
        for saved in accounts:
            saved_key = str(saved.get("uid")) if saved.get("type") == "guest" else str(saved.get("token", ""))[:20]
            _done = COMPLETED_INFO.get(username, {}).get(saved_key)
            if _done and not saved.get("completed"):
                saved.update(_done)
                changed = True
            if saved.get("completed"):
                continue
            live = None
            for uid, acc in ds.bot_state.accounts.items():
                if acc.get("_owner") != username:
                    continue
                if str(uid) == saved_key:
                    live = acc
                    break
                cred = ds.bot_state.account_credentials.get(str(uid))
                if cred:
                    if saved.get("type") == "guest" and str(cred.get("auth_uid")) == saved_key:
                        live = acc
                        break
                    if saved.get("type") == "token" and str(cred.get("auth_token", ""))[:20] == saved_key:
                        live = acc
                        break
            if not live:
                continue
            if saved.get("initial_exp") is None and live.get("initial_exp") is not None:
                saved["initial_exp"] = live["initial_exp"]
                changed = True
            new_last_exp = live.get("current_exp")
            if new_last_exp is not None and saved.get("last_exp") != new_last_exp:
                saved["last_exp"] = new_last_exp
                changed = True
            new_level = live.get("level")
            if new_level is not None and saved.get("last_level") != new_level:
                saved["last_level"] = new_level
                changed = True
            new_nick = live.get("nickname")
            if new_nick and saved.get("last_nickname") != new_nick:
                saved["last_nickname"] = new_nick
                changed = True
            new_region = live.get("region")
            if new_region and saved.get("last_region") != new_region:
                saved["last_region"] = new_region
                changed = True
            new_gained = live.get("gained_exp")
            if new_gained is not None and saved.get("gained_exp") != new_gained:
                saved["gained_exp"] = new_gained
                changed = True
            new_played = live.get("matches_played")
            if new_played is not None and saved.get("matches_played") != new_played:
                saved["matches_played"] = new_played
                changed = True
            if live.get("created_at") and saved.get("created_at") != live.get("created_at"):
                saved["created_at"] = live.get("created_at")
                changed = True
            saved["last_update"] = time.time()
            changed = True
        if changed:
            save_users(users)
    except Exception as e:
        print(f"[auth] sync_user_accounts_to_disk error for {username}: {e}", flush=True)


def _ensure():
    os.makedirs(DATA_DIR, exist_ok=True)


def _read(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def _write(path, data):
    _ensure()
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, path)


def load_users():
    return _read(USERS_FILE, {})


def save_users(u):
    _write(USERS_FILE, u)


def load_sessions():
    return _read(SESSIONS_FILE, {})


def save_sessions(s):
    _write(SESSIONS_FILE, s)


def hash_pw(pw, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)
    h = hashlib.pbkdf2_hmac("sha256", pw.encode(), salt.encode(), 120000)
    return h.hex(), salt


def verify_pw(pw, h, salt):
    hh, _ = hash_pw(pw, salt)
    return secrets.compare_digest(hh, h)


def create_session(username, is_admin=False):
    token = secrets.token_urlsafe(32)
    s = load_sessions()
    now = time.time()
    s[token] = {"username": username, "is_admin": is_admin, "created_at": now, "expires_at": now + SESSION_TTL}
    now_ts = time.time()
    s = {k: v for k, v in s.items() if v.get("expires_at", 0) > now_ts}
    save_sessions(s)
    return token


def get_session(token):
    if not token:
        return None
    s = load_sessions()
    v = s.get(token)
    if not v:
        return None
    if time.time() > v.get("expires_at", 0):
        s.pop(token, None)
        save_sessions(s)
        return None
    return v


def destroy_session(token):
    s = load_sessions()
    s.pop(token, None)
    save_sessions(s)


def cur_user(req):
    return get_session(req.cookies.get(SESSION_COOKIE))


def cur_admin(req):
    s = cur_user(req)
    if s and s.get("is_admin"):
        return s
    return None


def _set_ck(resp, token):
    resp.set_cookie(SESSION_COOKIE, token, max_age=SESSION_TTL, httponly=True, samesite="Lax", path="/")


def _clr_ck(resp):
    resp.del_cookie(SESSION_COOKIE, path="/")


_orig_register = ds.BotState.register_account


def _patched_register(self, uid, nickname, region, level, exp, likes=0):
    uid_str = str(uid)
    owner = _CURRENT_OWNER.get()

    if owner is None:
        try:
            for un, udata in load_users().items():
                for acc in udata.get("accounts", []):
                    if acc.get("type") == "guest":
                        acc_uid = str(acc.get("uid", ""))
                    else:
                        acc_uid = str(acc.get("token", ""))[:20]
                    if acc_uid == uid_str:
                        owner = un
                        break
                if owner:
                    break
        except Exception:
            pass

    if owner:
        deleted = USER_DELETED.get(owner, set())
        paused = USER_PAUSED.get(owner, set())
        if uid_str in deleted or uid_str in paused:
            return

    saved_initial = None
    saved_matches = 0
    saved_created = None
    if owner:
        try:
            users = load_users()
            u = users.get(owner)
            if u:
                for saved in u.get("accounts", []):
                    saved_key = str(saved.get("uid")) if saved.get("type") == "guest" else str(saved.get("token", ""))[:20]
                    if saved_key == uid_str:
                        saved_initial = saved.get("initial_exp")
                        saved_matches = saved.get("matches_played", 0)
                        saved_created = saved.get("created_at")
                        break
        except Exception:
            pass

    is_new = uid_str not in self.accounts
    _orig_register(self, uid, nickname, region, level, exp, likes)
    acc = self.accounts.get(uid_str)
    if not acc:
        return

    if saved_initial is not None:
        acc["initial_exp"] = saved_initial
        acc["gained_exp"] = max(0, exp - saved_initial)
    if saved_matches > 0:
        acc["matches_played"] = saved_matches
    if saved_created:
        acc["created_at"] = saved_created

    if owner:
        acc["_owner"] = owner

    if is_new and "created_at" not in acc:
        acc["created_at"] = time.time()

    acc["last_update"] = time.time()

    if owner:
        try:
            users = load_users()
            u = users.get(owner)
            if u:
                for saved in u.get("accounts", []):
                    saved_key = str(saved.get("uid")) if saved.get("type") == "guest" else str(saved.get("token", ""))[:20]
                    if saved_key == uid_str:
                        if saved.get("initial_exp") is None:
                            saved["initial_exp"] = acc["initial_exp"]
                        saved["last_exp"] = acc["current_exp"]
                        saved["last_level"] = acc["level"]
                        saved["last_nickname"] = acc["nickname"]
                        saved["last_region"] = acc["region"]
                        saved["gained_exp"] = acc["gained_exp"]
                        saved["matches_played"] = acc["matches_played"]
                        saved["created_at"] = acc.get("created_at")
                        saved["last_update"] = time.time()
                        break
                save_users(users)
        except Exception:
            pass


ds.BotState.register_account = _patched_register


def _is_completed(username, acc):
    """True if this saved account record has finished System 1 (Limited)."""
    return bool(acc.get("completed")) or _key_of(acc) in COMPLETED_INFO.get(username, {})


def _saved_mode(username, key):
    """'limited' or 'unlimited' (default) for a saved account key."""
    try:
        u = load_users().get(username) or {}
        for a in u.get("accounts", []):
            if _key_of(a) == str(key):
                return "limited" if a.get("mode") == "limited" else "unlimited"
    except Exception:
        pass
    return "unlimited"


def _mark_completed(username, key, ad):
    """Retire a Limited account that reached the limit: persist it and drop its live state."""
    key = str(key)
    acc_id = str(ad.get("account_id", ""))
    live = ds.bot_state.accounts.get(acc_id) or {}
    try:
        level = int(live.get("level") or ad.get("level") or 0)
    except Exception:
        level = 0
    info = {"completed": True, "completed_at": time.time(), "final_level": level}
    nick = live.get("nickname") or ad.get("nickname")
    if nick:
        info["last_nickname"] = str(nick)
    COMPLETED_INFO.setdefault(username, {})[key] = info
    try:
        users = load_users()
        u = users.get(username)
        if u:
            for a in u.get("accounts", []):
                if _key_of(a) == key:
                    a.update(info)
            save_users(users)
    except Exception as e:
        print(f"[auth] could not persist completed {key}: {e}", flush=True)
    # remove the finished account from the live list / caches
    for k in {acc_id, key, key[:20]}:
        if not k:
            continue
        ds.bot_state.accounts.pop(k, None)
        ds.bot_state.account_credentials.pop(k, None)
        try:
            ds.cache_invalidate(k)
        except Exception:
            pass
    try:
        ds.bot_state.recalc_totals()
    except Exception:
        pass


def _completed_rows(username, u, with_password=False):
    """Completed (Limited) accounts of one user, oldest first."""
    info = COMPLETED_INFO.get(username, {})
    rows = []
    for a in u.get("accounts", []):
        key = _key_of(a)
        if not key or not (a.get("completed") or key in info):
            continue
        meta = dict(info.get(key, {}))
        for f in ("completed_at", "final_level", "last_nickname"):
            if a.get(f) is not None:
                meta[f] = a[f]
        row = {
            "uid": key,
            "type": a.get("type"),
            "level": int(meta.get("final_level") or a.get("last_level") or 0),
            "nickname": meta.get("last_nickname") or a.get("last_nickname") or "",
            "completed_at": meta.get("completed_at") or 0,
        }
        if with_password:
            row["password"] = a.get("password") if a.get("type") == "guest" else None
        rows.append(row)
    rows.sort(key=lambda r: r["completed_at"])
    return rows


async def stop_user_workers(username):
    workers = USER_WORKERS.pop(username, {})
    tasks = list(workers.values())
    for t in tasks:
        if not t.done():
            t.cancel()
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)

    for key in list(bot_state.account_workers.keys()):
        if str(key).startswith(username + "::"):
            t = bot_state.account_workers.pop(key, None)
            if t and not t.done():
                t.cancel()
            if t:
                try:
                    await asyncio.wait_for(t, timeout=3)
                except Exception:
                    pass

    await asyncio.sleep(0.2)


async def start_user_workers(username):
    users = load_users()
    u = users.get(username)
    if not u:
        return
    if time.time() >= u.get("expires_at", 0):
        return

    if username not in USER_WORKERS:
        USER_WORKERS[username] = {}
    if username not in USER_PAUSED:
        USER_PAUSED[username] = set()
    if username not in USER_DELETED:
        USER_DELETED[username] = set()

    workers = USER_WORKERS[username]
    paused = USER_PAUSED[username]
    deleted = USER_DELETED[username]

    for acc in u.get("accounts", []):
        key = acc.get("uid") if acc.get("type") == "guest" else acc.get("token", "")[:20]
        if not key:
            continue
        if key in paused or key in deleted:
            continue
        if _is_completed(username, acc):
            continue
        if key in workers and not workers[key].done():
            continue
        if acc.get("type") == "guest":
            t = asyncio.create_task(_guest_worker(username, acc["uid"], acc["password"]))
        else:
            t = asyncio.create_task(_token_worker(username, acc["token"]))
        workers[key] = t
        bot_state.account_workers[username + "::" + key] = t


async def _guest_worker(username, uid, password):
    try:
        import main as m
    except Exception as e:
        print(f"[auth] Cannot import main: {e}", flush=True)
        return
    while True:
        try:
            if uid in USER_DELETED.get(username, set()):
                print(f"[auth] Guest worker {uid} deleted -> exit", flush=True)
                break
            if uid in USER_PAUSED.get(username, set()):
                print(f"[auth] Guest worker {uid} paused -> exit", flush=True)
                break
            cv = _CURRENT_OWNER.set(username)
            try:
                print(f"[auth] Guest login starting user={username} uid={uid}", flush=True)
                async with orch.login_semaphore():
                    ad = await m.process_account_uid_pass(uid, password)
                if not ad:
                    fails = orch.LOGIN_FAILS.get((username, str(uid)), 0) + 1
                    orch.LOGIN_FAILS[(username, str(uid))] = fails
                    wait = 15 if fails < cfgmod.get()["login_fail_limit"] else 60
                    print(f"[auth] Guest login FAILED user={username} uid={uid} (#{fails}) -> retry in {wait}s", flush=True)
                    await asyncio.sleep(wait)
                    continue
                orch.LOGIN_FAILS.pop((username, str(uid)), None)

                acc_id = str(ad.get("account_id", ""))
                if uid in USER_DELETED.get(username, set()) or acc_id in USER_DELETED.get(username, set()):
                    print(f"[auth] Guest worker {uid}/{acc_id} deleted after login -> exit", flush=True)
                    break
                if uid in USER_PAUSED.get(username, set()) or acc_id in USER_PAUSED.get(username, set()):
                    print(f"[auth] Guest worker {uid}/{acc_id} paused after login -> exit", flush=True)
                    break

                print(f"[auth] Guest login OK user={username} uid={uid} acc_id={acc_id}", flush=True)
                result = await orch.run_account(m, ad, uid, mode=_saved_mode(username, uid))
                if result == "COMPLETED":
                    _mark_completed(username, uid, ad)
                    print(f"[auth] Guest {uid} reached the limit level -> completed, worker done", flush=True)
                    break

                if uid in USER_DELETED.get(username, set()) or acc_id in USER_DELETED.get(username, set()):
                    print(f"[auth] Guest worker {uid}/{acc_id} deleted -> exit", flush=True)
                    break

                print(f"[auth] Guest worker exited user={username} uid={uid} -> restart in 3s", flush=True)
                await asyncio.sleep(3)
            finally:
                _CURRENT_OWNER.reset(cv)
        except asyncio.CancelledError:
            print(f"[auth] Guest worker cancelled user={username} uid={uid}", flush=True)
            break
        except Exception as e:
            print(f"[auth] Guest worker error user={username} uid={uid}: {type(e).__name__}: {e}", flush=True)
            await asyncio.sleep(10)


async def _token_worker(username, token):
    try:
        import main as m
    except Exception as e:
        print(f"[auth] Cannot import main: {e}", flush=True)
        return
    while True:
        try:
            key = token[:20]
            if key in USER_DELETED.get(username, set()):
                print(f"[auth] Token worker {key} deleted -> exit", flush=True)
                break
            if key in USER_PAUSED.get(username, set()):
                print(f"[auth] Token worker {key} paused -> exit", flush=True)
                break
            cv = _CURRENT_OWNER.set(username)
            try:
                print(f"[auth] Token login starting user={username} token={key}...", flush=True)
                async with orch.login_semaphore():
                    ad = await m.process_account_token(token)
                if not ad:
                    fails = orch.LOGIN_FAILS.get((username, key), 0) + 1
                    orch.LOGIN_FAILS[(username, key)] = fails
                    wait = 15 if fails < cfgmod.get()["login_fail_limit"] else 60
                    print(f"[auth] Token login FAILED user={username} (#{fails}) -> retry in {wait}s", flush=True)
                    await asyncio.sleep(wait)
                    continue
                orch.LOGIN_FAILS.pop((username, key), None)

                acc_id = str(ad.get("account_id", ""))
                if key in USER_DELETED.get(username, set()) or acc_id in USER_DELETED.get(username, set()):
                    print(f"[auth] Token worker {key}/{acc_id} deleted after login -> exit", flush=True)
                    break
                if key in USER_PAUSED.get(username, set()) or acc_id in USER_PAUSED.get(username, set()):
                    print(f"[auth] Token worker {key}/{acc_id} paused after login -> exit", flush=True)
                    break

                print(f"[auth] Token login OK user={username} acc_id={acc_id}", flush=True)
                result = await orch.run_account(m, ad, acc_id, mode=_saved_mode(username, key))
                if result == "COMPLETED":
                    _mark_completed(username, key, ad)
                    print(f"[auth] Token {key} reached the limit level -> completed, worker done", flush=True)
                    break

                if key in USER_DELETED.get(username, set()) or acc_id in USER_DELETED.get(username, set()):
                    print(f"[auth] Token worker {key}/{acc_id} deleted -> exit", flush=True)
                    break

                print(f"[auth] Token worker exited user={username} -> restart in 3s", flush=True)
                await asyncio.sleep(3)
            finally:
                _CURRENT_OWNER.reset(cv)
        except asyncio.CancelledError:
            print(f"[auth] Token worker cancelled user={username}", flush=True)
            break
        except Exception as e:
            print(f"[auth] Token worker error user={username}: {type(e).__name__}: {e}", flush=True)
            await asyncio.sleep(10)


async def h_root(req):
    return web.Response(text=HOME_HTML, content_type="text/html")


async def h_login_get(req):
    s = cur_user(req)
    if s and not s.get("is_admin"):
        raise web.HTTPFound("/dashboard")
    return web.Response(text=LOGIN_HTML, content_type="text/html")


async def h_login_post(req):
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    u = (d.get("username") or "").strip()
    p = d.get("password") or ""
    if not u or not p:
        return web.json_response({"status": "error", "error": "Missing Credentials"})
    users = load_users()
    x = users.get(u)
    if not x:
        print(f"[auth] Login FAILED (no user) username={u}", flush=True)
        return web.json_response({"status": "error", "error": "Invalid Credentials"})
    if not verify_pw(p, x.get("password_hash", ""), x.get("salt", "")):
        print(f"[auth] Login FAILED (bad pass) username={u}", flush=True)
        return web.json_response({"status": "error", "error": "Invalid Credentials"})
    token = create_session(u, False)
    print(f"[auth] Login OK user={u}", flush=True)
    resp = web.json_response({"status": "ok", "redirect": "/dashboard"})
    _set_ck(resp, token)
    if time.time() < x.get("expires_at", 0):
        asyncio.create_task(start_user_workers(u))
    return resp


async def h_signup(req):
    raise web.HTTPFound("/plans")


async def h_plans(req):
    s = cur_user(req)
    un = s["username"] if s else "{{USERNAME}}"
    return web.Response(text=PLANS_HTML.replace("{{USERNAME}}", un), content_type="text/html")


async def h_logout(req):
    token = req.cookies.get(SESSION_COOKIE)
    if token:
        s = get_session(token)
        if s and not s.get("is_admin"):
            print(f"[auth] Logout user={s['username']} (syncing state, workers kept alive)", flush=True)
            await sync_user_accounts_to_disk(s["username"])
        destroy_session(token)
    r = web.HTTPFound("/login")
    _clr_ck(r)
    raise r


async def h_dash(req):
    s = cur_user(req)
    if not s or s.get("is_admin"):
        raise web.HTTPFound("/login")
    users = load_users()
    x = users.get(s["username"])
    if not x:
        raise web.HTTPFound("/logout")
    if time.time() >= x.get("expires_at", 0):
        raise web.HTTPFound("/expired")
    return web.Response(text=DASHBOARD_HTML.replace("{{USERNAME}}", s["username"]), content_type="text/html")


async def h_expired(req):
    s = cur_user(req)
    if not s or s.get("is_admin"):
        raise web.HTTPFound("/login")
    return web.Response(text=EXPIRED_HTML, content_type="text/html")


async def h_stats(req):
    s = cur_user(req)
    if not s or s.get("is_admin"):
        return web.json_response({"error": "unauthorized"}, status=401)
    un = s["username"]
    users = load_users()
    u = users.get(un, {})
    now = time.time()
    exp_at = u.get("expires_at", 0)
    expired = now >= exp_at
    left = max(0, int(exp_at - now))
    paused = USER_PAUSED.get(un, set())
    deleted = USER_DELETED.get(un, set())
    completed_keys = {r["uid"] for r in _completed_rows(un, u)}
    saved_modes = {_key_of(_a): ("limited" if _a.get("mode") == "limited" else "unlimited")
                   for _a in u.get("accounts", []) if _key_of(_a)}

    def _mode_for(live_uid):
        m_ = saved_modes.get(str(live_uid))
        if m_:
            return m_
        cred_ = ds.bot_state.account_credentials.get(str(live_uid)) or {}
        for k_ in (cred_.get("auth_uid"), str(cred_["auth_token"])[:20] if cred_.get("auth_token") else None):
            if k_ and saved_modes.get(str(k_)):
                return saved_modes[str(k_)]
        return "unlimited"

    # Periodic lightweight sync of live bot_state → users.json (every ~30s)
    last_sync = _LAST_SYNC.get(un, 0)
    if now - last_sync > 30:
        _LAST_SYNC[un] = now
        asyncio.create_task(sync_user_accounts_to_disk(un))

    if not expired and un not in USER_WORKERS:
        asyncio.create_task(start_user_workers(un))

    out = []
    seen_keys = set()

    for uid, a in list(ds.bot_state.accounts.items()):
        if a.get("_owner") != un:
            continue
        if uid in deleted:
            continue
        if uid in completed_keys:
            continue
        is_paused = uid in paused
        status = "PAUSED" if is_paused else a.get("status", "LIVE")
        out.append({
            "uid": uid,
            "nickname": a.get("nickname", "?"),
            "region": a.get("region", "IND"),
            "level": a.get("level", 1),
            "initial_exp": a.get("initial_exp", 0),
            "current_exp": a.get("current_exp", 0),
            "gained_exp": a.get("gained_exp", 0),
            "matches_played": a.get("matches_played", 0),
            "status": status,
            "mode": _mode_for(uid),
            "phase": a.get("phase", "PENDING"),
            "phase_note": a.get("phase_note", ""),
            "active_matches": a.get("active_matches", 0),
            "created_at": a.get("created_at"),
            "last_update": a.get("last_update"),
        })
        seen_keys.add(str(uid))
        # Also mark the login key (guest UID / token prefix) of this live account,
        # so its saved placeholder row isn't listed a second time.
        try:
            _cred = ds.bot_state.account_credentials.get(str(uid)) or {}
            if _cred.get("auth_uid"):
                seen_keys.add(str(_cred["auth_uid"]))
            if _cred.get("auth_token"):
                seen_keys.add(str(_cred["auth_token"])[:20])
        except Exception:
            pass

    for acc in u.get("accounts", []):
        acc_type = acc.get("type")
        key = acc.get("uid") if acc_type == "guest" else acc.get("token", "")[:20]
        if not key:
            continue
        key_str = str(key)
        if key_str in seen_keys or key_str in deleted or key_str in completed_keys:
            continue
        is_paused = key_str in paused

        saved_exp = acc.get("last_exp", 0)
        saved_level = acc.get("last_level", 1)
        saved_nickname = acc.get("last_nickname", "Loading...")
        saved_region = acc.get("last_region", "IND")
        saved_initial = acc.get("initial_exp", saved_exp)
        saved_gained = acc.get("gained_exp", max(0, saved_exp - saved_initial))
        saved_played = acc.get("matches_played", 0)
        saved_created = acc.get("created_at")
        saved_updated = acc.get("last_update")

        out.append({
            "uid": key_str,
            "nickname": saved_nickname,
            "region": saved_region,
            "level": saved_level,
            "initial_exp": saved_initial,
            "current_exp": saved_exp,
            "gained_exp": saved_gained,
            "matches_played": saved_played,
            "status": "PAUSED" if is_paused else (
                "LOGIN FAILED" if orch.LOGIN_FAILS.get((un, key_str), 0) >= cfgmod.get()["login_fail_limit"]
                else "CONNECTING"),
            "mode": "limited" if acc.get("mode") == "limited" else "unlimited",
            "phase": "PENDING",
            "phase_note": "",
            "active_matches": 0,
            "created_at": saved_created,
            "last_update": saved_updated,
        })

    out.sort(key=lambda x: x.get("gained_exp", 0), reverse=True)
    _lim = cfgmod.slot_limit(u)
    _cfg = cfgmod.get()
    return web.json_response({
        "username": un,
        "slots": -1 if _lim is None else _lim,
        "unlimited": _lim is None,
        "gld_min_level": _cfg["gld_min_level"],
        "lvl_min_level": _cfg["lvl_min_level"],
        "limited_max_level": _cfg["limited_max_level"],
        "completed": _completed_rows(un, u),
        "seconds_left": left,
        "expired": expired,
        "accounts": out,
    })


async def h_acc_check(req):
    s = cur_user(req)
    if not s or s.get("is_admin"):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    un = s["username"]
    users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Missing"})
    if time.time() >= u.get("expires_at", 0):
        return web.json_response({"status": "error", "error": "Plan Expired"})
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})

    accs = u.setdefault("accounts", [])
    slots = u.get("slots", 0)
    un_deleted = USER_DELETED.get(un, set())
    active_accs = []
    for a in accs:
        key = str(a.get("uid")) if a.get("type") == "guest" else str(a.get("token", ""))[:20]
        if key and key not in un_deleted and not _is_completed(un, a):
            active_accs.append(a)
    if cfgmod.limit_reached(u, len(active_accs)):
        return web.json_response({"status": "error", "error": "No Free Slots"})

    try:
        import main as m
    except Exception:
        return web.json_response({"status": "error", "error": "Main module unavailable"})

    acc_data = None
    if "uid" in d and "password" in d:
        uid = str(d["uid"]).strip()
        pw = str(d["password"]).strip()
        if not uid or not pw:
            return web.json_response({"status": "error", "error": "UID And Password Required"})
        for a in accs:
            if a.get("type") == "guest" and str(a.get("uid")) == uid:
                return web.json_response({"status": "error", "error": "UID Already Added"})
        cached = m.cache_get(uid)
        if cached and cached.get("level"):
            acc_data = cached
        else:
            try:
                acc_data = await m.process_account_uid_pass(uid, pw)
            except Exception:
                return web.json_response({"status": "error", "error": "Login Failed - Invalid UID/Password"})
    elif "token" in d:
        tk = str(d["token"]).strip()
        if not tk:
            return web.json_response({"status": "error", "error": "Token Required"})
        for a in accs:
            if a.get("type") == "token" and a.get("token") == tk:
                return web.json_response({"status": "error", "error": "Token Already Added"})
        cache_key = f"tok_{tk[:20]}"
        cached = m.cache_get(cache_key)
        if cached and cached.get("level"):
            acc_data = cached
        else:
            try:
                acc_data = await m.process_account_token(tk)
            except Exception:
                return web.json_response({"status": "error", "error": "Login Failed - Invalid Token"})
    else:
        return web.json_response({"status": "error", "error": "Invalid Payload"})

    if not acc_data:
        return web.json_response({"status": "error", "error": "Login Failed"})

    return web.json_response({
        "status": "ok",
        "level": int(acc_data.get("level", 1) or 1),
        "region": str(acc_data.get("region", "") or "").upper(),
        "nickname": str(acc_data.get("nickname", "") or ""),
        "account_id": str(acc_data.get("account_id", "")),
        "lvl_min_level": cfgmod.get()["lvl_min_level"],
        "gld_min_level": cfgmod.get()["gld_min_level"],
        "limited_max_level": cfgmod.get()["limited_max_level"],
    })


async def h_acc_add(req):
    s = cur_user(req)
    if not s or s.get("is_admin"):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    un = s["username"]
    users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Missing"})
    if time.time() >= u.get("expires_at", 0):
        return web.json_response({"status": "error", "error": "Plan Expired"})
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    accs = u.setdefault("accounts", [])
    slots = u.get("slots", 0)
    mode = "limited" if str(d.get("mode", "")).lower() == "limited" else "unlimited"

    un_deleted = USER_DELETED.get(un, set())
    active_accs = []
    for a in accs:
        key = str(a.get("uid")) if a.get("type") == "guest" else str(a.get("token", ""))[:20]
        if key and key not in un_deleted and not _is_completed(un, a):
            active_accs.append(a)

    if cfgmod.limit_reached(u, len(active_accs)):
        return web.json_response({"status": "error", "error": "No Free Slots"})

    if un not in USER_DELETED:
        USER_DELETED[un] = set()
    if un not in USER_PAUSED:
        USER_PAUSED[un] = set()

    def _clear_all_keys_for(uid_or_token):
        keys = {str(uid_or_token)}
        keys.add(str(uid_or_token)[:20])
        try:
            cred = ds.bot_state.account_credentials.get(str(uid_or_token))
            if cred:
                if cred.get("account_id"):
                    keys.add(str(cred.get("account_id")))
                if cred.get("auth_uid"):
                    keys.add(str(cred.get("auth_uid")))
                if cred.get("auth_token"):
                    keys.add(str(cred.get("auth_token"))[:20])
        except Exception:
            pass
        try:
            for k, cred in list(ds.bot_state.account_credentials.items()):
                if str(cred.get("auth_uid", "")) == str(uid_or_token) or \
                   str(cred.get("account_id", "")) == str(uid_or_token) or \
                   str(cred.get("auth_token", ""))[:20] == str(uid_or_token)[:20]:
                    if cred.get("account_id"):
                        keys.add(str(cred.get("account_id")))
                    if cred.get("auth_uid"):
                        keys.add(str(cred.get("auth_uid")))
                    if cred.get("auth_token"):
                        keys.add(str(cred.get("auth_token"))[:20])
        except Exception:
            pass
        for k in keys:
            USER_DELETED[un].discard(k)
            USER_PAUSED[un].discard(k)
            try:
                ds.cache_invalidate(k)
            except Exception:
                pass
        return keys

    if "uid" in d and "password" in d:
        uid = str(d["uid"]).strip()
        pw = str(d["password"]).strip()
        if not uid or not pw:
            return web.json_response({"status": "error", "error": "UID And Password Required"})
        for a in accs:
            if a.get("type") == "guest" and str(a.get("uid")) == uid:
                return web.json_response({"status": "error", "error": "UID Already Added"})
        cleared = _clear_all_keys_for(uid)
        accs.append({"type": "guest", "uid": uid, "password": pw, "created_at": time.time(), "mode": mode})
        print(f"[api] Account add user={un} uid={uid} (guest) cleared={cleared}", flush=True)
    elif "token" in d:
        tk = str(d["token"]).strip()
        if not tk:
            return web.json_response({"status": "error", "error": "Token Required"})
        for a in accs:
            if a.get("type") == "token" and a.get("token") == tk:
                return web.json_response({"status": "error", "error": "Token Already Added"})
        cleared = _clear_all_keys_for(tk)
        accs.append({"type": "token", "token": tk, "created_at": time.time(), "mode": mode})
        print(f"[api] Account add user={un} token={tk[:20]}... cleared={cleared}", flush=True)
    else:
        return web.json_response({"status": "error", "error": "Invalid Payload"})

    u["accounts"] = accs
    users[un] = u
    save_users(users)
    asyncio.create_task(start_user_workers(un))
    return web.json_response({"status": "ok"})


async def h_acc_del(req):
    s = cur_user(req)
    if not s or s.get("is_admin"):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    un = s["username"]
    users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Missing"})
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    uid = str(d.get("uid", "")).strip()
    if not uid:
        return web.json_response({"status": "error", "error": "Missing UID"})

    print(f"[api] Account delete user={un} uid={uid}", flush=True)

    if un not in USER_DELETED:
        USER_DELETED[un] = set()
    if un not in USER_PAUSED:
        USER_PAUSED[un] = set()

    real_uid = None
    real_token_prefix = None
    try:
        cred = ds.bot_state.account_credentials.get(uid)
        if cred:
            if cred.get("auth_uid"):
                real_uid = str(cred.get("auth_uid"))
            if cred.get("auth_token"):
                real_token_prefix = str(cred.get("auth_token"))[:20]
    except Exception:
        pass

    if real_uid is None and real_token_prefix is None:
        try:
            for k, cred in list(ds.bot_state.account_credentials.items()):
                if str(cred.get("account_id", "")) == uid:
                    if cred.get("auth_uid"):
                        real_uid = str(cred.get("auth_uid"))
                        break
                    if cred.get("auth_token"):
                        real_token_prefix = str(cred.get("auth_token"))[:20]
                        break
        except Exception:
            pass

    USER_DELETED[un].add(uid)
    if real_uid:
        USER_DELETED[un].add(real_uid)
    if real_token_prefix:
        USER_DELETED[un].add(real_token_prefix)
    USER_PAUSED[un].discard(uid)
    if real_uid:
        USER_PAUSED[un].discard(real_uid)
    if real_token_prefix:
        USER_PAUSED[un].discard(real_token_prefix)

    keys_to_kill = [uid]
    if real_uid:
        keys_to_kill.append(real_uid)
    if real_token_prefix:
        keys_to_kill.append(real_token_prefix)

    workers = USER_WORKERS.get(un, {})
    for k in keys_to_kill:
        t = workers.pop(k, None)
        if t and not t.done():
            t.cancel()
            try:
                await asyncio.wait_for(t, timeout=5)
            except (asyncio.CancelledError, asyncio.TimeoutError, Exception):
                pass

    for key in list(bot_state.account_workers.keys()):
        if str(key).startswith(un + "::"):
            suffix = str(key).split("::", 1)[1]
            if suffix in keys_to_kill:
                t = bot_state.account_workers.pop(key, None)
                if t and not t.done():
                    t.cancel()
                    try:
                        await asyncio.wait_for(t, timeout=3)
                    except Exception:
                        pass

    for k in keys_to_kill:
        try:
            ds.cache_invalidate(k)
        except Exception:
            pass

    removed = False
    accs_list = list(u.get("accounts", []))
    for acc in list(accs_list):
        acc_type = acc.get("type")
        acc_uid = str(acc.get("uid", ""))
        acc_token_prefix = str(acc.get("token", ""))[:20]

        match = False
        if acc_type == "guest":
            if acc_uid == uid or (real_uid and acc_uid == real_uid):
                match = True
        elif acc_type == "token":
            if acc_token_prefix == uid[:20] or (real_token_prefix and acc_token_prefix == real_token_prefix):
                match = True

        if match:
            accs_list.remove(acc)
            removed = True
            print(f"[api] Removed from users.json: type={acc_type} uid={acc_uid} token={acc_token_prefix}", flush=True)
            break

    u["accounts"] = accs_list
    users[un] = u
    save_users(users)
    print(f"[api] After delete: {un} now has {len(accs_list)}/{u.get('slots', 0)} slots used", flush=True)

    for k in keys_to_kill:
        if k in bot_state.accounts:
            bot_state.accounts.pop(k, None)

    await asyncio.sleep(0.5)

    for k in keys_to_kill:
        if k in bot_state.accounts:
            bot_state.accounts.pop(k, None)

    return web.json_response({"status": "ok", "removed": removed})


async def h_acc_pause(req):
    s = cur_user(req)
    if not s or s.get("is_admin"):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    un = s["username"]
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    uid = str(d.get("uid", "")).strip()
    if not uid:
        return web.json_response({"status": "error", "error": "Missing UID"})

    print(f"[api] Account pause user={un} uid={uid}", flush=True)

    real_uid = None
    real_token_prefix = None
    try:
        cred = ds.bot_state.account_credentials.get(uid)
        if cred:
            if cred.get("auth_uid"):
                real_uid = str(cred.get("auth_uid"))
            if cred.get("auth_token"):
                real_token_prefix = str(cred.get("auth_token"))[:20]
    except Exception:
        pass

    if un not in USER_PAUSED:
        USER_PAUSED[un] = set()
    USER_PAUSED[un].add(uid)
    if real_uid:
        USER_PAUSED[un].add(real_uid)
    if real_token_prefix:
        USER_PAUSED[un].add(real_token_prefix)

    keys_to_kill = [uid]
    if real_uid:
        keys_to_kill.append(real_uid)
    if real_token_prefix:
        keys_to_kill.append(real_token_prefix)

    workers = USER_WORKERS.get(un, {})
    for k in keys_to_kill:
        t = workers.pop(k, None)
        if t and not t.done():
            t.cancel()
            try:
                await asyncio.wait_for(t, timeout=5)
            except (asyncio.CancelledError, asyncio.TimeoutError, Exception):
                pass

    for key in list(bot_state.account_workers.keys()):
        if str(key).startswith(un + "::"):
            suffix = str(key).split("::", 1)[1]
            if suffix in keys_to_kill:
                t = bot_state.account_workers.pop(key, None)
                if t and not t.done():
                    t.cancel()
                    try:
                        await asyncio.wait_for(t, timeout=3)
                    except Exception:
                        pass

    for k in keys_to_kill:
        if k in bot_state.accounts:
            bot_state.accounts[k]["status"] = "PAUSED"

    return web.json_response({"status": "ok"})


async def h_acc_resume(req):
    s = cur_user(req)
    if not s or s.get("is_admin"):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    un = s["username"]
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    uid = str(d.get("uid", "")).strip()
    if not uid:
        return web.json_response({"status": "error", "error": "Missing UID"})

    print(f"[api] Account resume user={un} uid={uid}", flush=True)

    real_uid = None
    real_token_prefix = None
    try:
        cred = ds.bot_state.account_credentials.get(uid)
        if cred:
            if cred.get("auth_uid"):
                real_uid = str(cred.get("auth_uid"))
            if cred.get("auth_token"):
                real_token_prefix = str(cred.get("auth_token"))[:20]
    except Exception:
        pass

    keys_to_release = [uid]
    if real_uid:
        keys_to_release.append(real_uid)
    if real_token_prefix:
        keys_to_release.append(real_token_prefix)

    if un in USER_PAUSED:
        for k in keys_to_release:
            USER_PAUSED[un].discard(k)
    if un in USER_DELETED:
        for k in keys_to_release:
            USER_DELETED[un].discard(k)

    users = load_users()
    u = users.get(un, {})
    if time.time() < u.get("expires_at", 0):
        asyncio.create_task(start_user_workers(un))

    return web.json_response({"status": "ok"})


async def h_adm_login_get(req):
    s = cur_user(req)
    if s and s.get("is_admin"):
        raise web.HTTPFound(ADMIN_PATH + "/panel")
    return web.Response(text=ADMIN_LOGIN_HTML, content_type="text/html")


async def h_adm_login_post(req):
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    u = (d.get("username") or "").strip()
    p = d.get("password") or ""
    if u == ADMIN_USERNAME and p == ADMIN_PASSWORD:
        token = create_session(u, True)
        print(f"[auth] Admin login OK", flush=True)
        r = web.json_response({"status": "ok", "redirect": ADMIN_PATH + "/panel"})
        _set_ck(r, token)
        return r
    print(f"[auth] Admin login FAILED username={u}", flush=True)
    return web.json_response({"status": "error", "error": "Access Denied"})


async def h_adm_logout(req):
    token = req.cookies.get(SESSION_COOKIE)
    if token:
        destroy_session(token)
    r = web.HTTPFound(ADMIN_PATH)
    _clr_ck(r)
    raise r


async def h_adm_panel(req):
    if not cur_admin(req):
        raise web.HTTPFound(ADMIN_PATH)
    return web.Response(text=ADMIN_PANEL_HTML, content_type="text/html")


async def h_adm_create(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    u = (d.get("username") or "").strip()
    p = (d.get("password") or "").strip()
    unlimited = bool(d.get("unlimited", False))
    try:
        slots = int(d.get("slots", cfgmod.get()["default_slots"]))
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid Slots"})
    hours = int(d.get("hours", 24))
    if not u or not p:
        return web.json_response({"status": "error", "error": "Username And Password Required"})
    _cap = cfgmod.get()["max_slots_cap"]
    if not unlimited and (slots < 1 or slots > _cap):
        return web.json_response({"status": "error", "error": "Slots Must Be 1-%d" % _cap})
    if hours < 1 or hours > 8760:
        return web.json_response({"status": "error", "error": "Hours Must Be 1-8760"})
    users = load_users()
    if u in users:
        return web.json_response({"status": "error", "error": "Username Already Exists"})
    ph, salt = hash_pw(p)
    now = time.time()
    users[u] = {
        "password_hash": ph,
        "salt": salt,
        "slots": slots,
        "unlimited": unlimited,
        "plan_hours": hours,
        "created_at": now,
        "expires_at": now + hours * 3600,
        "accounts": [],
        "_expired_flag": False,
    }
    save_users(users)
    print(f"[api] Admin created user={u} slots={slots} hours={hours}", flush=True)
    return web.json_response({"status": "ok"})


async def h_adm_list(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    users = load_users()
    out = []
    for un, u in users.items():
        used = sum(1 for a in ds.bot_state.accounts.values() if a.get("_owner") == un)
        out.append({
            "username": un,
            "slots": u.get("slots", 0),
            "unlimited": bool(u.get("unlimited")),
            "used_slots": used,
            "expires_at": u.get("expires_at", 0),
            "created_at": u.get("created_at", 0),
        })
    out.sort(key=lambda x: x.get("created_at", 0), reverse=True)
    return web.json_response({"status": "ok", "users": out})


async def h_adm_ext(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    un = d.get("username", "").strip()
    hours = int(d.get("hours", 24))
    users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Not Found"})
    now = time.time()
    base = max(now, u.get("expires_at", 0))
    u["expires_at"] = base + hours * 3600
    u["_expired_flag"] = False
    save_users(users)
    if un in USER_DELETED:
        USER_DELETED[un].clear()
    print(f"[api] Admin extended user={un} +{hours}h", flush=True)
    asyncio.create_task(start_user_workers(un))
    return web.json_response({"status": "ok"})


async def h_adm_slot(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    un = d.get("username", "").strip()
    count = int(d.get("count", 1))
    users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Not Found"})
    u["slots"] = min(cfgmod.get()["max_slots_cap"], max(0, u.get("slots", 0) + count))
    save_users(users)
    print(f"[api] Admin added {count} slot to user={un}", flush=True)
    return web.json_response({"status": "ok"})


async def h_adm_del(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    un = d.get("username", "").strip()
    users = load_users()
    if un not in users:
        return web.json_response({"status": "error", "error": "User Not Found"})
    print(f"[api] Admin deleted user={un}", flush=True)
    await stop_user_workers(un)
    users.pop(un, None)
    save_users(users)
    USER_PAUSED.pop(un, None)
    USER_DELETED.pop(un, None)
    USER_WORKERS.pop(un, None)
    return web.json_response({"status": "ok"})


async def h_adm_reset_pw(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})
    un = d.get("username", "").strip()
    new_pw = d.get("password", "").strip()
    if not un or not new_pw:
        return web.json_response({"status": "error", "error": "Username And Password Required"})
    users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Not Found"})
    ph, salt = hash_pw(new_pw)
    u["password_hash"] = ph
    u["salt"] = salt
    users[un] = u
    save_users(users)
    print(f"[api] Admin reset password user={un}", flush=True)
    return web.json_response({"status": "ok"})



def _key_of(a):
    return str(a.get("uid")) if a.get("type") == "guest" else str(a.get("token", ""))[:20]


def _release_keys(un, uid_or_token):
    """Same cleanup h_acc_add does before (re)adding an account."""
    keys = {str(uid_or_token), str(uid_or_token)[:20]}
    try:
        for k, cred in list(ds.bot_state.account_credentials.items()):
            if str(cred.get("auth_uid", "")) == str(uid_or_token) or \
               str(cred.get("account_id", "")) == str(uid_or_token) or \
               str(cred.get("auth_token", ""))[:20] == str(uid_or_token)[:20]:
                for f in ("account_id", "auth_uid"):
                    if cred.get(f):
                        keys.add(str(cred.get(f)))
                if cred.get("auth_token"):
                    keys.add(str(cred.get("auth_token"))[:20])
    except Exception:
        pass
    for k in keys:
        USER_DELETED.setdefault(un, set()).discard(k)
        USER_PAUSED.setdefault(un, set()).discard(k)
        try:
            ds.cache_invalidate(k)
        except Exception:
            pass


async def h_acc_bulk(req):
    """Add many accounts at once. Body: {"text": "uid:pass\\nuid:pass\\n..."}"""
    s = cur_user(req)
    if not s or s.get("is_admin"):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    un = s["username"]
    users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Missing"})
    if time.time() >= u.get("expires_at", 0):
        return web.json_response({"status": "error", "error": "Plan Expired"})
    try:
        d = await req.json()
    except Exception:
        return web.json_response({"status": "error", "error": "Invalid JSON"})

    mode = "limited" if str(d.get("mode", "")).lower() == "limited" else "unlimited"
    cfg = cfgmod.get()
    parsed, errors = orch.parse_bulk(str(d.get("text", "")), cfg["bulk_max_lines"])
    if not parsed and not errors:
        return web.json_response({"status": "error", "error": "Nothing To Add"})

    accs = u.setdefault("accounts", [])
    deleted = USER_DELETED.get(un, set())
    active = [a for a in accs if _key_of(a) and _key_of(a) not in deleted and not _is_completed(un, a)]
    existing = {("g:" + str(a.get("uid"))) if a.get("type") == "guest" else ("t:" + str(a.get("token", ""))[:20])
                for a in active}
    free = cfgmod.free_slots(u, len(active))   # None = unlimited

    added, skipped = [], list(errors)
    for item in parsed:
        ident = ("g:" + item["uid"]) if item["type"] == "guest" else ("t:" + item["token"][:20])
        label = item["uid"] if item["type"] == "guest" else item["token"][:6] + "***"
        if ident in existing:
            skipped.append({"line": item["line"], "text": label, "error": "Already Added"})
            continue
        if free is not None and free <= 0:
            skipped.append({"line": item["line"], "text": label, "error": "No Free Slots"})
            continue
        _release_keys(un, item["uid"] if item["type"] == "guest" else item["token"])
        rec = {"type": item["type"], "created_at": time.time(), "mode": mode}
        if item["type"] == "guest":
            rec.update({"uid": item["uid"], "password": item["password"]})
        else:
            rec["token"] = item["token"]
        accs.append(rec)
        existing.add(ident)
        added.append({"line": item["line"], "text": label})
        if free is not None:
            free -= 1

    if added:
        u["accounts"] = accs
        users[un] = u
        save_users(users)
        asyncio.create_task(start_user_workers(un))
    print(f"[api] Bulk add user={un} added={len(added)} skipped={len(skipped)}", flush=True)
    skipped.sort(key=lambda x: x.get("line", 0))
    return web.json_response({
        "status": "ok",
        "added": len(added),
        "skipped": len(skipped),
        "skipped_detail": skipped[:200],
    })


# ----------------------------- System 1: completed accounts download -----------------------------
async def h_dl_completed(req):
    """Download the logged-in user's own finished (Limited) accounts as UID:password."""
    s = cur_user(req)
    if not s or s.get("is_admin"):
        return web.json_response({"error": "unauthorized"}, status=401)
    un = s["username"]
    u = load_users().get(un) or {}
    rows = [r for r in _completed_rows(un, u, with_password=True) if r["type"] == "guest" and r.get("password")]
    if not rows:
        return web.json_response({"error": "No completed accounts to download"}, status=404)
    cap = cfgmod.get()["limited_max_level"]
    fmt = str(req.query.get("format", "txt")).lower()
    if fmt == "csv":
        buf = io.StringIO()
        w = csv.writer(buf)
        w.writerow(["uid", "password", "level", "completed_at_utc"])
        for r in rows:
            w.writerow([r["uid"], r["password"], r["level"],
                        time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(r["completed_at"] or 0))])
        body, ctype, ext = buf.getvalue(), "text/csv", "csv"
    else:
        body = "".join("%s:%s\n" % (r["uid"], r["password"]) for r in rows)
        ctype, ext = "text/plain", "txt"
    return web.Response(text=body, content_type=ctype, charset="utf-8", headers={
        "Content-Disposition": 'attachment; filename="ghostx_level%s_accounts.%s"' % (cap, ext),
        "Cache-Control": "no-store",
    })


async def h_completed_clear(req):
    """Remove the user's finished (Limited) accounts from their list."""
    s = cur_user(req)
    if not s or s.get("is_admin"):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    un = s["username"]
    users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Missing"})
    accs = u.get("accounts", [])
    keep = [a for a in accs if not _is_completed(un, a)]
    removed = len(accs) - len(keep)
    u["accounts"] = keep
    users[un] = u
    save_users(users)
    COMPLETED_INFO.pop(un, None)
    return web.json_response({"status": "ok", "removed": removed})


# ----------------------------- admin: settings / unlimited / control -----------------------------
async def _adm_json(req):
    if not cur_admin(req):
        return None, web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    try:
        return await req.json(), None
    except Exception:
        return None, web.json_response({"status": "error", "error": "Invalid JSON"})


async def h_adm_cfg_get(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    return web.json_response({"status": "ok", "config": cfgmod.get()})


async def h_adm_cfg_set(req):
    d, err = await _adm_json(req)
    if err:
        return err
    try:
        new = cfgmod.update(d.get("config", d))
    except Exception as e:
        return web.json_response({"status": "error", "error": str(e)})
    print(f"[api] Admin updated config: {new}", flush=True)
    return web.json_response({"status": "ok", "config": new})


async def h_adm_unlimited(req):
    """Toggle unlimited slots for one user, or set exact slots."""
    d, err = await _adm_json(req)
    if err:
        return err
    un = str(d.get("username", "")).strip()
    users = load_users()
    u = users.get(un)
    if not u:
        return web.json_response({"status": "error", "error": "User Not Found"})
    if "unlimited" in d:
        u["unlimited"] = bool(d["unlimited"])
    if "slots" in d and d["slots"] is not None:
        try:
            n = int(d["slots"])
        except Exception:
            return web.json_response({"status": "error", "error": "Invalid Slots"})
        cap = cfgmod.get()["max_slots_cap"]
        if n < 0 or n > cap:
            return web.json_response({"status": "error", "error": "Slots Must Be 0-%d" % cap})
        u["slots"] = n
    save_users(users)
    print(f"[api] Admin set user={un} unlimited={u.get('unlimited')} slots={u.get('slots')}", flush=True)
    return web.json_response({"status": "ok"})


async def h_adm_accounts(req):
    """Every live account across all users (phase, level, status)."""
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    out = []
    for uid, a in list(ds.bot_state.accounts.items()):
        out.append({
            "uid": uid,
            "owner": a.get("_owner", "?"),
            "nickname": a.get("nickname", "?"),
            "level": a.get("level", 1),
            "status": a.get("status", "LIVE"),
            "phase": a.get("phase", "PENDING"),
            "force": orch.FORCE.get(str(uid), "auto"),
            "matches_played": a.get("matches_played", 0),
            "gained_exp": a.get("gained_exp", 0),
        })
    out.sort(key=lambda x: (x["owner"], x["uid"]))
    return web.json_response({"status": "ok", "accounts": out})


async def h_adm_force(req):
    """Override level routing for one account: gld | lvl | auto."""
    d, err = await _adm_json(req)
    if err:
        return err
    uid = str(d.get("uid", "")).strip()
    mode = str(d.get("mode", "auto")).lower()
    if uid not in ds.bot_state.accounts:
        return web.json_response({"status": "error", "error": "Account Not Live"})
    if mode not in ("gld", "lvl", "auto"):
        return web.json_response({"status": "error", "error": "Mode Must Be gld, lvl or auto"})
    if mode == "auto":
        orch.FORCE.pop(uid, None)
    else:
        orch.FORCE[uid] = mode
    # kick the worker so the new routing is applied right away
    try:
        ds.bot_state.close_writers_for_account(uid)
    except Exception:
        pass
    print(f"[api] Admin force uid={uid} mode={mode}", flush=True)
    return web.json_response({"status": "ok"})


async def h_adm_logs(req):
    if not cur_admin(req):
        return web.json_response({"status": "error", "error": "unauthorized"}, status=401)
    return web.json_response({"status": "ok", "logs": ds.bot_state.logs[-120:]})


async def expiry_watcher():
    while True:
        try:
            users = load_users()
            now = time.time()
            changed = False
            for un, u in users.items():
                exp = now >= u.get("expires_at", 0)
                was = u.get("_expired_flag", False)
                if exp and not was:
                    print(f"[expiry] Plan expired user={un} -> stopping workers", flush=True)
                    await stop_user_workers(un)
                    u["_expired_flag"] = True
                    changed = True
                elif not exp and was:
                    u["_expired_flag"] = False
                    changed = True
                    asyncio.create_task(start_user_workers(un))
            if changed:
                save_users(users)
        except Exception:
            pass
        await asyncio.sleep(5)


async def start_web_dashboard(host="0.0.0.0", port=20335):
    app = web.Application()

    app.router.add_get("/", h_root)
    app.router.add_get("/login", h_login_get)
    app.router.add_post("/login", h_login_post)
    app.router.add_get("/signup", h_signup)
    app.router.add_get("/plans", h_plans)
    app.router.add_get("/logout", h_logout)
    app.router.add_get("/dashboard", h_dash)
    app.router.add_get("/expired", h_expired)

    app.router.add_get("/api/stats", h_stats)
    app.router.add_post("/api/account/check", h_acc_check)
    app.router.add_post("/api/account/bulk", h_acc_bulk)
    app.router.add_post("/api/account/add", h_acc_add)
    app.router.add_post("/api/account/delete", h_acc_del)
    app.router.add_post("/api/account/pause", h_acc_pause)
    app.router.add_post("/api/account/resume", h_acc_resume)
    app.router.add_get("/api/download/completed", h_dl_completed)
    app.router.add_post("/api/completed/clear", h_completed_clear)

    app.router.add_get(ADMIN_PATH, h_adm_login_get)
    app.router.add_post(ADMIN_PATH, h_adm_login_post)
    app.router.add_get(ADMIN_PATH + "/logout", h_adm_logout)
    app.router.add_get(ADMIN_PATH + "/panel", h_adm_panel)

    app.router.add_post("/api/admin/create-user", h_adm_create)
    app.router.add_get("/api/admin/list-users", h_adm_list)
    app.router.add_post("/api/admin/extend-time", h_adm_ext)
    app.router.add_post("/api/admin/add-slot", h_adm_slot)
    app.router.add_post("/api/admin/delete-user", h_adm_del)
    app.router.add_post("/api/admin/reset-password", h_adm_reset_pw)
    app.router.add_get("/api/admin/config", h_adm_cfg_get)
    app.router.add_post("/api/admin/config", h_adm_cfg_set)
    app.router.add_post("/api/admin/set-unlimited", h_adm_unlimited)
    app.router.add_get("/api/admin/accounts", h_adm_accounts)
    app.router.add_post("/api/admin/force", h_adm_force)
    app.router.add_get("/api/admin/logs", h_adm_logs)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()

    print(f"Web Dashboard Running On http://{host}:{port}", flush=True)
    print(f"Admin Panel: http://{host}:{port}{ADMIN_PATH}", flush=True)

    asyncio.create_task(expiry_watcher())

    try:
        users = load_users()
        now = time.time()
        for un, u in users.items():
            if now < u.get("expires_at", 0):
                asyncio.create_task(start_user_workers(un))
    except Exception:
        pass


__all__ = ["bot_state", "start_web_dashboard"]