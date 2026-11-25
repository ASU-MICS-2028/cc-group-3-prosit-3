---
issue: 47
title: Final architecture document, first version
date: 2026-11-24
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `docs/architecture.md`, the Lab 14 Part C document:
  - AgroConnect and HealthConnect as deployed, with their as-deployed diagrams embedded from the Prosit 1 and 2 repos
  - SmartCity as built locally, with a Mermaid diagram and measured results, and as planned on AWS from the budget model
  - a placeholder for the integration design (#46)
  - eight lessons learned
- Linked from the README and `docs/README.md`. Plan `plans/47-l14-architecture-doc.md`.

## Why

Part C is 20% of the final project. Writing the finished prosits now leaves only two sections to add: the SmartCity AWS deployment and the integration design.

## How to check
- Read `docs/architecture.md` on GitHub. The Mermaid diagram and both embedded images should render.
- Every SmartCity number links to an evidence file or a README. The ASG sizes and single-AZ databases for Prosits 1 and 2 match their `infra/` Terraform.

## AI use
- **Tool:** Claude Code
- **What it did:**
  - Two read-only agents summarised the Prosit 1 and 2 repos.
  - Claude checked the key facts against the Terraform and wrote the document.
  - It didn't copy the HealthConnect diagram, because the diagram shows the AWS account number; it links to it instead.
- **Prompts / session summary:** "go ahead with #47".
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- none

## Not done
- The SmartCity as-deployed diagram (after #28, #29, #35) and the integration design (#46). The PR says "Part of #47", so the issue stays open.
