#!/usr/bin/env bash
# #19: 24 h of real Madina PM2.5 from OpenAQ and 24 h of simulator PM2.5 through the same broker, bridge
# and DB, then compare their variability. Run from the repo root with the venv's python as $PY and ingest/.env set.
set -u
PY=${PY:-python3}; E=evidence/lab12
dc() { docker compose -f ingest/compose.yaml --env-file ingest/.env "$@"; }
"$PY" ingest/devices.py init >/dev/null   # includes aq-madina-001
set -a; . ingest/.env; set +a
export DATABASE_URL="postgresql://smartcity:${POSTGRES_PASSWORD}@localhost:5432/smartcity"
export MQTT_USERNAME=bridge
MQTT_PASSWORD=$(awk -F, '$1 == "bridge" {print $2}' ingest/device_credentials.csv); export MQTT_PASSWORD
dc up -d >/dev/null 2>&1; dc restart mosquitto >/dev/null 2>&1; sleep 3
dc exec -T timescaledb psql -q -U smartcity -c "TRUNCATE air_quality, waste, flood" >/dev/null
rm -f ingest/spool.jsonl
"$PY" ingest/bridge.py > $E/19-bridge-log.txt 2>&1 & BRIDGE=$!
sleep 2
"$PY" sensors/openaq.py > $E/19-openaq-publish.txt 2>&1
"$PY" sensors/simulator.py --ticks 8640 --speed 0 --seed 19 > /dev/null 2>&1   # 24 h
sleep 5
kill $BRIDGE; wait $BRIDGE 2>/dev/null
dc exec -T timescaledb psql -U smartcity -c "
-- step = mean absolute change between one reading and the next; hourly_sd = spread of the hourly means
WITH r AS (SELECT device_id, source, ts, pm25, abs(pm25 - lag(pm25) OVER (PARTITION BY device_id ORDER BY ts)) AS step
           FROM air_quality),
     h AS (SELECT device_id, avg(pm25) AS m FROM air_quality GROUP BY device_id, time_bucket('1 hour', ts))
SELECT r.device_id, source, count(*) AS readings, round(min(pm25)::numeric, 1) AS min, round(max(pm25)::numeric, 1) AS max,
       round(avg(pm25)::numeric, 1) AS mean, round(stddev(pm25)::numeric, 1) AS sd, round(avg(step)::numeric, 1) AS step,
       (SELECT round(stddev(m)::numeric, 1) FROM h WHERE h.device_id = r.device_id) AS hourly_sd
FROM r GROUP BY r.device_id, source ORDER BY source, r.device_id;" > $E/19-query-output.txt
dc down >/dev/null 2>&1
