---
title: Carried over from Prosits 1 and 2 (map)
tags: [process]
source: index of the notes below
---

AgroConnect and HealthConnect architecture, and the patterns and gotchas we reuse.

**Taught or given**

- [After Prosit 1 as a quick translation, Prosit 2 needs real engineering and database design](prosit-2-expects-engineering-and-database-design.md)

- [AgroConnect (Prosit 1) system overview: offline-first PWA, one API, Postgres, three-tier VPC](agroconnect-system-overview.md)

- [AgroConnect AWS infrastructure inventory: network, compute, data, security, observability, cost](agroconnect-aws-infrastructure-inventory.md)

- [AgroConnect mapped Ghana's Act 843 principles to concrete controls and listed its gaps](agroconnect-act-843-privacy-controls.md)

- [AgroConnect picked af-south-1 by measuring latency from Ghana (74 ms median)](agroconnect-region-selection-by-latency.md)

- [AgroConnect scales on ALBRequestCountPerTarget (500 per minute), not CPU](agroconnect-target-tracking-request-count-decision.md)

- [Clone and build a partner's repo to catch files that were never committed](partner-clone-build-catches-uncommitted-files.md)

- [Ground rules for community-engaged prosits (consent, sign-off)](agroconnect-community-ground-rules.md)

- [HealthConnect (Prosit 2) system overview: what was built and what was designed only](healthconnect-system-overview.md)

- [HealthConnect AWS infrastructure inventory (deployed state, November 2026)](healthconnect-aws-infrastructure-inventory.md)

- [HealthConnect disease surveillance: aggregated counts, a rule-based signal and human-confirmed alerts](healthconnect-surveillance-design.md)

- [HealthConnect event flow: appointment.created fans out to two independent Lambdas](healthconnect-event-flow-sns-sqs-lambda.md)

- [HealthConnect keeps one API with route modules instead of sixteen services (D-035)](healthconnect-one-api-with-route-modules.md)

- [HealthConnect PWA and sync architecture in one page](healthconnect-pwa-and-sync-architecture.md)

- [HealthConnect telemedicine: WebRTC with a signaling server and an audio-only fallback](healthconnect-telemedicine-call-architecture.md)

- [HealthConnect treats Ghana's Act 843 as the law and HIPAA only as a safeguards checklist](healthconnect-act-843-and-hipaa-stance.md)

- [HealthConnect's FHIR R4 schema: tables, FHIR resources, consent purposes and audit](healthconnect-fhir-shaped-schema-and-consent.md)

- [HealthConnect's known weak points, useful input for a consolidated architecture review](healthconnect-known-weak-points.md)

- [One backend service implements every contract (AgroConnect ADR-013)](agroconnect-one-backend-service-for-all-contracts.md)

- [Out-of-band AWS changes (drift) can silently block terraform apply and stall deployments](configuration-drift-blocks-terraform-apply.md)

- [Questions the instructor and peers asked at the Prosit 1 presentations](prosit-1-presentation-qa-themes.md)

- [Queue offline writes in IndexedDB and replay with Background Sync](background-sync-offline-write-queue.md)

- [Service worker plus manifest gives an installable, offline-rendering app shell](service-worker-cache-first-offline-shell.md)

- [Tests can pass for the wrong reason; test each rule separately and on real devices](tests-can-pass-for-the-wrong-reason.md)

- [The Prosit 2 brief: problem numbers, four weeks of asks, targets and assessment](prosit-2-brief-problem-and-assessment.md)

- [WebRTC - test across two networks because direct peer links often fail](webrtc-stun-turn-cross-network-testing.md)

- [What HealthConnect reused from AgroConnect, as a map for reusing both in SmartCity](prosit-1-to-2-reuse-map.md)

**Found out by doing** (in `learnings/`)

- [A destructive database test script must refuse production, even through a tunnel](../learnings/db-test-script-must-refuse-rds.md)

- [Apply SQL migrations through a logbook table with checksums and a baseline option](../learnings/migration-logbook-with-checksums.md)

- [Branch protection with one approval, and the traps of stacked pull requests](../learnings/branch-protection-and-stacked-pr-traps.md)

- [Build images for the servers' CPU (linux/amd64) from an ARM Mac, and keep disk free](../learnings/docker-build-for-the-servers-architecture.md)

- [Capture evidence honestly: report the real result, label what is faked, never rewrite history](../learnings/honest-evidence-capture.md)

- [Copy and trim Terraform modules from the previous prosit instead of rebuilding](../learnings/reuse-terraform-modules-across-prosits.md)

- [Events arrive at least once; claim the id with a conditional write before acting](../learnings/at-least-once-events-need-idempotent-consumers.md)

- [Infrastructure as Code has edges: Amplify hosting could not be fully created by Terraform](../learnings/amplify-terraform-github-app-gap.md)

- [Never stop a terraform apply half-way; recover with force-unlock and import](../learnings/terraform-interrupted-apply-recovery.md)

- [Put the team's working rules in AGENTS.md so every teammate's coding assistant follows them](../learnings/shared-agent-instructions-in-the-repo.md)

- [SNS fan-out to one SQS queue per consumer, batch size 1, dead-letter queue each](../learnings/sns-fanout-sqs-per-consumer-and-dlq.md)

- [Static PWA hosting: cache headers and how a new release reaches phones](../learnings/pwa-cache-headers-and-service-worker-updates.md)

- [Terraform state lives in a bootstrapped S3 bucket with native locking, shared across projects by key](../learnings/terraform-remote-state-s3-native-locking.md)

- [Two ways to migrate a private database: on boot under an advisory lock, or by hand through an SSM tunnel](../learnings/migrations-on-boot-versus-by-hand.md)

- [Use terraform apply -target for a one-off change, then do the full apply later](../learnings/terraform-target-for-one-off-applies.md)

- [What slowed the team down in Prosits 1 and 2, and how to avoid it in Prosit 3](../learnings/what-slowed-the-team-down.md)

## Related
- [Lectures by week (map)](map-lectures.md)

- [SmartCity Accra brief and our scope (map)](map-smartcity-brief.md)

- [Labs 0–14 (map)](map-labs.md)

- [Course facts (map)](map-course.md)
