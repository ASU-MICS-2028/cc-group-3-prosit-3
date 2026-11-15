---
title: Federated learning with edge-level averaging keeps data local
tags: [ml, edge, privacy]
source: Lecture 9
---

Centralised learning sends all data to one server. Federated learning trains on each client and shares only model updates, which are averaged. The reviewed skin-cancer paper added a middle layer: models are averaged on edge servers first, then at the global server, cutting training time and keeping patient data in the hospitals.

Reviewer caveats: tested with only four simulated clients in Google Colab; interpretability and uneven (heterogeneous) data across clients remain unsolved.

For SmartCity Accra: a way to train across many sites or sensors without moving raw data, and it fits an edge-gateway tier.

## Related
- [Nano services on IoT sensors and the cache eviction choice](nano-services-iot-lru-vs-lfu.md)
- [Deadline-aware GPU scheduling across mixed GPU types](gpu-deadline-scheduling-mixed-gpus.md)
