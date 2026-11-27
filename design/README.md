# Design

- **Owner:** Perfect
- **Purpose:** One look for the AMA web dashboard and the citizen mobile app: colours, type, components and the main screens.
- **Builds against:** [`contracts/api.openapi.yaml`](../contracts/api.openapi.yaml) (field names and the plain-words `reason` on alerts)

Plain HTML and CSS. No build step: open the files in a browser.

## What's here

| File | What it is |
| --- | --- |
| [`design-system.html`](./design-system.html) | **The design system.** One page: colour, type, icons, shape and space, and every component with its states. Start here. |
| [`tokens.css`](./tokens.css) | Colours (light and dark), type scale, spacing, radius. Set `data-theme="light"` or `"dark"` on any element. |
| [`components.css`](./components.css) | The components: dial, vertical slider, bubbles, options, switches, tiles, tabs, pill nav, glass cards, alerts, badges, forms. |
| [`icons.css`](./icons.css) | Line icons (Feather, MIT licence). `<i class="ico i-home" aria-hidden="true"></i>` |
| [`screens/citizen-app.html`](./screens/citizen-app.html) | Six citizen screens: welcome, home, flood warning (why + flag), report an issue, my alerts, offline. |
| [`screens/ama-dashboard.html`](./screens/ama-dashboard.html) | The AMA officials' dashboard. |
| [`check_contrast.py`](./check_contrast.py) | Checks every text and background pair in `tokens.css`, light and dark, including text on glass. |
| [`check_layout.sh`](./check_layout.sh) | Opens a page in a true 320 px frame at 100% and 200% text and reports sideways overflow. |

Screens show the contract's example values, not live data. The layout and controls follow the reference the team shared; the colours are the "Stone" palette (greige, off-white, sand, charcoal) the team chose on 27 Nov over louder lime and two other options; the design system page shows it in full.

## Using it (Elise, and the app)

```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="design/tokens.css">
<link rel="stylesheet" href="design/icons.css">
<link rel="stylesheet" href="design/components.css">
```

Use the variables (`var(--ink)`, `var(--surface)`, `var(--space-4)`) instead of hard-coded colours or sizes. Wrap each screen in `<section class="screen" data-theme="dark">` (or `"light"`), and put cards in `class="glass"`.

## Rules

- **Sand is a fill, with dark text.** Never sand text on a light background.
- **Never colour alone.** Status is always an icon plus a word.
- **Touch targets are at least 44 px** (`--tap`).
- **Sizes in rem, never px for text**, so 200% text size scales everything. Long words wrap (`overflow-wrap: anywhere`).
- **Glass falls back to solid** on phones that cannot blur, and when the user asks for reduced transparency. Text contrast is checked against the glass over both ends of the backdrop.
- **Poppins, with system fonts as the fallback**, so text shows at once even if the font is slow. If the font proves too heavy for low-end phones, remove the font link; nothing else changes.

## Check it

```bash
python3 design/check_contrast.py           # every pair must PASS
design/check_layout.sh design/design-system.html   # needs Google Chrome; overflow must be 0px
```

Evidence for Lab 12 is in [`evidence/lab12/`](../evidence/lab12/): contrast output and layout check output (text only; no screenshots, to keep the repo small).

## Not here yet

- No real charts: the chart frame is a placeholder the app fills.
- No photographs: the reference uses photos behind its screens; we use soft glows instead.
- No translations; issue #43 decides which languages matter.
- Not tested on a real low-end phone: that needs a person.
