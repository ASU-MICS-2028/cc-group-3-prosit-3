---
title: WebRTC results: direct paths worked, Chrome Slow 3G does not throttle media, TURN cost is a range
tags: [networking, edge, prosit-2]
source: Prosit 2 learnings/lab7-webrtc.md (sections 6b and 8)
---

Calls between two ISPs about 120 km apart all connected directly via a public STUN server (`srflx`); no TURN relay was needed. Round trip was 138-192 ms. Three calls do not prove every carrier allows it, so production still budgets for TURN. Same Wi-Fi still showed `srflx` pairs because Chrome hides local addresses.

Under a bad connection WebRTC dropped frames (to 1-2 per second), not packets: adaptive bitrate.

Chrome DevTools "Slow 3G" does not throttle WebRTC media. The team shaped the whole Mac with macOS's built-in tools: `sudo dnctl pipe 1 config bw 400Kbit/s delay 150 plr 0.01`, then `pfctl` rules (undo: `pfctl -f /etc/pf.conf; pfctl -d; dnctl -q flush`). Result: round trip 157 to 735-947 ms, jitter 16 to 409-827 ms, video 31 to 5-7 fps, call never dropped; so be audio-first on 3G.

TURN cost, 50 calls/day x 15 min all relayed (about 337 GB/month at 1 Mbit/s, assumed): Cloudflare managed ~$0 (free tier), Twilio ~$135, self-hosted coturn ~$9 server plus unconfirmed af-south-1 egress.

Method lesson: use browser stats (`getStats`) and quote the numbers.

## Related
- [A load balancer cuts silent connections after 60 seconds, so ping every 25](websocket-idle-timeout-needs-heartbeat.md)
- [Capture evidence honestly: report the real result, label what is faked, never rewrite history](honest-evidence-capture.md)
