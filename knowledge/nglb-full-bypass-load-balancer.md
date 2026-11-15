---
title: Alibaba's next-generation load balancer takes the data path out of the balancer
tags: [networking, scaling, lecture]
source: Lecture 9
---

A student reviewed an Alibaba Cloud paper on a load balancer that stays off the data path. Problems with the old design: traffic through balancer clusters averaged about 1.8 Tbit/s, each balancer did packet and data work, dual-zone redundancy was hard to keep, and tracking every connection did not scale.

How the new design (NGLB) works: the balancer only handles connection setup. A small extra header is added to the first packets so the host virtual switch (AVS) and a kernel module on the backend (VCTK) learn each other's addresses; later packets go direct. The kernel module also handles multi-tenant isolation, since different customers' VPCs can reuse the same IP addresses.

Reported results: about 18 percent lower latency, flat latency under load, about 10 times more connections, and far fewer listeners for the same throughput. Open issues named by the reviewer: DDoS behaviour, and monitoring, because traffic no longer passes the balancer so telemetry must move to the server level.

## Related
- [Direct server return (DNAT) versus full NAT](direct-server-return-dnat-vs-fnat.md)
- [Per-service idle timeouts instead of one global timeout](per-service-idle-timeouts.md)
- [Dual-zone redundancy means each zone runs at about 50 percent](dual-zone-redundancy-50-percent-headroom.md)
