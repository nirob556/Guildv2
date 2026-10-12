# LVL + GLD unified

Run exactly like before:  `pip install -r requirements.txt` then `python main.py`
(dashboard on port 20335, admin at `/admin/vaibhav/levelup/adm-dash`).

## How an account flows
1. Add it (UID+Password, Access Token, or **Bulk** tab: one `uid:pass` per line).
2. After login the level is read from the game server:
   * level `>=` **LVL From Level** (default 3)  -> LVL levels it up (as before)
   * level from **GLD From Level** (default 1) up to 2 -> **GLD** (`gld_engine.py`, your
     app.py in solo mode, no team, no clan join) plays solo matches
   * every `level_poll_seconds` (default 30s) the level is re-checked; at Level 3 GLD stops
     and LVL takes over automatically on the same account.

## Limits
* Each user has `slots`; bulk add fills free slots top-to-bottom and reports the rest as "No Free Slots".
* Admin panel -> per-user **Unlimited** button, "Unlimited slots" checkbox when creating a user,
  and a **Global unlimited** switch in System Settings.
* All other knobs (thresholds, default slots, slot cap, bulk line cap, poll interval, parallel
  logins, login-fail limit) are in the admin **System Settings** card (stored in `data/config.json`).
* Admin can also force one account to GLD / LVL / AUTO and watch live logs.

## Notes
* Admin login can be overridden with env vars `ADMIN_USERNAME` / `ADMIN_PASSWORD`.
* The hardcoded GLD accounts list was NOT carried over.

## Two systems (choose per account when adding)
The Add Account form has a **System** selector (applies to single add, token and bulk):
* **Unlimited XP** (default, the original behaviour): levels the account with no limit.
* **Limited**: levels the account up to **Limited System Max Level** (default 8, admin
  System Settings), then stops it for good and marks it completed. Completed accounts leave
  the live list, do **not** use a slot, and are never restarted (also not after a server restart).

**Download** button (top bar): lists the finished accounts of the logged-in user and downloads
them as `.txt` (`UID:Password` per line, same format as the Bulk tab) or `.csv`. Only the user's
own accounts are included. Token accounts have no password, so they are listed but not in the
files. "Clear list" removes them from the list (download first).
Existing accounts without a mode keep running as Unlimited.
