---
title: Service worker plus manifest gives an installable, offline-rendering app shell
tags: [lab, prosit-1]
source: Lab 4 Part D and Troubleshooting
---

Register sw.js, precache the shell (/ , index.html, manifest.json) on install, and answer fetches cache-first. Add manifest.json (name, start_url, display standalone, icons) to make it installable. Test: DevTools, Application, Service Workers, tick Offline, reload; run Lighthouse PWA audit.

Gotchas: browsers cache service workers aggressively, so hard refresh or unregister while developing; low Lighthouse scores usually mean missing icons, no offline fallback, or no HTTPS (localhost is exempt).

SmartCity Accra: a resident dashboard could use the same shell.

## Related
- [Queue offline writes in IndexedDB and replay with Background Sync](background-sync-offline-write-queue.md)
- [Lab 4 - managed Postgres, private object storage and an offline-capable PWA](lab-4-managed-database-storage-offline-pwa.md)
