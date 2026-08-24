# Skill-router eval: eval-drills.tsv

Method: generated the exact production roster (Step 1 command, `router.py:roster()`, 45 skill
lines, each truncated to 104 chars with no ellipsis — this is literally what gets injected into
every message). Read only column 1 of `eval-drills.tsv`. Classified in four batches of 13,
writing predictions to a file before revealing column 2 for each batch, so no answer was seen
before its prediction was committed.

## Score

- **Top-1 accuracy: 52/52 = 100%**
- **First 20 lines (five untested skills: attack, prove, check-numbers, lesson, delegate): 20/20 = 100%**
- **Remaining 32 lines (eight confusable pairs): 32/32 = 100%**
- **Misses: none.**

Per-pair breakdown (all 4/4):

| Pair | Lines | Score |
|---|---|---|
| attack vs critic | 21–24 | 4/4 |
| prep vs stakeholder-brief | 25–28 | 4/4 |
| process-audit vs incident | 29–32 | 4/4 |
| decode vs teach-me | 33–36 | 4/4 |
| document vs sop | 37–40 | 4/4 |
| decide vs priorities | 41–44 | 4/4 |
| brain-dump vs roadmap | 45–48 | 4/4 |
| remember vs handoff | 49–52 | 4/4 |

## Full table

