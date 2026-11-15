---
title: HealthConnect's known weak points, useful input for a consolidated architecture review
tags: [prosit-2, reliability, aws]
source: Prosit 2 knowledge/sessions/2026-10-27-architecture-diagram.md and 2026-11-09-aws-architecture-diagram.md; Prosit 2 learnings/infra.md (sections 5 and 6); Prosit 2 learnings/database.md (section 5)
---

Weaknesses the team listed (and left off the "before" diagram for the Lab 8 peer review, then showed honestly in the final diagram):
- One call server (rooms in memory), one NAT instance in one AZ, single-AZ database; no TURN relay.
- No outbox: a booking can be saved without its event being published.
- Dead-letter queues have no alarm; the specialist-notify function has no duplicate check.
- Migrations and Terraform applied by hand; one person at a time.
- Failover test: stopping one of two API servers dropped about half of the requests for a minute (unexplained).
- Photos and voice notes stored in Postgres until media uploads move to S3.
- No role-specific database users yet; admin can still read patient rows via one route.
- The audit trail grows forever with no retention rule.
- No WAF and no customer-managed KMS keys (accepted findings with reasons).

Lab 8's four questions are a good template for Lab 14: where does it break at 10x load, the weakest security link, what happens if the network or database drops, one open question.

## Related
- [HealthConnect AWS infrastructure inventory (deployed state, November 2026)](healthconnect-aws-infrastructure-inventory.md)
- [HealthConnect (Prosit 2) system overview: what was built and what was designed only](healthconnect-system-overview.md)
