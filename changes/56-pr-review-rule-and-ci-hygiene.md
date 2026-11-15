---
issue: 56
title: Review open PRs first; CI hygiene
date: 2026-11-15
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `CONTRIBUTING.md` step 0 and `AGENTS.md` "Always": before starting anything, run `gh pr list --state open`, review PRs you didn't author, approve and merge the ready ones, comment on the rest.
- `.github/workflows/checks.yml`: `permissions: contents: read`, so the PR checks' token can't write to the repo.
- `scripts/check_change_file.py`: a decision file added in a PR must carry the PR's issue number (same as its change file) and be listed in `decisions/README.md`. Three new tests.

## Why

PRs only merge when someone reviews them, so reviewing first keeps everyone moving. The workflow token had default permissions; decision numbers weren't checked (both from the setup review).

## How to check
```bash
python3 -m unittest discover scripts/tests -v   # 14 tests OK
```

## AI use
- **Tool:** Claude Code
- **What it did:** wrote the rule text, the workflow change, the decision check and its tests, this file and the plan.
- **Prompts / session summary:** "make sure that in the repo there is a rule (add to existing rules) that whenever working, always check for any open PRs and approve, merge / review before starting anything", plus the known gaps from the setup handoff.
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- none

## Not done
- Old commits keep the personal email; history on `main` isn't rewritten. Joseph's new commits use the GitHub noreply address.
