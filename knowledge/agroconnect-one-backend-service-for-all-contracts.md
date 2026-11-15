---
title: One backend service implements every contract (AgroConnect ADR-013)
tags: [prosit-1, containers, databases]
source: Prosit 1 docs/architecture-decisions.md ADR-013
---

The PWA was built against six contracts (farmers, auth, admin, payments, advice, listings) and a mock server with tests, while the real backend had four in-memory routes. Rather than create a service per contract (more ECR repos, target groups and listener rules for no gain), the team built one service `agroconnect-api` with a route module per contract.

Choices: port the mock's 89 contract tests into the backend so parity is proven; Postgres does integrity (unique `client_id`, audit trigger with actor from `set_config`); migrations on boot under an advisory lock; secrets by ARN; real integrations in test mode (Arkesel SMS, votex365 checkout with an HMAC-signed webhook); tests on PGlite by default and real Postgres 16 in CI.

Costs: one blast radius, one deploy; demo accounts with public passwords must be off before real data. Each route module can later be split behind the same path. HealthConnect repeated the choice (D-035).

## Related
- [HealthConnect keeps one API with route modules instead of sixteen services (D-035)](healthconnect-one-api-with-route-modules.md)
- [AgroConnect (Prosit 1) system overview: offline-first PWA, one API, Postgres, three-tier VPC](agroconnect-system-overview.md)
