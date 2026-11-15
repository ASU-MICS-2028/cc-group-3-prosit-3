---
title: Two ways to migrate a private database: on boot under an advisory lock, or by hand through an SSM tunnel
tags: [databases, ci-cd, prosit-1, prosit-2]
source: Prosit 1 docs/architecture-decisions.md ADR-013 and docs/data-tier.md; Prosit 2 learnings/infra.md (section 5)
---

The database sits in private data subnets, so CI cannot reach it directly.

- **Prosit 1:** every instance applies pending migrations on boot under a Postgres advisory lock, so a rolling deploy migrates exactly once and no bastion is needed.
- **Prosit 2:** migrations are run by hand through an SSM tunnel (`db/migrate.sh`); the service does not migrate on boot. The order matters: migrate first, then seed or deploy code that needs the new tables. Merging code first is safe only if old routes keep working.

Trade-off: boot migrations are hands-free but make every server start a migration risk; manual ones are safer for destructive changes but easy to forget. Either way keep the pipeline unable to change the database role.

SmartCity: choose one and write it as an ADR before the first deploy.

## Related
- [Apply SQL migrations through a logbook table with checksums and a baseline option](migration-logbook-with-checksums.md)
- [Deploy from GitHub Actions with OIDC, no stored keys, and trust only the main branch](github-oidc-deploy-role-limited-to-main.md)
