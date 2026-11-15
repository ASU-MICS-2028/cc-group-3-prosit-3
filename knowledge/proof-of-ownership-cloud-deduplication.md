---
title: Deduplication with short hashes lets anyone who learns the hash claim a file; proof of ownership fixes it
tags: [storage, security, lecture]
source: Lecture 10 (paper presentation by a student group)
---

Deduplication stores one copy of identical files and gives each owner a pointer. Early schemes identify a file by a short hash, so possession of the hash is treated as ownership; anyone who learns the tag can fetch the file (a replay-style weakness).

The paper's fix: the server sends a fresh seed, and the client must compute an iterative hash over every block of the file, binding the proof to the whole file. Fresh seeds reduce replay value.
- Limitation: proof and verification time grow with file size.
- Future work: combine proof of ownership with proof of storage, encrypted deduplication, production-scale tests.

Relevance: a general lesson that an identifier is not a credential. Useful when thinking about device IDs and topic names in MQTT.

## Related
- [IoT loop: sense at the edge, communicate over MQTT to a central store, compute and control](iot-sense-communicate-compute-control.md)
