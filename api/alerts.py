"""Flood alert checker (#25): opens and closes rows in `alerts`, which GET /alerts serves.

Run:   DATABASE_URL=... python3 api/alerts.py            # check every 30 s
       DATABASE_URL=... python3 api/alerts.py --once     # one pass (cron, tests)

The rules, in plain words (each alert's `reason` says which one fired and the numbers):
- Flood warning: the drain's water is at or above the 60 cm warning line. It closes once the water is
  back below 50 cm, so a level wobbling around the line doesn't open and close alerts every minute.
- Rising fast (anomaly): the water rose 15 cm or more in the last 15 minutes, usually the first sign of a
  storm. It closes once the rise over 15 minutes is under 5 cm.
Times are the readings' own times, not the clock, so replayed or buffered data opens alerts at the right moment.
"""
import argparse
import os
import time
from datetime import timezone
from pathlib import Path

# Calibration knobs: one line for every drain for now. A real drain's line depends on its depth and
# what floods first; move these into a per-device table when real gauges are installed.
WARN_CM, CLEAR_CM = 60, 50
RISE_CM, SETTLED_CM, WINDOW_MIN = 15, 5, 15


def decide(level, earlier, open_kinds, warn=WARN_CM, clear=CLEAR_CM):
    """Latest level, level WINDOW_MIN earlier (or None), kinds already open -> [("open", kind, reason) | ("close", kind)].
    warn/clear are only changed by the what-if replay (api/what_if.py)."""
    out = []
    if level >= warn and "flood_warning" not in open_kinds:
        out.append(("open", "flood_warning", f"Drain level {level:.0f} cm, at or above the {warn} cm warning line"))
    elif level < clear and "flood_warning" in open_kinds:
        out.append(("close", "flood_warning"))
    rise = 0 if earlier is None else level - earlier
    if rise >= RISE_CM and "anomaly" not in open_kinds:
        out.append(("open", "anomaly", f"Drain level rose {rise:.0f} cm in {WINDOW_MIN} minutes, now {level:.0f} cm"))
    elif rise < SETTLED_CM and "anomaly" in open_kinds:
        out.append(("close", "anomaly"))
    return out


def check(conn):
    """One pass over every flood gauge's latest reading. Returns the actions taken."""
    taken = []
    with conn.transaction(), conn.cursor() as cur:
        cur.execute(f"""
            SELECT DISTINCT ON (l.device_id) l.device_id, l.neighbourhood, l.ts, l.water_level_cm AS level,
                   (SELECT e.water_level_cm FROM flood e WHERE e.device_id = l.device_id
                      AND e.ts <= l.ts - interval '{WINDOW_MIN} minutes' ORDER BY e.ts DESC LIMIT 1) AS earlier,
                   ARRAY(SELECT kind FROM alerts a WHERE a.device_id = l.device_id AND status = 'open') AS open_kinds
            FROM flood l ORDER BY l.device_id, l.ts DESC""")
        for dev, hood, ts, level, earlier, open_kinds in cur.fetchall():
            for action in decide(level, earlier, open_kinds):
                if action[0] == "open":
                    cur.execute("""INSERT INTO alerts (kind, domain, neighbourhood, device_id, opened_at, reason)
                                   VALUES (%s, 'flood', %s, %s, %s, %s)""", (action[1], hood, dev, ts, action[2]))
                else:
                    cur.execute("""UPDATE alerts SET status = 'closed', closed_at = %s
                                   WHERE device_id = %s AND kind = %s AND status = 'open'""", (ts, dev, action[1]))
                taken.append((ts, dev, *action))
    return taken


def main():
    import psycopg

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--every", type=float, default=30, help="seconds between passes")
    a = ap.parse_args()
    with psycopg.connect(os.environ["DATABASE_URL"], autocommit=True) as conn:
        conn.execute(Path(__file__).with_name("schema.sql").read_text())
        while True:
            for ts, dev, verb, kind, *reason in check(conn):
                print(f"{ts.astimezone(timezone.utc):%Y-%m-%dT%H:%M:%SZ} {verb} {kind} {dev} {' '.join(reason)}", flush=True)
            if a.once:
                break
            time.sleep(a.every)


if __name__ == "__main__":
    main()
