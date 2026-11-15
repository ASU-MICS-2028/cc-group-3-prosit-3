---
title: A paho-mqtt script publishing a JSON reading every 5 seconds stands in for real hardware
tags: [lab, mqtt, iot]
source: Lab 12 (week12_lab_Students) Part B
---

The lab starter creates a paho-mqtt client with the sensor ID as client_id and username, publishes {sensor_id, pm25 random 10-80, timestamp} to the sensor topic every 5 seconds, and disconnects on Ctrl+C. With real hardware (Raspberry Pi plus an air-quality or ultrasonic distance sensor for a bin fill level) only the random value line is replaced by a sensor read. Keep the same JSON schema so downstream storage and ML do not change.

## Related
- [Optional: feed 24 hours of real Accra PM2.5 from OpenAQ through the same MQTT pipeline](openaq-real-pm25-data-option.md)
- [Each device gets its own MQTT credential so one can be revoked alone](per-device-mqtt-credentials-and-revocation.md)
- [Lab 12 overview: MQTT sensor to broker to time-series DB to live chart, with buffering and device security](lab-12-iot-sensor-pipeline.md)
