#!/usr/bin/env python3
"""Final acceptance run for the whole converted chapter.

Re-runs the English-untouched gate and the block-structure checker for every
page against its pre-translation backup, so the claim "chapter verified" rests
on evidence produced now, not on logs from the individual applies.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/root/repos/Chem324")
BACKUPS = {
    "01-schrodinger-equation": "/tmp/01-schrodinger-equation.EN.md",
    "02-particle-in-a-box": "/tmp/02-particle-in-a-box.EN.md",
    "03-tunneling-and-finite-square-well": "/tmp/03-tunneling-and-finite-square-well.EN.md",
    "04-operators": "/tmp/04-operators.EN.md",
    "05-eigenvalues-and-expectation": "/tmp/ch03_05_EN_backup.md",
    "06-time-dependence": "/tmp/06-time-dependence.EN.md",
}
SEL = [sys.executable, str(ROOT / "scripts" / "myst_slice.py")]

fails = []
print(f"{'page':<38} {'gate':<50} {'blocks'}")
print("-" * 100)
for stem, backup in BACKUPS.items():
    page = f"ch03/{stem}.md"
    r = subprocess.run(SEL + ["verify", backup, page, "--strip-interleaved"],
                       cwd=ROOT, capture_output=True, text=True)
    gate = (r.stdout + r.stderr).strip().splitlines()[0] if (r.stdout or r.stderr) else "?"
    r2 = subprocess.run([sys.executable, str(ROOT / "scripts" / "check_blocks.py"), page],
                        cwd=ROOT, capture_output=True, text=True)
    glued = re.search(r"not preceded by a blank line\s*:\s*(\d+)", r2.stdout)
    depth = re.search(r"depth at EOF \(0 = balanced\)\s*:\s*(-?\d+)", r2.stdout)
    blk = f"glued={glued.group(1) if glued else '?'} depth={depth.group(1) if depth else '?'}"
    ok = r.returncode == 0 and glued and glued.group(1) == "0" and depth and depth.group(1) == "0"
    if not ok:
        fails.append(stem)
    print(f"{stem:<38} {gate[:48]:<50} {blk}  {'OK' if ok else 'FAIL'}")

r = subprocess.run([sys.executable, str(ROOT / "scripts" / "test_roundtrip.py")],
                   cwd=ROOT, capture_output=True, text=True)
print("\n" + (r.stdout + r.stderr).strip().splitlines()[0])

print(f"\n{len(BACKUPS) - len(fails)}/{len(BACKUPS)} pages verified"
      + (f"  FAILED: {fails}" if fails else ""))
sys.exit(1 if fails else 0)
