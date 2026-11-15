---
title: HealthConnect telemedicine: WebRTC with a signaling server and an audio-only fallback
tags: [prosit-2, networking, edge]
source: Prosit 2 learnings/lab7-webrtc.md; Prosit 2 learnings/frontend.md (FB-4); Prosit 2 docs/decisions.md D-023
---

Media goes directly between browsers; the servers only do signaling (a Node WebSocket server with rooms of at most two people, no login) and STUN is public. It runs as one container on one server behind the ALB (host-header rule) because rooms live in memory, with a 25 s heartbeat.

In the app: 320x240 at about 15 fps and about 150 kbit/s video cap (usable on 3G); stats every 2 s judged good or weak; two weak readings (4 s) suggest "Switch to audio?", five (10 s) switch automatically; a pre-call check page (secure page, signal, server reachable, microphone); call codes are case- and space-insensitive and made from the appointment; a dropped connection waits 10 s then ends with a plain message. Your own preview is mirrored, the sent video is not.

Not built: TURN relay, authenticated rooms, recording with consent.

SmartCity: only relevant if the capstone adds live video; otherwise the heartbeat and single-stateful-server lessons still apply to MQTT.

## Related
- [HealthConnect's known weak points, useful input for a consolidated architecture review](healthconnect-known-weak-points.md)
- [HealthConnect PWA and sync architecture in one page](healthconnect-pwa-and-sync-architecture.md)
