# -*- coding: utf-8 -*-
"""
Runtime settings for the unified LVL + GLD system.

Stored in data/config.json and editable from the admin panel.
All values are validated here so a bad edit can never break the bot.
"""
import os
import json
import threading

DATA_DIR = "data"
CONFIG_FILE = os.path.join(DATA_DIR, "config.json")

DEFAULTS = {
    # --- level routing ---------------------------------------------------
    # level <  gld_min_level                  -> LVL
    # gld_min_level <= level < lvl_min_level  -> GLD (solo matches until lvl_min_level)
    # level >= lvl_min_level                  -> LVL (normal level-up)
    "gld_min_level": 1,
    "lvl_min_level": 3,

    # --- limits ----------------------------------------------------------
    "default_slots": 5,        # slots given to a new user if admin doesn't specify
    "max_slots_cap": 20,       # hard cap for normal (non-unlimited) users
    "global_unlimited": False,  # True = nobody has a slot limit
    "bulk_max_lines": 0,       # max lines per bulk paste (0 = no extra limit)

    # --- engine ----------------------------------------------------------
    "level_poll_seconds": 30,  # how often GLD phase re-checks the account level
    "max_parallel_logins": 25,  # simultaneous logins (raise/lower from the admin panel)
    "login_fail_limit": 3,     # after N failed logins the account shows LOGIN FAILED

    # --- System 1 (Limited) ---------------------------------------------
    # Accounts added in "Limited" mode stop at this level, are marked completed
    # and move to the Download section. "Unlimited" accounts are not affected.
    "limited_max_level": 8,
}

# (type, min, max) for validation
_RULES = {
    "gld_min_level": (int, 1, 100),
    "lvl_min_level": (int, 2, 100),
    "default_slots": (int, 1, 100000),
    "max_slots_cap": (int, 1, 100000),
    "global_unlimited": (bool, None, None),
    "bulk_max_lines": (int, 0, 100000),
    "level_poll_seconds": (int, 10, 600),
    "max_parallel_logins": (int, 1, 50),
    "login_fail_limit": (int, 1, 50),
    "limited_max_level": (int, 2, 100),
}

_lock = threading.Lock()
_cache = None


def _coerce(key, value):
    typ, lo, hi = _RULES[key]
    if typ is bool:
        if isinstance(value, str):
            return value.strip().lower() in ("1", "true", "yes", "on")
        return bool(value)
    v = int(value)
    if lo is not None and v < lo:
        raise ValueError("%s must be >= %s" % (key, lo))
    if hi is not None and v > hi:
        raise ValueError("%s must be <= %s" % (key, hi))
    return v


def _load_from_disk():
    cfg = dict(DEFAULTS)
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                raw = json.load(f)
            for k in DEFAULTS:
                if k in raw:
                    try:
                        cfg[k] = _coerce(k, raw[k])
                    except Exception:
                        pass
    except Exception:
        pass
    if cfg["gld_min_level"] >= cfg["lvl_min_level"]:
        cfg["gld_min_level"] = max(1, cfg["lvl_min_level"] - 1)
    return cfg


def get():
    """Return a copy of the current settings."""
    global _cache
    with _lock:
        if _cache is None:
            _cache = _load_from_disk()
        return dict(_cache)


def update(changes):
    """Validate + persist a partial update. Raises ValueError on bad input."""
    global _cache
    with _lock:
        cur = _cache if _cache is not None else _load_from_disk()
        new = dict(cur)
        for k, v in (changes or {}).items():
            if k not in DEFAULTS:
                continue
            new[k] = _coerce(k, v)
        if new["gld_min_level"] >= new["lvl_min_level"]:
            raise ValueError("gld_min_level must be lower than lvl_min_level")
        os.makedirs(DATA_DIR, exist_ok=True)
        tmp = CONFIG_FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(new, f, indent=2)
        os.replace(tmp, CONFIG_FILE)
        _cache = new
        return dict(new)


# ---------------------------------------------------------------------------
# Slot helpers (None == unlimited)
# ---------------------------------------------------------------------------
def slot_limit(user):
    """Effective slot limit for a user dict, or None if unlimited."""
    cfg = get()
    if cfg["global_unlimited"] or (user or {}).get("unlimited"):
        return None
    return int((user or {}).get("slots", 0) or 0)


def limit_reached(user, used):
    lim = slot_limit(user)
    return lim is not None and used >= lim


def free_slots(user, used):
    """Free slots, or None if unlimited."""
    lim = slot_limit(user)
    return None if lim is None else max(0, lim - used)
