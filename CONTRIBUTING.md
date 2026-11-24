# How we work

Using a coding assistant? It follows [`AGENTS.md`](./AGENTS.md), which builds on this file.

## The flow of one task

0. **Open PRs first.** Before starting anything (a task, a session, a day's work), run `gh pr list --state open` and deal with what's there: review every PR you didn't author, approve and merge the ones that are ready (checks green, nothing wrong in the diff), and leave a review comment on the rest. Your own PRs: answer review comments. Then start new work. Unreviewed PRs block teammates; new work can wait ten minutes.
1. **Issue.** Every task is a GitHub issue with one owner (the assignee) and labels for area, lab and week. Pick one assigned to you, or ask in the group before taking someone else's.
2. **Plan.** Fill in `plans/<issue-number>-<slug>.md` (copy [`plans/TEMPLATE.md`](./plans/TEMPLATE.md)): goal, what gets built, depends on, done when, evidence to capture. Add a row to [`plans/README.md`](./plans/README.md). If the plan needs agreement first, open a small PR with just the plan.
3. **Branch and PR.** Branch `<area>/<issue-number>-<slug>` off an up-to-date `main`. One PR per issue; its body says `Closes #<issue-number>`.
4. **Change file.** Every PR adds **one** `changes/<issue-number>-<slug>.md` (copy [`changes/TEMPLATE.md`](./changes/TEMPLATE.md)) and fills its issue's line in [`changes/README.md`](./changes/README.md). It says what changed and why, **who was in charge**, who reviewed it, **what AI did** (tool, which parts, what you checked or changed after), how to check it, and what's not done. A pure chore (typo, index fix) can skip it with the label `skip-change-file`.
5. **Decisions.** Each decision is its own `decisions/<issue-number>-<slug>.md` (copy [`decisions/TEMPLATE.md`](./decisions/TEMPLATE.md)), listed on its issue's line in [`decisions/README.md`](./decisions/README.md). Link it from your change file.
6. **Notes.** Facts go in [`knowledge/`](./knowledge/README.md), things you found out by doing in [`learnings/`](./learnings/README.md): one idea per note (rules below).
7. **Review and merge.** **One approval from anyone who isn't the author** merges it. No area needs a particular reviewer; CODEOWNERS only suggests one. Never merge with `--admin`. Merging closes the issue.

**No merge conflicts in the indexes:** files are named after the issue number, so two PRs never pick the same name. The indexes (`plans/`, `changes/`, `decisions/`) have one hidden slot line per issue, `<!-- #12 -->`, with blank lines between them: replace your issue's slot with your entry and touch nothing else. Note indexes (`knowledge/`, `learnings/`) keep a blank line between entries for the same reason; insert yours in alphabetical order in its section.

## Working without waiting

Every part builds against the shared formats in [`contracts/`](./contracts/README.md) (sensor reading, MQTT topics, API, storage), using fake data until the real thing exists. Changing a contract is its own PR with a decision file; tag the people it affects so they see it. Like any PR, it merges on one non-author approval.

**Getting a part onto AWS:** the owner packages it (a container image plus a short README: ports, environment variables, secrets and resources it needs) and runs it locally first. Eugene writes and applies the Terraform in `infra/aws/`. Only Eugene applies live AWS changes. A "live on AWS" issue lists Eugene as a dependency; building and testing locally never waits on him.

## Notes: one idea per file

- `knowledge/` = what we were taught or given (lectures, labs, the brief, course facts). `learnings/` = what we found out by doing (procedures, gotchas, what worked or failed).
- One idea per note, ideally under ~40 lines. The file name states the idea: `golden-signals.md`, `mosquitto-listens-on-localhost-by-default.md`.
- Front matter `title`, `tags`, `source` (e.g. `Lecture 7`, `Lab 12 Part C`, `PR #14`), and a `## Related` section linking other notes.
- Every note is linked from its folder's `README.md`. Big topics get a `map-<topic>.md` note that groups the notes. No subfolders.
- CI checks all of this (`scripts/check_notes.py`).
- Daily learning logs: `logs/<github-user>/YYYY-MM-DD.md`, short. Anything worth keeping becomes a learnings note.

## Ground rules

- **The repo is public.** No secrets, keys, passwords, student IDs, phone numbers or personal emails. No course handouts (summaries only).
- **Synthetic or public data only** (OpenAQ is fine). No personal data about residents.
- **Every cloud resource is tagged** `project=smartcity` and torn down when its lab is done.
- **Peer evaluations are not kept here.** Each person submits their own where the course asks.

## Checks on every PR

| Check | What it enforces |
|---|---|
| `change-file` | Exactly one new `changes/<issue-number>-*.md`, linked from `changes/README.md` (or label `skip-change-file`); any new decision file is `decisions/<same number>-*.md` and listed in `decisions/README.md` |
| `notes` | Front matter, `## Related`, and index link for every note |
| `links` | No broken relative links in Markdown |
| `unit` | Tests for the checks themselves |
| `contracts` | Contract examples match the schema; the API lists the agreed paths; simulated readings and topics match the contract |
