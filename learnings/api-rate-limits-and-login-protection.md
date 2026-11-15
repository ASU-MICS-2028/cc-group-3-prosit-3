---
title: Sign-in and rate-limit choices that held up in the HealthConnect API
tags: [security, prosit-2]
source: Prosit 2 learnings/patient-record-service.md (Signing in J1); Prosit 2 docs/decisions.md D-026, D-036
---

- scrypt-hashed passwords (built into Node, slow on purpose); five wrong passwords lock the account for 15 minutes; wrong password and unknown user answer the same, in similar time.
- One-hour token plus a 30-day refresh token that works once and is stored only as a hash; reuse of a used one ends all that person's sign-ins.
- The role in the token is only for the app: the API looks the role up on every request, so deactivation works at once.
- Rate limits: 60 calls/minute on `/auth` and 600 on everything else per address per server; `/health` and `/ready` sit above the limiter. Added after CodeQL flagged every route. A load test from one machine must raise the limits or it gets refused.
- CORS allows only the app origin.
- Every login attempt goes in an append-only table.

Known gaps: the lock is per account, so someone can lock a known username on purpose; no password reset.

## Related
- [When the database is unreachable answer 503 with Retry-After; keep /health green, make /ready fail](health-stays-200-ready-fails-when-database-down.md)
- [A scan gate can turn red when no code changed; fix by bumping, not by deleting the scan](security-scan-gates-can-go-red-without-code-changes.md)
