"""SmartCity Accra REST API (contracts/api.openapi.yaml): what the web dashboard and the mobile app call.

Run:   DATABASE_URL=postgresql://smartcity:<password>@localhost:5432/smartcity python3 api/app.py
Env:   PORT (8000)
Reads the tables the bridge writes (ingest/dev-schema.sql, later Elise's #22) and creates its own
(api/schema.sql). Standard library HTTP server plus psycopg; no framework.
"""
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
API = yaml.safe_load((ROOT / "contracts" / "api.openapi.yaml").read_text())
REPORT = jsonschema.Draft202012Validator(API["components"]["schemas"]["CitizenReport"],
                                         format_checker=jsonschema.FormatChecker())
# contracts/storage.md: one table per domain, value column named after the metric
DOMAINS = {"air_quality": ("pm25", "ug/m3"), "waste": ("fill_pct", "%"), "flood": ("water_level_cm", "cm")}
PREFIX = {"aq": "air_quality", "wb": "waste", "fl": "flood"}
# ponytail: naive baseline until Elise's registered model lands (#30); swap forecast() and this name then.
MODEL_VERSION = "naive-seasonal-24h"
MAX_BODY = 10_000


class HttpError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status


def iso(t):
    return t.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def when(q, name, default=None):
    if name not in q:
        if default is None:
            raise HttpError(400, f"{name} is required")
        return default
    try:
        t = datetime.fromisoformat(q[name])
    except ValueError:
        raise HttpError(400, f"{name} must be an RFC 3339 date-time") from None
    return t if t.tzinfo else t.replace(tzinfo=timezone.utc)


def choice(q, name, options, default):
    v = q.get(name, default)
    if v not in options:
        raise HttpError(400, f"{name} must be one of {', '.join(map(str, options))}")
    return v


def domain_of(device_id):
    d = PREFIX.get(device_id.split("-")[0])
    if d is None:
        raise HttpError(404, f"no device {device_id}")
    return d


def reading(domain, row):
    """DB row -> contracts/sensor-reading.schema.json."""
    metric, unit = DOMAINS[domain]
    r = {"device_id": row["device_id"], "domain": domain, "metric": metric, "value": row["value"],
         "unit": unit, "ts": iso(row["ts"]), "seq": row["seq"], "source": row["source"]}
    if row["battery_pct"] is not None:
        r["battery_pct"] = row["battery_pct"]
    return r


def aggregate(domain, row):
    a = {"domain": domain, "neighbourhood": row["neighbourhood"], "hour": iso(row["hour"]),
         "avg": row["avg"], "min": row["min"], "max": row["max"], "count": row["count"]}
    if "device_id" in row:
        a["device_id"] = row["device_id"]
    return a


def forecast(hourly, horizon_h):
    """{hour: mean pm25} -> [(hour, pm25)] for the next horizon_h hours.
    Each hour repeats the same hour 1 or 2 days earlier; with no such history, the latest hourly mean."""
    last = max(hourly)
    out = []
    for i in range(1, horizon_h + 1):
        t = last + timedelta(hours=i)
        v = hourly.get(t - timedelta(days=1), hourly.get(t - timedelta(days=2), hourly[last]))
        out.append((t, round(v, 1)))
    return out


def check_report(body):
    try:
        r = json.loads(body)
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise HttpError(400, "body must be JSON") from None
    errors = sorted(REPORT.iter_errors(r), key=str)
    if errors:
        raise HttpError(400, errors[0].message)
    return r


# --- handlers: each takes (cur, query) and returns (status, body) -------------------------------------------

def latest(cur, q):
    domains = [choice(q, "domain", list(DOMAINS), None)] if "domain" in q else list(DOMAINS)
    out = []
    for d in domains:
        cur.execute(f"""SELECT DISTINCT ON (device_id) device_id, ts, seq, {DOMAINS[d][0]} AS value, battery_pct, source
                        FROM {d} WHERE %(n)s::text IS NULL OR neighbourhood = %(n)s
                        ORDER BY device_id, ts DESC""", {"n": q.get("neighbourhood")})
        out += [reading(d, r) for r in cur.fetchall()]
    return 200, out


def history(cur, q):
    device = q.get("device_id") or ""
    d = domain_of(device)
    args = {"dev": device, "from": when(q, "from"), "to": when(q, "to")}
    col = DOMAINS[d][0]
    if choice(q, "interval", ["raw", "1h"], "raw") == "raw":
        # ponytail: no paging; a device makes ~1,440 readings a day, so ask for days, not months.
        cur.execute(f"""SELECT device_id, ts, seq, {col} AS value, battery_pct, source FROM {d}
                        WHERE device_id = %(dev)s AND ts >= %(from)s AND ts < %(to)s ORDER BY ts""", args)
        return 200, [reading(d, r) for r in cur.fetchall()]
    # ponytail: rolled up from raw on each call; read the *_hourly tables once #22 adds them.
    cur.execute(f"""SELECT device_id, neighbourhood, time_bucket('1 hour', ts) AS hour, avg({col}) AS avg,
                           min({col}) AS min, max({col}) AS max, count(*) AS count FROM {d}
                    WHERE device_id = %(dev)s AND ts >= %(from)s AND ts < %(to)s
                    GROUP BY device_id, neighbourhood, hour ORDER BY hour""", args)
    return 200, [aggregate(d, r) for r in cur.fetchall()]


