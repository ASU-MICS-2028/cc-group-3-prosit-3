# Prosit 3 Repo Setup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the empty `ASU-MICS-2028/cc-group-3-prosit-3` into a working team repo: skeleton and rules, GitHub labels/milestones/issues with plan stubs, seeded atomic knowledge notes, and a first draft of the shared contracts.

**Architecture:** Mostly Markdown and GitHub config. Two small Python checks (`scripts/check_notes.py`, `scripts/check_change_file.py`) and a contracts test enforce the conventions in CI, so the process doesn't depend on people remembering it. Task 1 is pushed straight to `main`; Tasks 2–4 each go through the flow they set up (issue → plan → PR → change file → one non-author approval).

**Tech Stack:** Markdown, GitHub Actions, `gh` CLI, Python 3.11+ stdlib (+ `jsonschema` for Task 4 only), `lychee` link checker (offline mode).

**Spec:** `docs/specs/2026-11-14-setup-design.md` (approved 15 Nov 2026).

## Global Constraints

- Public repo: no secrets, keys, passwords, student IDs, phone numbers, personal emails; course handouts are never committed (summaries only, `week*.docx`, `Prosit*.docx`, `*.pptx` in `.gitignore`).
- Synthetic or public data only.
- PRs into `main`: one approval from anyone who is not the author; code-owner review **off**; stale approvals **not** dismissed; never `--admin`.
- Notes: one idea per file, kebab-case name stating the idea, front matter `title`, `tags`, `source`, a `## Related` section; aim under ~40 lines; flat folders, indexed by `README.md`.
- Change files `changes/C-NNN-<slug>.md`, decisions `decisions/D-NNN-<slug>.md`, plans `plans/<issue>-<slug>.md`; numbers are 3-digit, taken at PR time.
- Live AWS changes are applied by Eugene only. This plan creates no cloud resources.
- GitHub users: `josetseph` (Joseph), `eugene-sew` (Eugene), `Elise-Oyi` (Elise), `PeaElorm` (Perfect).
- Commit messages and PR bodies carry no AI attribution lines.

## Review Focus

1. A PR that touches only an index file or a typo still needs a change file → `check_change_file.py` must allow a `skip-change-file` label for pure chores, and say so in its failure message. (Test in Task 1.)
2. A note added to `knowledge/` but not linked from `knowledge/README.md` silently becomes unfindable → `check_notes.py` fails on unindexed notes. (Test in Task 1.)
3. Two PRs pick the same `C-NNN` → `check_change_file.py` fails if the number already exists on `main`. (Test in Task 1.)
4. A note copies a lecture transcript verbatim or includes a classmate's name or phone number from the transcript → Task 3 reviewer checks every note for names other than the four members and course staff, and for passages over ~3 lines quoted directly.
5. A contract example drifts from the schema → Task 4's test validates every file in `contracts/examples/` and has one deliberately bad example that must fail.

---

### Task 1: Skeleton, rules and CI checks (first commit to `main`)

**Files:**
- Create: `README.md`, `CONTRIBUTING.md`, `AGENTS.md`, `CLAUDE.md` (one line: "Follow AGENTS.md."), `.gitignore`
- Create: `plans/README.md`, `plans/TEMPLATE.md`; `changes/README.md`, `changes/TEMPLATE.md`; `decisions/README.md`, `decisions/TEMPLATE.md`; `knowledge/README.md`, `knowledge/TEMPLATE.md`; `learnings/README.md`, `learnings/TEMPLATE.md`; `logs/README.md`
- Create: `README.md` in each of `contracts/ sensors/ ingest/ api/ db/ ml/ web/ mobile/ design/ infra/aws/ infra/gcp/ loadtest/ evidence/ docs/` (owner, purpose, contract it builds against, "no code yet")
- Create: `.github/pull_request_template.md`, `.github/ISSUE_TEMPLATE/task.md`, `.github/ISSUE_TEMPLATE/decision.md`, `.github/CODEOWNERS`, `.github/workflows/checks.yml`
- Create: `scripts/check_notes.py`, `scripts/check_change_file.py`, `scripts/tests/test_checks.py`
- Keep: `docs/specs/2026-11-14-setup-design.md`, this plan

