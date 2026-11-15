---
title: Edge compute lets sensitive data be used locally instead of moved to the cloud
tags: [edge, privacy, data-governance]
source: Lecture 10
---

The lecturer argued that edge hardware changes the "build ever bigger data centres" philosophy. Hospitals, for example, hold proprietary data that cannot leave the premises without patient consent, and getting consent from everyone is impractical. With local edge devices they can learn from the data on site. Data protection laws push in this direction (Ghana's Data Protection Act was cited; Europe is stricter, the US more liberal).

Related point: large data centres face public pushback (noise, environmental impact, "not in my backyard"), so shifting some compute to the edge is also a sustainability and social argument.

For SmartCity Accra: air, waste and flood readings are less sensitive than health data, but the same reasoning applies to anything tied to households or locations.

## Related
- [Edge devices with CPU and GPU on one chip share memory, enabling zero-copy inference](edge-ai-shared-memory-zero-copy.md)
- [Four places to run ML: cloud, separate CPU+GPU, CPU-only, or a single-chip edge device](edge-vs-cloud-vs-cpu-gpu-tradeoffs.md)
