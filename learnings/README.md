# Learnings

**What we found out by doing:** procedures, gotchas, approaches that worked or failed. One idea per note, from [`TEMPLATE.md`](./TEMPLATE.md). Facts we were taught go in [`../knowledge/`](../knowledge/README.md) instead.

Every note is listed below under a topic.

## Scaling, reliability and monitoring

- [A load balancer cuts silent connections after 60 seconds, so ping every 25](websocket-idle-timeout-needs-heartbeat.md)

- [Check that a service and instance type exist in af-south-1 before designing around it](check-service-availability-in-af-south-1.md)

- [Roll servers with instance refresh at MinHealthy 100 and MaxHealthy 200 to avoid downtime](rolling-deploy-instance-refresh-minhealthy-100.md)

- [The outbox gap: saving data then publishing can lose the event](outbox-pattern-for-lost-events.md)

- [Unconfirmed SNS email subscriptions are silently deleted after three days](alarm-email-subscriptions-expire-after-3-days.md)

- [When the database is unreachable answer 503 with Retry-After; keep /health green, make /ready fail](health-stays-200-ready-fails-when-database-down.md)

## Cost and sustainability

- [af-south-1 costs 29% more and emits about twice as much as us-east-1 for the same servers](af-south-1-costs-more-and-emits-twice-us-east-1.md)

- [Cost per user falls in the city-wide budget scenario](pilot-cost-per-user-falls-in-city-projection.md)

- [Cost tracking and teardown: what keeps billing and what to delete by hand](cost-tracking-and-teardown-checklist.md)

- [fck-nat instance versus managed NAT Gateway: about $3 versus $32 a month](fck-nat-vs-nat-gateway.md)

## IoT, edge and offline

- [Drain the offline queue in the background, with a Web Lock so only one runner sends](background-sync-with-web-locks.md)

- [Ids created on the device make offline retries idempotent](client-generated-uuids-make-retries-safe.md)

- [Offline app design: save locally first, encrypt, queue, and let a person settle conflicts](offline-conflicts-are-shown-to-a-person.md)

- [Paho raises on publish while the broker is down; catch it or the sensor dies](paho-publish-raises-while-broker-is-down.md)

- [Sync downloads with a running-number bookmark can skip records unless numbering is ordered](sync-bookmark-lock-avoids-skipped-records.md)

- [WebRTC results: direct paths worked, Chrome Slow 3G does not throttle media, TURN cost is a range](webrtc-testing-and-turn-findings.md)

## Security, privacy and data governance

- [A scan gate can turn red when no code changed; fix by bumping, not by deleting the scan](security-scan-gates-can-go-red-without-code-changes.md)

- [Capture least-privilege evidence with the IAM policy simulator](prove-iam-with-policy-simulator.md)

- [CI/CD shape that worked: test everything, scan, then deploy only what changed on merge to main](cicd-pipeline-shape-test-scan-deploy-changed.md)

- [CloudFront needs its certificate in us-east-1 and routes by Host header, not by DNS target](cloudfront-cert-region-and-host-header-routing.md)

- [Create secrets empty in Terraform and fill the value from the CLI so it never enters state or git](secrets-set-by-hand-stay-out-of-state.md)

- [Deploy from GitHub Actions with OIDC, no stored keys, and trust only the main branch](github-oidc-deploy-role-limited-to-main.md)

- [HTTPS on the ALB with an ACM certificate when DNS lives outside Terraform](https-acm-certificate-with-external-dns.md)

- [Least privilege in practice: one IAM role per job, each permission naming one resource](least-privilege-one-role-per-job.md)

- [Put the safety rules in the database so psql and scripts cannot skip them](database-enforces-rules-not-only-the-api.md)

- [Run each write in one transaction that first tells the database who is acting](transaction-sets-acting-user-for-audit.md)

- [Sign-in and rate-limit choices that held up in the HealthConnect API](api-rate-limits-and-login-protection.md)

- [Synthetic data and sandbox integrations must be labelled on screen and in the report](synthetic-data-and-labelled-sandbox-integrations.md)

- [Team IAM with a group, PowerUser, and a ForceMFA deny policy](force-mfa-team-iam-group.md)

## Carried over from Prosits 1 and 2

- [A destructive database test script must refuse production, even through a tunnel](db-test-script-must-refuse-rds.md)

- [Apply SQL migrations through a logbook table with checksums and a baseline option](migration-logbook-with-checksums.md)

- [Branch protection with one approval, and the traps of stacked pull requests](branch-protection-and-stacked-pr-traps.md)

- [Build images for the servers' CPU (linux/amd64) from an ARM Mac, and keep disk free](docker-build-for-the-servers-architecture.md)

- [Capture evidence honestly: report the real result, label what is faked, never rewrite history](honest-evidence-capture.md)

- [Copy and trim Terraform modules from the previous prosit instead of rebuilding](reuse-terraform-modules-across-prosits.md)

- [Events arrive at least once; claim the id with a conditional write before acting](at-least-once-events-need-idempotent-consumers.md)

- [Infrastructure as Code has edges: Amplify hosting could not be fully created by Terraform](amplify-terraform-github-app-gap.md)

- [Never stop a terraform apply half-way; recover with force-unlock and import](terraform-interrupted-apply-recovery.md)

- [Put the team's working rules in AGENTS.md so every teammate's coding assistant follows them](shared-agent-instructions-in-the-repo.md)

- [SNS fan-out to one SQS queue per consumer, batch size 1, dead-letter queue each](sns-fanout-sqs-per-consumer-and-dlq.md)

- [Static PWA hosting: cache headers and how a new release reaches phones](pwa-cache-headers-and-service-worker-updates.md)

- [Terraform state lives in a bootstrapped S3 bucket with native locking, shared across projects by key](terraform-remote-state-s3-native-locking.md)

- [Two ways to migrate a private database: on boot under an advisory lock, or by hand through an SSM tunnel](migrations-on-boot-versus-by-hand.md)

- [Use terraform apply -target for a one-off change, then do the full apply later](terraform-target-for-one-off-applies.md)

- [What slowed the team down in Prosits 1 and 2, and how to avoid it in Prosit 3](what-slowed-the-team-down.md)