**Interfaces:**
- Produces: `check_notes.py <dir>...` exits 1 listing (a) notes missing `title`/`tags`/`source` front matter or a `## Related` heading, (b) notes not linked from that folder's `README.md`. Ignores `README.md`, `TEMPLATE.md`. `check_change_file.py --base <ref> --labels <comma-list>` exits 1 unless the diff `<ref>...HEAD` adds exactly one `changes/C-NNN-*.md` whose `NNN` is not already in `<ref>`, or labels contain `skip-change-file`.

Template contents (exact field headings):
- `plans/TEMPLATE.md`: Issue · Owner · Goal · What gets built · Depends on · Done when · Evidence to capture · Not doing.
- `changes/TEMPLATE.md`: front matter `id, title, date, issue, pr, in_charge, reviewed_by`; sections What changed · Why · How to check · AI use (tool · what it did · what the person checked or changed; or "None") · Decisions made · Not done.
- `decisions/TEMPLATE.md`: front matter `id, title, date, decided_by, status (proposed|accepted|replaced by D-NNN)`; sections Context · Options · Decision · Consequences.
- `knowledge/TEMPLATE.md` and `learnings/TEMPLATE.md`: front matter `title, tags, source`; body; `## Related`.
- Index rows: plans `| #issue | plan | owner | status |`; changes `| C-NNN | title | in charge | issue |`; decisions `| D-NNN | title | status |`; notes grouped under topic headings as `- [title](file.md) — one-line hook`.
- `CONTRIBUTING.md`: the design's section 6 flow, section 7 contract rule, section 8 note rules, ground rules, review rule, deploy rule ("package + README; Eugene applies Terraform").
- `AGENTS.md`: same rules addressed to assistants, plus "never print secrets; never `--admin`; never tick human tasks; live AWS read-only".
- `README.md`: one paragraph on SmartCity Accra and the three domains, team table (design section 5), "Start here" links to every index, link to open issues and milestones.
- `CODEOWNERS`: `/infra/aws/ @eugene-sew`, `/loadtest/ @eugene-sew`, `/db/ /ml/ /web/ @Elise-Oyi`, `/mobile/ /design/ @PeaElorm`, `/sensors/ /ingest/ /api/ /infra/gcp/ /contracts/ @josetseph`.
- `checks.yml` on `pull_request`: job `notes` runs `python scripts/check_notes.py knowledge learnings`; job `change-file` runs `check_change_file.py --base origin/${{ github.base_ref }} --labels "${{ join(github.event.pull_request.labels.*.name, ',') }}"`; job `links` runs `lycheeverse/lychee-action` with `--offline --no-progress '**/*.md'`; job `unit` runs `python -m unittest discover scripts/tests`.

- [ ] **Step 1: Write failing tests** in `scripts/tests/test_checks.py` using `tempfile` dirs and a throwaway `git init` repo:
  - `test_note_missing_source_fails`, `test_note_missing_related_fails`, `test_unindexed_note_fails`, `test_good_indexed_note_passes`
  - `test_pr_without_change_file_fails`, `test_pr_with_one_new_change_file_passes`, `test_duplicate_change_number_fails` (C-001 exists on base, PR adds `C-001-other.md`), `test_skip_label_passes`, `test_two_change_files_fails`
