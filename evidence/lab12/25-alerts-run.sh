#!/usr/bin/env bash
# #25: 24 simulated hours at 600x (about 2.5 min) through broker, bridge and DB, with the alert checker
# running every second, then GET /alerts from the API. Run from the repo root with $PY = the venv's python.
set -u
PY=${PY:-python3}; E=evidence/lab12; B=http://localhost:8000
dc() { docker compose -f ingest/compose.yaml --env-file ingest/.env "$@"; }
"$PY" ingest/devices.py init >/dev/null
set -a; . ingest/.env; set +a
export DATABASE_URL="postgresql://smartcity:${POSTGRES_PASSWORD}@localhost:5432/smartcity"
export MQTT_USERNAME=bridge
MQTT_PASSWORD=$(awk -F, '$1 == "bridge" {print $2}' ingest/device_credentials.csv); export MQTT_PASSWORD
dc up -d >/dev/null 2>&1; dc restart mosquitto >/dev/null 2>&1; sleep 3
"$PY" api/alerts.py --once >/dev/null   # creates the API's tables if this DB is new
dc exec -T timescaledb psql -q -U smartcity -c "TRUNCATE air_quality, waste, flood, alerts" >/dev/null
rm -f ingest/spool.jsonl
"$PY" ingest/bridge.py > /dev/null 2>&1 & BRIDGE=$!
"$PY" api/alerts.py --every 1 > $E/25-alerts-log.txt 2>&1 & CHECK=$!
sleep 2
"$PY" sensors/simulator.py --ticks 8640 --speed 600 --seed 25 > /dev/null 2>&1
sleep 4
kill $BRIDGE $CHECK; wait $BRIDGE $CHECK 2>/dev/null
"$PY" api/app.py > /dev/null 2>&1 & APP=$!
sleep 2
{ echo '$ curl /alerts'; curl -s "$B/alerts"; echo; echo; echo '$ curl /alerts?status=closed'; curl -s "$B/alerts?status=closed"; echo; } > $E/25-api-alerts.txt
kill $APP; wait $APP 2>/dev/null
dc exec -T timescaledb psql -U smartcity -c "
SELECT device_id, round(min(water_level_cm)::numeric) AS min_cm, round(max(water_level_cm)::numeric) AS max_cm, count(*) AS readings
FROM flood GROUP BY 1 ORDER BY 1;
SELECT device_id, kind, status, opened_at, closed_at, closed_at - opened_at AS lasted, reason
FROM alerts ORDER BY opened_at;" > $E/25-query-output.txt
dc down >/dev/null 2>&1
