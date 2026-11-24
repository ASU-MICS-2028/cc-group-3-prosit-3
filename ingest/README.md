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

Next: the bridge with local buffering (#20), per-device credentials (#21).