- [ ] **Step 2: Run** `python3 -m unittest discover scripts/tests -v` → all 9 FAIL (modules missing).
- [ ] **Step 3: Implement** both scripts (stdlib only: `argparse`, `pathlib`, `re`, `subprocess`). Failure messages name the file and the fix, e.g. `knowledge/x.md: not linked from knowledge/README.md — add "- [title](x.md) — hook"`.
- [ ] **Step 4: Run tests** → 9 PASS. Run `python3 scripts/check_notes.py knowledge learnings` on the skeleton → exit 0.
- [ ] **Step 5: Write all skeleton files** listed above.
- [ ] **Step 6: Secret and handout scan:** `git add -A && git diff --cached --name-only | grep -E '\.(docx|pptx|pdf|env|pem)$'` → no output; `grep -rIE '(AKIA[0-9A-Z]{16}|BEGIN (RSA|OPENSSH) PRIVATE|password\s*=)' .` → no output.
- [ ] **Step 7: Commit and push to create `main`:**
```bash
git add -A && git commit -m "chore: repo skeleton, process rules and checks for Prosit 3"
git push -u origin main
```
- [ ] **Step 8: Protect `main`:**
```bash
gh api -X PUT repos/ASU-MICS-2028/cc-group-3-prosit-3/branches/main/protection --input - <<'EOF'
{"required_status_checks":{"strict":false,"contexts":["notes","change-file","links","unit"]},
 "enforce_admins":true,
 "required_pull_request_reviews":{"required_approving_review_count":1,"dismiss_stale_reviews":false,"require_code_owner_reviews":false},
 "restrictions":null}
EOF
```
  Verify: `gh api repos/ASU-MICS-2028/cc-group-3-prosit-3/branches/main/protection -q '.required_pull_request_reviews'` shows count 1, code owners false.

### Task 2: Labels, milestones, initial issues and plan stubs

**Files:**
- Create: `plans/<n>-<slug>.md` for every issue below (from `plans/TEMPLATE.md`, Goal/Done when filled from the lab rubric or brief line; Owner; Depends on)
- Modify: `plans/README.md` (one row per plan)
- Create: `changes/C-001-initial-issues-and-plans.md`
- Scratch (not committed): `$SCRATCH/issues.tsv`, `$SCRATCH/create_issues.sh`

**Interfaces:**
- Consumes: Task 1 templates, labels in `check_change_file.py` (`skip-change-file`).
- Produces: issue numbers that later plans and PRs reference; labels and milestones below.

Labels (create with `gh label create --force`): `area:infra-aws area:infra-gcp area:sensors area:ingest area:api area:data area:ml area:web area:mobile area:design area:docs area:process area:community`, `lab:10 … lab:14`, `week:1 … week:4`, `type:task type:decision type:report`, `blocked`, `skip-change-file`.

Milestones (title → due date): `Lab 10` → 2026-11-16, `Lab 11` → 2026-11-23, `Lab 12` → 2026-11-30, `Lab 13` → 2026-12-07, `Lab 14 / final` → 2026-12-11.

Issues (owner → labels → milestone). Owners for the five written reports and capstone pieces are my defaults; Joseph can reassign.

