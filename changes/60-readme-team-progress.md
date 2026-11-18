---
issue: 60
title: README with team cards and live progress
date: 2026-11-18
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `README.md` restructured after mle-group-2-prosit-2's: header with live badges (closed/open issues, open PRs), team cards with GitHub avatars, roles and owned folders, progress per lab (live milestone badges), open issues per person (live badges plus links), what we build with a pipeline sketch, quick start, repository map, how we work.

## Why

Joseph liked the other team's front page; it shows the team and the state of the work without opening the issues list.

## How to check

Open the README on this branch on GitHub: four photos (Elise shows GitHub's default pattern until she uploads a photo), every badge shows a number, every link works (`links` check).

## AI use
- **Tool:** Claude Code
- **What it did:** read the other team's README, wrote this one, checked each badge URL returns a live count, checked each person's description against their assigned issues, wrote the plan and this file.
- **Prompts / session summary:** "I also like how one of the teams structured their github repo readme even including the team members and their images. I would like to replicate that here. I think the images can be derived from linkedin (or anywhere else you can get it)". Claude used GitHub avatars instead of LinkedIn (see the plan's "Not doing").
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- none

## Not done
- Elise's photo: she adds one on her GitHub profile and it appears here automatically.
- The quick start's broker and simulator commands work once PR #58 (#18) is merged.
