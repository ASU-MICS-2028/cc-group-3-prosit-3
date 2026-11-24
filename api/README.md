# API

- **Owner:** Joseph
- **Purpose:** REST API for the web and mobile apps: readings, alerts, citizen reports, open data, and the prediction endpoint.
- **Builds against:** contracts/api, contracts/storage

## Run it (#31)

```bash
docker compose -f ingest/compose.yaml --env-file ingest/.env up -d   # TimescaleDB (see ingest/README.md)
pip install -r api/requirements.txt
set -a; . ingest/.env; set +a
DATABASE_URL="postgresql://smartcity:${POSTGRES_PASSWORD}@localhost:5432/smartcity" python3 api/app.py
curl 'http://localhost:8000/readings/latest?domain=air_quality'
```

For data, run the bridge and simulator (ingest/README.md). `--speed 0` fills two days in under a minute.

`app.py` serves every path in [`contracts/api.openapi.yaml`](../contracts/api.openapi.yaml), using Python's standard HTTP server plus psycopg. It reads the bridge's tables and creates its own (`schema.sql`: `alerts`, `citizen_reports`, `predictions`) at start-up.

| Path | Notes |
|---|---|
| `GET /readings/latest` | one reading per device; `domain`, `neighbourhood` filters |
| `GET /readings` | `device_id`, `from`, `to` required; `interval=1h` for hourly aggregates |
| `GET /alerts` | from the `alerts` table; flood rules that fill it are #25 |
| `GET /predictions/pm25` | `station` = an `aq-` device, `horizon_h` 24 or 48 |
| `POST /reports` | checked against `CitizenReport`; unknown fields such as a phone number are refused |
| `GET /open-data/{domain}` | hourly per neighbourhood, no device ids; default last 7 days |

Errors are JSON `{"error": "..."}`: 400 bad input, 404 unknown device or path, 503 database down.

**Forecast.** Until Elise's model is registered (#30), `/predictions/pm25` serves a naive baseline. Each future hour gets the hourly mean from the same hour a day earlier, or two days earlier for the second day of a 48 h forecast. With no history that far back it uses the latest hour. `model_version` says `naive-seasonal-24h`. To switch to the real model, change `forecast()` and `MODEL_VERSION`. The response shape stays the same. Every point served goes into `predictions`, so the drift log (#32) can compare it with what was measured.

**Before AWS (#35):** sign-in and a rate limit on `POST /reports` (auth is still open in the contract), CORS narrowed to the dashboard's domain, a connection pool if the load test asks for one.

Evidence: `PY=python3 bash evidence/lab13/31-api-run.sh` loads ~50 h of simulated readings, calls every endpoint plus the error cases, and stops the DB for the last call. Output in `evidence/lab13/31-*.txt`.

Tests: `python3 -m unittest discover api/tests -v` (forecast and report validation; needs `contracts/requirements.txt`).