| Issue | Owner | Labels | Milestone |
|---|---|---|---|
| Open initial issues and plan stubs | josetseph | area:process type:task | Lab 10 |
| Draft shared contracts (reading, topics, API, storage) | josetseph | area:process type:task week:1 | Lab 10 |
| Seed knowledge notes from lectures, labs, Prosits 1–2, brief | josetseph | area:docs type:task | Lab 10 |
| Auto Scaling Group with target-tracking policy (L10-A) | eugene-sew | area:infra-aws lab:10 | Lab 10 |
| Dashboard with four golden signals and error-rate alert (L10-B) | eugene-sew | area:infra-aws lab:10 | Lab 10 |
| k6 ramp load test with scale-out evidence (L10-C) | eugene-sew | area:infra-aws lab:10 | Lab 10 |
| Decide message broker and time-series DB (L10-D) | eugene-sew | area:data type:decision lab:10 | Lab 10 |
| Lab 10 report (300 words) | eugene-sew | type:report lab:10 | Lab 10 |
| Weekly report: performance optimisations (500 words) | eugene-sew | type:report | Lab 11 |
| Cost audit since Week 1, top 3 drivers (L11-A) | eugene-sew | area:infra-aws lab:11 | Lab 11 |
| Two cost optimisations with before/after (L11-B) | eugene-sew | area:infra-aws lab:11 | Lab 11 |
| SmartCity budget model at stated sensor volume (L11-C) | Elise-Oyi | area:data lab:11 | Lab 11 |
| Sustainability estimate and region choice (L11-D) | josetseph | area:infra-gcp lab:11 | Lab 11 |
| Lab 11 report (300 words) | eugene-sew | type:report lab:11 | Lab 11 |
| Weekly report: cost optimisation plan (500 words) | josetseph | type:report | Lab 12 |
| GCP project, budget alert and billing export | josetseph | area:infra-gcp | Lab 11 |
| Design system and screen set for web and mobile | PeaElorm | area:design week:1 | Lab 12 |
| MQTT broker and three-domain sensor simulator (L12-A/B) | josetseph | area:sensors lab:12 week:1 | Lab 12 |
| OpenAQ feeder for real Accra PM2.5 | josetseph | area:sensors lab:12 | Lab 12 |
| MQTT bridge with local buffering (L12-C) | josetseph | area:ingest lab:12 | Lab 12 |
| Per-device credentials and revocation drill (L12-E) | josetseph | area:ingest lab:12 | Lab 12 |
| Time-series storage and hourly rollup (L12-C) | Elise-Oyi | area:data lab:12 | Lab 12 |
| AMA web dashboard shell with live chart (L12-D) | Elise-Oyi | area:web lab:12 | Lab 12 |
| Citizen mobile app shell with live readings (L12-D) | PeaElorm | area:mobile lab:12 | Lab 12 |
| Flood early-warning alerts (API + app) | josetseph | area:api week:2 | Lab 12 |
| Lab 12 report (300 words) | josetseph | type:report lab:12 | Lab 12 |
| Weekly report: edge/IoT paper review (1,000 words) | PeaElorm | type:report | Lab 13 |
| Deploy broker and bridge to AWS | eugene-sew | area:infra-aws | Lab 12 |
| Deploy time-series DB to AWS | eugene-sew | area:infra-aws | Lab 12 |
| PM2.5 forecast: data, baseline, model, MLflow (L13-A/B/C) | Elise-Oyi | area:ml lab:13 week:2 | Lab 13 |
| Prediction API endpoint (L13-D) | josetseph | area:api lab:13 | Lab 13 |
| Drift log: predictions vs later actuals (L13-E) | Elise-Oyi | area:ml lab:13 | Lab 13 |
| Waste fill-rate prediction and collection routes | Elise-Oyi | area:ml week:3 | Lab 13 |
| Citizen issue reporting in the mobile app | PeaElorm | area:mobile week:2 | Lab 13 |
| Deploy API and web dashboard to AWS | eugene-sew | area:infra-aws | Lab 13 |
| Lab 13 report (300 words) | Elise-Oyi | type:report lab:13 | Lab 13 |
| Weekly report: ML component justification (500 words) | Elise-Oyi | type:report | Lab 14 / final |
| Open data endpoint and portal page | Elise-Oyi | area:web week:4 | Lab 14 / final |
| SDG 11 dashboard view | Elise-Oyi | area:web week:4 | Lab 14 / final |
| Community: privacy and data-ownership note | josetseph | area:community | Lab 12 |
| Community: citizens can see and question an AI alert or route | PeaElorm | area:community | Lab 13 |
| Community: open data "non-sensitive only" rule | Elise-Oyi | area:community | Lab 13 |
| Community: inclusion for informal settlements and low-end phones | PeaElorm | area:community | Lab 13 |
| Community: stakeholder session and what changed | eugene-sew | area:community | Lab 14 / final |
| Advanced feature test: same pipeline on AWS and GCP (L14-A) | josetseph | area:infra-gcp lab:14 | Lab 14 / final |
| Capstone integration design (L14-B) | Elise-Oyi | area:docs lab:14 | Lab 14 / final |
| Consolidated architecture document (L14-C) | josetseph | area:docs lab:14 | Lab 14 / final |
| Presentation and backup demo video (L14-D) | PeaElorm | area:docs lab:14 | Lab 14 / final |
| Decommissioning plan with owner and date (L14-E) | eugene-sew | area:infra-aws lab:14 | Lab 14 / final |
| Research proposal on a cloud trend (1,500 words) | josetseph | type:report | Lab 14 / final |

