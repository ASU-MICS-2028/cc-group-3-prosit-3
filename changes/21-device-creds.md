---
issue: 21
title: Per-device MQTT credentials and revocation drill (Lab 12 Part E)
date: 2026-11-23
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `ingest/mosquitto/mosquitto.conf`: anonymous clients refused; password file + ACL.
- `ingest/devices.py`: `init` gives the bridge and every simulator device its own random password (hashed by Mosquitto's `mosquitto_passwd`) and writes an ACL where each device may **write only its own topic** and the bridge may **only read** `accra/#`. `revoke <id>` removes one device and reloads the broker. All three output files are gitignored and mode 600.
- `sensors/simulator.py` reads each device's password (`--creds`) and logs refusals; `ingest/bridge.py` signs in with `MQTT_USERNAME`/`MQTT_PASSWORD` and no longer subscribes after a refused connection.
- `ingest/compose.yaml` mounts the whole `mosquitto/` folder, so a rewritten `passwd`/`acl` is seen on reload.
- Drill: `evidence/lab12/21-revocation-drill.sh` and its output. aq-nima-001 revoked 25 s in: it stopped at 8 readings, 5 reconnects refused, 12 readings dropped; the other 10 devices stored all 20 each (208 published, 208 stored).
- `evidence/lab12/20-outage-run.sh` passes the bridge's password now.
- `learnings/mosquitto-reload-disconnects-a-revoked-device.md`.

## Why

Lab 12 Part E, and `contracts/mqtt-topics.md` ("no shared credentials; publish only to its own topic"). The broker can't go on AWS without it.

## How to check
```bash
python3 -m unittest discover ingest/tests -v          # ACL rules
python3 ingest/devices.py init && docker compose -f ingest/compose.yaml --env-file ingest/.env up -d
PY=python3 bash evidence/lab12/21-revocation-drill.sh  # ~70 s; then read evidence/lab12/21-query-output.txt
```

## AI use
- **Tool:** Claude Code
- **What it did:** wrote `devices.py`, the config, simulator/bridge changes, the test, the drill script, the docs, the note and this file; ran the probes and the drill.
- **Prompts / session summary:** "yes, close them and start #21". Probes first: right password connects, wrong or anonymous is refused, a device writing to another device's topic is dropped, and a `SIGHUP` after revoking disconnects that device while the bridge stays connected. First drill run failed because the CSV had `\r\n` endings and the shell read the bridge password with a stray `\r`; fixed with `lineterminator="\n"`.
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- none

## Not done
- TLS on 8883 (before the broker is internet-facing, #28).
- Adding one device back without re-running `init`.
