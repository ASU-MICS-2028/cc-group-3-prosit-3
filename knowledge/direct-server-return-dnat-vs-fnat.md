---
title: Direct server return (DNAT) versus full NAT
tags: [networking, scaling, lecture]
source: Lecture 9
---

Three stages in the Alibaba load balancer paper, retold with the hospital analogy:
- Full NAT (FNAT): requests and responses both go through the balancer (you always return to reception).
- DNAT with direct server response (DSR): the TCP handshake and requests still go through the balancer, but responses go straight from server to client. Reported effect: about 80 percent less traffic through the balancer, since responses are usually the large part.
- Full bypass: only connection setup uses the balancer; the rest flows directly between client and server (next note).

The TCP connection is set up by SYN, SYN-ACK packets before data flows; the balancer's decision is made at that first step.

## Related
- [A load balancer presents one virtual IP and translates to real servers](load-balancer-virtual-ip-and-nat.md)
- [Alibaba's next-generation load balancer takes the data path out of the balancer](nglb-full-bypass-load-balancer.md)
