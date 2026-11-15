---
title: Build images for the servers' CPU (linux/amd64) from an ARM Mac, and keep disk free
tags: [containers, process, prosit-2]
source: Prosit 2 learnings/infra.md (section 4 and section 6); Prosit 2 knowledge/sessions/2026-10-26-lab7-event-infra.md
---

Team laptops were ARM Macs; the `t3.micro` servers are x86, so images must be built with `--platform linux/amd64` or they will not start. (Prosit 1's NAT and database used ARM Graviton, which is why the NAT instance type matters separately.)

Docker (OrbStack) crashed twice at 96% disk during builds. Keep about 20 GB free; `docker builder prune -af` clears only the build cache (freed 1.9 GB).

Also: image pins the af-south-1 RDS certificate bundle, so `/ready` fails against a database in another region (`/health` is unaffected). Remove npm and corepack from the runtime image (the server only needs `node`); use `USER node`; tag with the commit SHA as well as latest. Image scan before push.

CI now builds so laptops are not the build path.

## Related
- [CI/CD shape that worked: test everything, scan, then deploy only what changed on merge to main](cicd-pipeline-shape-test-scan-deploy-changed.md)
- [What slowed the team down in Prosits 1 and 2, and how to avoid it in Prosit 3](what-slowed-the-team-down.md)
