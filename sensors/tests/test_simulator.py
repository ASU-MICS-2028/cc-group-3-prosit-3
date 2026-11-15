"""Every simulated reading matches the contract; topics and timing follow contracts/mqtt-topics.md.

Run: pip install -r contracts/requirements.txt && python3 -m unittest discover sensors/tests -v
"""
import json
import random
import re
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "sensors"))
import simulator  # noqa: E402

SCHEMA = json.loads((ROOT / "contracts" / "sensor-reading.schema.json").read_text())
VALIDATOR = jsonschema.Draft202012Validator(SCHEMA, format_checker=jsonschema.FormatChecker())
TOPIC = re.compile(r"^accra/[a-z-]+/(air_quality|waste|flood)/[a-z]+-[a-z0-9-]+-\d{3}$")


def simulate(ticks, seed=1, start=datetime(2026, 11, 16, 6, tzinfo=timezone.utc)):
    out = []
    simulator.run(ticks, 0, start, random.Random(seed), lambda dev, r: out.append((simulator.topic(dev), r)))
    return out


class Simulator(unittest.TestCase):
    def test_a_day_of_readings_matches_the_contract(self):
        out = simulate(ticks=8640)  # 24 h
        self.assertTrue(out)
        for t, r in out:
            VALIDATOR.validate(r)
            m = TOPIC.match(t)
            self.assertTrue(m, t)
            self.assertEqual(m.group(1), r["domain"])
            self.assertTrue(t.endswith("/" + r["device_id"]))

    def test_every_domain_and_device_publishes(self):
        out = simulate(ticks=6)
        self.assertEqual({r["device_id"] for _, r in out}, {d[0] for d in simulator.FLEET})

    def test_device_ts_is_unique_and_seq_counts_up(self):
        out = simulate(ticks=8640)
        keys = [(r["device_id"], r["ts"]) for _, r in out]
        self.assertEqual(len(keys), len(set(keys)))
        for dev in simulator.FLEET:
            seqs = [r["seq"] for _, r in out if r["device_id"] == dev[0]]
            self.assertEqual(seqs, list(range(len(seqs))))

    def test_air_and_waste_publish_once_a_minute(self):
        out = simulate(ticks=360)  # 1 h
        n = sum(1 for _, r in out if r["device_id"] == "aq-makola-001")
        self.assertEqual(n, 60)

    def test_flood_publishes_faster_while_rising(self):
        out = simulate(ticks=8640 * 3)  # 3 days: storms are certain
        n = sum(1 for _, r in out if r["device_id"] == "fl-nima-001")
        self.assertGreater(n, 3 * 1440)  # more than once a minute on average

    def test_same_seed_same_run(self):
        self.assertEqual(simulate(100, seed=7), simulate(100, seed=7))


if __name__ == "__main__":
    unittest.main()
