# Web dashboard

- **Owner:** Elise (UI/UX with Perfect)
- **Purpose:** AMA officials' dashboard: live readings, alerts, forecasts, open data, SDG 11 view.
- **Builds against:** [API contract](../contracts/api.openapi.yaml)

## Run locally

Use Node.js 22.12+ on the 22.x line, or a newer supported Node.js release. From the repo root:

```sh
cd web
npm ci
npm run dev
```

Open the URL Vite prints. The scaffold displays the dashboard heading. Run `npm run build` to type-check and build it.

The [#23 plan](../plans/23-l12-web-shell.md) tracks the live chart and lab evidence.
