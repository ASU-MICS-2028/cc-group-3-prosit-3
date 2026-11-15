---
title: Static PWA hosting: cache headers and how a new release reaches phones
tags: [storage, networking, prosit-2]
source: Prosit 2 learnings/infra.md (items 15 and section 6); Prosit 2 docs/decisions.md D-033; Prosit 1 docs/learnings.md (candidate L-006)
---

Deploy shape in Prosit 2: build, upload `assets/` (hashed names, immutable, never deleted), then upload everything else as `no-cache` with `--delete`, invalidate `/*` on CloudFront, and smoke-test `/`, `/login`, `/sw.js` and the manifest. Takes about two minutes.

Rules Prosit 1 recorded as the target: `index.html` no-cache, `sw.js` never cached, hashed assets cached for a year.

Gotchas:
- A new release reaches phones on their next open, not instantly: the service worker serves the saved app first (that is the offline feature). Change the worker's `VERSION` when its behaviour changes.
- The PWA and the API are different origins, so the API needs CORS for the app's origin, or route `/api/*` through CloudFront.
- Merging a frontend change does nothing unless a deploy job runs.

Relevance: the SmartCity operator dashboard or citizen app can follow the same pattern.

## Related
- [CloudFront needs its certificate in us-east-1 and routes by Host header, not by DNS target](cloudfront-cert-region-and-host-header-routing.md)
- [CI/CD shape that worked: test everything, scan, then deploy only what changed on merge to main](cicd-pipeline-shape-test-scan-deploy-changed.md)
