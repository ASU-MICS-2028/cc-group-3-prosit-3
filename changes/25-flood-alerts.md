---
issue: 25
title: Flood alerts, a warning line and a rising-fast rule behind GET /alerts
date: 2026-11-23
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `api/alerts.py`: checks every drain gauge's latest reading every 30 s.
  - Opens a **flood warning** at 60 cm or more, and closes it below 50 cm.
  - Opens a **rising fast** (`anomaly`) alert at +15 cm in 15 minutes, and closes it under +5 cm.
  - Each alert's `reason` is a plain-words sentence with the numbers. Times come from the readings.
- `api/schema.sql`: `alerts.closed_at`.
- `api/tests/test_alerts.py`: the rules, including no duplicate alerts and no flapping between 50 and 60 cm.
- Evidence: `evidence/lab12/25-alerts-run.sh` ran 24 simulated hours through broker, bridge and DB with the checker live.
  - 4 storms opened 8 alerts, and all 8 closed after the water drained.
  - The rising-fast alert came 7 to 23 minutes before each warning.
  - `GET /alerts?status=closed` serves them.
- `api/README.md`: the rules in plain words.

## Why

Issue #25: warn residents when drains rise.

## How to check
```bash
python3 -m unittest discover api/tests -v
PY=python3 bash evidence/lab12/25-alerts-run.sh   # ~3 min; then read evidence/lab12/25-query-output.txt
```

## AI use
- **Tool:** Claude Code
- **What it did:** wrote the checker, tests, evidence script, docs and this file, and ran the evidence.
- **Prompts / session summary:** "go ahead with #25". The thresholds were chosen against the simulator's drains (bases 18 and 25 cm, storms up to about +80 cm).
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- A rate-of-rise rule as the "anomaly", rather than an ML model, because it's easy to explain to residents.
- One line for all drains until real gauges are installed.

## Not done
- The app screen (#24) and flagging an alert as wrong (#41), both Pea's.
- Per-drain thresholds, push or SMS.
