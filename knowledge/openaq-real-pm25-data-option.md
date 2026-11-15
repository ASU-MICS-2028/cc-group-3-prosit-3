---
title: Optional: feed 24 hours of real Accra PM2.5 from OpenAQ through the same MQTT pipeline
tags: [lab, iot, ml]
source: Lab 12 (week12_lab_Students) homework extension
---

OpenAQ publishes historical and near-real-time air-quality data for Accra stations (the lab names Nima, Jamestown, Asylum Down) through a free public API. The extension pulls the last 24 hours for one station and publishes it with the same schema in place of the simulator, then compares real variability with the simulator's noise range in two sentences. It does not replace the synthetic dataset, which stays the controllable one.

## Related
- [A paho-mqtt script publishing a JSON reading every 5 seconds stands in for real hardware](sensor-simulator-mqtt-publisher.md)
- [Lab 12 overview: MQTT sensor to broker to time-series DB to live chart, with buffering and device security](lab-12-iot-sensor-pipeline.md)