| # | Sentence | My pick | Correct | Result |
|---|---|---|---|---|
| 1 | Before I sign off on this budget, I want someone to poke holes in it from every angle - facts, failure case, whether it's overbuilt, whether the math actually works. | attack | attack | MATCH |
| 2 | We're about to approve the Q4 expansion plan and I need it stress tested hard before Friday's board call. | attack | attack | MATCH |
| 3 | Can you tear into this strategy doc before I bring it to the partners? I want the worst-case argument laid out too. | attack | attack | MATCH |
| 4 | This budget looks clean but I want it hit from every side - is it too much, are the numbers real, what's the case it flops. | attack | attack | MATCH |
| 5 | Marketing keeps saying the campaign lifted signups 40 percent and I want that checked against the actual data before we brag about it in the board deck. | prove | prove | MATCH |
| 6 | You told me the migration was done last week - I need that confirmed against something real before I tell the client it's live. | prove | prove | MATCH |
| 7 | Our ops lead swears the new vendor cut costs 15 percent, but I want that run down against the invoices before I repeat it anywhere. | prove | prove | MATCH |
| 8 | The report says churn dropped this quarter. Before I put that in front of investors, somebody needs to trace it back to the source. | prove | prove | MATCH |
| 9 | I've got the pricing memo open and I'm about to greenlight it, but every dollar figure in here needs to trace back to where it actually came from. | check-numbers | check-numbers | MATCH |
| 10 | This forecast has six figures on it and I'm not signing off until each one's origin is nailed down. | check-numbers | check-numbers | MATCH |
| 11 | Before this deck goes to the investors, walk every figure back to its source so nothing gets caught out later. | check-numbers | check-numbers | MATCH |
| 12 | There are a dozen percentages on this slide and I need to know where each one came from before I use it in the pitch. | check-numbers | check-numbers | MATCH |
| 13 | This is the third time you've quoted a price we froze months ago - I need that to actually stop happening, not just get apologized for again. | lesson | lesson | MATCH |
| 14 | We've been over this before about sending drafts without asking first, and it keeps slipping through, so make it stick this time. | lesson | lesson | MATCH |
| 15 | I corrected this same formatting mistake two weeks ago and here it is again - I need a real fix, not another sorry. | lesson | lesson | MATCH |
| 16 | You keep mixing up which account this data belongs to, and I've flagged it before. Make sure it actually holds this time. | lesson | lesson | MATCH |
| 17 | This competitor teardown is way too big for one pass - get some people digging, someone drafting, and someone else checking it before it lands on my desk. | delegate | delegate | MATCH |
| 18 | I need the vendor comparison researched, written up, and reviewed by a second set of eyes, not just knocked out in one go. | delegate | delegate | MATCH |
| 19 | Split the onboarding rewrite across a few hands - research the gaps, draft the fix, then have someone else check it before it comes back to me. | delegate | delegate | MATCH |
| 20 | This is too much for one shot. Get it researched, drafted, and reviewed in stages instead of trying to answer it all at once. | delegate | delegate | MATCH |
| 21 | I really like this expansion idea and that's exactly why I need someone to argue hard against it before I fall in love with it completely. | critic | critic | MATCH |
| 22 | Poke every hole you can find in this hiring plan - I'm attached to it and that's the problem, so give me a straight yes or no at the end. | critic | critic | MATCH |
| 23 | Before the board votes on this budget Friday, run it through the full gauntlet - facts, failure case, bloat, and whether the money actually works. | attack | attack | MATCH |
| 24 | This restructuring plan needs the whole workup before I approve it: check the assumptions, find the failure mode, see if it's overbuilt, and stress the numbers. | attack | attack | MATCH |
| 25 | I've got the leadership offsite Thursday and need the room, the agenda, and what outcome I'm walking out with. | prep | prep | MATCH |
| 26 | Get me ready for tomorrow's quarterly review - what's the setup, who's in the room, and what am I trying to land. | prep | prep | MATCH |
| 27 | I'm sitting down with Marcus Whitfield next week and need to know exactly what he's going to want from me walking in. | stakeholder-brief | stakeholder-brief | MATCH |
| 28 | Before I call Deborah Ashcroft tomorrow, tell me what she's holding that I need and how she tends to push back. | stakeholder-brief | stakeholder-brief | MATCH |
| 29 | Every month our invoice reconciliation eats two full days and half the time something's wrong at the end - I want to know why. | process-audit | process-audit | MATCH |
| 30 | The onboarding checklist keeps producing the same three mistakes over and over and I want to know where it's breaking down. | process-audit | process-audit | MATCH |
| 31 | The Tuesday deploy took down billing for four hours and I need an honest writeup of exactly what happened. | incident | incident | MATCH |
| 32 | We shipped the wrong pricing to eleven customers last night and I need a straight account of how that got out the door. | incident | incident | MATCH |
| 33 | Someone in the meeting kept saying 'attribution modeling' and I nodded along but I have no idea what that actually means. | decode | decode | MATCH |
| 34 | What does 'burn multiple' mean? Just give me the quick version so I'm not lost next time it comes up. | decode | decode | MATCH |
| 35 | I want to actually understand how our ad spend attribution works, not just the one-liner - walk me through it properly over a few sessions. | teach-me | teach-me | MATCH |
| 36 | Sit me down and go through how cap tables work from the ground up, I've got time this week and I want it to actually stick. | teach-me | teach-me | MATCH |
| 37 | Put together something clean I can hand Marcus summarizing where the partnership stands right now. | document | document | MATCH |
| 38 | I need a one-pager I can send the board explaining why we're pausing the hire. | document | document | MATCH |
| 39 | Write down how we close the books each month so Priya can run it without me walking her through it live. | sop | sop | MATCH |
| 40 | I want the vendor onboarding steps captured somewhere so whoever takes this over next quarter doesn't have to ask me. | sop | sop | MATCH |
| 41 | Just tell me straight - do we renew the Simmons contract or not, I've been sitting on this too long. | decide | decide | MATCH |
| 42 | Give me a yes or no on the office lease. I need to stop going back and forth on this one thing. | decide | decide | MATCH |
| 43 | I've got about nine things hanging over me right now and no idea which one to touch first - sort it out for me. | priorities | priorities | MATCH |
| 44 | Everything's piling up at once. Tell me what actually matters this week and what can wait. | priorities | priorities | MATCH |
| 45 | Okay so the lease is up, Priya's asking about her raise, the vendor thing is still unresolved, and I forgot to call the accountant back - just help me sort through all this. | brain-dump | brain-dump | MATCH |
| 46 | I've got like six half-finished thoughts rattling around, some about hiring, some about the product, just catch it all and organize it. | brain-dump | brain-dump | MATCH |
| 47 | I want to get us from where we are now to a working pilot by November - lay out the steps to get there. | roadmap | roadmap | MATCH |
| 48 | Give me the path from zero to a hundred paying customers, in order, so I know what comes first. | roadmap | roadmap | MATCH |
| 49 | Make sure this sticks for good - we never say 'affordable' in outbound copy again. | remember | remember | MATCH |
| 50 | Going forward, log that Priya prefers async updates over calls, that's permanent from now on. | remember | remember | MATCH |
| 51 | I'm out for the rest of today, jot down exactly where this build stands so tomorrow doesn't start from scratch. | handoff | handoff | MATCH |
| 52 | Before I close this out for the night, capture what's done and what's still hanging so the next session isn't guessing. | handoff | handoff | MATCH |

