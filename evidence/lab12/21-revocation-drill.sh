#!/usr/bin/env bash
# Lab 12 Part E revocation drill (#21): fresh per-device credentials, then bridge + simulator run while
# one device (aq-nima-001) is revoked mid-run. The others must keep publishing; the revoked one must stop.
# Run from the repo root with the venv's python as $PY (needs ingest/requirements.txt) and ingest/.env set.
set -u
PY=${PY:-python3}; E=evidence/lab12; VICTIM=aq-nima-001
dc() { docker compose -f ingest/compose.yaml --env-file ingest/.env "$@"; }
set -a; . ingest/.env; set +a
export DATABASE_URL="postgresql://smartcity:${POSTGRES_PASSWORD}@localhost:5432/smartcity"
export MQTT_USERNAME=bridge

"$PY" ingest/devices.py init > /dev/null 2>&1
dc up -d >/dev/null 2>&1; dc restart mosquitto >/dev/null 2>&1; sleep 3
dc exec -T timescaledb psql -q -U smartcity -c "TRUNCATE air_quality, waste, flood" >/dev/null
rm -f ingest/spool.jsonl
MQTT_PASSWORD=$(awk -F, '$1 == "bridge" {print $2}' ingest/device_credentials.csv) \
  "$PY" ingest/bridge.py > $E/21-bridge-log.txt 2>&1 & BRIDGE=$!
sleep 2
( sleep 25; echo "$(date -u +%T) revoking $VICTIM: python3 ingest/devices.py revoke $VICTIM"
  "$PY" ingest/devices.py revoke $VICTIM 2>&1 | grep -v -E "Killing|Killed"
  echo "$(date -u +%T) devices left in ACL: $(grep -c '^user ' ingest/mosquitto/acl) (bridge + 10)" ) > $E/21-drill-timeline.txt & DRILL=$!
"$PY" sensors/simulator.py --ticks 120 --speed 20 --seed 21 > $E/21-simulator-publish.txt 2> $E/21-simulator-stderr.txt
wait $DRILL
sleep 3
kill $BRIDGE; wait $BRIDGE 2>/dev/null
dc logs --no-log-prefix mosquitto 2>&1 | grep -E "$VICTIM" | grep -v "New connection" | tail -6 \
  | sed -E 's/from [0-9.]+:[0-9]+/from <host>/' > $E/21-broker-log.txt
dc exec -T timescaledb psql -U smartcity -c "
-- per device: the revoked one stops early, every other device runs to the end
SELECT device_id, count(*) AS readings, max(seq) AS last_seq, max(ts) AS last_reading
FROM (SELECT device_id, seq, ts FROM air_quality UNION ALL SELECT device_id, seq, ts FROM waste
      UNION ALL SELECT device_id, seq, ts FROM flood) r
GROUP BY device_id ORDER BY device_id;" > $E/21-query-output.txt
