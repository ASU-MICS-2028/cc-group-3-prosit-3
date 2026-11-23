"""Bridge logic without a broker or DB: the trust-boundary checks and the spool that buffers through outages.

Run: pip install -r contracts/requirements.txt && python3 -m unittest discover ingest/tests -v
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "ingest"))
import bridge  # noqa: E402

GOOD = json.loads((ROOT / "contracts" / "examples" / "air-quality.json").read_text())
TOPIC = "accra/jamestown/air_quality/aq-jamestown-001"


def row(i):
    return {**GOOD, "seq": i, "ts": f"2026-11-16T09:{i:02d}:00Z", "neighbourhood": "jamestown"}


class Parse(unittest.TestCase):
    def test_good_reading_gets_neighbourhood_from_topic(self):
        r = bridge.parse(TOPIC, json.dumps(GOOD).encode())
        self.assertEqual(r["neighbourhood"], "jamestown")
        self.assertEqual(r["value"], GOOD["value"])

    def test_rejects(self):
        cases = {
            "not json": (TOPIC, b"{oops"),
            "schema": (TOPIC, json.dumps({**GOOD, "value": -5}).encode()),
            "unknown field": (TOPIC, json.dumps({**GOOD, "phone": "000"}).encode()),
            "device spoofs another topic": ("accra/jamestown/air_quality/aq-jamestown-002", json.dumps(GOOD).encode()),
            "domain mismatch": ("accra/jamestown/flood/aq-jamestown-001", json.dumps(GOOD).encode()),
            "wrong neighbourhood": ("accra/makola/air_quality/aq-jamestown-001", json.dumps(GOOD).encode()),
            "bad topic": ("city/jamestown/air_quality/aq-jamestown-001", json.dumps(GOOD).encode()),
        }
        for name, (topic, payload) in cases.items():
            with self.subTest(name), self.assertRaises(ValueError):
                bridge.parse(topic, payload)


class SpoolAndFlush(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.spool = bridge.Spool(Path(self.tmp.name) / "spool.jsonl")
        self.db = []

    def tearDown(self):
        self.tmp.cleanup()

    def write_ok(self, rows):
        self.db.extend(rows)

    def write_down(self, rows):
        raise ConnectionError("db down")

    def test_rows_reach_the_db_and_leave_the_spool(self):
        for i in range(3):
            self.spool.append(row(i))
        self.assertEqual(bridge.flush(self.spool, self.write_ok, 500), 3)
        self.assertEqual([r["seq"] for r in self.db], [0, 1, 2])
        self.assertEqual(self.spool.read(), [])

    def test_outage_keeps_everything_then_flushes_in_order(self):
        for i in range(5):
            self.spool.append(row(i))
        for _ in range(3):  # DB down for three flush attempts
            with self.assertRaises(ConnectionError):
                bridge.flush(self.spool, self.write_down, 500)
        self.assertEqual(len(self.spool.read()), 5)
        self.spool.append(row(5))  # readings keep arriving during the outage
        while bridge.flush(self.spool, self.write_ok, 2):
            pass
        self.assertEqual([r["seq"] for r in self.db], list(range(6)))
        self.assertEqual(self.spool.read(), [])

    def test_batches_are_capped(self):
        for i in range(5):
            self.spool.append(row(i))
        self.assertEqual(bridge.flush(self.spool, self.write_ok, 2), 2)
        self.assertEqual(len(self.spool.read()), 3)

    def test_spool_survives_a_restart(self):
        self.spool.append(row(0))
        again = bridge.Spool(self.spool.path)
        self.assertEqual(again.read(), [row(0)])


if __name__ == "__main__":
    unittest.main()
