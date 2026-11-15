---
title: Each device gets its own MQTT credential so one can be revoked alone
tags: [lab, security, mqtt]
source: Lab 12 (week12_lab_Students) Part E
---

Part E: confirm every simulated device has its own username/password, not a shared one, and document how to revoke one device without touching the rest of the fleet. The optional drill: actually delete or disable one device's credential, confirm it can no longer publish while the others keep working, and write down the exact steps. The starter simulator uses the sensor ID as username with a per-device secret (never commit real secrets).

## Related
- [A paho-mqtt script publishing a JSON reading every 5 seconds stands in for real hardware](sensor-simulator-mqtt-publisher.md)
- [Lab 12 overview: MQTT sensor to broker to time-series DB to live chart, with buffering and device security](lab-12-iot-sensor-pipeline.md)
