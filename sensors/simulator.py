"""Three-domain sensor simulator: air quality (PM2.5), waste bin fill, flood/drain level.

Publishes readings shaped like contracts/sensor-reading.schema.json to
accra/<neighbourhood>/<domain>/<device_id> at QoS 1. Each device has its own MQTT
connection with client_id and username = device_id (contracts/mqtt-topics.md).

Run:   python3 sensors/simulator.py --host localhost
Try:   python3 sensors/simulator.py --dry-run --ticks 12 --speed 600   # no broker, prints JSON
Every tick is 10 simulated seconds. Air and waste publish every 60 s; flood every 60 s,
or every tick while the water is rising. --speed 60 runs an hour of the city per minute.
"""
import argparse
import json
import math
import os
import random
import sys
import time
from datetime import datetime, timedelta, timezone

TICK_S = 10
EVERY_S = 60

# Calibration knobs: real sensors read off, so each device keeps its own offset.
FLEET = [
    # (device_id, neighbourhood, domain, knobs)
    ("aq-jamestown-001", "jamestown", "air_quality", {"offset": 6.0}),   # coastal, fish smoking
    ("aq-makola-001", "makola", "air_quality", {"offset": 10.0}),        # market traffic
    ("aq-nima-001", "nima", "air_quality", {"offset": 4.0}),
    ("aq-east-legon-001", "east-legon", "air_quality", {"offset": -4.0}),
    ("aq-asylum-down-001", "asylum-down", "air_quality", {"offset": 0.0}),
    ("wb-makola-001", "makola", "waste", {"rate_pct_h": 6.0}),           # fills in ~16 h
    ("wb-makola-002", "makola", "waste", {"rate_pct_h": 4.0}),
    ("wb-jamestown-001", "jamestown", "waste", {"rate_pct_h": 2.5}),
    ("wb-nima-001", "nima", "waste", {"rate_pct_h": 3.0}),
    ("fl-nima-001", "nima", "flood", {"base_cm": 18.0}),                 # drain gauges
    ("fl-asylum-down-001", "asylum-down", "flood", {"base_cm": 25.0}),
]
METRIC = {"air_quality": ("pm25", "ug/m3"), "waste": ("fill_pct", "%"), "flood": ("water_level_cm", "cm")}


def topic(dev):
    return f"accra/{dev['neighbourhood']}/{dev['domain']}/{dev['device_id']}"


def new_device(device_id, neighbourhood, domain, knobs, rng):
    return {"device_id": device_id, "neighbourhood": neighbourhood, "domain": domain, **knobs,
            "seq": 0, "battery": rng.uniform(70, 100), "last_pub": None,
            "level": knobs.get("base_cm", 0.0), "rain_ticks": 0, "rising": False,
            "fill": rng.uniform(0, 60)}


def pm25(dev, t, rng):
    """Diurnal PM2.5 in ug/m3: morning and evening traffic peaks, higher in harmattan (Nov-Feb)."""
    h = t.hour + t.minute / 60
    peaks = 18 * math.exp(-((h - 7.5) ** 2) / 4) + 22 * math.exp(-((h - 19) ** 2) / 5)
    harmattan = 1.8 if t.month in (11, 12, 1, 2) else 1.0
    return max(0.0, (25 + peaks) * harmattan + dev["offset"] + rng.gauss(0, 5))


def advance(dev, t, rng):
    """Move one device on by one tick of simulated time."""
    if dev["domain"] == "waste":
        dev["fill"] += dev["rate_pct_h"] * TICK_S / 3600 * rng.uniform(0.5, 1.5)
        # A truck empties a nearly full bin at some point; overflowing bins sit at 100.
        if dev["fill"] >= 90 and rng.random() < 0.002:
            dev["fill"] = rng.uniform(0, 3)
        dev["fill"] = min(dev["fill"], 100.0)
    elif dev["domain"] == "flood":
        if dev["rain_ticks"] == 0 and rng.random() < 0.0004:   # a storm roughly every 7 h of sim time
            dev["rain_ticks"] = rng.randint(60, 360)           # lasting 10-60 min
        dev["rising"] = dev["rain_ticks"] > 0
        if dev["rain_ticks"]:
            dev["rain_ticks"] -= 1
            dev["level"] += rng.uniform(0.05, 0.4)             # up to ~80 cm over an hour-long storm
        else:  # drain empties back towards its base level
            dev["level"] = dev["base_cm"] + (dev["level"] - dev["base_cm"]) * 0.995
        dev["level"] = min(max(dev["level"] + rng.gauss(0, 0.1), 0.0), 1000.0)
    dev["battery"] = max(0.0, dev["battery"] - 0.0002)


