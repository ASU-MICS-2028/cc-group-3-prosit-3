# Plan: Consolidated architecture document (L14-C)

- **Issue:** #47
- **Owner:** Joseph (`josetseph`)
- **Milestone:** Lab 14 / final
- **Status:** in progress (first version merged; the SmartCity AWS section and the integration design follow)

## Goal
Lab 14 Part C (20%): the core of the final submission.

## What gets built
- `docs/architecture.md`, one document with:
  - a comparison table of the three systems
  - AgroConnect and HealthConnect as deployed, with their diagrams embedded from the Prosit 1 and 2 repos
  - SmartCity as built, with a Mermaid diagram, and as planned on AWS
  - the integration design (link to #46)
  - eight lessons learned
- Facts about Prosits 1 and 2 come from those repos' docs and Terraform. The ASG sizes and single-AZ databases were checked against the Terraform.

## Depends on
- #46 for section 4
- #28, #29, #35 for the SmartCity as-deployed diagram

## Done when
- AgroConnect, HealthConnect and SmartCity final architectures, the integration design, and an honest lessons-learned page
- Diagrams match what is actually deployed

## Evidence to capture
- none: the document links to the evidence each number comes from

## Not doing
- Redrawing the Prosit 1 and 2 diagrams. They were already drawn as deployed, so we link them rather than copy them.
