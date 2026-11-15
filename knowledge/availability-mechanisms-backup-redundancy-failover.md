---
title: Keep systems available with backups, redundancy and failover
tags: [security, reliability, lecture]
source: Lecture 3
---

The lecture listed the common mechanisms for availability: backups, redundancy, and failover servers so that if one server fails another keeps the service running. Large providers keep copies of the same data in data centers spread across the world.

Related point: data loss (for example a crashed disk) is a security issue because it makes data unavailable, even though people rarely think of it that way. A service provider relying on interdependent support systems (internet, hosting, power) should have backups and failover for each.

For SmartCity Accra: run the broker, database and API in more than one availability zone, and keep backups of the time-series data.

## Related
- [Availability is about the system being up; accessibility is a different idea](availability-vs-accessibility.md)
- [Delay and degraded quality of service count as an availability failure](quality-of-service-deviation-is-availability-issue.md)
