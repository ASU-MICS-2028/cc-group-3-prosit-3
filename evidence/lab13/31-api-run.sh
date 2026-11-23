#!/usr/bin/env bash
# Lab 13 Part D (#31): fill the DB with ~50 h of simulated readings, start the API, call every endpoint.
# Run from the repo root with the venv's python as $PY (needs ingest/, sensors/ and api/ requirements)
# and ingest/.env set. Issues fresh MQTT passwords first, so a device revoked in an earlier drill is back.
set -u
PY=${PY:-python3}; E=evidence/lab13; PORT=8000
dc() { docker compose -f ingest/compose.yaml --env-file ingest/.env "$@"; }
"$PY" ingest/devices.py init >/dev/null
set -a; . ingest/.env; set +a
export DATABASE_URL="postgresql://smartcity:${POSTGRES_PASSWORD}@localhost:5432/smartcity"
export MQTT_USERNAME=bridge
MQTT_PASSWORD=$(awk -F, '$1 == "bridge" {print $2}' ingest/device_credentials.csv); export MQTT_PASSWORD
dc up -d >/dev/null 2>&1; dc restart mosquitto >/dev/null 2>&1; sleep 3
dc exec -T timescaledb psql -q -U smartcity -c "TRUNCATE air_quality, waste, flood" >/dev/null
rm -f ingest/spool.jsonl
"$PY" ingest/bridge.py > /dev/null 2>&1 & BRIDGE=$!
sleep 2
"$PY" sensors/simulator.py --ticks 18000 --speed 0 --seed 31 > /dev/null 2> $E/31-simulator-stderr.txt
sleep 5   # let the bridge flush
kill $BRIDGE; wait $BRIDGE 2>/dev/null

"$PY" api/app.py > $E/31-api-log.txt 2>&1 & APP=$!
sleep 2
# A hand-made alert row so /alerts has something to return; real flood alerts come from #25.
dc exec -T timescaledb psql -q -U smartcity -c "TRUNCATE alerts, citizen_reports, predictions;
  INSERT INTO alerts (kind, domain, neighbourhood, device_id, reason) VALUES
  ('flood_warning', 'flood', 'nima', 'fl-nima-001', 'TEST ROW: drain level 120 cm, above the 100 cm warning line')" >/dev/null

B=http://localhost:$PORT
call() {  # call <label> <curl args...>: request line, status, first 600 chars of the body
  echo "### $1"; shift
  echo "\$ curl ${*/$B/}"
  curl -s -w '\nHTTP %{http_code}, %{time_total}s\n' "$@" | cut -c1-600; echo
}
TO=$(date -u -v+3d +%FT%TZ 2>/dev/null || date -u -d '+3 days' +%FT%TZ)
FROM=$(date -u +%FT%TZ)
{
call "latest reading per device (air quality)" "$B/readings/latest?domain=air_quality"
call "latest in one neighbourhood" "$B/readings/latest?neighbourhood=nima"
call "raw history" "$B/readings?device_id=wb-makola-001&from=$FROM&to=$TO"
call "hourly history" "$B/readings?device_id=fl-nima-001&from=$FROM&to=$TO&interval=1h"
call "PM2.5 forecast, 24 h" "$B/predictions/pm25?station=aq-makola-001"
call "PM2.5 forecast, 48 h" "$B/predictions/pm25?station=aq-nima-001&horizon_h=48"
call "open alerts" "$B/alerts"
call "citizen report" -X POST -H 'Content-Type: application/json' \
  -d '{"category":"flooding","description":"Drain blocked near the market","lat":5.55,"lon":-0.21}' "$B/reports"
call "open data, per neighbourhood only" "$B/open-data/air_quality?from=$FROM&to=$TO"
echo "## errors"
call "forecast for a bin, not an air sensor" "$B/predictions/pm25?station=wb-makola-001"
call "unknown device" "$B/predictions/pm25?station=aq-nowhere-001"
call "bad horizon" "$B/predictions/pm25?station=aq-makola-001&horizon_h=12"
call "missing from/to" "$B/readings?device_id=aq-nima-001"
call "report with a phone number field" -X POST -H 'Content-Type: application/json' \
  -d '{"category":"waste","description":"x","lat":5.5,"lon":-0.2,"phone":"0240000000"}' "$B/reports"
} > $E/31-api-calls.txt

dc exec -T timescaledb psql -U smartcity -c "
SELECT 'air_quality' AS tbl, count(*) AS rows, min(ts), max(ts) FROM air_quality
UNION ALL SELECT 'waste', count(*), min(ts), max(ts) FROM waste
UNION ALL SELECT 'flood', count(*), min(ts), max(ts) FROM flood;
SELECT station, model_version, count(*) AS points_logged FROM predictions GROUP BY 1, 2;
SELECT category, description FROM citizen_reports;" > $E/31-query-output.txt

dc stop timescaledb >/dev/null 2>&1
call "database down" "$B/readings/latest" >> $E/31-api-calls.txt
kill $APP; wait $APP 2>/dev/null
dc down >/dev/null 2>&1
