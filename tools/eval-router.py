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

tuned  = score(ROOT/"tools/eval-cases.tsv")
held   = score(ROOT/"tools/eval-heldout.tsv")
drills = score(ROOT/"tools/eval-drills.tsv")
show("TUNED SET", tuned, "  <- author wrote both triggers and test. Inflated. Not a result.")
show("HELD-OUT SET", held, "  <- honest: written without sight of the triggers")
show("ADVERSARIAL SET", drills, "  <- honest and deliberately hard: confusable pairs only")

# The gate is PRECISION, not accuracy, and that is deliberate. Recall belongs to the roster layer,
# which a script cannot measure. All this layer must promise is that when it speaks up loudly it
# is usually right, because a confident wrong answer is worse than staying quiet.
GATE = 60.0
worst = min(held["precision"], drills["precision"])
ok = worst >= GATE
print(f"\nGATE: high-confidence precision on BOTH honest sets must be >= {GATE}%")
print(f"      held-out {held['precision']:.1f}%   adversarial {drills['precision']:.1f}%   "
      f"worst {worst:.1f}%  ->  {'PASS' if ok else 'FAIL'}")
print("\nNote: top-1 on this layer is low by design and is not gated. The roster injected on every")
print("prompt is what carries recall, and it is measured against a real model in")
print("tools/eval-model-results.md and tools/eval-drills-results.md.")
if "-v" in sys.argv:
    for label, r in (("held-out", held), ("adversarial", drills)):
        print(f"\n{label} misses:")
        for said, want, got in r["misses"]:
            print(f"  want={want:<18} got={got[0] if got else 'NOTHING':<18} {said[:58]}")
sys.exit(0 if ok else 1)
