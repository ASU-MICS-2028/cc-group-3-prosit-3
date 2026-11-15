---
title: Four places to run ML: cloud, separate CPU+GPU, CPU-only, or a single-chip edge device
tags: [edge, ml, cloud-basics]
source: Lecture 10
---

The lecturer framed four options for running models:
1. Cloud: powerful, but fails when the network is down and raises privacy concerns.
2. System with a separate CPU and GPU: very fast, but power hungry.
3. CPU-only: cheap and low power, but slow.
4. Edge device with CPU and GPU on one chip: fast, energy efficient, and a sweet spot, but needs software that exploits shared memory.

For SmartCity Accra, sensors sit across a city with uneven connectivity and power, so the choice between running forecasts at the edge or in af-south-1 is a trade of latency, power, cost and data movement. The lecturer also said small devices should be called "AI devices" once they can run models.

## Related
- [Edge devices with CPU and GPU on one chip share memory, enabling zero-copy inference](edge-ai-shared-memory-zero-copy.md)
- [IoT loop: sense at the edge, communicate over MQTT to a central store, compute and control](iot-sense-communicate-compute-control.md)
