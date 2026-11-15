---
title: Validate at front end, API and database; range limits catch impossible values
tags: [databases, security, prosit-2]
source: Lecture 11 (our Prosit 2 design)
---

We validated at every layer: if the front end or API misses something, the database still rejects it. Examples: clinical code ranges reject a 375 degree temperature; every write must carry a user id; the audit log cannot be written directly, only by the system; an exclusion constraint blocks double booking.

For SmartCity Accra: set plausible min/max for PM2.5, bin fill (0 to 100%) and water level at the database, so a faulty sensor cannot poison forecasts.

## Related
- [Client-generated IDs, record versions and cursor downloads make sync safe on flaky networks](idempotent-ids-and-versions-for-flaky-connectivity.md)
- [Three ways to make synthetic data: LLM prompts with a schema, GANs, or distribution parameters](synthetic-data-for-testing-without-real-data.md)
