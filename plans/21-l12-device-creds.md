# Plan: Per-device credentials and revocation drill (L12-E)

- **Issue:** #21
- **Owner:** Joseph (`josetseph`)
- **Milestone:** Lab 12
- **Status:** done in this PR

## Goal
Secure devices individually (Lab 12 Part E, 10%).

## What gets built
- `ingest/mosquitto/mosquitto.conf`: no anonymous clients, `password_file` + `acl_file`.
- `ingest/devices.py`: `init` (a random password per device and for the bridge, hashed by `mosquitto_passwd`, ACL generated from the simulator's `FLEET`) and `revoke <id>` (remove one, `SIGHUP` the broker).
- Simulator and bridge sign in with their own credentials.
- Revocation drill script and evidence; exact steps in `ingest/README.md`.

## Depends on
- #18 (broker, simulator), #20 (bridge); this PR is stacked on #62.

## Done when
- Each device has its own MQTT username/password and an ACL limited to its topic
- Revoking one device stops it publishing while others carry on; exact steps documented

## Evidence to capture
- `evidence/lab12/21-*`: drill timeline, broker log, simulator stderr, per-device query (revoked device stops at 8 readings, the other 10 store all 20).

## Not doing
- TLS (passwords cross the network in clear; fine on localhost, needed before the broker is internet-facing, #28).
- Re-adding a single device without re-running `init` (a `mosquitto_passwd -b` one-liner, added when a real device needs it).
- Mosquitto's dynamic-security plugin: a password file is enough at this size.
