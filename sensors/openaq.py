"""OpenAQ feeder (#19): the last 24 h of real PM2.5 from one Accra station, through the same MQTT pipeline.

Run:   python3 sensors/openaq.py              # publish as aq-madina-001 (needs its password: ingest/devices.py init)
Try:   python3 sensors/openaq.py --dry-run    # print the readings instead
Reads OpenAQ's public S3 archive, which needs no API key. The archive runs a few days behind, so
"last 24 h" means the 24 h before the station's newest archived reading. Timestamps are kept as measured.
"""
import argparse
import csv
import gzip
import io
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(__file__))
from simulator import load_passwords, mqtt_publisher, topic  # noqa: E402

ARCHIVE = "https://openaq-data-archive.s3.amazonaws.com"
LOCATION = 3025587  # "Madina Zongo Junction", 5.6779 N, -0.17295 E: a low-cost PM2.5 sensor in Madina, Accra
DEVICE = ("aq-madina-001", "madina", "air_quality")  # its MQTT identity; devices.py gives it a password and ACL


def get(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read()


def latest_files(location, now, n=2):
    """Archive keys of the station's last n daily files, looking in this month and last month."""
    keys = []
    for t in (now.replace(day=1) - timedelta(days=1), now):
        prefix = f"records/csv.gz/locationid={location}/year={t.year}/month={t.month:02d}/"
        keys += re.findall(r"<Key>([^<]+)</Key>", get(f"{ARCHIVE}/?list-type=2&prefix={prefix}").decode())
    return sorted(keys)[-n:]


def readings(rows, hours=24):
    """OpenAQ archive CSV rows -> sensor readings (contracts/sensor-reading) for the last `hours` before the newest."""
    pm = sorted({datetime.fromisoformat(r["datetime"]): float(r["value"])
                 for r in rows if r["parameter"] == "pm25" and 0 <= float(r["value"]) <= 1000}.items())
    if not pm:
        return []
    since = pm[-1][0] - timedelta(hours=hours)
    return [{"device_id": DEVICE[0], "domain": "air_quality", "metric": "pm25", "value": round(v, 1),
             "unit": "ug/m3", "ts": t.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "seq": i,
             "source": "openaq"}
            for i, (t, v) in enumerate(p for p in pm if p[0] > since)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--host", default="localhost")
    ap.add_argument("--port", type=int, default=1883)
    ap.add_argument("--location", type=int, default=LOCATION)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--creds", default=os.path.join(os.path.dirname(__file__), "..", "ingest", "device_credentials.csv"))
    a = ap.parse_args()

    rows = []
    for key in latest_files(a.location, datetime.now(timezone.utc)):
        rows += csv.DictReader(io.StringIO(gzip.decompress(get(f"{ARCHIVE}/{key}")).decode("utf-8")))
    out = readings(rows)
    if not out:
        sys.exit(f"no PM2.5 readings in the archive for location {a.location}")
    print(f"{len(out)} readings {out[0]['ts']} .. {out[-1]['ts']}", file=sys.stderr)
    dev = dict(zip(("device_id", "neighbourhood", "domain"), DEVICE))
    if a.dry_run:
        publish = lambda d, r: print(topic(d), json.dumps(r))  # noqa: E731
    else:
        publish, clients = mqtt_publisher(a.host, a.port, load_passwords(a.creds))
    for r in out:
        publish(dev, r)
    if not a.dry_run:
        for c in clients.values():
            c.disconnect()
            c.loop_stop()


if __name__ == "__main__":
    main()
