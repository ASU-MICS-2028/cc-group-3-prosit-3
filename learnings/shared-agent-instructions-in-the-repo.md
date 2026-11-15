---
title: Put the team's working rules in AGENTS.md so every teammate's coding assistant follows them
tags: [process, prosit-2]
source: Prosit 2 learnings/repo-and-tooling.md; Prosit 2 AGENTS.md; Prosit 2 CONTRIBUTING.md; Prosit 2 docs/decisions.md D-007, D-020
---

Each teammate used a different assistant on a different laptop. Root `AGENTS.md` holds the rules; `CLAUDE.md` is one line (`@AGENTS.md`); each area (`backend/`, `db/`, `infra/`) has its own short guide with commands and traps.

Contents that mattered: read README then PLAN then ADRs first; plan in small steps and explain each before doing it; test every branch including failures; capture evidence as you go; record learnings, ADRs and knowledge in the same PR; ask before `terraform apply/destroy`, deleting things, merging, or changing GitHub settings; the repo is public so no secrets or personal data.

Testing it: ask a question only the instructions answer from each folder (for example "can I fix a typo in migration 001?" expects "no, add a new one"); a request to commit an AWS key was refused.

Other process choices: README shows only the current stage (details in PLAN.md); every owner writes a plain-language note ("write for a teammate who will never open your folder"); a PR without its learnings note is not done; real deadlines beat syllabus dates.

## Related
- [Branch protection with one approval, and the traps of stacked pull requests](branch-protection-and-stacked-pr-traps.md)
- [What slowed the team down in Prosits 1 and 2, and how to avoid it in Prosit 3](what-slowed-the-team-down.md)
