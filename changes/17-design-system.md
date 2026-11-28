---
issue: 17
title: Design tokens, components and screens for the web dashboard and citizen app
date: 2026-11-25
pr: "(this PR)"
in_charge: Perfect Elorm Avugla
reviewed_by: (whoever approves this PR)
---

## What changed

- `design/design-system.html`: the design system on one page (colour, type, icons, shape and space, every component and state).
- `design/tokens.css`, `design/components.css`, `design/icons.css`: the styles. Light and dark themes per screen; dial, vertical slider, round bubbles, options, switches, tiles, tabs, pill nav, glass cards, alerts, badges, forms.
- `design/screens/`: six citizen app screens and the AMA dashboard, using field names from `contracts/api.openapi.yaml`.
- Colours: the "Stone" palette (greige, off-white, sand, charcoal). The first lime and yellow version was called too loud; the team compared four options and chose Stone on 27 Nov. Every colour in the styles is a token, so changing the look again means editing only `tokens.css`.
- `design/check_contrast.py` (every text/background pair, including text on glass) and `design/check_layout.sh` (overflow at 320 px, 100% and 200% text).
- `design/README.md`, the plan for #17, and evidence in `evidence/lab12/` (check output as text; no screenshots, to keep the repo small).

## Why

Elise's dashboard (#23) and my app (#24) should look like one product and not be designed twice. The look follows the reference I chose (round controls, light and dark screens, Poppins, frosted glass), in calm colours the team picked. A first version only copied its colours and looked generic; this one reproduces its controls and feel.

## How to check
```bash
python3 design/check_contrast.py                       # ends with "0 failing pair(s)"
design/check_layout.sh design/design-system.html      # overflow=0px at 100% and 200%
design/check_layout.sh design/screens/citizen-app.html
design/check_layout.sh design/screens/ama-dashboard.html
open design/design-system.html design/screens/citizen-app.html design/screens/ama-dashboard.html
```
The design system page shows light and dark panels side by side. Needs internet once for the Poppins font.

## AI use
- **Tool:** Claude Code
- **What it did:** wrote the plan, tokens, components, screens, the two check scripts and the README; built a comparison page of four colour options for the team's vote, then applied the chosen one; found and fixed contrast failures (borders, muted text on the warm glow), overflow at 200% text, and wrapping of tile names. A first version was rejected as generic and redone against the reference images.
- **Prompts / session summary:** asked for a roadmap and checklist for my issues, then to start on #17 using two design reference images I supplied. After reviewing the first result I said it looked generic and nothing like the reference, and asked where the design system file was; it was rebuilt to match. The team then found the colours too loud; after comparing options they chose Stone, and I asked for it to be applied and for screenshots to be left out of the repo.
- **What the person checked or changed:** I supplied the reference images and rejected the first version as generic; the team chose the Stone colours. I opened all the HTML pages (design-system.html, citizen-app.html, ama-dashboard.html) in Chrome and inspected them at small screen widths, where I found table text breaking mid-word, which was then fixed.

## Decisions made
- none

## Not done
- Not tested on a real low-end phone (needs a person).
- No real charts; the chart frame is a placeholder.
- No photographs behind screens (the reference has them); soft glows instead.
- `check_layout.sh` measures sideways overflow only; it doesn't catch words split mid-word (that was found by eye on the dashboard table and fixed), so look at the pages at phone width too.
