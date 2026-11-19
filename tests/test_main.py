import unittest
from main import parse_importtime, render_tree

class ImportTimeTests(unittest.TestCase):
    def test_parses_nested_rows(self):
        rows = parse_importtime("import time: 100 | 200 | json\nimport time: 20 | 30 | .json.decoder")
        self.assertEqual([row["depth"] for row in rows], [0, 1])
        self.assertEqual(rows[1]["name"], "json.decoder")
    def test_ignores_unrelated_lines(self):
        self.assertEqual(parse_importtime("noise\n"), [])
    def test_renders_timing(self):
        self.assertIn("self=12µs", render_tree([{"name":"demo","depth":0,"self_us":12,"cumulative_us":18}]))

if __name__ == "__main__":
    unittest.main()
