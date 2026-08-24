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
sys.exit(0 if ok else 1)
