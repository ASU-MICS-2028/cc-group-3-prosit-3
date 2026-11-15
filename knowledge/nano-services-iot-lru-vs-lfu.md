---
title: Nano services on IoT sensors and the cache eviction choice
tags: [iot, edge, security]
source: Lecture 9
---

A reviewed paper ran small services on ESP32 sensor nodes with Zero Trust, so each device only reaches what it needs and a compromised device stays an isolated event. Placing services on the sensor avoids multi-hop trips to the cloud, which cuts latency (wait time grows with number of hops).

When a sensor's memory fills, the paper evicts the least recently used service (LRU). The reviewer argued least frequently used (LFU) would keep popular services on the device; with LRU a service with 300 users can be evicted just because no request came recently, forcing slow trips through edge nodes.

For SmartCity Accra: a useful design question for what logic runs on sensors versus gateways versus cloud.

## Related
- [Federated learning with edge-level averaging keeps data local](federated-learning-at-the-edge.md)
- [Multi-cloud data recovery with erasure coding and encryption](multi-cloud-data-recovery-erasure-coding.md)