def due(dev, t):
    if dev["last_pub"] is None or (t - dev["last_pub"]).total_seconds() >= EVERY_S:
        return True
    return dev["domain"] == "flood" and dev["rising"]


def reading(dev, t, rng):
    metric, unit = METRIC[dev["domain"]]
    value = {"air_quality": lambda: pm25(dev, t, rng),
             "waste": lambda: dev["fill"],
             "flood": lambda: dev["level"]}[dev["domain"]]()
    r = {"device_id": dev["device_id"], "domain": dev["domain"], "metric": metric,
         "value": round(min(value, 1000.0), 1), "unit": unit,
         "ts": t.strftime("%Y-%m-%dT%H:%M:%SZ"), "seq": dev["seq"],
         "battery_pct": round(dev["battery"], 1), "source": "simulator"}
    dev["seq"] += 1
    dev["last_pub"] = t
    return r


def run(ticks, speed, start, rng, publish):
    """Drive the fleet. publish(dev, reading) is called for every reading that is due."""
    fleet = [new_device(*d, rng) for d in FLEET]
    t = start
    n = 0
    while ticks is None or n < ticks:
        for dev in fleet:
            advance(dev, t, rng)
            if due(dev, t):
                publish(dev, reading(dev, t, rng))
        n += 1
        t += timedelta(seconds=TICK_S)
        if speed:
            time.sleep(TICK_S / speed)


def mqtt_publisher(host, port):
    import paho.mqtt.client as mqtt  # only needed when talking to a broker

    clients = {}

    def publish(dev, r):
        c = clients.get(dev["device_id"])
        if c is None:
            c = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=dev["device_id"])
            # Per-device credentials come in #21; until then the dev broker allows anonymous.
            c.username_pw_set(dev["device_id"], os.environ.get("SIM_PASSWORD") or None)
            c.connect_async(host, port)  # paho keeps retrying in the background if the broker is down
            c.loop_start()
            for _ in range(50):  # give the first connection up to 5 s before publishing
                if c.is_connected():
                    break
                time.sleep(0.1)
            clients[dev["device_id"]] = c
        try:
            c.publish(topic(dev), json.dumps(r), qos=1).wait_for_publish(5)  # wait for the broker's PUBACK
        except (RuntimeError, ValueError) as e:
            # ponytail: a reading made while the broker is down is dropped, not buffered on the
            # "device"; seq still counts up, so the gap shows downstream. Buffering lives in the bridge (#20).
            print(f"dropped {dev['device_id']} seq {r['seq']}: {e}", file=sys.stderr, flush=True)
            return
        print(topic(dev), json.dumps(r), flush=True)

    return publish, clients


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--host", default="localhost")
    ap.add_argument("--port", type=int, default=1883)
    ap.add_argument("--ticks", type=int, help="stop after this many 10 s ticks (default: run forever)")
    ap.add_argument("--speed", type=float, default=1.0, help="simulated seconds per real second; 0 = no sleeping")
    ap.add_argument("--seed", type=int, help="fix the random numbers for a repeatable run")
    ap.add_argument("--dry-run", action="store_true", help="print readings instead of publishing")
    a = ap.parse_args()
    rng = random.Random(a.seed)
    start = datetime.now(timezone.utc).replace(microsecond=0)
    if a.dry_run:
        run(a.ticks, a.speed, start, rng, lambda dev, r: print(topic(dev), json.dumps(r), flush=True))
        return 0
    publish, clients = mqtt_publisher(a.host, a.port)
    try:
        run(a.ticks, a.speed, start, rng, publish)
    except KeyboardInterrupt:
        pass
    finally:
        for c in clients.values():
            c.disconnect()
            c.loop_stop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
