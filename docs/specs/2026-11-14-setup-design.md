# Prosit 3 setup: repo, process and scope (design)

Status: ready for Joseph's approval, 14 Nov 2026. Sources: `Prosit 3.docx`, `Prosit 3 Launch.pptx`, Labs 10–14 handouts (course files, not in this repo), Prosit 2 repo (`ASU-MICS-2028/cc-group-3-prosit-2`).

## 1. Why

Prosit 3 is **SmartCity Accra**: an IoT + ML + AI platform for the Accra Metropolitan Assembly (AMA). Four weeks, Labs 10–14, $500 cloud credit per team, final project = 20% of the course grade. Prosit 2 worked, but most of its record keeping lived in a few long files (`PLAN.md`, `docs/decisions.md`, `docs/ai-tools-usage.md`) that everyone edited and that conflicted in PRs (e.g. the sign-off table, 13 Nov). Joseph wants to refine the process:

- every task is a **GitHub issue** with its own **plan file**;
- every **change** and every **decision** is its own small file, listed in an index file;
- **AI use is recorded inside each change**, with who was in charge;
- all notes (knowledge, learnings, docs) are **one idea per file** with an index, Zettelkasten style;
- the work is split so **nobody waits on anyone** unless a dependency is explicit.

Success: any teammate (or coding assistant) can open the repo, find their next issue, see its plan, do it alone, and leave a change file that says what was done, by whom, and what AI did. The final report and lab reports can be assembled from these files without hunting.

## 2. Goals, non-goals, anti-goals

**Goals**
- Repo skeleton in `ASU-MICS-2028/cc-group-3-prosit-3` (currently empty) with the folders, index files, templates, agent instructions and GitHub config below.
- GitHub labels, issue templates and the initial set of issues (Labs 10–14 and brief weeks 1–4) with plan stubs.
- Shared **contracts** written first, so each area can start on day one with fake data.
- A `knowledge/` folder seeded from the 11 lecture transcripts, Labs 1–14, Prosit 1 and 2 knowledge and learnings, and this brief, as atomic notes.

**Non-goals**
- No product code in this setup step (simulator, bridge, dashboards, models come through their own issues).
- No cloud resources created in this step.
- Not migrating Prosit 2 code. Its VPC, CI/CD and monitoring patterns are templates to adapt (Lab 10 says so).

