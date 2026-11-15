---
title: Lab 12 Part A: install Mosquitto and subscribe to accra/# to see all sensor topics
tags: [lab, mqtt, iot]
source: Lab 12 (week12_lab_Students) Part A
---

Without a managed IoT platform, run the open-source Mosquitto broker: install mosquitto and mosquitto-clients, enable the service, then mosquitto_sub -h localhost -t "accra/#" -v to watch every topic under accra/. Lab 12's topic style is accra/<neighbourhood>/<domain>/<measure>, for example accra/eastlegon/airquality/pm25.

## Related
- [If the MQTT broker refuses connections, check mosquitto.conf listener settings](mosquitto-listens-localhost-only-by-default.md)
- [A paho-mqtt script publishing a JSON reading every 5 seconds stands in for real hardware](sensor-simulator-mqtt-publisher.md)
- [Lab 12 overview: MQTT sensor to broker to time-series DB to live chart, with buffering and device security](lab-12-iot-sensor-pipeline.md)
