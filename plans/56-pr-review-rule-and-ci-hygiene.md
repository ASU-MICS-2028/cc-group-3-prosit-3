# Plan: Review open PRs first; CI hygiene

- **Issue:** #56
- **Owner:** Joseph (`josetseph`)
- **Status:** done in this PR

## Goal
Keep PRs from sitting unreviewed, and close two small CI gaps from the setup review.

## What gets built
- Rule (CONTRIBUTING step 0, AGENTS "Always"): check open PRs and review / approve / merge before starting anything.
- `permissions: contents: read` on the checks workflow.
- `check_change_file.py`: a new decision file must be `decisions/<the PR's issue number>-<slug>.md` and listed in `decisions/README.md`; three tests.

## Depends on
- nothing

## Done when
- Rule in both files; `python3 -m unittest discover scripts/tests` passes; CI green on this PR.

## Evidence to capture
- CI run on this PR.

## Not doing
- Rewriting old commits that carry a personal email: rewriting merged history on `main` breaks everyone's clones. New commits use the GitHub noreply address.
