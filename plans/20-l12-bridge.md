# Plan: MQTT bridge with local buffering (L12-C)

- **Issue:** #20
- **Owner:** Joseph (`josetseph`)
- **Milestone:** Lab 12
- **Status:** done in this PR (stacked on #18's PR)

## Goal
Carry readings from MQTT into storage, surviving outages (Lab 12 Part C, 35% + 20%).

## What gets built
- `ingest/bridge.py`: subscribes to `accra/+/+/+` (QoS 1, persistent session), validates each reading against the contract and checks it matches its topic, appends it to a local spool file, and writes the spool to the DB in batches every second (`ON CONFLICT (device_id, ts) DO NOTHING`). DB down: the spool grows; DB back: the backlog goes in first.
- `ingest/compose.yaml`: TimescaleDB added next to Mosquitto; `ingest/dev-schema.sql` makes the three tables from `contracts/storage.md` for local runs.
- `ingest/tests/test_bridge.py`, run in CI.

## Depends on
- #2 (contracts), #18 (broker, simulator)
- #7 decision: not made yet. Built on TimescaleDB, the Lab 12 handout's choice; only `Db.write` changes if #7 picks something else.

## Done when
- Bridge consumes MQTT and writes to the time-series DB in batches
- Stopping the DB buffers readings locally; they flush on recovery with none lost (demonstrated)

## Evidence to capture
- `evidence/lab12/20-*`: bridge log through a DB outage, simulator output, query showing every published reading stored with no `seq` gaps.

## Not doing
- The real schema, rollups and retention: Elise's #22. `dev-schema.sql` is a stand-in.
- Per-device passwords: #21.
- Container image for AWS: once #7 is decided, so it's packaged for the right DB.
