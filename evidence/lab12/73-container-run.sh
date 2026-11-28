#!/usr/bin/env bash
# #73: build the one SmartCity image, check what's inside it, run the whole pipeline in containers
# (broker, DB, bridge, API, alert checker), feed it 3 simulated hours, then call the API.
# Run from the repo root with $PY = a python that has ingest/ requirements (for devices.py init).
set -u
PY=${PY:-python3}; E=evidence/lab12
"$PY" ingest/devices.py init >/dev/null
set -a; . ingest/.env; set +a
MQTT_PASSWORD=$(awk -F, '$1 == "bridge" {print $2}' ingest/device_credentials.csv); export MQTT_PASSWORD
dc() { docker compose -f ingest/compose.yaml --env-file ingest/.env --profile app "$@"; }
dc down -v >/dev/null 2>&1

{
echo '$ docker build -t smartcity:local .'
docker build -q -t smartcity:local . >/dev/null && echo "built"
echo; echo '$ docker image ls smartcity:local'
docker image ls smartcity:local --format '{{.Repository}}:{{.Tag}}  {{.Size}}'
echo; echo '$ docker run --rm smartcity:local sh -c "whoami; find /app -type f | sort"'
docker run --rm smartcity:local sh -c "whoami; find /app -type f | sort"
echo; echo '# any credential, password, ACL or .env file anywhere in the image? (expect none)'
docker run --rm smartcity:local sh -c "find / -xdev \( -name '*credentials*' -o -name passwd.mosq -o -name acl -o -name '.env' -o -name 'spool.jsonl' \) -path '/app/*' 2>/dev/null; echo done"
} > $E/73-image-check.txt 2>&1

dc up -d --wait >/dev/null 2>&1; sleep 3   # --wait: until the DB is healthy and every service is up
# the simulator, also from the same image, on the compose network: 3 simulated hours as fast as it can
docker run --rm --network ingest_default -v "$PWD/ingest/device_credentials.csv:/run/creds.csv:ro" smartcity:local \
  python sensors/simulator.py --host mosquitto --creds /run/creds.csv --ticks 1080 --speed 0 --seed 73 \
  2> $E/73-simulator-stderr.txt | wc -l | tr -d ' ' > $E/73-published-count.txt
sleep 10

B=http://localhost:8000
{
echo '$ docker compose --profile app ps'
dc ps --format '{{.Service}}  {{.Image}}  {{.Status}}'
echo; echo '$ curl /readings/latest?domain=flood'; curl -s "$B/readings/latest?domain=flood"; echo
echo; echo '$ curl /readings/latest?neighbourhood=nima'; curl -s "$B/readings/latest?neighbourhood=nima"; echo
echo; echo '$ curl /alerts'; curl -s "$B/alerts"; echo
echo; echo "published by the simulator: $(cat $E/73-published-count.txt) readings"
echo '$ psql: rows stored per table'
dc exec -T timescaledb psql -U smartcity -c "SELECT 'air_quality' AS tbl, count(*) FROM air_quality UNION ALL SELECT 'waste', count(*) FROM waste UNION ALL SELECT 'flood', count(*) FROM flood;"
echo '$ docker compose logs bridge api alerts (last lines)'
dc logs --no-log-prefix --tail 4 bridge api alerts
} > $E/73-pipeline-run.txt 2>&1

dc down -v >/dev/null 2>&1
