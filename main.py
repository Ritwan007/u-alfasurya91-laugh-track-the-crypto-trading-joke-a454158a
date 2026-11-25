#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes a single one-line crypto/trading joke to /output/entry.txt.

The gate requires UTF-8 text of 1-200 characters, not only whitespace,
so the program validates the line before writing and fails loudly if
it ever stops meeting the gate.
"""

JOKE = "Bought at the top, sold at the bottom, and somehow still convinced myself I'm early."

def main():
    import os
    import sys

    line = JOKE.strip()
    if not line or len(line) > 200 or "\n" in line:
        sys.exit("entry invalid: must be one non-empty line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
