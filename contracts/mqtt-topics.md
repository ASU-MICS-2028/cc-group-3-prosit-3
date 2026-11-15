# MQTT topics

Draft v0 (D-001, proposed). Every reading is published as JSON matching [`sensor-reading.schema.json`](./sensor-reading.schema.json).

## Topic layout

```
accra/<neighbourhood>/<domain>/<device_id>
```

| Part | Values | Example |
|---|---|---|
| `neighbourhood` | kebab-case: `east-legon`, `jamestown`, `makola`, `nima`, `asylum-down` (add more by PR) | `jamestown` |
| `domain` | `air_quality`, `waste`, `flood` | `air_quality` |
| `device_id` | `<aq\|wb\|fl>-<neighbourhood>-<NNN>` | `aq-jamestown-001` |

Example: `accra/jamestown/air_quality/aq-jamestown-001`

Subscribers use wildcards: the bridge subscribes to `accra/+/+/+`; a dashboard for one area can use `accra/makola/#`.

## Delivery

- **QoS 1** (at least once). Duplicates are possible, so consumers drop repeats using `(device_id, ts)`. `seq` restarts at 0 when a device restarts, so never use it alone to detect duplicates.
- No retained messages for readings. Devices publish every 60 s by default (simulator setting); flood devices every 10 s when the level is rising.

## Device identity

- Each device signs in with **its own** username (= `device_id`) and password. No shared credentials.
- The broker ACL lets a device **publish only to its own topic** and subscribe to nothing.
- Revoking a device = deleting its credential; other devices are unaffected (Lab 12 Part E).
