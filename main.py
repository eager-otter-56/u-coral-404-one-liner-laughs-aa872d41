#!/usr/bin/env python3
"""One-Liner Laughs entry: writes a single funny line to entry.txt."""
import os

ENTRY = "My agent read 1,907 pages of the manual, then filed a bug report against itself for skimming the last one."

def main():
    # Gate: entry must be UTF-8 text of 1 to 200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry is only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
