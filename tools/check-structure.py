#!/usr/bin/env python3
"""Structural gate: counts, manifests, frontmatter. Exits non-zero on any violation."""
import pathlib, json, re, sys
R = pathlib.Path(__file__).resolve().parent.parent
ok = True
def say(name, good, extra=""):
    global ok
    print(("  PASS  " if good else "  FAIL  ") + name + ("" if good else "  -> " + extra))
    if not good: ok = False

mk = json.loads((R/".claude-plugin/marketplace.json").read_text())
declared = {p["name"] for p in mk["plugins"]}
ondisk = {p.name for p in (R/"plugins").iterdir() if p.is_dir()}
say("marketplace matches disk", declared == ondisk, str(sorted(declared ^ ondisk)))
for p in sorted(ondisk):
    j = R/"plugins"/p/".claude-plugin"/"plugin.json"
    say(f"{p}: manifest valid", j.exists() and json.loads(j.read_text())["name"] == p)
counts = {p: len(list((R/"plugins"/p/"skills").glob("*/SKILL.md"))) for p in sorted(ondisk)}
say("exec core has 25 skills", counts.get("exec") == 25, str(counts))
say("every lane pack has 5", all(v == 5 for k, v in counts.items() if k != "exec"), str(counts))
# Quoted and unquoted YAML scalars are both valid, so match on the value, not the raw line.
drills = [f for f in R.glob("plugins/*/skills/*/SKILL.md")
          if re.search(r'^description:\s*["\']?Battle drill\.', f.read_text(), re.M)]
say("5 battle drills", len(drills) == 5, str(len(drills)))
bad, notrig, toolong = [], [], []
for f in R.glob("plugins/*/skills/*/SKILL.md"):
    t = f.read_text(); m = re.match(r"^---\s*\n(.*?)\n---\s*\n", t, re.S)
    n = f.parts[-2]
    if not m or "description:" not in m.group(1): bad.append(n)
    elif "when_to_use:" not in m.group(1): notrig.append(n)
    if len(t.splitlines()) > 120: toolong.append(n)
say("all skills: valid frontmatter", not bad, str(bad[:4]))
say("all skills: trigger phrases present", not notrig, str(notrig[:4]))
say("all skills: under 120 lines", not toolong, str(toolong[:4]))

# Every skill must be DISTINGUISHABLE in the injected roster. A line like "Battle drill." tells
# the model nothing, so that skill can never be chosen on meaning. Six shipped that way once.
import importlib.util
sp = importlib.util.spec_from_file_location("router", R/"plugins/exec/hooks/router.py")
rt = importlib.util.module_from_spec(sp); sp.loader.exec_module(rt)
rt.skill_dirs = lambda: [d for d in sorted(R.glob("plugins/*/skills/*")) if (d/"SKILL.md").is_file()]
thin = [r.strip() for r in rt.roster() if len(r.split(": ", 1)[1]) < 45]
say("every skill is distinguishable in the roster", not thin, str([t[:40] for t in thin[:4]]))

# Eight pairs are close enough that a positive description alone will not separate them. Each of
# those sixteen skills must carry an explicit negative clause INSIDE the roster's truncation
# budget. It is not enough for the clause to exist in the file: if it falls past the cut it does
# not exist as far as the model is concerned, which is how it was wrong the first two times.
PAIRS = [("document", "sop"), ("brain-dump", "roadmap"), ("decide", "priorities"),
         ("critic", "attack"), ("prep", "stakeholder-brief"), ("process-audit", "incident"),
         ("decode", "teach-me"), ("remember", "handoff")]
lines = {r.strip().split(":")[0]: r.strip() for r in rt.roster()}
weak = [n for a, b in PAIRS for n in (a, b)
        if n in lines and " Not " not in lines[n] and "wrong skill" not in lines[n]]
say("confusable pairs carry a visible negative clause", not weak, str(weak))

# A roster that lists one name twice with two different descriptions is worse than omitting it:
# the model is asked to choose between two things it has no way to tell apart.
#
# This has to exercise the real discovery function against a real collision. An earlier version
# checked the kit's own folders for duplicate names, which cannot collide by construction, so it
# passed whether the dedup existed or not. It was caught by deleting the dedup and watching the
# check still pass.
import collections, tempfile, os
with tempfile.TemporaryDirectory() as tmp:
    t = pathlib.Path(tmp)
    for pack in ("packA", "packB"):                      # same skill name in two packs
        d = t/pack/"skills"/"collide"
        d.mkdir(parents=True)
        (d/"SKILL.md").write_text(f"---\ndescription: from {pack}\n---\nbody\n")
    # A FRESH module: rt.skill_dirs was replaced above with a kit-only stub, so calling it here
    # would test the stub rather than the code that ships. This is the exact trap that made the
    # first version of this check pass while the dedup was deleted.
    sp2 = importlib.util.spec_from_file_location("router_probe", R/"plugins/exec/hooks/router.py")
    probe = importlib.util.module_from_spec(sp2); sp2.loader.exec_module(probe)
    real_home = pathlib.Path.home
    os.environ["CLAUDE_PLUGIN_ROOT"] = str(t/"packA")
    pathlib.Path.home = staticmethod(lambda: t/"nonexistent-home")   # isolate from this machine
    try:
        found = [d.name for d in probe.skill_dirs()]
    finally:
        pathlib.Path.home = real_home
        os.environ.pop("CLAUDE_PLUGIN_ROOT", None)
    dupes = {k: v for k, v in collections.Counter(found).items() if v > 1}
    say("discovery deduplicates colliding skill names", not dupes and found.count("collide") == 1,
        f"saw {found}")
sys.exit(0 if ok else 1)
