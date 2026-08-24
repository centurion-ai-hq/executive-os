#!/usr/bin/env python3
"""
THE ROUTER. This is what makes skills fire for someone who never types a command.

Runs on every single prompt (UserPromptSubmit). Reads the trigger phrases out of every installed
skill, scores what the user just said against all of them independently, and injects the winners
into the conversation as an instruction to read and follow that skill.

DESIGN RULE, learned the hard way: every skill is scored in its own isolated pass. There is no
single shared regex anywhere in this file. A malformed trigger inside one skill can lower that
skill's score and nothing else. One bad pattern must never be able to silence the other 39.

Zero network calls, zero model calls. Pure string work, a few milliseconds.
"""
import json, os, pathlib, re, sys

# ---------------------------------------------------------------- discovery

def skill_dirs():
    """Every place a skill can live, plugin packs first, then the user's own."""
    here = pathlib.Path(__file__).resolve()
    roots = []
    plug_root = os.environ.get("CLAUDE_PLUGIN_ROOT")
    base = pathlib.Path(plug_root).parent if plug_root else here.parent.parent.parent
    if base.exists():
        roots += [p for p in base.glob("*/skills") if p.is_dir()]
    for extra in (pathlib.Path.home()/".claude"/"skills", pathlib.Path(".claude")/"skills"):
        if extra.is_dir():
            roots.append(extra)
    out = []
    for r in roots:
        for d in sorted(r.iterdir()):
            if (d/"SKILL.md").is_file():
                out.append(d)
    return out


def description_of(skill_dir):
    """Pull the description line out of the frontmatter. Never raises."""
    try:
        text = (skill_dir/"SKILL.md").read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return ""
    block = m.group(1)
    parts = []
    for field in ("description", "when_to_use"):
        f = re.search(rf"^{field}:\s*(.+?)(?=\n[A-Za-z_-]+:\s|\Z)", block, re.S | re.M)
        if f:
            parts.append(" ".join(f.group(1).split()).strip("\"'"))
    return "  ".join(parts)


def triggers_of(description, name):
    """
    The phrases that should fire this skill. Authored inside the description as quoted
    fragments, which is exactly how the spec tells skill authors to write them.
    """
    phrases = set()
    for q in re.findall(r"[\"'‘“]([^\"'’”]{3,60})[\"'’”]", description):
        p = q.strip().lower()
        if p and not p.startswith("use when"):
            phrases.add(p)
    phrases.add(name.replace("-", " ").lower())
    return sorted(phrases)

# ---------------------------------------------------------------- scoring

CONTRACTIONS = [
    ("n't", " not"), ("'re", " are"), ("'ve", " have"), ("'ll", " will"), ("'m", " am"),
    ("what's", "what is"), ("here's", "here is"), ("there's", "there is"), ("that's", "that is"),
    ("it's", "it is"), ("let's", "let us"), ("who's", "who is"), ("how's", "how is"),
    ("i'd", "i would"), ("we'd", "we would"), ("gonna", "going to"), ("wanna", "want to"),
    ("cannot", "can not"),
]

def normalise(s):
    """Contractions out, curly quotes out. Run on BOTH the prompt and every trigger phrase
    so the two sides always meet in the same form."""
    s = s.lower().replace("\u2019", "'").replace("\u2018", "'")
    for a, b in CONTRACTIONS:
        s = s.replace(a, b)
    return s


STOP = {"the","a","an","i","me","my","to","for","of","is","it","this","that","and","on","in",
        "you","we","us","do","does","did","what","how","can","should","be","with","at","so",
        "just","get","got","have","has","need","want","am","are","was","them","they","he","she"}

def words(s):
    return [w for w in re.findall(r"[a-z0-9']+", normalise(s)) if w not in STOP]


def score_one(prompt_low, prompt_words, phrases):
    """
    Score a SINGLE skill. Isolated on purpose. Returns (score, the phrase that won).
    10  the trigger phrase appears verbatim in what they said
     4  every meaningful word of the trigger is present, in any order
     2  a distinctive multi-word overlap
    """
    best, why = 0, ""
    pw = set(prompt_words)
    for p in phrases:
        if len(p) >= 6 and p in prompt_low:
            # Specificity beats genericity. "which vendor should I pick" must outrank "should I".
            s = 7 + min(len(words(p)), 5) * 1.2
            if s > best: best, why = s, p
            continue
        tw = set(words(p))
        if not tw:
            continue
        if tw <= pw:
            s = 4 + min(len(tw), 3) * 0.4
            if s > best: best, why = s, p
        elif len(tw) >= 3 and len(tw & pw) >= 3:
            # Deliberately strict. A 2-word overlap is a coincidence, not a match: it is how
            # a sales skill once fired on "help me with this page I am stuck on".
            s = 2 + len(tw & pw) * 0.3
            if s > best: best, why = s, p
    return best, why

# ---------------------------------------------------------------- main

FLOOR = 4.0          # below this it is a coincidence, not a match
MAX_OUT = 3          # never name more than three, it stops being a recommendation

