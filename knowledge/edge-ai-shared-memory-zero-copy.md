---
title: Edge devices with CPU and GPU on one chip share memory, enabling zero-copy inference
tags: [edge, ml, lecture]
source: Lecture 10 (edge AI paper discussion)
---

A paper discussed in class showed that small edge boards (NVIDIA Jetson class) put CPU and GPU on one chip with one shared memory. Because both read the same memory, data does not need to be copied between them ("zero-copy"), which saves time and energy. The same idea is why Apple Silicon has unified RAM.

The engine in the paper tackled three problems: small memory, making the CPU help the few GPU cores (CPU-GPU synergy), and smart task splitting.
- Reader and writer on the same data: no copy. Two writers on the same data: copy to avoid conflict.
- Task split is measured once (time CPU part vs GPU part, try both ways, pick the fastest) and reused, since ML loops repeat. If copying the split result costs more than the GPU doing it alone, do not split.
- Reported results: beat CPU-only on every platform, about 55.8% speed gain, more energy and cost efficient, and faster than cloud.
- Weaknesses: older models only, no Transformers, NVIDIA chips only, and a Raspberry Pi is cheaper.

Why it matters for SmartCity Accra: forecasting at a gateway or edge node is a real option when the network is poor or data should stay local.

## Related
- [Four places to run ML: cloud, separate CPU+GPU, CPU-only, or a single-chip edge device](edge-vs-cloud-vs-cpu-gpu-tradeoffs.md)
- [Edge compute lets sensitive data be used locally instead of moved to the cloud](edge-inference-keeps-data-on-premises.md)