def alerts(cur, q):
    cur.execute("""SELECT id::text, kind, domain, neighbourhood, device_id, opened_at, status, reason FROM alerts
                   WHERE status = %s ORDER BY opened_at DESC""", (choice(q, "status", ["open", "closed"], "open"),))
    out = []
    for r in cur.fetchall():
        r["opened_at"] = iso(r["opened_at"])
        out.append({k: v for k, v in r.items() if v is not None})
    return 200, out


def predict(cur, q):
    station = q.get("station") or ""
    if domain_of(station) != "air_quality":
        raise HttpError(400, "station must be an air-quality device (aq-...)")
    horizon = int(choice(q, "horizon_h", ["24", "48"], "24"))
    cur.execute("""SELECT time_bucket('1 hour', ts) AS hour, avg(pm25) AS v FROM air_quality
                   WHERE device_id = %(s)s AND ts > (SELECT max(ts) FROM air_quality WHERE device_id = %(s)s) - interval '49 hours'
                   GROUP BY hour""", {"s": station})
    hourly = {r["hour"]: r["v"] for r in cur.fetchall()}
    if not hourly:
        raise HttpError(404, f"no readings for {station}")
    points = forecast(hourly, horizon)
    cur.executemany("INSERT INTO predictions (station, model_version, target_ts, pm25) VALUES (%s, %s, %s, %s)",
                    [(station, MODEL_VERSION, t, v) for t, v in points])
    return 200, {"station": station, "horizon_h": horizon, "model_version": MODEL_VERSION,
                 "points": [{"ts": iso(t), "pm25": v} for t, v in points]}


def report(cur, body):
    r = check_report(body)
    # ponytail: no sign-in or rate limit yet (auth is undecided in contracts/api); add both before #35 goes public.
    cur.execute("""INSERT INTO citizen_reports (category, description, lat, lon, photo_url)
                   VALUES (%(category)s, %(description)s, %(lat)s, %(lon)s, %(photo_url)s) RETURNING id::text""",
                {"photo_url": None, **r})
    return 201, {"id": cur.fetchone()["id"]}


def open_data(cur, q, domain):
    if domain not in DOMAINS:
        raise HttpError(404, f"no domain {domain}")
    col = DOMAINS[domain][0]
    args = {"from": when(q, "from", datetime.now(timezone.utc) - timedelta(days=7)),
            "to": when(q, "to", datetime.max.replace(tzinfo=timezone.utc))}
    # Per neighbourhood only: no device ids or finer location (#42).
    cur.execute(f"""SELECT neighbourhood, time_bucket('1 hour', ts) AS hour, avg({col}) AS avg, min({col}) AS min,
                           max({col}) AS max, count(*) AS count FROM {domain}
                    WHERE ts >= %(from)s AND ts < %(to)s GROUP BY neighbourhood, hour ORDER BY hour, neighbourhood""", args)
    return 200, [aggregate(domain, r) for r in cur.fetchall()]


GET = {"/readings/latest": latest, "/readings": history, "/alerts": alerts, "/predictions/pm25": predict}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):  # the default puts the caller's IP address first; we don't keep it (docs/privacy.md)
        print(f"[{self.log_date_time_string()}] {fmt % args}", file=sys.stderr)

    def send(self, status, body):
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        # ponytail: any origin may call; narrow to the dashboard's domain when it is deployed (#35).
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def run(self, fn):
        import psycopg
        from psycopg.rows import dict_row

        try:
            # ponytail: one connection per request; add psycopg_pool when the load test (#6) says so.
            with psycopg.connect(os.environ["DATABASE_URL"], connect_timeout=2, row_factory=dict_row) as conn:
                with conn.cursor() as cur:
                    self.send(*fn(cur))
        except HttpError as e:
            self.send(e.status, {"error": str(e)})
        except psycopg.OperationalError as e:
            print(f"db unavailable: {e}", file=sys.stderr)
            self.send(503, {"error": "database unavailable"})

    def do_GET(self):
        url = urlparse(self.path)
        q = {k: v[-1] for k, v in parse_qs(url.query).items()}
        if url.path in GET:
            self.run(lambda cur: GET[url.path](cur, q))
        elif url.path.startswith("/open-data/"):
            self.run(lambda cur: open_data(cur, q, url.path.removeprefix("/open-data/")))
        else:
            self.send(404, {"error": "not found"})

    def do_POST(self):
        if urlparse(self.path).path != "/reports":
            return self.send(404, {"error": "not found"})
        n = int(self.headers.get("Content-Length") or 0)
        if not 0 < n <= MAX_BODY:
            return self.send(400, {"error": f"body must be 1 to {MAX_BODY} bytes"})
        body = self.rfile.read(n)
        self.run(lambda cur: report(cur, body))

    def do_OPTIONS(self):  # CORS preflight for the dashboard's POST
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


def main():
    import psycopg

    with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
        conn.execute((Path(__file__).parent / "schema.sql").read_text())
    port = int(os.environ.get("PORT", 8000))
    print(f"API on http://localhost:{port}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
