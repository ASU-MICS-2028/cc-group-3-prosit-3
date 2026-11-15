---
title: A load balancer cuts silent connections after 60 seconds, so ping every 25
tags: [networking, reliability, prosit-2]
source: Prosit 2 learnings/infra.md (items 8 and 9, section 6); Prosit 2 knowledge/sessions/2026-10-23-https-and-call-hosting.md; Prosit 2 learnings/lab7-webrtc.md
---

The ALB closes any connection silent for 60 s. A WebSocket whose owner is waiting (a caller waiting for the doctor) is silent, so without a keep-alive the other person joined an empty room. The signaling server now pings every connection every 25 s and drops those that stop answering. Tested: a caller idle for 90 s through the ALB stayed in the room.

Same applies to tunnels and any future live dashboard.

Related trap: the signaling server kept rooms in its own memory, so with two servers callers could land on different ones and never meet. It runs as exactly one server (a shared store such as Redis would lift that) and the ALB sends the call hostname to it via a host-header rule.

SmartCity: MQTT over WebSockets for a dashboard needs keep-alive intervals below the idle limit; and a stateful broker is not something to put behind a plain round-robin target group.

## Related
- [WebRTC results: direct paths worked, Chrome Slow 3G does not throttle media, TURN cost is a range](webrtc-testing-and-turn-findings.md)
- [HTTPS on the ALB with an ACM certificate when DNS lives outside Terraform](https-acm-certificate-with-external-dns.md)
