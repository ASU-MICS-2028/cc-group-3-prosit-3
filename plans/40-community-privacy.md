# Plan: Community: privacy and data-ownership note

- **Issue:** #40
- **Owner:** Joseph (`josetseph`)
- **Milestone:** Lab 12
- **Status:** done

## Goal
Community engagement: say plainly who owns the data, what we never collect, and how a neighbourhood can opt out.

## What gets built
- `docs/privacy.md`: an ownership table, a "never collect" list with where each claim is enforced, the steps to switch a neighbourhood off (revoke, delete, switch back on), and the gaps before going live (Act 843 registration, data stored outside Ghana, how long reports are kept, photos).
- `api/app.py`: the request log stops recording callers' IP addresses, so the "never collect" list is true.
- Links from the README and from `docs/README.md`.

## Depends on
- nothing

## Done when
- Short note: who owns sensor data, what we never collect, how a neighbourhood could switch off its sensors
- Linked from the README and used in the final report

## Evidence to capture
- none beyond the note: each claim links to the code, contract or test that enforces it

## Not doing
- Registering with the Data Protection Commission, or a retention job for reports. Both are listed in the note as gaps.
- The open-data publishing rule, which is #42 (Elise's).
