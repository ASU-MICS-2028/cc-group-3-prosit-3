---
title: Delay and degraded quality of service count as an availability failure
tags: [security, reliability, lecture]
source: Lecture 3
---

A service does not have to be fully down to break availability. If a provider promises something like 99.9% uptime and fast turnaround, but users meet frequent delays or disruption, that deviation in quality of service is an availability issue, and users experience it as unreliability.

Causes the lecture gave: failure of interdependent support systems such as internet service, web hosting, communications or power irregularities. The user often cannot see the cause; the provider treats it as a security matter and should have backups and failover, and may compensate users (extra data, refunds) depending on the agreement.

For SmartCity Accra: this is the same idea as an SLA or SLO; track latency and error rate, not just "up or down".

## Related
- [Availability is about the system being up; accessibility is a different idea](availability-vs-accessibility.md)
- [Keep systems available with backups, redundancy and failover](availability-mechanisms-backup-redundancy-failover.md)
