# Plan: MQTT broker and three-domain sensor simulator (L12-A/B)

- **Issue:** #18
- **Owner:** Joseph (`josetseph`)
- **Milestone:** Lab 12
- **Status:** done in this PR

## Goal
Stand up the broker and simulate the sensors (Lab 12 Parts A–B), so the bridge, DB and ML work have realistic readings in all three domains.

## What gets built
- `ingest/compose.yaml` + `ingest/mosquitto/mosquitto.conf`: Mosquitto 2.0 on localhost:1883.
- `sensors/simulator.py`: 11 devices across 5 neighbourhoods, contract-shaped readings at QoS 1, one MQTT connection per device; air quality with diurnal and harmattan pattern, bin fill with collections, drain level with storms; `--speed`, `--seed`, `--ticks`, `--dry-run`.
- `sensors/tests/test_simulator.py`, run by the `contracts` CI job.

## Depends on
- #2

## Done when
- Mosquitto running; simulator publishes contract-shaped readings for air quality, waste and flood on a schedule
- mosquitto_sub output in evidence/lab12/

## Evidence to capture
- `evidence/lab12/18-simulator-publish.txt` and `18-mosquitto-sub.txt`: same 66 readings on both sides.
- `evidence/lab12/18-broker-outage-*.txt`: broker stopped for 5 s; simulator keeps running, logs dropped readings, `seq` gap shows.

## Not doing
- Per-device passwords and ACL: #21. Anonymous access is local only.
- Buffering on the simulated device: the bridge buffers (#20).
- `neighbourhood` field in the reading: it is in the topic and the storage layout already; adding it to API responses is a contract PR.