**Anti-goals** (would be a failure even if it "works")
- A process so heavy that people skip it. Every file type must be short and have a template.
- Shared files that everyone edits in every PR (the source of Prosit 2's merge conflicts). Index files are the only shared files, and each PR adds one line to them.
- Claiming scope we didn't build. Anything not built is listed as "not built, and why".
- Secrets, real personal data, or course handouts committed to a public repo.

## 3. Constraints

- **Public repo.** No secrets, keys, passwords, student IDs, phone numbers, personal emails. Course handouts are not committed (summaries only), as in Prosit 2.
- **Reviews (Joseph, 14 Nov):** a PR into `main` needs **one approval from anyone who is not its author**. No required code-owner or per-area reviewer, because chasing a specific person is the main source of delay. Never merge with `--admin`. (The very first commit that creates `main` is pushed directly, because protection can't be set on an empty repo.)
- **Synthetic or public data only.** Real public data is allowed (OpenAQ air quality for Accra). No personal data about citizens.
- **AWS is the graded cloud**, region `af-south-1`, owned by Eugene. Lab 11's cost audit covers spend since Week 1, which exists only on AWS.
- **Grading weights** (launch deck): technical 40%, community engagement 30%, learning process 20%, collaboration 10%. The deck also asks for **daily learning logs** and **weekly peer evaluations**.
- **Dates** (course description): Week 10 = 10–14 Nov, 11 = 17–21 Nov, 12 = 24–28 Nov, 13 = 1–5 Dec, 14 = 8–11 Dec, 15 = 12–19 Dec (revision and exams). Each lab report is due before the next week's Monday lecture: Lab 10 by 16 Nov, Lab 11 by 23 Nov, Lab 12 by 30 Nov, Lab 13 by 7 Dec; the Lab 14 final package before Week 15. *My call:* brief week 1 = Week 11, week 2 = Week 12, week 3 = Week 13, week 4 = Week 14; Lab 10 is the foundation week before it.
- **Weekly written reports** besides the labs (course description): performance optimisations, 500 words, due Week 11; cost optimisation plan, 500 words, due Week 12; edge/IoT paper review, 1,000 words, due Week 13; ML component justification, 500 words, due Week 14; research proposal on a cloud trend, 1,500 words, and the 10–15 min presentation, due Week 15. Each gets an issue (`type:report`).
- **Repo access:** all four members are admins on `cc-group-3-prosit-3`, so any of us can set labels, milestones and branch protection.

## 4. Scope decided (Joseph, 14 Nov)

Three sensor domains, each feeding one ML/AI piece:

| Domain | Data | ML / AI it feeds |
|---|---|---|
| Air quality (PM2.5) | Simulator + real OpenAQ readings from Accra stations | 24–48 h forecast (Lab 13; brief week 2) |
| Waste bin fill level | Simulator | Fill-rate prediction → collection route planning (brief week 3) |
| Flood / drain water level | Simulator | Anomaly detection and early warning to the citizen app |

Not built, recorded with reasons: traffic, water-pipe and energy sensors; computer vision, NLP, reinforcement learning, digital twin, federated learning, chatbots. One of these may become the Lab 14 advanced-feature test.

## 5. Roles (decided)

| Person | GitHub | Area |
|---|---|---|
| Joseph Etse | `josetseph` | PM and process; sensor simulator; MQTT bridge with local buffering; per-device credentials and revocation; API including the prediction endpoint; final architecture document. Personal **GCP rebuild** in `infra/gcp/`, off the critical path |
| Eugene Sewor | `eugene-sew` | AWS: Terraform, auto-scaling, monitoring dashboard and alert, load tests, cost audit and optimisations, decommissioning plan |
| Elise Kennedy-Angbo | `Elise-Oyi` | Data: time-series DB, schema, retention, downsampling, ML models (baseline, MLflow, drift log). Web admin dashboard for AMA officials |
| Perfect Avugla | `PeaElorm` | UI/UX across both apps (design system); citizen mobile app |

**Community engagement (30% of the grade) is owned by all four** (Joseph, 14 Nov). It is split into issues labelled `area:community`, each with one owner, spread so everyone has some: privacy and data-ownership note (who owns sensor data, what is never collected); citizen input on AI decisions (the mobile app lets residents see and question an alert or a route, Perfect); open data portal and its "non-sensitive only" rule (Elise for the web side, Joseph for the API); inclusion of informal settlements and low-end phones (Perfect); a stakeholder session, real or stand-in (Lab 14 extension), and how community feedback changed the design. Joseph coordinates.

**Getting each part onto AWS** (Joseph, 14 Nov): each owner packages their own part (a container image plus a short README of ports, environment variables, secrets and resources it needs) and runs it locally first. Eugene writes and applies the Terraform for it in `infra/aws/`. So "live on AWS" tasks depend on Eugene, and say so in their issue; building and testing locally never waits on him. Live AWS changes are applied by Eugene only, as in Prosit 2.

The message broker and time-series database are chosen in Lab 10 Part D (Eugene and Elise, recorded as decisions). The web stack is Elise's call, the mobile stack (PWA or native) Perfect's; each is recorded as a decision.

## 5a. Setup step scope (my call)

This setup step delivers: (1) the skeleton, templates, agent files and GitHub config, pushed as the first commit to `main`; then, through the normal flow (issue, plan, PR, change file): (2) the labels, milestones and initial issues; (3) the knowledge seeding; (4) a **first draft** of the contracts, opened as a PR for the team to comment on (any one non-author approval merges it). Only step 1 skips the flow, because `main` must exist before protection can be set.

## 6. The flow of one task

1. **Issue.** One owner (assignee), labels for area, lab and week. Title says the outcome. Body links the plan file.
2. **Plan.** `plans/<issue-number>-<slug>.md` from `plans/TEMPLATE.md`: goal, what's built, depends on, done when (how we'll know), evidence to capture. Added in the same PR as the work, or earlier in a small PR when the plan needs agreement first. `plans/README.md` lists every plan with issue, owner and status.
3. **Work.** Branch `<area>/<issue-number>-<slug>`, one PR per issue, PR body says `Closes #N`.
4. **Change file.** Every PR adds `changes/C-<NNN>-<slug>.md` from `changes/TEMPLATE.md`:
   - what changed and why; issue and PR links;
   - **in charge** (one person) and **reviewed by**;
   - **AI use**: tool, which parts it did, what the person checked or changed afterwards (or "none");
   - how to check it (commands), what's not done.
   One line is added to `changes/README.md`.
5. **Decisions.** Each decision is `decisions/D-<NNN>-<slug>.md` from `decisions/TEMPLATE.md` (context, options, decision, consequences, who decided, date), with one line in `decisions/README.md`. A change file links the decisions it made.
6. **Notes.** Facts and how-tos go into `knowledge/` or `learnings/` as one-idea notes (section 8).
7. **Merge** after one non-author approval closes the issue.

**Numbering without collisions:** C- and D- numbers are taken by the next free number at PR time; if two open PRs pick the same number, the second to merge renumbers (a rename, not a conflict in content). Index files sort by number.

## 7. Working without waiting

Contracts are written in week 1 (issue owned by Joseph; the PR is shared with everyone for comment) and live in `contracts/`:

- `sensor-reading` – the JSON a sensor publishes (device id, domain, metric, value, unit, timestamp, sequence number), as a JSON Schema plus examples;
- `mqtt-topics` – topic layout, e.g. `accra/<neighbourhood>/<domain>/<device-id>`;
- `api` – REST endpoints the web and mobile apps call (latest readings, history, alerts, predictions, citizen reports), as OpenAPI;
- `storage` – the logical tables or measurements per domain, and the hourly rollup.

Each area builds against the contract with fake data: the simulator publishes contract-shaped readings; the bridge consumes them; the apps call a mock API from the OpenAPI file; the ML work trains on backfilled synthetic or OpenAQ data. A contract change is its own PR with a decision file. The author tags the owners it affects so they see it, but like every PR it merges on any one non-author approval.

## 8. Notes, Zettelkasten style

- `knowledge/` = **what we were taught or given**: lecture concepts, lab requirements and rubrics, brief facts, course logistics, carried-over facts from Prosit 1 and 2.
- `learnings/` = **what we found out by doing**: procedures, gotchas, approaches that worked or failed.
- Each note: one idea, short (aim under ~40 lines), a kebab-case file name that says the idea (`golden-signals.md`, `mosquitto-listens-on-localhost-by-default.md`), front matter with `title`, `tags`, `source` (lecture N, lab N, brief, PR), and a **Related** list of links to other notes.
- Each folder has a `README.md` index grouping notes by topic. Larger topics may get their own small index note (a "map" note) that the README links to. Notes stay flat in the folder; topics are expressed by tags and index notes, not by subfolders.
- Peer evaluations are **not** kept in the repo (it is public, and they are personal); each person submits their own where the course asks. *My call.*
- Daily learning logs (launch deck) go in `logs/<github-user>/YYYY-MM-DD.md`, short, personal; anything worth keeping is promoted to a learnings note.

## 9. Repo layout

```
README.md            what's open now, who has it, links to indexes
CONTRIBUTING.md      the flow in section 6, ground rules
AGENTS.md, CLAUDE.md instructions for coding assistants (same rules)
plans/  changes/  decisions/  knowledge/  learnings/  logs/   (each with README.md index + TEMPLATE.md where relevant)
contracts/           sensor-reading, mqtt-topics, api, storage
sensors/             simulator, OpenAQ feeder               (Joseph)
ingest/              MQTT bridge, buffering, device creds   (Joseph)
api/                 REST + prediction API                  (Joseph)
db/                  time-series schema, rollups            (Elise)
ml/                  training, MLflow, drift log            (Elise)
web/                 AMA admin dashboard                    (Elise)
mobile/              citizen app                            (Perfect)
design/              design system, screens                 (Perfect)
infra/aws/           Terraform, graded build                (Eugene)
infra/gcp/           Joseph's personal rebuild, not graded
loadtest/            k6 scripts                             (Eugene)
evidence/lab10…14/   screenshots, outputs, scripts that made them
docs/                architecture diagrams, report sources, specs
.github/             issue templates, PR template, CODEOWNERS, CI
```

Folders for product code start as a `README.md` saying owner, purpose and the contract they build against; code arrives through issues.

## 10. GitHub setup

- **Labels:** `area:infra-aws`, `area:infra-gcp`, `area:sensors`, `area:ingest`, `area:api`, `area:data`, `area:ml`, `area:web`, `area:mobile`, `area:design`, `area:docs`, `area:process`, `area:community`; `lab:10` … `lab:14`; `week:1` … `week:4` (brief weeks); `type:task`, `type:decision`, `type:report`; `blocked`.
- **Issue templates:** task (owner, plan file, done when, depends on) and decision.
- **PR template:** `Closes #`, change file path, decisions added, notes added, evidence, AI use summary, "no secrets" check.
- **CODEOWNERS:** area folders → their owner, only so GitHub *suggests* the right reviewer. "Require review from code owners" stays **off**.
- **Branch protection on `main`:** one approving review from a non-author (GitHub never counts the author's own approval), stale approvals not dismissed, code-owner review not required, no admin bypass. Joseph sets it up once `main` exists (all four members are admins).
- **CI:** start with a markdown link check and a check that each PR adds a change file; code CI arrives with code.
- Milestones: one per lab (Lab 10 … Lab 14) with the due date.

## 11. Initial issues

One issue per lab deliverable part, each with a plan stub, owner and labels. Roughly:

- **Setup:** contracts (Joseph), branch protection and labels (Joseph), knowledge seeding (Joseph, with AI).
- **Lab 10:** auto-scaling, dashboard (4 golden signals) + alert, k6 load test, report (Eugene); broker + time-series DB decision (Eugene and Elise).
- **Lab 11:** cost audit, two optimisations, sustainability estimate (Eugene); SmartCity budget model (Eugene with Elise for data volumes).
- **Lab 12:** MQTT broker, simulator, per-device credentials and revocation drill (Joseph); bridge with buffering (Joseph); time-series storage + hourly rollup (Elise); live chart in web (Elise) and mobile (Perfect).
- **Lab 13:** training data + baseline + model + MLflow + drift log (Elise); prediction endpoint (Joseph).
- **Lab 14:** advanced-feature test, capstone integration design, consolidated architecture document, presentation, decommissioning plan (split at Lab 14).
- **Brief weeks 2–4 not covered by labs:** route planning for waste, flood early-warning alerts, citizen reporting in the mobile app, open data endpoint, SDG 11 dashboard view.
- **Community engagement** (all four, one owner per issue): see section 5.
- **Deploy to AWS** per component (Eugene, after its owner's package is ready).
- **GCP track** (Joseph, `area:infra-gcp`, not on the critical path).

## 12. Left to the builder

- Exact wording of templates and index files, provided they stay short.
- Which tags and topic groupings the knowledge index uses.
- How many issues exactly, and their titles, within section 11.
- Choice of CI tools for the two starting checks.
- How the knowledge seeding is split among assistant runs; every note must cite its source.
