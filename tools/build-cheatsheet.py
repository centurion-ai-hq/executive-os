#!/usr/bin/env python3
"""Regenerates CHEAT-SHEET.html from the skills actually on disk. Run after adding a skill."""
import pathlib, re, html, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent

# The short spoken trigger and the plain outcome. Authored, because a 500 char
# description is not a cheat sheet line.
SAY = {
 "brain-dump":("Here is everything on my mind","Your dump split, numbered, sorted, nothing dropped"),
 "priorities":("What should I do first","Your board re-ranked, with what is getting dropped named"),
 "decide":("Should I do this","One committed call, with the reason and an expiry date"),
 "critic":("Poke holes in this","The strongest case that your plan fails, then a verdict"),
 "panel":("Run the panel on this","Five operator viewpoints argue it out, then one verdict"),
 "roadmap":("How do we get from here to there","An ordered plan, every step with an owner and a finish line"),
 "decode":("What is this","Any term or tool in plain English, and why it matters to you"),
 "teach-me":("Teach me X","A tutor that goes one step at a time and remembers what you know"),
 "research":("Look this up properly","A sourced answer with citations, and what could not be found"),
 "daily-brief":("What is on my plate today","Schedule, replies that matter, deadlines, and your top three"),
 "browse":("Look at this page with me","It reads, navigates, and pulls from the site you are on"),
 "email":("Draft an email to X","One clean draft parked in your drafts. It never sends"),
 "voice":("Does this sound like me","Learns how you write, then fixes anything that misses"),
 "recap":("Here is the transcript","Commitments, what they actually want, a recap, a follow up"),
 "prep":("I have a call with X","A one page prep sheet and the pushback to expect"),
 "document":("Write me a one pager","A finished document you can open, print, and hand over"),
 "sop":("Turn this into a procedure","A written process someone else could follow without asking"),
 "handoff":("I have to go, save my place","Your place saved, so the next session starts clean"),
 "remember":("Remember this","Written to permanent memory, read back every session"),
 "new-skill":("Turn this into a skill","A permanent one phrase shortcut for what you keep asking"),
 "model-routing":("Which one are you using","The right-sized model picked for you, explained when it matters"),
 "one-question":("Write something up for me","One sharp question back when the ask is too thin to aim at"),
 "pressure-test":("Attack this plan before I commit","Four angles at your plan, then one verdict"),
 "prove-it":("Is that actually true","The claim checked against real evidence, or marked unproven"),
 "check-numbers":("Where did that number come from","Every figure traced to its source, or flagged"),
 "lesson-learned":("You did that wrong","The correction logged, and made impossible to repeat"),
 "delegate-to-agents":("Have the team do this","A researcher, a drafter and a reviewer, then one result"),
 "pipeline":("Review my pipeline","Where deals are stuck, what to call, what to kill"),
 "prospects":("Build me a prospect list","Real scored organisations and named people to approach"),
 "outreach":("Write outreach to X","One personalised first touch, grounded in something true"),
 "proposal":("Turn this into a proposal","Problem, deliverables, price, timeline, and exclusions"),
 "objections":("What pushback should I expect","Five likely objections ranked by damage, with answers"),
 "process-audit":("Where is the time going","The steps that eat your week, and the one to fix first"),
 "vendor-compare":("Which one should I pick","Honest comparison with real pricing and one recommendation"),
 "checklist":("Make this a checklist","A numbered run sheet with an owner and a pass or fail per line"),
 "incident":("Write up what happened","The honest account: timeline, real cause, and the fix"),
 "dashboard":("What should I be watching","Seven numbers max, each with its source and what bad looks like"),
 "budget":("How are we doing against budget","Variances explained, and one call on where to cut"),
 "spend-ledger":("What are we paying for","Every subscription, its cost, its owner, and what renews soon"),
 "forecast":("Will we run out of money","A base case and a downside, every assumption on its own line"),
 "unit-economics":("What does it cost us per customer","The arithmetic in the open, and your break even"),
 "collections":("Who owes us money","Aged invoices and a drafted chase for each. It never sends"),
 "grants":("Find us funding","Open grants and funding ranked, with deadlines verified"),
 "stakeholder-brief":("Prep me for this call","What they have backed, your ask, and what they will push back on"),
 "board-packet":("Build the board packet","Decisions on page one, the numbers with their story"),
 "impact-report":("Write our impact report","Outcomes kept separate from outputs, every number sourced"),
 "volunteers":("Set up a volunteer programme","Role, onboarding, shifts, and the follow up that brings them back"),
}
PACKS = [("exec","The core twenty","Everyone gets these."),
         ("exec-sales","Sales and revenue","If you carry a number."),
         ("exec-ops","Operations","If you run the machine."),
         ("exec-finance","Finance and money","If you watch the cash."),
         ("exec-mission","Mission and stakeholders","If you answer to a board, a funder, or a mission.")]

