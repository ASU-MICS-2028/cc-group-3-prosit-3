---
title: Firewalls should block persistent flooding sources to stop DDoS
tags: [lecture, security, networking]
source: Lecture 6
---

Many locally built systems follow ordinary software engineering (requirements, backend, database, UI) but skip network defence. The lecturer's point: configure firewalls so that when a connection keeps shooting packets at the server, that link can be blocked permanently, preventing a distributed denial of service.

Professionals plan for this; students often treat security as extra work.

For SmartCity Accra: use security groups, rate limiting and a managed shield or WAF in front of public endpoints.

## Related
- [Do not put frontend, backend and database on the same host](separate-tiers-across-hosts-and-networks.md)
- [Users and insiders are usually the weakest security link](users-are-weakest-security-link.md)
