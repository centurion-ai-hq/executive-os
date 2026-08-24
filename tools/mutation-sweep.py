#!/usr/bin/env python3
"""
Proves every gate in check-structure.py actually discriminates.

A gate that passes while the code it tests is deleted is worse than no gate: it reports safety
that is not there. Three gates in this repo did exactly that before being caught here. So each
mutation below deletes or corrupts one specific behaviour and asserts the suite goes red.

Run it after touching router.py or check-structure.py.
"""
import pathlib, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
TARGET = ROOT/"plugins/exec/hooks/router.py"

MUTATIONS = [
    ("roster budget slashed to 40 chars",
     "def one_liner(desc, limit=112, floor=45):", "def one_liner(desc, limit=40, floor=45):"),
    ("deduplication deleted",
     'if d.name in seen or not (d/"SKILL.md").is_file():', 'if not (d/"SKILL.md").is_file():'),
    ("floor semantics inverted back to stop-when-reached",
     "if len(out) + 1 + len(part) > limit and len(out) >= floor:",
     "if len(out) + 1 + len(part) > limit or len(out) >= floor:"),
    ("skill discovery returns nothing",
     "    out, seen = [], set()", "    return []\n    out, seen = [], set()"),
]

def suite_exit():
    return subprocess.run([sys.executable, str(ROOT/"tools/check-structure.py")],
                          capture_output=True, text=True).returncode

original = TARGET.read_text()
baseline = suite_exit()
print(f"  baseline, nothing broken           exit={baseline}  "
      f"{'OK' if baseline == 0 else 'ALREADY FAILING, fix that first'}")
if baseline != 0:
    sys.exit(1)

failures = []
for name, find, repl in MUTATIONS:
    if find not in original:
        print(f"  {name:<50} SKIP  anchor not found, mutation is stale")
        failures.append(name)
        continue
    try:
        TARGET.write_text(original.replace(find, repl, 1))
        code = suite_exit()
    finally:
        TARGET.write_text(original)
    caught = code != 0
    print(f"  {name:<50} exit={code}  {'CAUGHT' if caught else 'MISSED, gate is decorative'}")
    if not caught:
        failures.append(name)

restored = suite_exit()
print(f"\n  restored                           exit={restored}")
print(f"  mutations: {len(MUTATIONS)}   uncaught: {len(failures)}")
if failures:
    print("  UNCAUGHT: " + ", ".join(failures))
sys.exit(0 if not failures and restored == 0 else 1)