Issue body (from `.github/ISSUE_TEMPLATE/task.md`): Owner · Plan: `plans/<n>-<slug>.md` · Done when (rubric line) · Depends on (e.g. "Deploy …" issues depend on the component issue and on Eugene; ML depends on storage; app live charts depend on the contracts issue only — they use mock data until storage lands).

- [ ] **Step 1:** Create labels and milestones; verify `gh label list --limit 100 | wc -l` ≥ 31 and `gh api repos/ASU-MICS-2028/cc-group-3-prosit-3/milestones -q 'length'` = 5.
- [ ] **Step 2:** Create issues from `issues.tsv` with `gh issue create --title --body --assignee --label --milestone`; record each returned number. Verify `gh issue list --limit 100 --json number -q length` = 50.
- [ ] **Step 3:** Generate one plan stub per issue named `plans/<number>-<slug>.md`; edit each issue body to link its plan path.
- [ ] **Step 4:** Fill `plans/README.md` rows; write `changes/C-001-initial-issues-and-plans.md` (AI use: Claude Code generated issue text and stubs from the lab handouts and brief; Joseph reviewed owners).
- [ ] **Step 5:** Branch `process/<n>-initial-issues` (n = the "Open initial issues and plan stubs" issue), commit, open PR with `Closes #<n>`. CI green → one non-author approval → merge.

### Task 3: Seed `knowledge/` (and starter `learnings/`) as atomic notes

**Files:**
- Create: `knowledge/*.md` (expected ~80–150 notes) and topic map notes `knowledge/map-<topic>.md`
- Create: `learnings/*.md` for gotchas and procedures carried over from Prosit 1–2 learnings and sessions (expected ~20–40)
- Modify: `knowledge/README.md`, `learnings/README.md`
- Create: `changes/C-002-seed-knowledge.md`

**Interfaces:**
- Consumes: note template and `check_notes.py` from Task 1.
- Sources (read-only): lecture transcripts `/Users/josetseph/Library/CloudStorage/OneDrive-Personal/KB/ashesi/notes/Cloud Computing/Lectures/Lecture 1–11.md`, `Notes.md`, `Study Session 1.md`; labs `/Users/josetseph/Downloads/school/Cloud Computing/{Complete/prosit 1,prosit 2,prosit 3}/week*_lab*.docx` (convert with `textutil -convert txt -stdout`); brief `prosit 3/Prosit 3.docx` and `Prosit 3 Launch.pptx`; course description; Prosit 2 repo `knowledge/`, `learnings/`, `knowledge/sessions/`, `docs/decisions.md`; Prosit 1 repo `docs/`.

Topic maps (one `map-*.md` each, linked from `README.md`): `map-course` (logistics, grading, dates), `map-lectures` (one entry per lecture → its concept notes), `map-labs` (one note per lab: requirements, deliverables, rubric), `map-smartcity-brief`, `map-scaling-monitoring`, `map-cost-sustainability`, `map-iot-edge`, `map-ml-mlops`, `map-security`, `map-prosit-1-2-carryover`.

- [ ] **Step 1:** Open issue "Seed knowledge notes…" (already created in Task 2) and branch `docs/<n>-seed-knowledge`.
- [ ] **Step 2:** Fan out in parallel, one worker per source group: (a) lectures 1–4, (b) lectures 5–8, (c) lectures 9–11 + notes, (d) labs 0–9, (e) labs 10–14 + brief + launch deck + course description, (f) Prosit 1–2 knowledge/learnings/decisions → carry-over notes. Each worker writes notes only (no README edits), cites `source:` precisely (e.g. `Lecture 7`, `Lab 12 Part C`, `Prosit 2 D-031`), and returns its file list with a one-line hook per note and a suggested map.
- [ ] **Step 3:** Merge duplicates (same idea from two sources → one note, both sources), add `## Related` links across workers' notes, write the maps and both README indexes.
- [ ] **Step 4:** Run `python3 scripts/check_notes.py knowledge learnings` → exit 0; `lychee --offline 'knowledge/**/*.md' 'learnings/**/*.md'` → 0 errors.
- [ ] **Step 5:** Privacy pass (Review Focus 4): `grep -rniE '\+?233[0-9 ]{9}|@[a-z0-9.-]+\.(com|edu)' knowledge learnings` → no output; read every note that mentions a person and keep only the four members and course staff.
- [ ] **Step 6:** Write `changes/C-002-seed-knowledge.md` (AI use: Claude Code subagents drafted notes from the listed sources; Joseph spot-checked N notes per map); commit, PR, approval, merge.

