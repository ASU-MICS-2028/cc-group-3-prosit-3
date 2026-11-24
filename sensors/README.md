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

## OpenAQ feeder (`openaq.py`, #19)

Publishes the last 24 h of **real** PM2.5 from Madina Zongo Junction (OpenAQ location 3025587, a low-cost sensor in Madina) as device `aq-madina-001` on `accra/madina/air_quality/aq-madina-001`. It uses the same schema and broker as the simulator, with `source: "openaq"`. `devices.py init` gives it a password like any other device.

```bash
python3 sensors/openaq.py --dry-run    # print them
python3 sensors/openaq.py              # publish (broker and bridge running)
```

It reads OpenAQ's public S3 archive, which needs no API key. The v3 API needs one, and we don't have one. The archive runs a few days behind, so "last 24 h" means the 24 h before the station's newest archived reading, with the timestamps as measured. `--location` picks another station.

**Real vs simulated** (`PY=python3 bash evidence/lab12/19-openaq-run.sh`; output in `evidence/lab12/19-query-output.txt`):

| | Real (Madina) | Simulator (5 stations) |
|---|---|---|
| Readings in 24 h | 35, irregular | 1,384 each, one a minute |
| Mean | 24.5 µg/m³ | 52.7 to 66.9 |
| Std dev | 8.4 | 13.7 to 13.9 |
| Range | 14.9 to 61.9 | 25.1 to 110.6 |
| Mean step between readings | 4.9 | 5.5 to 5.9 |

The real station was less than half as polluted and about 40 % less variable than the simulator. That's mostly because the simulator applies its harmattan ×1.8 from 1 November, and the real air hadn't caught up by 18 to 19 November. Reading-to-reading jumps are similar (about 5 µg/m³), so the noise term is about right, but the real sensor reports only every ~17 min with gaps, which the dashboard and the forecast must tolerate.

One station and one day is not enough to recalibrate the simulator, so the knobs are unchanged.

Next: flood alerts (#25).
