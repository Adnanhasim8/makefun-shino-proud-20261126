#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (one line, 75 characters) to entry.txt.
Python 3.13 standard library only. No network at run time.
"""

import argparse
import os
from pathlib import Path

ENTRY = "Every morning, Dad still cuts the crusts off my sandwiches. I'm twenty-six."


def main() -> None:
    parser = argparse.ArgumentParser(description="Write the family scene entry.")
    parser.add_argument("--out", default=None, help="Output file path (default: $MAKEFUN_OUTPUT_DIR/entry.txt or /output/entry.txt)")
    args = parser.parse_args()

    if args.out:
        out_path = Path(args.out)
    else:
        base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        out_path = Path(base) / "entry.txt"

    # Gate assertions: 1-2 lines, totalling 1-280 characters, non-empty.
    assert ENTRY.strip(), "entry must not be empty or only whitespace"
    assert 1 <= len(ENTRY) <= 280, f"entry must be 1-280 characters, got {len(ENTRY)}"
    assert 1 <= len(ENTRY.splitlines()) <= 2, "entry must be one or two lines"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ENTRY, encoding="utf-8")

    # Verify what was written matches the gate too.
    written = out_path.read_text(encoding="utf-8")
    assert written == ENTRY
    assert 1 <= len(written) <= 280
    assert 1 <= len(written.splitlines()) <= 2


if __name__ == "__main__":
    main()