def skills(pack):
    d = ROOT/"plugins"/pack/"skills"
    return sorted(p.name for p in d.iterdir() if (p/"SKILL.md").exists()) if d.exists() else []

rows, missing, total = [], [], 0
for pack, title, sub in PACKS:
    names = skills(pack); total += len(names)
    body = ""
    for n in names:
        say, got = SAY.get(n, ("", ""))
        if not say: missing.append(f"{pack}/{n}")
        body += (f'<tr><td class="sk">{html.escape(n)}</td>'
                 f'<td class="say">&ldquo;{html.escape(say)}&rdquo;</td>'
                 f'<td>{html.escape(got)}</td></tr>\n')
    rows.append(f'''<h2>{html.escape(title)} <span class="cnt">{len(names)}</span></h2>
<p class="lede">{html.escape(sub)}</p>
<table><tr><th>Skill</th><th>Say something like</th><th>And you get</th></tr>
{body}</table>''')

if missing:
    raise SystemExit("FAIL: no cheat-sheet line authored for: " + ", ".join(missing))

CSS = """:root{--ground:#faf7f0;--ink:#22201c;--soft:#5d574c;--navy:#1b3a5c;--bronze:#9a7b4f;--rule:#e0d8c8}
*{box-sizing:border-box}body{margin:0;background:var(--ground);color:var(--ink);
font-family:Georgia,'Iowan Old Style','Times New Roman',serif;font-size:15px;line-height:1.5}
.wrap{max-width:52rem;margin:0 auto;padding:2.6rem 1.8rem 3rem}
.kicker{font-size:.7rem;letter-spacing:.19em;text-transform:uppercase;color:var(--bronze);font-weight:700}
h1{font-size:1.95rem;color:var(--navy);margin:.45rem 0 .3rem;font-weight:700}
.sub{color:var(--soft);margin:0 0 .4rem;font-size:.98rem}
header{border-bottom:2px solid var(--bronze);padding-bottom:1rem;margin-bottom:1.4rem}
h2{font-size:1.1rem;color:var(--navy);margin:1.8rem 0 .1rem;font-weight:700}
.cnt{font-size:.68rem;letter-spacing:.1em;color:var(--bronze);background:#f3eee2;border:1px solid var(--rule);
border-radius:9px;padding:.08rem .5rem;vertical-align:middle;margin-left:.4rem}
.lede{color:var(--soft);font-size:.9rem;margin:.1rem 0 .5rem}
table{width:100%;border-collapse:collapse;margin:.3rem 0 .2rem;font-size:.92rem}
th{text-align:left;font-size:.66rem;letter-spacing:.13em;text-transform:uppercase;color:var(--bronze);
border-bottom:1.5px solid var(--bronze);padding:.4rem .55rem .3rem}
td{padding:.38rem .55rem;border-bottom:1px solid var(--rule);vertical-align:top}
td.sk{white-space:nowrap;font-weight:700;color:var(--navy);width:9.5rem}
td.say{color:var(--ink);width:17rem;font-style:italic}
.note{background:#fffdf8;border:1px solid var(--rule);border-left:3px solid var(--navy);
padding:.85rem 1.1rem;margin:1.5rem 0;border-radius:2px}
.note b{color:var(--navy)}
footer{color:var(--soft);font-size:.78rem;border-top:1px solid var(--rule);margin-top:2rem;padding-top:1rem}
@media print{body{background:#fff;font-size:9.6pt}.wrap{padding:0;max-width:none}}"""

doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Skills Cheat Sheet</title><style>{CSS}</style></head><body><div class="wrap">
<header><div class="kicker">Centurion AI &middot; Executive OS</div>
<h1>Skills Cheat Sheet</h1>
<p class="sub">{total} skills. You get the core twenty plus the one pack that matches your work.</p></header>

<div class="note"><b>You do not have to say these exactly.</b> The phrases below are examples, not
commands. Say what you need in your own words and the right skill fires by itself. This page is for
when you want to know what is in the box.</div>

{"".join(rows)}

<div class="note"><b>Missing something?</b> Say &ldquo;turn this into a skill&rdquo; and describe
what you keep asking for. It writes a new one, tests it in front of you, and tells you the phrase
that triggers it from then on.</div>

<footer>Centurion AI &middot; Executive OS v1.0 &middot; Generated from the skills on disk on
{datetime.date.today().isoformat()}. Regenerate with <code>python3 tools/build-cheatsheet.py</code>.</footer>
</div></body></html>"""

(ROOT/"CHEAT-SHEET.html").write_text(doc)
print(f"CHEAT-SHEET.html written: {total} skills across {len(PACKS)} packs, 0 missing lines")
