---
title: A load balancer presents one virtual IP and translates to real servers
tags: [networking, scaling, lecture]
source: Lecture 9
---

Clients send traffic to a single virtual IP (VIP) owned by the load balancer, never to the individual servers' addresses. The balancer picks a backend and rewrites addresses, typically with NAT (network address translation). Analogy used in class: a hospital reception that routes each patient to a free consulting room.

In "full NAT" every request and every response passes through the balancer. That makes the balancer a data path, not just a router, so its load grows with total traffic and it must remember which server each connection went to.

For SmartCity Accra: this is what the AWS load balancer in front of the ingestion or API tier does; knowing the model explains why it becomes a bottleneck or cost item at high volume.

## Related
- [Direct server return (DNAT) versus full NAT](direct-server-return-dnat-vs-fnat.md)
- [Alibaba's next-generation load balancer takes the data path out of the balancer](nglb-full-bypass-load-balancer.md)
