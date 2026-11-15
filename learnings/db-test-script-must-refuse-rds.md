---
title: A destructive database test script must refuse production, even through a tunnel
tags: [databases, process, prosit-2]
source: Prosit 2 knowledge/sessions/2026-10-26-migration-safety.md; Prosit 2 learnings/database.md (section 4)
---

The schema test script drops and recreates a database. Its first guard checked the hostname, but an SSM tunnel makes RDS answer on `localhost`, so the check passed. Better guard: ask the server. Only RDS has a role called `rds_superuser`, so the script refuses any server that has it.

Other lessons from the same script:
- It builds its test database through the migration tool, so CI tests the migration tool on every PR.
- It overwrote the Lab 6 evidence file unless given another output path.
- If a GUI client has the test database open, the script cannot rebuild it.
- psql fills `:'variable'` only in input read from a file or stdin, not in `-c` commands.
- Make failure observable: a deliberately broken check proved the script exits with code 1 so CI goes red.

## Related
- [Apply SQL migrations through a logbook table with checksums and a baseline option](migration-logbook-with-checksums.md)
- [Put the safety rules in the database so psql and scripts cannot skip them](database-enforces-rules-not-only-the-api.md)