### Task 4: First draft of the shared contracts

**Files:**
- Create: `contracts/sensor-reading.schema.json`, `contracts/examples/{air-quality,waste-bin,flood-level}.json`, `contracts/examples/bad/missing-unit.json`
- Create: `contracts/mqtt-topics.md`, `contracts/api.openapi.yaml`, `contracts/storage.md`
- Create: `contracts/tests/test_contracts.py`, `contracts/requirements.txt` (`jsonschema==4.23.0`, `PyYAML==6.0.2`)
- Modify: `contracts/README.md`, `.github/workflows/checks.yml` (job `contracts`: install requirements, run tests; add `contracts` to the protection contexts)
- Create: `decisions/D-001-sensor-reading-and-topic-contract.md` (status `proposed`), `changes/C-003-contracts-draft.md`

**Interfaces:**
- Produces (values every area builds against):
  - Reading fields: `device_id` (string, `^[a-z]+-[a-z0-9-]+-\d{3}$`, e.g. `aq-jamestown-001`), `domain` (`air_quality` | `waste` | `flood`), `metric` (`pm25` | `fill_pct` | `water_level_cm`), `value` (number), `unit` (`ug/m3` | `%` | `cm`), `ts` (RFC 3339 UTC string), `seq` (integer ≥ 0, per device), optional `battery_pct` (0–100), optional `source` (`simulator` | `openaq` | `device`). `additionalProperties: false`. Domain/metric/unit pairs enforced with `oneOf`.
  - Topic: `accra/<neighbourhood>/<domain>/<device_id>`, QoS 1, neighbourhood kebab-case (`east-legon`, `jamestown`, `makola`, `nima`, `asylum-down`). Per-device MQTT username = `device_id`; ACL lets a device publish only to its own topic.
  - API (OpenAPI 3.1, paths only with request/response schemas): `GET /readings/latest?domain=`, `GET /readings?device_id=&from=&to=&interval=raw|1h`, `GET /alerts?status=open`, `GET /predictions/pm25?station=&horizon_h=24|48`, `POST /reports` (citizen report: category, description, lat, lon, optional photo URL), `GET /open-data/{domain}` (hourly aggregates only).
  - Storage (logical): one measurement/table per domain (`air_quality`, `waste`, `flood`) with tags `device_id, neighbourhood` and the reading fields; hourly rollup `<domain>_hourly` (avg/min/max/count); raw retention 90 days (Lab 11 Part C).

- [ ] **Step 1: Write failing tests** `test_examples_valid` (each `examples/*.json` validates), `test_bad_example_rejected` (each `examples/bad/*.json` raises `ValidationError`), `test_wrong_unit_for_domain_rejected` (air_quality with `unit: "cm"` fails), `test_openapi_has_paths` (the six paths above exist in `api.openapi.yaml`).
- [ ] **Step 2: Run** `python3 -m unittest discover contracts/tests -v` → FAIL (files missing).
- [ ] **Step 3: Write** the schema, examples, topics doc, OpenAPI file, storage doc with the values above.
- [ ] **Step 4: Run tests** → 4 PASS.
- [ ] **Step 5:** Write D-001 (proposed: options considered, e.g. topic per device vs per domain) and C-003; open PR tagging `@eugene-sew @Elise-Oyi @PeaElorm` for comment; merge on one non-author approval. D-001 status flips to `accepted` in that PR or a follow-up once nobody objects.

---

## Execution order

Task 1 → Task 2 → Tasks 3 and 4 in parallel (independent folders; each adds its own change file — C-002 and C-003 are reserved here so they don't collide).
