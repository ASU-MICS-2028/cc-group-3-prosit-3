---
issue: 73
title: One container image for the API, bridge, alert checker and simulator
date: 2026-11-28
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `Dockerfile` (repo root) and `.dockerignore`. The `.dockerignore` is an allow-list.
  - One 242 MB image, running as user `app`, holding 12 runtime files.
  - The command picks the process: API (the default), bridge, alert checker or simulator.
- `ingest/compose.yaml`: `--profile app` runs the bridge, API and alert checker from that image next to the broker and DB. The DB has a health check that the app services wait for.
- `ingest/mosquitto/mosquitto.conf`: `max_queued_messages 100000`. The default of 1000 made the broker drop readings when the bridge fell behind: 1,565 of 2,214 stored before the fix, 2,214 of 2,214 after.
- `ingest/README.md`: a "Containers" section, with a table for #28 and #35 listing each process's command, env vars, port or volume, secrets and health check.
- `learnings/mosquitto-drops-queued-messages-past-1000.md`.
- Evidence: `evidence/lab12/73-container-run.sh` and `73-*.txt`.

## Why

Eugene deploys each part "from its owner's package" (#28, #35), and the bridge and API had none. The broker fix matters on its own: our buffering only covered a database outage, and a slow or restarting bridge could lose readings past 1,000 queued.

## How to check
```bash
PY=python3 bash evidence/lab12/73-container-run.sh   # needs Docker and ingest/.env
cat evidence/lab12/73-image-check.txt evidence/lab12/73-pipeline-run.txt
```
- The image check lists only code and contracts, with no credentials.
- The pipeline run shows the published count equal to the rows stored.

## AI use
- **Tool:** Claude Code
- **What it did:**
  - Wrote the Dockerfile, the compose services, the evidence script and the README section, then ran it.
  - Found that readings were going missing and read the broker log ("Outgoing messages are being dropped").
  - Raised the queue limit, re-ran the test and wrote the learnings note.
- **Prompts / session summary:** "go ahead with the containers".
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- none (one image for every process is recorded in the Dockerfile header)

## Not done
- AWS deployment (#28, #35, Eugene).
- Broker persistence on AWS, noted in the README for #28.
- A `/health` endpoint, which would be a contract change.
