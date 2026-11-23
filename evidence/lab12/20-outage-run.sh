#!/usr/bin/env bash
# Lab 12 Part C buffering test (#20): bridge + simulator run while the DB is stopped for ~12 s.
# Run from the repo root with the venv's python as $PY (needs ingest/requirements.txt) and ingest/.env set.
set -u
PY=${PY:-python3}; E=evidence/lab12
dc() { docker compose -f ingest/compose.yaml --env-file ingest/.env "$@"; }
set -a; . ingest/.env; set +a
export DATABASE_URL="postgresql://smartcity:${POSTGRES_PASSWORD}@localhost:5432/smartcity"
dc exec -T timescaledb psql -q -U smartcity -c "TRUNCATE air_quality, waste, flood" >/dev/null
rm -f ingest/spool.jsonl
"$PY" ingest/bridge.py > $E/20-bridge-log.txt 2>&1 & BRIDGE=$!
sleep 2
( sleep 15; echo "$(date -u +%T) stopping DB"; dc stop -t 2 timescaledb >/dev/null 2>&1
  sleep 6; echo "$(date -u +%T) DB down; spool holds $(wc -l < ingest/spool.jsonl | tr -d ' ') readings"
  sleep 6; echo "$(date -u +%T) starting DB"; dc start timescaledb >/dev/null 2>&1 ) > $E/20-outage-timeline.txt & OUTAGE=$!
"$PY" sensors/simulator.py --ticks 150 --speed 30 --seed 20 > $E/20-simulator-publish.txt 2>&1
wait $OUTAGE
sleep 8   # let the bridge flush the backlog
echo "$(date -u +%T) spool after recovery: $(wc -l < ingest/spool.jsonl | tr -d ' ') readings" >> $E/20-outage-timeline.txt
kill $BRIDGE; wait $BRIDGE 2>/dev/null
dc exec -T timescaledb psql -U smartcity -c "
SELECT 'air_quality' AS tbl, count(*) AS rows, count(DISTINCT device_id) AS devices FROM air_quality
UNION ALL SELECT 'waste', count(*), count(DISTINCT device_id) FROM waste
UNION ALL SELECT 'flood', count(*), count(DISTINCT device_id) FROM flood;" > $E/20-query-output.txt
dc exec -T timescaledb psql -U smartcity -c "
-- seq gaps per device: 0 everywhere means no reading was lost
SELECT device_id, count(*) AS readings, min(seq), max(seq), max(seq) - min(seq) + 1 - count(*) AS missing
FROM (SELECT device_id, seq FROM air_quality UNION ALL SELECT device_id, seq FROM waste UNION ALL SELECT device_id, seq FROM flood) r
GROUP BY device_id ORDER BY device_id;" >> $E/20-query-output.txt
