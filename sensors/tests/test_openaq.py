import json
import sys
import unittest
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "sensors"))
from openaq import readings  # noqa: E402

SCHEMA = json.loads((ROOT / "contracts" / "sensor-reading.schema.json").read_text())


def row(ts, value, parameter="pm25"):
    return {"datetime": ts, "parameter": parameter, "value": str(value)}


class OpenAQTest(unittest.TestCase):
    rows = [row("2026-11-19T00:21:36+00:00", 29.46), row("2026-11-18T00:10:00+00:00", 40),   # 24 h 11 min before: out
            row("2026-11-18T12:00:00+00:00", 18.04), row("2026-11-18T12:00:00+00:00", 18.04),  # repeat: once
            row("2026-11-18T13:00:00+00:00", 5, "pm10"), row("2026-11-18T14:00:00+00:00", -3)]   # not pm25 / bad

    def test_last_24h_sorted_deduped_and_valid(self):
        out = readings(self.rows)
        self.assertEqual([(r["ts"], r["value"], r["seq"]) for r in out],
                         [("2026-11-18T12:00:00Z", 18.0, 0), ("2026-11-19T00:21:36Z", 29.5, 1)])
        for r in out:
            jsonschema.validate(r, SCHEMA, format_checker=jsonschema.FormatChecker())
            self.assertEqual(r["source"], "openaq")

    def test_nothing_in(self):
        self.assertEqual(readings([]), [])


if __name__ == "__main__":
    unittest.main()
