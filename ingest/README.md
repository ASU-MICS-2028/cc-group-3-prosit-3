# Ingest

- **Owner:** Joseph
- **Purpose:** MQTT broker config, the bridge from MQTT to the message broker and time-series DB, local buffering through outages, per-device credentials and revocation.
- **Builds against:** contracts/sensor-reading, contracts/mqtt-topics, contracts/storage

## Broker (#18)

Mosquitto 2.0 in Docker, published on `localhost:1883` only.

```bash
python3 ingest/devices.py init                     # passwords + ACL, see "Device credentials" below
docker compose -f ingest/compose.yaml up -d mosquitto
docker compose -f ingest/compose.yaml exec mosquitto mosquitto_sub -u bridge \
  -P "$(awk -F, '$1=="bridge" {print $2}' ingest/device_credentials.csv)" -t 'accra/#' -v
docker compose -f ingest/compose.yaml down
```

No anonymous clients. The `chown: ... Read-only file system` line at start-up is the image's entrypoint and harmless.

**For AWS (Eugene):** image `eclipse-mosquitto:2.0.20`, port 1883/tcp (8883 once TLS is added), config file mounted at `/mosquitto/config/mosquitto.conf`, no persistent storage needed, tiny (measured 2.6 MiB RAM, 0.07 % CPU with all 11 devices publishing at `--speed 10`). Mount the whole `mosquitto/` folder (config, `passwd`, `acl`), owned by uid 1883 and mode 600. Plain MQTT for now: add TLS on 8883 before it faces the internet.

## Bridge (#20)

`bridge.py` subscribes to `accra/+/+/+` (QoS 1, persistent session), checks every reading against the contract and against its topic (a device can't post as another device or neighbourhood), appends it to `ingest/spool.jsonl`, and writes the spool to TimescaleDB in batches once a second. If the DB is down the spool grows; when it is back the backlog goes in first. Repeats are ignored because `(device_id, ts)` is unique.

```bash
cp ingest/.env.example ingest/.env                 # set a password; .env is never committed
docker compose -f ingest/compose.yaml --env-file ingest/.env up -d    # broker + TimescaleDB with dev tables
pip install -r ingest/requirements.txt
set -a; . ingest/.env; set +a
export MQTT_USERNAME=bridge MQTT_PASSWORD="$(awk -F, '$1=="bridge" {print $2}' ingest/device_credentials.csv)"
DATABASE_URL="postgresql://smartcity:${POSTGRES_PASSWORD}@localhost:5432/smartcity" python3 ingest/bridge.py
python3 sensors/simulator.py --speed 30            # in another terminal
```

Buffering test (Lab 12 Part C): `PY=python3 bash evidence/lab12/20-outage-run.sh` stops the DB for ~12 s mid-run, then checks every published reading was stored with no `seq` gaps. Result in `evidence/lab12/20-*.txt`: 289 published, 289 stored, 0 missing.

`dev-schema.sql` is a stand-in shaped by `contracts/storage.md`; the real schema is Elise's (#22). Tests: `python3 -m unittest discover ingest/tests -v`.

## Device credentials (#21)

Every device signs in with its own username (its `device_id`) and its own random password. The ACL lets a device **write only its own topic** (`accra/<neighbourhood>/<domain>/<device_id>`) and read nothing; the bridge may only read `accra/#`. Anyone else, anonymous included, is refused.

`python3 ingest/devices.py init` makes a password for the bridge and every device in the simulator's `FLEET`, and writes three gitignored, owner-only files: `mosquitto/passwd` (hashed by `mosquitto_passwd`), `mosquitto/acl`, and `device_credentials.csv` (plain passwords for the simulator and bridge; on AWS these belong in Secrets Manager). Running `init` again replaces every password.

**Revoking one device** (e.g. a stolen sensor):

1. `python3 ingest/devices.py revoke <device_id>`. This removes its password and ACL entry, then sends the broker `SIGHUP`.
2. On reload Mosquitto disconnects the device at once, and refuses it from then on (`not authorised`). Nothing else reconnects.
3. Check: `docker compose -f ingest/compose.yaml logs mosquitto | grep <device_id>`. You should see `disconnected, not authorised`.
4. To bring a replacement online, run `init` again and restart the devices (or add the device back to `FLEET` first).

Drill (Lab 12 Part E): `PY=python3 bash evidence/lab12/21-revocation-drill.sh` runs the bridge and simulator and revokes `aq-nima-001` 25 s in. Result in `evidence/lab12/21-*.txt`: aq-nima-001 stops at 8 readings, its reconnects are refused and its later readings dropped; the other 10 devices store all 20 readings each (208 published, 208 stored).
