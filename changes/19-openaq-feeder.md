---
issue: 19
title: OpenAQ feeder, 24 h of real Madina PM2.5 through the same pipeline
date: 2026-11-23
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `sensors/openaq.py`: pulls the station's last 24 h of PM2.5 from OpenAQ's public S3 archive (no API key) and publishes it as `aq-madina-001`, with the same topic, schema and broker as the simulator and `source: "openaq"`. It reuses the simulator's MQTT publisher.
- `ingest/devices.py`: the feeder gets its own password and ACL like any device.
- Tests: `sensors/tests/test_openaq.py` and an ACL case in `ingest/tests/test_devices.py`.
- Evidence: `evidence/lab12/19-openaq-run.sh` and output. 35 real readings (18 Nov 20:33 to 19 Nov 20:06 UTC) were published and all 35 stored, next to 24 h of simulator data.
- The real-vs-simulated comparison is in `sensors/README.md`. Learning: `learnings/openaq-archive-needs-no-key-but-lags-days.md`.

## Why

Lab 12 extension: real data through the pipeline, and a check on how realistic the simulator is.

## How to check
```bash
python3 -m unittest discover sensors/tests -v && python3 -m unittest discover ingest/tests -v
python3 sensors/openaq.py --dry-run
PY=python3 bash evidence/lab12/19-openaq-run.sh   # then read evidence/lab12/19-query-output.txt
```

## AI use
- **Tool:** Claude Code
- **What it did:** found the station, wrote the feeder, tests, evidence script, docs, note and this file, and ran the evidence.
- **Prompts / session summary:** "go ahead with #19". The v3 API refused without a key (401) and v2 is retired (410). A web search gave a candidate location id, and its archive file showed it was Madina, Accra.
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- Archive instead of the live API (no key; a few days old).

## Not done
- Recalibrating the simulator's harmattan start (one station-day is not enough).
- Running the feeder on a schedule.
