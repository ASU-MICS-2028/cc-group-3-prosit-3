---
title: Run each write in one transaction that first tells the database who is acting
tags: [databases, security, prosit-1, prosit-2]
source: Prosit 2 learnings/patient-record-service.md (section 2, step 1; section 6); Prosit 2 learnings/database.md (section 6); Prosit 1 docs/architecture-decisions.md ADR-013
---

Pattern (both prosits): the API wraps every write in `withTransaction(user, work)` that begins with `SELECT set_config('app.user_id', '<uuid>', true)`. A database trigger reads that setting to stamp the actor and write the audit row; with no actor the write is refused ("No acting user set").

Why: using `pool.query()` alone sends statements on random connections, so the actor setting may be lost; separate data and audit writes can disagree; a faked `x-user-id` header must never be the source. The user id comes from the verified token, and the practitioner is re-checked as active on every request.

The Lab 6 starter code had five flaws this fixes: audit foreign key broke 404 logging, forgeable header, no transaction, serial ids clashing with offline clients, editable audit log.

SmartCity: ingest workers should stamp a service identity the same way.

## Related
- [Put the safety rules in the database so psql and scripts cannot skip them](database-enforces-rules-not-only-the-api.md)
- [Ids created on the device make offline retries idempotent](client-generated-uuids-make-retries-safe.md)
