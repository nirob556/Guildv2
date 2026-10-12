# -*- coding: utf-8 -*-
"""
Console quieting for many-account runs.

With 100 accounts, per-account chatter makes the terminal unreadable. In quiet
mode (default) only failures/warnings are printed, plus a one-line status
summary every 15 seconds. The web dashboard log is NOT affected.
Set the environment variable GHOSTX_VERBOSE=1 to get the full per-account output.
"""
import os
import builtins

QUIET = os.environ.get("NIROBBZ", "0").strip().lower() not in ("1", "true", "yes", "on")

_ALWAYS = ("fail", "error", "cannot", "expire", "stall", "traceback")


def print(*args, **kwargs):  # intentionally shadows the builtin in modules that import it
    if not QUIET:
        return builtins.print(*args, **kwargs)
    try:
        text = " ".join(str(a) for a in args).lower()
    except Exception:
        return builtins.print(*args, **kwargs)
    if any(k in text for k in _ALWAYS):
        return builtins.print(*args, **kwargs)
