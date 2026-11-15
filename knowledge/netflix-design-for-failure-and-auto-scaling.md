---
title: Netflix lesson - design for failure and auto-scale to demand
tags: [reliability, scaling, aws]
source: Lecture 2
---

Netflix runs almost entirely on AWS with no data centre of its own for streaming, serving hundreds of millions of streams. Two practices the lecture highlighted as transferable to a four-person student team:

- Design for failure: Chaos Monkey randomly kills production instances, and the system must tolerate it.
- Auto-scale relentlessly: capacity follows real-time demand instead of being provisioned for the worst-case peak.

It also shows a business built on rented infrastructure and open-source tools, with no physical servers.

For SmartCity Accra: test by killing a service instance and show the platform keeps ingesting readings.

## Related
- [Five essential characteristics of cloud computing](five-essential-cloud-characteristics.md)
- [The course is platform-agnostic - justify every provider choice](justify-provider-choice-platform-agnostic.md)
