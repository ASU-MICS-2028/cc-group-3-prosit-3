---
title: Ids created on the device make offline retries idempotent
tags: [databases, edge, prosit-1, prosit-2]
source: Prosit 1 docs/architecture-decisions.md ADR-002; Prosit 2 docs/decisions.md D-011; Prosit 2 learnings/database.md (section 3)
---

Both prosits had phones that work offline and resend later. If the database makes the id, a lost reply plus a retry creates two records. Instead the device generates a UUID at creation and the server uses `INSERT ... ON CONFLICT (id)` (Prosit 1: a unique `client_id` mapped from error 23505).

Server answers: same id with identical data means it was a retry, return 200 with the original; same id with different data returns 409.

Extras: UUID primary keys avoid the serial-id clashes of the lab starter; the booking route answered 200 for a repeated booking, 409 `double_booked` for the same slot.

SmartCity: sensor messages should carry a device-generated message id (and timestamp) so a gateway resend or MQTT QoS 1 duplicate does not insert a second reading.

## Related
- [Events arrive at least once; claim the id with a conditional write before acting](at-least-once-events-need-idempotent-consumers.md)
- [Sync downloads with a running-number bookmark can skip records unless numbering is ordered](sync-bookmark-lock-avoids-skipped-records.md)
