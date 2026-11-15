---
title: WebRTC - test across two networks because direct peer links often fail
tags: [networking, lab, prosit-2]
source: Lab 7 Part C and Troubleshooting
---

A WebSocket signaling server relays offers, answers and ICE candidates; STUN helps NAT traversal. Same-network calls connect directly; across a campus network and mobile data they often fail because carrier NATs block peer-to-peer, so production needs a TURN relay and a bandwidth budget. Homework: estimate TURN cost for 50 calls/day x 15 min for Week 11.

If messages do not relay, confirm both tabs connected (log onopen).

## Related
- [Measure connection quality with real stats](webrtc-measure-real-stats-not-impressions.md)
- [Lab 7 - event-driven serverless reminders and a WebRTC video call](lab-7-event-driven-serverless-and-webrtc.md)
