"""Contract tests: examples match the schema, bad ones don't, and the API lists the agreed paths.

Run: pip install -r contracts/requirements.txt && python3 -m unittest discover contracts/tests -v
"""
import json
import unittest
from pathlib import Path

import jsonschema
import yaml

C = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((C / "sensor-reading.schema.json").read_text())
VALIDATOR = jsonschema.Draft202012Validator(SCHEMA, format_checker=jsonschema.FormatChecker())


def load(p):
    return json.loads(p.read_text())


class SensorReading(unittest.TestCase):
    def test_examples_valid(self):
        examples = sorted((C / "examples").glob("*.json"))
        self.assertGreaterEqual(len(examples), 3)  # one per domain at least
        for p in examples:
            with self.subTest(p.name):
                VALIDATOR.validate(load(p))

    def test_bad_example_rejected(self):
        bad = sorted((C / "examples" / "bad").glob("*.json"))
        self.assertTrue(bad)
        for p in bad:
            with self.subTest(p.name):
                with self.assertRaises(jsonschema.ValidationError):
                    VALIDATOR.validate(load(p))

    def test_wrong_unit_for_domain_rejected(self):
        r = load(C / "examples" / "air-quality.json")
        r["unit"] = "cm"
        with self.assertRaises(jsonschema.ValidationError):
            VALIDATOR.validate(r)

    def test_unknown_field_rejected(self):
        r = load(C / "examples" / "flood-level.json")
        r["owner_phone"] = "000"
        with self.assertRaises(jsonschema.ValidationError):
            VALIDATOR.validate(r)


class Api(unittest.TestCase):
    def test_openapi_has_paths(self):
        api = yaml.safe_load((C / "api.openapi.yaml").read_text())
        self.assertEqual(api["openapi"][:3], "3.1")
        for path in ["/readings/latest", "/readings", "/alerts", "/predictions/pm25", "/reports", "/open-data/{domain}"]:
            with self.subTest(path):
                self.assertIn(path, api["paths"])


if __name__ == "__main__":
    unittest.main()
