---
title: Google Cloud IoT Core, listed in the brief, was retired by Google in August 2023
tags: [prosit-3-brief, gcp, iot]
source: Prosit 3 brief (IoT Platform options); standard knowledge
---

The Prosit 3 brief (and launch deck resources) list Google Cloud IoT Core as an IoT platform option, but Google shut the service down in August 2023, so it cannot be chosen. Realistic replacements are AWS IoT Core, Azure IoT Hub, a self-run MQTT broker such as Mosquitto or EMQX, or Pub/Sub with a partner IoT platform. Mention this in the architecture justification instead of picking the retired service.

## Related
- [Teams must choose and justify IoT platform, protocol, edge hardware, pipeline and database](smartcity-architecture-decisions-required.md)
- [Lab 12 Part A: install Mosquitto and subscribe to accra/# to see all sensor topics](mosquitto-local-mqtt-broker-setup.md)
