#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke, one line.

Revised after scoring 7 candidates in candidates.md: the reply-all
loop won (25/25) — the apology IS the second offence, and the twist
lands on the last words. Writes exactly one line to /output/entry.txt
with no trailing newline.
"""

import os

# Chosen line: the reply-all apology that commits the same sin twice.
JOKE = "I replied-all to apologize for replying-all, which is how I became the reply-all guy twice in one email."


def main() -> None:
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, f"line length {len(line)} out of gate"
    assert line == line.strip() and "\n" not in line
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
