# Ingest

- **Owner:** Joseph
- **Purpose:** MQTT broker config, the bridge from MQTT to the message broker and time-series DB, local buffering through outages, per-device credentials and revocation.
- **Builds against:** contracts/sensor-reading, contracts/mqtt-topics, contracts/storage

## Broker (#18)

Mosquitto 2.0 in Docker, published on `localhost:1883` only.

```bash
docker compose -f ingest/compose.yaml up -d
docker compose -f ingest/compose.yaml exec mosquitto mosquitto_sub -t 'accra/#' -v
docker compose -f ingest/compose.yaml down
```

`mosquitto/mosquitto.conf` allows anonymous clients: **local dev only.** Per-device passwords and the ACL (each device publishes only to its own topic) come in #21. The `chown: ... Read-only file system` line at start-up is the image's entrypoint and harmless.

**For AWS (Eugene):** image `eclipse-mosquitto:2.0.20`, port 1883/tcp (8883 once TLS is added), config file mounted at `/mosquitto/config/mosquitto.conf`, no persistent storage needed, tiny (measured 2.6 MiB RAM, 0.07 % CPU with all 11 devices publishing at `--speed 10`). Not internet-facing until #21 is merged.

## Bridge (#20)

`bridge.py` subscribes to `accra/+/+/+` (QoS 1, persistent session), checks every reading against the contract and against its topic (a device can't post as another device or neighbourhood), appends it to `ingest/spool.jsonl`, and writes the spool to TimescaleDB in batches once a second. If the DB is down the spool grows; when it is back the backlog goes in first. Repeats are ignored because `(device_id, ts)` is unique.

```bash
cp ingest/.env.example ingest/.env                 # set a password; .env is never committed
docker compose -f ingest/compose.yaml --env-file ingest/.env up -d    # broker + TimescaleDB with dev tables
pip install -r ingest/requirements.txt
set -a; . ingest/.env; set +a
DATABASE_URL="postgresql://smartcity:${POSTGRES_PASSWORD}@localhost:5432/smartcity" python3 ingest/bridge.py
python3 sensors/simulator.py --speed 30            # in another terminal
```

Buffering test (Lab 12 Part C): `PY=python3 bash evidence/lab12/20-outage-run.sh` stops the DB for ~12 s mid-run, then checks every published reading was stored with no `seq` gaps. Result in `evidence/lab12/20-*.txt`: 289 published, 289 stored, 0 missing.

`dev-schema.sql` is a stand-in shaped by `contracts/storage.md`; the real schema is Elise's (#22). Tests: `python3 -m unittest discover ingest/tests -v`.

Next: per-device credentials (#21).
