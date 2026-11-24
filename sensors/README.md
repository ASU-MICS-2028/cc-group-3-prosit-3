# Sensors

- **Owner:** Joseph
- **Purpose:** Sensor simulator for the three domains (air quality, waste fill, flood level) and the OpenAQ feeder for real Accra PM2.5.
- **Builds against:** contracts/sensor-reading, contracts/mqtt-topics

## Simulator (`simulator.py`, #18)

11 devices in 5 neighbourhoods: 5 PM2.5 monitors, 4 bin fill sensors, 2 drain-level gauges. Each device has its own MQTT connection (client id and username = `device_id`) and publishes to `accra/<neighbourhood>/<domain>/<device_id>` at QoS 1.

| Domain | Model | Publishes |
|---|---|---|
| Air quality | Morning (07:30) and evening (19:00) traffic peaks, ×1.8 in harmattan (Nov–Feb), per-device offset, noise | every 60 s |
| Waste | Fills at the bin's rate (2.5–6 %/h), emptied at some point after 90 %, capped at 100 | every 60 s |
| Flood | Base level; a storm about every 7 h raises it by up to ~80 cm, then it drains back | every 60 s, every 10 s while rising |

Calibration knobs (offset, fill rate, base level) live in `FLEET` at the top of the file.

```bash
python3 ingest/devices.py init                     # one password per device (needs Docker)
docker compose -f ingest/compose.yaml up -d mosquitto   # broker on localhost:1883
pip install -r sensors/requirements.txt
python3 sensors/simulator.py                       # real time; Ctrl+C to stop
python3 sensors/simulator.py --speed 60            # an hour of city per minute
python3 sensors/simulator.py --dry-run --ticks 360 --speed 0   # no broker: print an hour of readings now
docker compose -f ingest/compose.yaml exec mosquitto mosquitto_sub -u bridge \
  -P "$(awk -F, '$1=="bridge" {print $2}' ingest/device_credentials.csv)" -t 'accra/#' -v   # watch
```

`--seed N` repeats a run exactly. If the broker goes down, readings made meanwhile are dropped (logged to stderr) and `seq` shows the gap; paho reconnects by itself. Each device signs in with its own password from `ingest/device_credentials.csv` (`--creds` to point elsewhere); see `ingest/README.md` for revoking one.

Tests: `python3 -m unittest discover sensors/tests -v` (needs `contracts/requirements.txt`): a simulated day validates against the schema, topics match, `(device_id, ts)` is unique, timing is right.

Next: the OpenAQ feeder (#19).
