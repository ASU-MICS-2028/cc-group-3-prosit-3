# Plan: Design system and screen set for web and mobile

- **Issue:** #17
- **Owner:** Perfect (`PeaElorm`)
- **Milestone:** Lab 12
- **Status:** in progress

## Goal
Give the AMA web dashboard (Elise) and the citizen app (Perfect) one look and one set of components, so neither is invented twice. It must work for residents on cheap phones and slow networks.

## What gets built
Look taken from the reference the team shared (light and dark phone screens, round controls, Poppins type, frosted glass), in the "Stone" colours the team chose on 27 Nov (greige, off-white, sand, charcoal):
- `design/design-system.html`: the design system in one page: colour (light and dark), type, icons, shape and space, and every component with its states.
- `design/tokens.css`: colours, type scale, spacing, radius. A theme is set per screen with `data-theme="light"` or `"dark"`.
- `design/components.css`: dial, vertical slider with value bubble, round bubbles, option buttons, switches, device tiles, tabs, pill bottom nav, glass cards, alerts, badges, forms, offline notice, chart frame.
- `design/icons.css`: line icons (Feather, MIT licence) as masks, so they take the text colour.
- `design/screens/citizen-app.html`: six citizen screens (welcome, home with PM2.5 dial, flood warning with "why" and flag, report an issue, my alerts, offline).
- `design/screens/ama-dashboard.html`: the officials' dashboard.
- `design/check_contrast.py` and `design/check_layout.sh`: contrast of every pair, and sideways overflow at 320 px at 100% and 200% text.
- `evidence/lab12/`: contrast output and layout output, as text.

## Depends on
- #2 (contracts, done): what data each screen shows.

## Done when
- Tokens, components and the main screens for both apps exist and open in a browser with no build step.
- Every text/background pair passes AA contrast, in light and dark.
- Screens stay usable at 200% text size and at 320 px width (no sideways scrolling, nothing cut off).
- Elise has been told where the tokens are, so #23 can use them.

## Evidence to capture
- Contrast check output (script plus its result) in `evidence/lab12/`.
- Layout check output (overflow at 320 px, 100% and 200% text). No screenshots in the repo: reviewers open the pages in a browser.

## Not doing
- No JavaScript framework or build tooling: plain HTML and CSS is easier for Elise and the PWA to reuse.
- No real data or API calls: screens use example values from `contracts/examples/`.
- No photographs. The reference uses photos behind its screens; we use soft glows, and real Accra photos can be added later.
- No translations yet; #43 checks which languages matter and states the gaps.
- Poppins is loaded from Google Fonts (a small download, with system fonts as fallback). If the team decides that is too heavy for low-end phones, drop the font link; nothing else changes.
