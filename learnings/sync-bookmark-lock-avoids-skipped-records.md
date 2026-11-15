---
title: Sync downloads with a running-number bookmark can skip records unless numbering is ordered
tags: [databases, edge, prosit-2]
source: Prosit 2 learnings/patient-record-service.md (Real sync J2); Prosit 2 docs/decisions.md D-032, D-037
---

HealthConnect's `GET /sync/pull?since=N` hands out records changed after bookmark N, 100 at a time. Trap: if record 6 commits before record 5 finishes, a client can read past 5 and never get it. Fix: the last step of a push takes a lock held until COMMIT, so numbers appear in commit order. That step is one-at-a-time, the first place to look if load tests show queueing.

Second trap: a doctor's first visit with a patient. The patient's older records were numbered before the doctor's bookmark, so the first booking renumbers them; other phones receive them again and ignore them because the version is unchanged.

Other design points: push saves the exact FHIR copy in `sync_records` and the real table in one transaction; push answers `ok`, `duplicate`, `conflict` (with server copy), `retry` or `rejected` with a reason; the server decides who sees what and the app only displays it; a record with unsent local changes is never overwritten by a download.

## Related
- [Offline app design: save locally first, encrypt, queue, and let a person settle conflicts](offline-conflicts-are-shown-to-a-person.md)
- [Ids created on the device make offline retries idempotent](client-generated-uuids-make-retries-safe.md)