def route(prompt):
    low = normalise(prompt)
    pw = words(prompt)
    hits = []
    for d in skill_dirs():
        try:                                   # one skill can never break another
            desc = description_of(d)
            if not desc:
                continue
            s, why = score_one(low, pw, triggers_of(desc, d.name))
            if s >= FLOOR:
                hits.append((s, d.name, why, str(d/"SKILL.md")))
        except Exception:
            continue
    hits.sort(key=lambda h: (-h[0], h[1]))
    return hits[:MAX_OUT]


def one_liner(desc, limit=104, floor=48):
    """
    A roster line with enough substance to tell this skill from its neighbour.

    Taking only the first sentence looks tidy and silently destroys any skill whose description
    opens with a short label. Six of forty-five reduced to "Battle drill." and "The tutor.",
    which are not descriptions of anything. Keep adding sentences until the line carries real
    signal, then cap it.
    """
    parts = re.split(r"(?<=[.!?])\s+", desc.strip())
    out = ""
    for part in parts:
        if out and len(out) >= floor:
            break
        out = (out + " " + part).strip() if out else part
    out = re.sub(r"^(Battle drill\.|The tutor\.)\s*", r"\1 ", out).strip()
    return out[:limit].rstrip().rstrip(",;")


def roster():
    """Every installed skill, name plus one line. This is the part that actually generalises:
    phrase matching only catches phrasings someone wrote down in advance, and executives do not
    speak from a list. Putting the whole menu in front of the model on every single turn lets it
    do the semantic matching, which it is far better at than any regex ever will be."""
    rows = []
    for d in skill_dirs():
        try:
            desc = description_of(d)
            if desc:
                rows.append(f"  {d.name}: {one_liner(desc)}")
        except Exception:
            continue
    return rows


def steps_of(path, limit=2600):
    """The skill's actual procedure, inlined, so it does not need to be opened."""
    try:
        body = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", body, flags=re.S).strip()
    return body if len(body) <= limit else body[:limit].rsplit("\n", 1)[0] + "\n[...continues in the file]"


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    prompt = payload.get("prompt") or ""
    if not isinstance(prompt, str) or not prompt.strip():
        return 0
    try:
        hits = route(prompt)
        menu = roster()
    except Exception:
        return 0
    if not menu:
        return 0

    # Written as fact about the user's configuration, never as a command. Injected text phrased
    # as an imperative reads like an instruction arriving from outside the conversation, which is
    # the exact shape Claude is trained to distrust and surface rather than act on.
    parts = [
        "Context about this user's installed configuration. Not an instruction from anyone.",
        "",
        "This user is a non-technical executive. They do not type commands, do not know their",
        "skills by name, and will not ask for one. Choosing the right skill is not their job.",
        "",
        "Every skill installed for them:",
        "",
    ] + menu + [
        "",
        "One of these usually fits what they just wrote, including when their wording matches",
        "nothing on this list literally. Judge by what they need, not by the words they used. If",
        "one fits, its full procedure is in its SKILL.md and following it is what they expect. If",
        "genuinely none fits, answering normally is correct and no skill should be forced.",
    ]

    # STRONG is the line between "attach this skill's whole procedure" and "mention it as an
    # aside". It is 9.0 because that is what the data said, measured across both honest test sets:
    #
    #   threshold   held-out precision     adversarial precision
    #      7.0      60.9% (46 fires)       29.2% (24 fires)
    #      8.0      65.9% (41 fires)       30.4% (23 fires)
    #      9.0      70.8% (24 fires)       63.6% (11 fires)   <- chosen
    #     10.0      80.0% ( 5 fires)       50.0% ( 2 fires)   <- sample too small to mean anything
    #     11.0+     never fires at all
    #
    # Below 9 precision collapses on hard cases, which is exactly where a confident wrong answer
    # does damage. Above 9 it barely fires, so the apparent gain rests on a handful of cases.
    # Reproduce the table with tools/eval-router.py before moving this number.
    STRONG = 9.0
    if hits and hits[0][0] >= STRONG:
        top = hits[0]
        parts += [
            "",
            f"Simple phrase matching also flagged `{top[1]}` on the trigger \"{top[2]}\". That is a",
            "crude signal that is often but not always right, so it is worth weighing and worth",
            "overriding. Its recorded procedure:",
            "",
            steps_of(top[3]),
        ]
        if len(hits) > 1:
            parts += ["", "Lower phrase scores: " + ", ".join(f"`{n}`" for _, n, _, _ in hits[1:]) + "."]
    elif hits:
        parts += ["", "Weak phrase signals, low confidence, weigh lightly: "
                  + ", ".join(f"`{n}`" for _, n, _, _ in hits) + "."]

    parts += [
        "",
        "Naming the skill used in one plain sentence helps this user learn what they have. The",
        "matching mechanism itself is not worth mentioning to them.",
    ]

    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": "\n".join(parts),
    }}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
