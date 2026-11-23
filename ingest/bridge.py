"""MQTT -> time-series DB bridge with local buffering (#20, Lab 12 Part C).

Every reading is first appended to a local spool file (JSON lines, fsynced), then written to the DB in
batches once a second. If the DB is down the spool just grows; when it comes back the backlog goes in
first. One path for normal running and outages, and a crash loses nothing that was acknowledged:
repeats are harmless because (device_id, ts) is unique and inserts use ON CONFLICT DO NOTHING.

Run:   DATABASE_URL=postgresql://smartcity:<password>@localhost:5432/smartcity python3 ingest/bridge.py
Env:   MQTT_HOST (localhost), MQTT_PORT (1883), SPOOL (ingest/spool.jsonl), BATCH_MAX (500)
"""
import json
import os
import sys
import threading
import time
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "contracts" / "sensor-reading.schema.json").read_text())
VALIDATOR = jsonschema.Draft202012Validator(SCHEMA, format_checker=jsonschema.FormatChecker())
# contracts/storage.md: one table per domain, the value column is named after the metric
TABLE = {"air_quality": ("air_quality", "pm25"), "waste": ("waste", "fill_pct"), "flood": ("flood", "water_level_cm")}


def parse(topic, payload):
    """Topic + payload -> row dict, or raise ValueError. This is the trust boundary: devices are not trusted."""
    parts = topic.split("/")
    if len(parts) != 4 or parts[0] != "accra":
        raise ValueError(f"bad topic {topic}")
    _, neighbourhood, domain, device_id = parts
    try:
        r = json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise ValueError(f"not JSON: {e}") from e
    errors = sorted(VALIDATOR.iter_errors(r), key=str)
    if errors:
        raise ValueError(f"schema: {errors[0].message}")
    if r["device_id"] != device_id or r["domain"] != domain:
        raise ValueError(f"payload {r['device_id']}/{r['domain']} does not match topic {topic}")
    if not device_id.split("-", 1)[1].startswith(neighbourhood + "-"):
        raise ValueError(f"device {device_id} is not in {neighbourhood}")
    return {**r, "neighbourhood": neighbourhood}


class Spool:
    """Append-only JSON-lines file; drained only after the DB commits. Thread-safe."""

    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch()
        self.lock = threading.Lock()  # MQTT thread appends while the main thread drains

    def append(self, row):
        with self.lock, self.path.open("a") as f:
            f.write(json.dumps(row) + "\n")
            f.flush()
            os.fsync(f.fileno())

    def read(self):
        with self.lock:
            return [json.loads(line) for line in self.path.read_text().splitlines() if line.strip()]

    def drop_first(self, n):
        with self.lock:
            rest = self.path.read_text().splitlines(keepends=True)[n:]
            tmp = self.path.with_suffix(".tmp")
            tmp.write_text("".join(rest))
            os.replace(tmp, self.path)  # atomic: a crash leaves either the old or the new file


def flush(spool, write, batch_max):
    """Write up to batch_max spooled rows. Returns rows written; leaves the spool alone if write() fails."""
    rows = spool.read()[:batch_max]
    if not rows:
        return 0
    write(rows)
    spool.drop_first(len(rows))
    return len(rows)


class Db:
    """TimescaleDB/Postgres writer. Reconnects on the next batch after a failure."""

    def __init__(self, url):
        self.url = url
        self.conn = None

    def write(self, rows):
        import psycopg

        try:
            if self.conn is None or self.conn.closed:
                self.conn = psycopg.connect(self.url, connect_timeout=2)
            with self.conn.transaction(), self.conn.cursor() as cur:
                for domain, (table, column) in TABLE.items():
                    batch = [r for r in rows if r["domain"] == domain]
                    if batch:
                        cur.executemany(
                            f"INSERT INTO {table} (ts, device_id, neighbourhood, source, seq, {column}, battery_pct) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (device_id, ts) DO NOTHING",
                            [(r["ts"], r["device_id"], r["neighbourhood"], r.get("source", "simulator"),
                              r["seq"], r["value"], r.get("battery_pct")) for r in batch])
        except psycopg.Error:
            if self.conn is not None:
                self.conn.close()
            self.conn = None
            raise


def main():
    import paho.mqtt.client as mqtt
    import psycopg

    spool = Spool(os.environ.get("SPOOL", ROOT / "ingest" / "spool.jsonl"))
    db = Db(os.environ["DATABASE_URL"])
    batch_max = int(os.environ.get("BATCH_MAX", "500"))

    def on_message(client, userdata, msg):
        try:
            spool.append(parse(msg.topic, msg.payload))
        except ValueError as e:
            print(f"rejected {msg.topic}: {e}", file=sys.stderr, flush=True)

    def on_connect(client, userdata, flags, reason, props):
        client.subscribe("accra/+/+/+", qos=1)
        print(f"connected to MQTT ({reason})", flush=True)

    # Fixed client id + clean_session=False: the broker keeps QoS 1 readings for us while the bridge is down.
    c = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="bridge-1", clean_session=False)
    c.on_message, c.on_connect = on_message, on_connect
    c.connect_async(os.environ.get("MQTT_HOST", "localhost"), int(os.environ.get("MQTT_PORT", "1883")))
    c.reconnect_delay_set(1, 30)
    c.loop_start()  # paho's thread receives and reconnects; this thread writes to the DB
    db_ok = True
    try:
        while True:
            time.sleep(1)
            try:
                while (n := flush(spool, db.write, batch_max)):
                    print(f"wrote {n}", flush=True)
                if not db_ok:
                    print("DB back; backlog flushed", flush=True)
                db_ok = True
            except psycopg.Error as e:
                if db_ok:
                    print(f"DB down, buffering to {spool.path}: {str(e).strip().splitlines()[0]}", flush=True)
                db_ok = False
    except KeyboardInterrupt:
        pass
    finally:
        c.disconnect()
        c.loop_stop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
