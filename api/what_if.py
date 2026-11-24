"""What-if replay (#45, Lab 14 Part A): what would a lower flood warning line have done?

Run:   python3 api/what_if.py                     # 30 simulated days, seed 45, lines 60 (today), 50, 40 cm
       python3 api/what_if.py --days 7 --lines 60 45
Makes the drain readings with the simulator (no broker or DB needed), then feeds each gauge's readings, in
time order, through the same decide() that api/alerts.py runs in production. A line's clear level is 10 cm
under it, as today (60/50). For each line it prints how many warnings opened, how much earlier than today's
line they came for the same storm, and how many were extra (the water never reached today's line).
"""
import argparse
import os
import random
import sys
from bisect import bisect_right
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "sensors"))
from alerts import CLEAR_CM, WARN_CM, WINDOW_MIN, decide  # noqa: E402
from simulator import run  # noqa: E402


def warnings(readings, warn, clear):
    """One gauge's [(ts, level)] in time order -> [(opened, closed or None, peak cm)] of flood warnings."""
    times = [t for t, _ in readings]
    out, open_kinds = [], set()
    for i, (t, level) in enumerate(readings):
        j = bisect_right(times, t - timedelta(minutes=WINDOW_MIN), 0, i) - 1
        for verb, kind, *_ in decide(level, readings[j][1] if j >= 0 else None, open_kinds, warn, clear):
            if kind != "flood_warning":
                continue
            if verb == "open":
                out.append([t, None, level])
                open_kinds.add(kind)
            else:
                out[-1][1] = t
                open_kinds.discard(kind)
        if "flood_warning" in open_kinds:
            out[-1][2] = max(out[-1][2], level)
    return [tuple(w) for w in out]


def compare(base, other):
    """Warnings at today's line vs another line -> (lead times in minutes for storms both caught, extra warnings)."""
    leads, extra = [], 0
    for opened, closed, _ in other:
        hits = [b for b in base if opened <= b[0] and (closed is None or b[0] <= closed)]
        if hits:
            leads.append((hits[0][0] - opened).total_seconds() / 60)
        else:
            extra += 1
    return leads, extra


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--seed", type=int, default=45)
    ap.add_argument("--lines", type=int, nargs="+", default=[WARN_CM, 50, 40])
    a = ap.parse_args()

    gauges = {}
    start = datetime(2026, 11, 1, tzinfo=timezone.utc)
    run(a.days * 8640, 0, start, random.Random(a.seed),
        lambda dev, r: r["domain"] == "flood" and gauges.setdefault(r["device_id"], []).append(
            (datetime.fromisoformat(r["ts"]), r["value"])))
    print(f"{a.days} simulated days from {start:%Y-%m-%d}, seed {a.seed}: "
          + ", ".join(f"{d} {len(rs)} readings, peak {max(v for _, v in rs):.0f} cm" for d, rs in sorted(gauges.items())))
    print(f"Today's line: warn at {WARN_CM} cm, clear under {CLEAR_CM} cm.\n")
    print(f"{'line':>6} {'warnings':>9} {'same storm':>11} {'earlier by (min)':>18} {'extra':>6} {'hours under warning':>20}")
    base = {d: warnings(rs, WARN_CM, CLEAR_CM) for d, rs in gauges.items()}
    end = start + timedelta(days=a.days)
    for line in a.lines:
        got = {d: warnings(rs, line, line - (WARN_CM - CLEAR_CM)) for d, rs in gauges.items()}
        leads, extra = [], 0
        for d in got:
            ls, x = compare(base[d], got[d])
            leads += ls
            extra += x
        hours = sum(((c or end) - o).total_seconds() for ws in got.values() for o, c, _ in ws) / 3600
        lead = f"{min(leads):.0f}-{max(leads):.0f}, mean {sum(leads) / len(leads):.0f}" if leads else "-"
        print(f"{line:>4}cm {sum(map(len, got.values())):>9} {len(leads):>11} {lead:>18} {extra:>6} {hours:>20.1f}")


if __name__ == "__main__":
    main()
