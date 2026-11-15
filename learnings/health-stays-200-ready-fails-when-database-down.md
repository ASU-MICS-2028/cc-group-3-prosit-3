---
title: When the database is unreachable answer 503 with Retry-After; keep /health green, make /ready fail
tags: [reliability, monitoring, prosit-2]
source: Prosit 2 learnings/patient-record-service.md (If the database is unreachable); Prosit 2 learnings/infra.md (item 7)
---

The API gives up connecting after 5 s and a query after 15 s, then answers 503 with `Retry-After: 15`, not a hang and not a 500. `/health` (what the load balancer checks) stays 200 and never touches the database; `/ready` also checks the database and answers 503.

Reason: if `/health` failed, the load balancer would pull every server and turn "no database" into "no API". The app treats a 503 as a network error and keeps its records.

Also: 10 repeated `/health` calls showed both instance ids, proving the load balancer spreads traffic (the id comes from an `INSTANCE_ID` env var the start-up script must set). Failover test result honestly reported: removal in about 18 s, but about half the requests in the next minute failed (5/10), unexplained at submission.

SmartCity: apply the same split to the ingest API and the MQTT consumer.

## Related
- [Capture evidence honestly: report the real result, label what is faked, never rewrite history](honest-evidence-capture.md)
- [Sign-in and rate-limit choices that held up in the HealthConnect API](api-rate-limits-and-login-protection.md)
