# Privacy and data ownership

Issue #40. Written for residents, assembly members and AMA staff, and used in the final report (#47).

**In short:** the sensors measure air, bins and drains, not people. The only personal data we hold is in citizen reports, and we keep those as small as we can. Any neighbourhood can have its sensors switched off.

## Who owns the data

| Data | Who owns it | Who can see it |
| --- | --- | --- |
| Sensor readings (PM2.5, bin fill, drain level, battery) | AMA, which owns the sensors. It holds the readings for the city's residents. | Everyone. Each neighbourhood's hourly figures are free to download from `/open-data`. [#42](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/issues/42) decides exactly what that portal may show. |
| Real air-quality readings from OpenAQ | The station's operator, which publishes them through OpenAQ. | Everyone. We tag them `source: openaq` so they stay credited. |
| Forecasts and flood alerts | AMA (the platform makes them from the readings) | Everyone, through the API, the dashboard and the app |
| Citizen reports | The resident who sends a report gives it to AMA so AMA can act on it | AMA staff only. No API endpoint returns reports. |

## What we never collect

- **Who sent a report.** A report holds a category, a description of up to 1,000 characters, a location, and optionally a photo link. That's all the API accepts: a report with a name, phone number or any other extra field is refused ([`contracts/api.openapi.yaml`](../contracts/api.openapi.yaml), `CitizenReport`). The test for this is `api/tests/test_app.py`.
- **IP addresses.** The API's request log keeps the time, the request and the status, but not the caller's address (`log_message` in [`api/app.py`](../api/app.py)).
- **Where people go.** A report carries one location, which the person chooses to send with it. Nothing receives a location history.
- **Images or sound of people.** We have no cameras and no computer vision ([decision 54](../decisions/54-not-built.md)).
- **Sensor locations finer than the neighbourhood in open data.** `/open-data` groups readings per neighbourhood per hour and leaves out device ids.

## How a neighbourhood can switch its sensors off

1. **Ask.** The assembly member or a community group writes to AMA. They don't have to give a reason.
2. **Cut the sensors off.** The operator revokes each device in that neighbourhood. Device ids contain the neighbourhood's name (for example `aq-nima-001`, `fl-nima-001`).
   ```bash
   python3 ingest/devices.py revoke aq-nima-001
   ```
   The broker drops that device at once and the others keep running. We tested this in the #21 drill: [`learnings/mosquitto-reload-disconnects-a-revoked-device.md`](../learnings/mosquitto-reload-disconnects-a-revoked-device.md). The device can then be taken down.
3. **Delete what's stored, if asked.** Run this for each of `air_quality`, `waste` and `flood`, and for each table's hourly rollup:
   ```sql
   DELETE FROM air_quality WHERE neighbourhood = 'nima';
   ```
   Without a request, raw readings are deleted after 90 days anyway ([`contracts/storage.md`](../contracts/storage.md); the deletion job is part of #22), and the hourly rollups are kept.
4. **Switch back on** whenever they ask: `devices.py init` issues new passwords for every device.

A resident who wants a report deleted gives AMA the report id that `POST /reports` returns, so the app should show that id after the report is sent.

## Gaps before this goes live

- **Ghana's Data Protection Act, 2012 (Act 843).** A report's location and description could identify the person who sent it (for example, "outside my house"), so reports count as personal data. AMA would need to register with the Data Protection Commission as the organisation responsible for that data before running the system for real.
- **Where the data is stored.** The database runs in AWS `af-south-1`, in Cape Town, outside Ghana ([decision 13](../decisions/13-region-choice-carbon.md)). That's fine for sensor readings, which aren't personal. For reports, AMA should check with the Data Protection Commission that storing them abroad is allowed, or keep reports in Ghana.
- **How long reports are kept** isn't set yet. Our proposal is to delete each report 12 months after it arrives.
- **Photos.** We store only a link to a photo, and a photo can still show faces or number plates. Before showing the photo option, the app should ask people not to photograph anyone.
