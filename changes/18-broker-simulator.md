---
issue: 18
title: MQTT broker and three-domain sensor simulator
date: 2026-11-15
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `ingest/compose.yaml`, `ingest/mosquitto/mosquitto.conf`: local Mosquitto 2.0 broker on `localhost:1883` (anonymous, dev only until #21).
- `sensors/simulator.py`: 11 simulated devices (5 PM2.5, 4 bins, 2 drain gauges) in 5 neighbourhoods. One MQTT connection per device, QoS 1, topics and JSON per `contracts/`. Air and waste publish every 60 s; flood every 10 s while the level is rising. Survives the broker going down (drops and logs readings, reconnects).
- `sensors/tests/test_simulator.py` (6 tests), added to the `contracts` CI job.
- `evidence/lab12/18-*`: publish and `mosquitto_sub` output; broker-outage run.
- `learnings/paho-publish-raises-while-broker-is-down.md`.
- READMEs for `sensors/` and `ingest/` (with what Eugene needs to run the broker on AWS).

## Why

Lab 12 Parts A–B, and every later part (bridge, DB, ML, dashboard) needs realistic readings in all three domains.

## How to check
```bash
pip install -r contracts/requirements.txt -r sensors/requirements.txt
python3 -m unittest discover sensors/tests -v                    # 6 tests OK
docker compose -f ingest/compose.yaml up -d
docker compose -f ingest/compose.yaml exec mosquitto mosquitto_sub -t 'accra/#' -v &
python3 sensors/simulator.py --ticks 36 --speed 20                # readings appear in the subscriber
docker compose -f ingest/compose.yaml down
```

## AI use
- **Tool:** Claude Code
- **What it did:** wrote the broker config, simulator, tests, READMEs, learnings note and this file; ran the broker and simulator and captured the evidence; found and fixed two failure-path bugs (crash on broker outage, first readings lost at start-up) by testing them.
- **Prompts / session summary:** "you can start work on each one" (the queue from the setup handoff: process fixes, #18, #13). The value ranges (PM2.5, fill rate, drain levels) are Claude's estimates, not measurements.
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- none (builds on decision 2)

## Not done
- Per-device passwords and ACL (#21); bridge and buffering (#20); OpenAQ feeder (#19).
- Simulated values are plausible, not calibrated against Accra data; #19 brings real PM2.5 to compare.