## Misses

None. 0 of 52.

## Per-pair discrimination analysis

For each pair, does the *actual injected roster text* (truncated to 104 chars, no ellipsis) carry
the words that separate the two skills? Quoting exactly what production sends.

**1. attack vs critic — sufficient, strong.**
- `attack: Battle drill. The full four-stage review of a plan the user is about to approve: the facts, the case tha[t...]`
- `critic: One honest voice arguing against a plan the user already likes, ending in a single verdict.`
Discriminator: "full four-stage... facts... case" (comprehensive, multi-dimension) vs "already likes... single verdict" (attachment/sunk-cost bias, one voice). Lines 21/22 say "I really like this," "I'm attached to it" — a direct lexical echo of "already likes." Lines 23/24 name multiple axes (facts, failure mode, bloat, numbers) — echoes "four-stage... facts."

**2. prep vs stakeholder-brief — sufficient, strong.**
- `prep: Readiness for a whole meeting or call: the room, the agenda, the outcome worth wanting, and the pushback`
- `stakeholder-brief: Readiness for ONE specific named person who holds something the user needs: a funder, an investor, a boa[rd...]`
Discriminator: "whole meeting or call" (event-level) vs "ONE specific named person" (person-level). Lines 27/28 name individuals (Marcus Whitfield, Deborah Ashcroft) with no meeting logistics mentioned — a clean match to "ONE specific named person."

**3. process-audit vs incident — sufficient, strong.**
- `process-audit: A recurring workflow that keeps wasting time or producing errors, every time it runs.`
- `incident: One specific thing that broke on one specific occasion, written up honestly.`
Discriminator: "recurring... every time" vs "one specific occasion." Lines 29/30 use "every month," "over and over"; lines 31/32 use "Tuesday," "last night" — single dated events.

**4. decode vs teach-me — sufficient, strong.**
- `decode: One term, tool, or concept explained plainly in a single answer.`
- `teach-me: A topic taught properly over several exchanges, one step at a time, checking understanding before moving`
Discriminator: "single answer" vs "several exchanges... one step at a time." Lines 35/36 explicitly ask for multi-session teaching ("over a few sessions," "I've got time this week").

**5. document vs sop — sufficient, but the closer of the eight.**
- `document: One finished written artifact to hand to a named person: a one pager, a memo, a brief.`
- `sop: A repeatable process written down so a different person could run it unaided.`
Discriminator: hand a finished artifact to a reader vs write steps so someone else can *execute* the process unaided. Both are "write something down," so the pair leans on the reader's role (informed vs empowered-to-run-it) rather than a sharp keyword split. Lines 39/40 ("so Priya can run it," "whoever takes this over... doesn't have to ask me") carry the operational-handoff language that "unaided" predicts, but a shorter or vaguer sentence in this territory could plausibly blur the two skills.

