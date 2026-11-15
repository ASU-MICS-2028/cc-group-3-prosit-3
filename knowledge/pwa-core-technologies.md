---
title: Core PWA technologies are the service worker, web app manifest and cache API
tags: [lecture, edge]
source: Lecture 6
---

A progressive web app (PWA) is a web app that installs from the browser and works offline. The three building blocks named in class:

- **Service worker**: script that intercepts requests and serves cached responses when offline.
- **Web app manifest**: JSON file giving the app its name, icons and install behaviour.
- **Cache API**: stores responses locally so content loads once and is reused.

Design goals from the Prosit 1 context: responsive across device sizes, minimal on-device storage, efficient caching to save data costs, browser-based install, automated updates, focus on Android over iOS, and attention to battery use.

## Related
- [Offline-first design for unreliable connectivity](offline-first-design-for-low-connectivity.md)
- [Offline sync needs a conflict resolution strategy, like merging in Git](offline-sync-conflict-resolution.md)
