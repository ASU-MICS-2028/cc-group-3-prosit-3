---
title: Attackers with a shell can hide their tracks, so protect and ship logs
tags: [lecture, security, monitoring]
source: Lecture 6
---

Operating systems log events and only administrators should read them, but an attacker with a shell on the server may intercept or alter log writing, so logs show logins yet not the file changes. In the incident discussed, grade changes were eventually visible in logs, though the lecturer noted logs can be removed.

Practical lesson: restrict log access, and keep copies off the machine being logged (central log service) so tampering is detectable.

For SmartCity Accra: send application and system logs to CloudWatch or similar so they survive a compromised instance.

## Related
- [Users and insiders are usually the weakest security link](users-are-weakest-security-link.md)
- [Do not put frontend, backend and database on the same host](separate-tiers-across-hosts-and-networks.md)
