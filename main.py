#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for the
invented city of Puddlewick to entry.txt inside the output directory.

Usage:
    python3 main.py                 # writes to /output/entry.txt
    OUTPUT_DIR=/tmp/out python3 main.py
"""

import os
import sys

MAX_CHARS = 140

FORECAST = (
    "Puddlewick: light drizzle until noon, puddles parting politely "
    "for every bus, with a 90% chance your umbrella finally earns its keep."
)


def main() -> int:
    line = FORECAST.strip()

    if not line:
        print("error: forecast is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: forecast must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: forecast is {len(line)} characters, over the "
            f"{MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    if "Puddlewick" not in line:
        print("error: forecast must name the invented city", file=sys.stderr)
        return 1

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")

    # Read the file back and confirm it holds exactly the forecast line.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line + "\n":
        print("error: written file does not match the forecast", file=sys.stderr)
        return 1

    print(f"wrote {len(line)}-character forecast to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