**6. decide vs priorities — sufficient, the cleanest of the eight.**
- `decide: One specific open decision, called. For ranking everything currently open, this is the wrong skill.`
- `priorities: Everything currently open, ranked, with what to do next and what is being dropped.`
The `decide` line contains a built-in negative example pointing at its own confusable neighbor ("for ranking everything currently open, this is the wrong skill"). This is the only skill in the roster with self-disambiguating text, and it worked exactly as designed.

**7. brain-dump vs roadmap — sufficient, but the weakest of the eight.**
- `brain-dump: Turn a raw brain dump into a clean, numbered ledger where nothing gets dropped, then act on it.`
- `roadmap: Turn a goal into an ordered step-by-step plan from where things stand now to the goal, with an owner, a[...]`
Discriminator: unconnected items with "nothing dropped" vs a single named destination with ordered steps. This held on the test lines because 47/48 name explicit destinations ("a working pilot by November," "a hundred paying customers") and 45/46 name disconnected topics with no shared destination ("hiring," "product," "lease," "raise," "vendor," "accountant"). But line 45 ("just help me sort through all this") on its own, without the enumerated disconnected list before it, would be a genuine coin-flip against `priorities` too — the roster text for brain-dump doesn't contain a word that rules out "rank this" the way `decide`'s does.

**8. remember vs handoff — sufficient, strong.**
- `remember: Storing a fact, ruling, price, or standing preference permanently.`
- `handoff: Saving the state of work in progress because the user is stopping for now.`
Discriminator: "permanently" (standing rule, no end date) vs "stopping for now" (temporary, session-bounded). Lines 49/50 use "for good," "permanent from now on"; lines 51/52 use "for the rest of today," "before I close this out for the night" — temporal language keyed directly to "stopping for now."

**Summary: all eight pairs had sufficient discriminating text in the actual 104-char-truncated
roster line.** The weakest was **document vs sop** and **brain-dump vs roadmap** — both resolved
correctly here because the test sentences carried strong secondary signals (an explicit
"unaided"-shaped clause; an explicit named destination/goal), not because the roster line alone
would firewall every possible phrasing. A shorter, vaguer real-world sentence in either of these
two territories is where I'd expect the first production miss.

## What this test cannot prove about production

1. I knew, going in, that every line was a classification exercise. In a real session the model is mid-task — half-attending to router output while actually doing research, writing, or code — and picking the "best label" is not the same posture as picking the best next action while busy with something else.
2. Every sentence was read in isolation, cold, with no conversation history. Real triggers arrive after paragraphs of context (an open document, a half-finished plan, a name mentioned three turns ago) that either resolve ambiguity for free or actively mislead the router toward a skill that fit turn 1 but not turn 9.
3. This set has exactly one skill-shaped ask per line. Real messages routinely carry two or three asks stacked together ("check these numbers, then draft the follow-up"), and nothing here measures whether the model picks one skill and drops the other, or fires both.
4. The five "previously untested" skills arrived in their own clean four-line block, immediately adjacent to their own vocabulary. Nothing here tests whether attack/prove/check-numbers/lesson/delegate stay correctly separated from each other or from older skills when a real sentence doesn't announce its category so cleanly.
5. All 52 sentences were written to be classifiable — none tested the "no skill fits, just answer" case, which is common in real traffic and is where a router most often over-fires.
6. I authored the pairing theory (which 4 lines belong to which pair) by pattern-matching before seeing answers, then those groupings shaped my read of borderline lines like #3 and #45. A test-taker without that meta-structure — i.e., the actual production router seeing lines in random order mixed with ordinary traffic — has strictly less signal than I used here.
7. 100% on 52 items is a small sample; it rules out gross roster defects, not rare failure modes, and a single well-designed adversarial sentence per pair (rather than the four written here) would tell us less, not more, about the floor.

---
**Word count: this analysis section is agent-facing, not a Luis-read document; the 500/1500-word
decision-document ceiling in CLAUDE.md does not apply to this file.**
