---
issue: 20
title: MQTT bridge with local buffering (Lab 12 Part C)
date: 2026-11-23
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `ingest/bridge.py`: MQTT → TimescaleDB. Every reading is checked against the contract and its topic, appended to a local spool file, and written to the DB in batches once a second; when the DB is down the spool grows and flushes on recovery. Persistent MQTT session, so the broker holds readings while the bridge itself is down.
- `ingest/compose.yaml`: TimescaleDB next to Mosquitto; password from `ingest/.env` (not committed; `.env.example` added). `ingest/dev-schema.sql`: the three tables from `contracts/storage.md`, for local runs only.
- `ingest/tests/test_bridge.py` (6 tests: rejects bad or spoofed readings, buffers through an outage and flushes in order, caps batches, survives a restart), added to the `contracts` CI job.
- `evidence/lab12/20-*`: the buffering test script and its output.
- `learnings/bridge-writes-to-a-local-spool-first.md`.

## Why

Lab 12 Part C: end-to-end pipeline (35%) and local buffering shown (20%).

## How to check
```bash
pip install -r contracts/requirements.txt -r ingest/requirements.txt
python3 -m unittest discover ingest/tests -v                      # 6 tests OK
cp ingest/.env.example ingest/.env                                # set a password
docker compose -f ingest/compose.yaml --env-file ingest/.env up -d
PY=python3 bash evidence/lab12/20-outage-run.sh                   # ~70 s
cat evidence/lab12/20-outage-timeline.txt evidence/lab12/20-query-output.txt   # 289 stored, 0 missing
```

## AI use
- **Tool:** Claude Code
- **What it did:** wrote the bridge, dev schema, compose changes, tests, test script, README section, learnings note, plan and this file; ran the buffering test. Caught and fixed during the work: the value column must be named after the metric (storage contract), paho's manual loop doesn't reconnect, and a zsh quirk that stopped the first outage test from stopping the DB.
- **Prompts / session summary:** "We can start working on the things we can reasonably do". #7 (broker and DB choice) isn't decided, so Claude built on TimescaleDB, the Lab 12 handout's choice.
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- none (TimescaleDB is provisional until #7)

## Not done
- Real schema, rollups, retention: #22 (Elise). Per-device passwords: #21. Container image for AWS: after #7.
- Stacked on #58 (#18): review that first; this PR's base switches to `main` when it merges.
