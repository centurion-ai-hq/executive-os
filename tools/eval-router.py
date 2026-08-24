#!/usr/bin/env python3
"""
Scores the router's PHRASE layer against two sets.

  tuned    tools/eval-cases.tsv    written by the same author as the triggers. Inflated by
                                   construction. Reported for contrast only, never as the result.
  heldout  tools/eval-heldout.tsv  written by an agent that never saw the triggers, the router,
                                   or any skill frontmatter. This is the honest number and the gate.

The phrase layer is deliberately high-precision and low-recall: the roster the hook injects on
every prompt is what carries recall, and that layer is measured separately by a real model in
tools/eval-model-results.md, because no script can measure it.
"""
import pathlib, sys, importlib.util

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("router", ROOT/"plugins/exec/hooks/router.py")
R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
# Only the skills this kit ships. The author's own personal library would otherwise compete
# while being absent on the executive's machine, measuring the wrong system entirely.
R.skill_dirs = lambda: [d for d in sorted((ROOT/"plugins").glob("*/skills/*")) if (d/"SKILL.md").is_file()]

STRONG = 9.0

def score(path):
    rows = [l.split("\t") for l in pathlib.Path(path).read_text().splitlines() if "\t" in l]
    rows = [(a.strip(), b.strip()) for a, b in rows if not a.startswith("«")]
    t1 = t3 = silent = 0
    strong_fired = strong_right = 0
    misses = []
    for said, want in rows:
        hits = R.route(said)
        names = [h[1] for h in hits]
        if not names:
            silent += 1
        else:
            if hits[0][0] >= STRONG:
                strong_fired += 1
                if names[0] == want: strong_right += 1
            if names[0] == want: t1 += 1; t3 += 1
            elif want in names: t3 += 1; misses.append((said, want, names))
            else: misses.append((said, want, names))
    n = len(rows)
    prec = (100*strong_right/strong_fired) if strong_fired else 0.0
    return dict(n=n, t1=t1, t3=t3, silent=silent, misses=misses,
                strong_fired=strong_fired, strong_right=strong_right, precision=prec)

def show(label, r, note):
    print(f"\n--- {label} ({r['n']} cases) {note}")
    print(f"    top-1            {r['t1']}/{r['n']} = {100*r['t1']/r['n']:.1f}%")
    print(f"    top-3            {r['t3']}/{r['n']} = {100*r['t3']/r['n']:.1f}%")
    print(f"    no match at all  {r['silent']}")
    print(f"    high-confidence  fired {r['strong_fired']}x, correct {r['strong_right']}x "
          f"= {r['precision']:.1f}% precision")

tuned = score(ROOT/"tools/eval-cases.tsv")
held  = score(ROOT/"tools/eval-heldout.tsv")
show("TUNED SET", tuned, "  <- author wrote both triggers and test. Inflated. Not the result.")
show("HELD-OUT SET", held, "  <- THE HONEST NUMBER")

GATE = 60.0   # precision floor: when the phrase layer speaks up loudly, it must usually be right
print(f"\nGATE: high-confidence precision on held-out must be >= {GATE}%  ->  "
      f"{held['precision']:.1f}%  {'PASS' if held['precision'] >= GATE else 'FAIL'}")
if "-v" in sys.argv:
    print("\nheld-out misses:")
    for said, want, got in held["misses"]:
        print(f"  want={want:<18} got={got[0] if got else 'NOTHING':<18} {said[:58]}")
sys.exit(0 if held["precision"] >= GATE else 1)
