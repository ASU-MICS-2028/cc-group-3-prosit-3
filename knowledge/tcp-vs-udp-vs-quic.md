---
title: TCP is reliable, UDP is fast and lossy, QUIC is Google's newer transport
tags: [lecture, networking]
source: Lecture 5
---

- **TCP**: reliable, ordered delivery; used for file downloads and anything that must arrive intact. Born from a US defence research network that needed supercomputers to share data reliably.
- **UDP**: no delivery guarantee but low overhead; video calls (e.g. Zoom) mostly use it because a few lost pixels are acceptable.
- **QUIC**: a newer protocol developed at Google to make internet traffic more efficient.

The lecturer also noted AI inference sends many tiny requests, which suits neither classic protocol well, so new transport work is under way. Treat that as context, not exam fact.

For SmartCity Accra: MQTT runs over TCP, which gives the reliability sensors need; very frequent, loss-tolerant telemetry could use UDP-based protocols if latency mattered more than completeness.

## Related
- [IPv6 is gradually replacing IPv4 and is what makes IoT addressing possible at scale](ipv6-and-iot.md)
- [In-memory data in a container is lost on restart; make it persistent](persistent-data-vs-in-memory-containers.md)
