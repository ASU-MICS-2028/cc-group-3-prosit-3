---
title: If the MQTT broker refuses connections, check mosquitto.conf listener settings
tags: [lab, mqtt]
source: Lab 12 (week12_lab_Students) Troubleshooting
---

Lab 12 troubleshooting: Mosquitto may listen only on localhost by default, so remote devices cannot connect until mosquitto.conf allows the interface and port you use.

## Related
- [Lab 12 Part A: install Mosquitto and subscribe to accra/# to see all sensor topics](mosquitto-local-mqtt-broker-setup.md)
