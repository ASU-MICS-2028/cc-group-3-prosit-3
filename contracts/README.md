# Contracts

**The shared formats every part builds against**, so nobody waits on anyone: the simulator, bridge, database, API, web dashboard, mobile app and ML work can all start on day one with fake data that matches these files.

Status: **draft v0**, proposed in [decisions/2-sensor-reading-and-topic-contract.md](../decisions/2-sensor-reading-and-topic-contract.md). Owner: Joseph. Changing a contract = its own PR with a decision file; tag the people it affects.

| File | What it fixes | Used by |
|---|---|---|
| [`sensor-reading.schema.json`](./sensor-reading.schema.json) | The JSON one device publishes: `device_id`, `domain`, `metric`, `value`, `unit`, `ts`, `seq` (+ optional `battery_pct`, `source`). Domain, metric and unit must match | sensors, ingest, db, ml |
| [`examples/`](./examples/) | One valid reading per domain; `examples/bad/` must fail | everyone (copy them into mocks) |
| [`mqtt-topics.md`](./mqtt-topics.md) | `accra/<neighbourhood>/<domain>/<device_id>`, QoS 1, one credential per device | sensors, ingest |
| [`api.openapi.yaml`](./api.openapi.yaml) | REST paths the apps call: latest readings, history, alerts, PM2.5 forecast, citizen reports, open data | api, web, mobile, ml |
| [`storage.md`](./storage.md) | One table per domain, `(device_id, ts)` unique, 90-day raw retention, hourly rollups | db, ingest, ml, api |

## Check it

```bash
pip install -r contracts/requirements.txt
python3 -m unittest discover contracts/tests -v
```

CI runs the same tests on every PR (job `contracts`).

## Mocking the API

Point a mock server at `api.openapi.yaml` (for example `npx @stoplight/prism-cli mock contracts/api.openapi.yaml`) to get fake responses before the real API exists.
