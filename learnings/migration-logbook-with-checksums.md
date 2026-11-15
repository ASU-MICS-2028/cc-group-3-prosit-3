---
title: Apply SQL migrations through a logbook table with checksums and a baseline option
tags: [databases, process, prosit-2]
source: Prosit 2 learnings/database.md; Prosit 2 knowledge/sessions/2026-10-26-migration-safety.md; Prosit 2 AGENTS.md
---

Rule: never edit an applied migration; add a new numbered file. Prosit 2 made the tool enforce it (`db/migrate.sh`, table `schema_migrations`: name, time, who, sha256).

- Each run applies only files not in the logbook, in order, and stops at the first error; `--dry-run` lists what would run.
- Refuses when an applied file was edited or deleted, or when tables exist but the logbook is empty (tells you to `--baseline`).
- `--baseline 003` records 001-003 as applied without running them, for a database migrated before the logbook existed.
- A lower number arriving late still applies, so gaps in numbering are fine.

Known rare gap: each file commits on its own and the logbook row follows; if the connection drops between, the next run fails with "already exists" and the fix is to add the row by hand. One person should run migrations at a time (an advisory lock is the proper fix).

SmartCity: the time-series and metadata schemas need the same discipline from the first table.

## Related
- [A destructive database test script must refuse production, even through a tunnel](db-test-script-must-refuse-rds.md)
- [Two ways to migrate a private database: on boot under an advisory lock, or by hand through an SSM tunnel](migrations-on-boot-versus-by-hand.md)
