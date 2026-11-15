---
title: Put the safety rules in the database so psql and scripts cannot skip them
tags: [databases, data-governance, prosit-2]
source: Prosit 2 learnings/database.md; Prosit 2 docs/decisions.md D-012, D-013, D-015, D-017; Prosit 2 docs/data-decisions.md
---

HealthConnect enforced these in Postgres (triggers, constraints, foreign keys), not only in the API:
- a reading needs a valid, unwithdrawn consent of the same patient;
- measurement codes come from a lookup table with unit and plausible range;
- no DELETE or TRUNCATE on clinical rows or logs: mark `entered-in-error` instead;
- who and when stamped by the database on every row, plus a change history (identity values redacted);
- an exclusion constraint (needs `btree_gist`) blocks double-booking.

Tests try each rule with one write that must fail and one that must pass (68 refused, 34 allowed by the end). The API's job is to turn database refusals into clear 409/403 responses, not 500s. A double-booking race can deadlock, so the booking routes take a lock per specialist first.

Gotchas: a superuser can disable triggers; audit tables grow forever and need a retention rule; app and database role names differ and the API translates.

SmartCity: device readings need similar guards (valid sensor, plausible range, no silent deletes).

## Related
- [Run each write in one transaction that first tells the database who is acting](transaction-sets-acting-user-for-audit.md)
- [HealthConnect's FHIR R4 schema: tables, FHIR resources, consent purposes and audit](../knowledge/healthconnect-fhir-shaped-schema-and-consent.md)
