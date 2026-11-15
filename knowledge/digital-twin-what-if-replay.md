---
title: Replay real sensor data against a hypothetical alert threshold and count the extra alerts
tags: [lab, iot, ml]
source: Lab 14 (week14_lab_Students) Part A Option 1
---

Script idea: load sensor_readings.csv, count readings above the current flood threshold (80 in the lab) and above a hypothetical one 20% lower (64), and print both counts and the difference. It is a small proof of concept of a digital twin: test a policy on recorded data before changing the real system. Fits the flood-level sensor.

## Related
- [Lab 14 overview: advanced feature test, capstone integration, final architecture doc, presentation](lab-14-advanced-feature-capstone-final-presentation.md)
- [Averaging two parties model weights may lose to a local model, and that is a legitimate result](federated-averaging-demo-honest-result.md)
