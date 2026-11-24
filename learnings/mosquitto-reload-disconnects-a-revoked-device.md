---
title: Revoke one MQTT device by deleting its password and sending Mosquitto SIGHUP; it is cut off at once
tags: [iot, security, mqtt]
source: Lab 12 Part E, issue #21 (evidence/lab12/21-*)
---

With Mosquitto 2.0's `password_file` and `acl_file`, revoking a device is: delete its line with `mosquitto_passwd -D`, drop its ACL entry, and send the broker `SIGHUP`. We expected an already-connected device to keep its session until it reconnected. In fact, on reload Mosquitto disconnects it straight away and then refuses every reconnect (`disconnected, not authorised`). The bridge and the other devices stayed connected throughout. In our drill the revoked sensor stopped at 8 readings and the other 10 stored all 20.

Two traps we hit:
- **A single-file bind mount** (`./passwd:/mosquitto/config/passwd`) keeps pointing at the old file once a tool replaces it. Mount the folder instead.
- **Python's `csv` writes `\r\n`.** A shell `awk` then read the password with a stray `\r`, and the broker refused it. Write with `lineterminator="\n"`.

Mosquitto also warns about world-readable `passwd`/`acl` files and says future versions will refuse them. Keep them at mode 600 and owned by the broker's uid (1883) on Linux.

## Related
- [Each device gets its own MQTT credential so one can be revoked alone](../knowledge/per-device-mqtt-credentials-and-revocation.md)
- [Paho raises on publish while the broker is down; catch it or the sensor dies](paho-publish-raises-while-broker-is-down.md)
- [Write every reading to a local spool first, so one path covers normal running and DB outages](bridge-writes-to-a-local-spool-first.md)
