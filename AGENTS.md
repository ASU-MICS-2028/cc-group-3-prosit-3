# Instructions for coding assistants

Read [`CONTRIBUTING.md`](./CONTRIBUTING.md) first; everything there applies to you. In addition:

## Always

- Work on one issue at a time, on its branch. Read its plan in `plans/` before changing anything; if there is no plan yet, write it first.
- Add exactly one change file per PR. In its **AI use** section, say plainly which parts you produced, and leave the "what the person checked" line for the person to complete truthfully. Never claim a human reviewed something they didn't.
- Record decisions as `decisions/D-NNN-*.md`; put new facts and gotchas in `knowledge/` or `learnings/` as one-idea notes, indexed in the folder README.
- Build against `contracts/`. If a contract is wrong, propose the change in its own PR with a decision file; don't silently diverge.
- Test the failure paths, not only the happy path. Capture evidence for labs in `evidence/labNN/`.
- Write plainly for a teammate who has never opened the folder: what, why, how to check, what's missing.

## Never

- Print, commit or paste secrets, passwords, tokens, keys or `.env` contents.
- Merge with `--admin`, approve your own human's PR, or bypass branch protection.
- Apply changes to live AWS; Eugene applies infrastructure. Read-only commands only.
- Tick off tasks that need a person (a signature, a real-phone test, a stakeholder conversation).
- Invent measurements, results or quotes. Report a failure honestly; the labs grade honest reporting.
- Commit course handouts or real personal data.
