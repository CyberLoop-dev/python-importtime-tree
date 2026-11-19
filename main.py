import argparse
import json
import re
from pathlib import Path

LINE = re.compile(r"^\s*import time:\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(.*)$")

def parse_importtime(text):
    rows = []
    for line in text.splitlines():
        match = LINE.match(line)
        if not match:
            continue
        raw_name = match.group(3).strip()
        depth = len(raw_name) - len(raw_name.lstrip("."))
        name = raw_name[depth:].strip()
        if name:
            rows.append({"name": name, "depth": depth, "self_us": int(match.group(1)), "cumulative_us": int(match.group(2))})
    return rows

def render_tree(rows):
    return "\n".join(
        f"{'  ' * row['depth']}{row['name']}  self={row['self_us']}µs  cumulative={row['cumulative_us']}µs"
        for row in rows
    )

def main():
    parser = argparse.ArgumentParser(description="Summarize CPython -X importtime output.")
    parser.add_argument("log", type=Path)
    parser.add_argument("--json", action="store_true", help="Print parsed rows as JSON.")
    args = parser.parse_args()
    rows = parse_importtime(args.log.read_text(encoding="utf-8", errors="replace"))
    if not rows:
        parser.error("No CPython importtime rows were found.")
    print(json.dumps(rows, indent=2) if args.json else render_tree(rows))

if __name__ == "__main__":
    main()
