---
title: Threshold load balancing, stop at 75 percent and resume below 25 percent
tags: [scaling, cloud-basics, lecture]
source: Lecture 9
---

A reviewed paper balanced VM load with thresholds: a VM stops accepting new requests at 75 percent load and starts again once it falls under 25 percent, with the nearest data center chosen to cut response time. The two different levels (hysteresis) stop a VM flapping on and off.

Reviewer criticism: the numbers were found by trial and error and only in simulation, so there was no evidence they hold for real workloads.

Same idea appears in auto scaling: separate scale-out and scale-in thresholds and cooldowns prevent oscillation.

## Related
- [Dynamic VM scheduling by chaining five existing algorithms](dynamic-vm-scheduling-five-algorithms.md)
- [Cloud research relies on simulators because providers rarely share real data](simulators-vs-real-cloud-data.md)
