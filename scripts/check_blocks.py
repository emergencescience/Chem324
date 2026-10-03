#!/usr/bin/env python3
"""Check that every inserted MyST directive starts on a line of its own with a
blank line before it, and that every opened directive is closed.

MyST parses a directive only at the start of a block; if an inserted
`:::{...}` is glued to the end of a preceding text line it becomes part of that
paragraph instead of a directive, so it renders as literal colons.
"""
import re
import sys
from pathlib import Path

for path in sys.argv[1:]:
    lines = Path(path).read_text(encoding="utf-8").split("\n")
    glued = []
    for i, ln in enumerate(lines):
        if re.match(r"^:{3,}\{", ln) and i > 0:
            prev = lines[i - 1]
            if prev.strip() != "" and not re.match(r"^:{3,}", prev):
                glued.append((i + 1, prev[:70]))
    # fence balance
    depth = 0
    unbalanced = []
    for i, ln in enumerate(lines):
        m = re.match(r"^(:{3,})\s*$", ln)
        o = re.match(r"^(:{3,})\{", ln)
        if o:
            depth += 1
        elif m:
            depth -= 1
            if depth < 0:
                unbalanced.append(i + 1)
                depth = 0
    print(f"{path}")
    print(f"  inserted directives not preceded by a blank line : {len(glued)}")
    for g in glued[:8]:
        print(f"     line {g[0]}: preceded by {g[1]!r}")
    print(f"  net directive depth at EOF (0 = balanced)        : {depth}")
    print(f"  premature closers                                : {len(unbalanced)}")
