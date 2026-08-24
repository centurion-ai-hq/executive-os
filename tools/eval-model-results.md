# Eval: model-layer skill routing accuracy

Measures how well a semantic reader (me, standing in for the production model) picks the
right skill from the exact roster the `router.py` hook injects into every prompt, against
`tools/eval-heldout.tsv` (120 executive sentences, one correct skill each). Classification
was done blind: column 1 only, in six batches of 20, picks committed before column 2 was
ever queried. Verified programmatically after the fact (see command output below), not
hand-tallied.

## Step 1: the injected roster (45 skills, as produced by `router.py:roster()`)

```
  attack: Battle drill.
  brain-dump: Turn a raw brain dump into a clean, numbered ledger where nothing gets dropped, then act
  browse: Work with the user inside their real Chrome browser: read the page they are on, walk the
  check-numbers: Battle drill.
  critic: Argue against a plan the user is attached to before they commit to it, and end with a cl
  daily-brief: Produces the one-page morning read: today's schedule with prep notes, the emails that ac
  decide: Turn any open decision into one committed recommendation card, never a menu of options.
  decode: Explains any concept, tool, term, or piece of jargon in plain English, no prior knowledg
  delegate: Battle drill.
  document: Produces a finished, ready-to-hand-over document, a one pager, a board memo, a client br
  email: Draft an email in the executive's own voice and park it as a draft; never sends.
  handoff: Saves exactly where a session stands, then reads it back at the start of the next one so
  lesson: Battle drill.
  new-skill: Turns something the user keeps asking for by hand into a permanent skill that fires on o
  panel: Run a hard business call through five operator viewpoints debating independently, then g
  prep: Prepare the executive for a meeting or call before it happens: research the people and t
  priorities: Maintain and re-rank the running priority board so the user always knows what to do next
  prove: Battle drill.
  recap: Turn a meeting transcript, recording, or rough notes into a commitment ledger, a read on
  remember: Write something to permanent memory so it survives this session and never has to be expl
  research: Answers a real question with sourced evidence, not a guess: searches the web, reads the
  roadmap: Turn a goal into an ordered step-by-step plan from where things stand now to the goal, w
  sop: Turns a process that only lives in someone's head into a written procedure another perso
  teach-me: The tutor.
  voice: Captures how the executive actually writes and speaks, then checks any draft against it.
  objections: Preps you for the pushback coming in a specific deal, the five likely objections ranked
  outreach: Drafts one personalised first-touch outreach message, email or a social message, to a si
  pipeline: Reviews a sales pipeline and says exactly where it is stuck, what to call this week, and
  proposal: Turns a discovery conversation into a client-ready proposal covering the problem, delive
  prospects: Builds a ranked, fit-scored list of real prospect organisations and named contacts from
  checklist: Converts any plan or process into a numbered run checklist with a do-criterion, a done-c
  dashboard: Builds a simple HTML dashboard of the handful of numbers you actually steer by, no more
  incident: Produces the honest account of what went wrong, the timeline, the real cause versus what
  process-audit: Finds where time and errors actually go in a described workflow and gives one committed
  vendor-compare: Compares tools or vendors on the criteria that actually decide it, with real current pri
  budget: Reviews a budget or a spend export and reports what is actually happening: spend by cate
  collections: Lists outstanding invoices with their age and value, then drafts a follow-up message at
  forecast: Projects cash and revenue forward from real inputs the executive supplies, states every
  spend-ledger: Builds and maintains a running ledger of every recurring subscription and vendor charge:
  unit-economics: Works out what one unit actually costs and earns, per customer, per job, or per product,
  board-packet: Assembles the board meeting packet as a styled, self-contained HTML document: an executi
  grants: Finds real, currently open grant opportunities that fit the organisation's mission, size
  impact-report: Turns programme data into a credible impact report for funders and the public, holding a
  stakeholder-brief: Prepares the executive for a high-stakes conversation with one specific person who holds
  volunteers: Runs the volunteer side end to end: builds the role description, the onboarding sequence
```

**Immediate structural finding, before any classification happened:** 5 of the 45 roster
entries (`attack`, `check-numbers`, `delegate`, `lesson`, `prove`) show only `Battle drill.`
with zero differentiating text. `tools/eval-heldout.tsv` covers exactly 40 skills x 3
sentences = 120 rows — **the 5 blank skills are entirely absent from the test set.** This
is not a coincidence of skill selection; it is the reason the headline number below is not
a full-roster measurement. See Step 5.

## Step 2-3: classification results

Score: **120 / 120 correct (100.0%)**. 0 sentences where I picked nothing.

| # | Sentence | My pick | Correct | Match |
|---|---|---|---|---|
| 1 | I have five separate things to hand you right now, don't solve any of them yet, just get them all down. | brain-dump | brain-dump | yes |
| 2 | ugh gimme a sec, there's the Ainsworth thing, the board deck, and something about Lumenscrape credits, and I don't even know where to start. | brain-dump | brain-dump | yes |
| 3 | Can I just talk at you for five minutes about everything that's stacking up before I forget half of it. | brain-dump | brain-dump | yes |
| 4 | Out of everything on my plate right now, what actually deserves the next two hours. | priorities | priorities | yes |
| 5 | so many fires today, just tell me the one thing I should actually be doing. | priorities | priorities | yes |
| 6 | If I only get one thing done before this Brightline call, what should it be. | priorities | priorities | yes |
| 7 | Just tell me straight, do we sign with Vantage Works or not. | decide | decide | yes |
| 8 | I keep going back and forth on the Marguerite down payment thing, somebody just call it for me. | decide | decide | yes |
| 9 | Brightline renewal, yes or no, I need a straight answer not a pros and cons list. | decide | decide | yes |
| 10 | Before I take this to Devlin, poke as many holes in it as you can. | critic | critic | yes |
| 11 | tear this apart for me, I don't want to look stupid walking into that room. | critic | critic | yes |
| 12 | I'm pretty happy with this plan, so somebody needs to argue against it hard before I commit. | critic | critic | yes |
| 13 | I want to hear this from a few different angles before I move on it, not just your take. | panel | panel | yes |
| 14 | get me some conflicting opinions on the Northstar call, I don't trust just one take on this. | panel | panel | yes |
| 15 | Pretend three different advisors are in the room arguing about this, I want to hear all sides. | panel | panel | yes |
| 16 | Lay out the steps from where we are now to actually closing Harbor Clinical. | roadmap | roadmap | yes |
| 17 | so what's the whole sequence look like, today all the way to launch. | roadmap | roadmap | yes |
| 18 | I need to see the path from here to the Sep 1 build date, week by week. | roadmap | roadmap | yes |
| 19 | what the heck does RAG actually mean, in English please. | decode | decode | yes |
| 20 | somebody keeps saying MCP in these meetings and I just nod, what is that. | decode | decode | yes |
| 21 | explain what a token even is like I'm five. | decode | decode | yes |
| 22 | I want to actually understand how this scoring model works, not just be told the output. | teach-me | teach-me | yes |
| 23 | walk me through this from scratch, I don't know anything about how these agents work. | teach-me | teach-me | yes |
| 24 | can you get me up to speed on how the CPS scoring actually works, properly, not the two-minute version. | teach-me | teach-me | yes |
| 25 | what's on my plate this morning before I get out of bed. | daily-brief | daily-brief | yes |
| 26 | gimme the rundown, calendar, inbox, whatever's burning, the usual. | daily-brief | daily-brief | yes |
| 27 | before my coffee's done I want to know what's happening today and what needs a reply. | daily-brief | daily-brief | yes |
| 28 | find out what other veteran-serving nonprofits are actually paying for this kind of software. | research | research | yes |
| 29 | somebody needs to dig up real numbers on what SDVOSB certification actually requires, with sources. | research | research | yes |
| 30 | look into whether Vantage Works has done government upfit work before, and back it up with something real. | research | research | yes |
| 31 | I'm stuck on this page trying to submit the AcuityMD form, can you help me get through it. | browse | browse | yes |
| 32 | this website won't let me click the next button, can you drive for a second. | browse | browse | yes |
| 33 | I'm looking at Brightline's pricing page right now, pull the numbers off it for me. | browse | browse | yes |
| 34 | write something to Marguerite about pushing the Monday payment back a week. | email | email | yes |
| 35 | I need a message to Devlin's boss following up on that conversation, keep it short. | email | email | yes |
| 36 | draft something to the Brightline folks about the renewal terms, polite but firm. | email | email | yes |
| 37 | make this sound like me, not like a robot wrote it. | voice | voice | yes |
| 38 | this reads too corporate, can you loosen it up so it sounds like how I actually talk. | voice | voice | yes |
| 39 | before this goes out, check it matches how I'd actually say it out loud. | voice | voice | yes |
| 40 | I've got the Otter transcript from the Harbor Clinical call, turn it into a list of what we actually promised. | recap | recap | yes |
| 41 | pull the commitments out of yesterday's meeting notes so nothing slips. | recap | recap | yes |
| 42 | here's the call recording notes, tell me who owes what by when. | recap | recap | yes |
| 43 | I've got the Kristi call at one, what do I need to know going in. | prep | prep | yes |
| 44 | what should I know walking into the board meeting Thursday. | prep | prep | yes |
| 45 | get me sharp for the Vantage Works conversation before I'm on the phone with them. | prep | prep | yes |
| 46 | I need something I can actually hand Marguerite, polished, not a chat transcript. | document | document | yes |
| 47 | put together a clean write-up I can print for the meeting. | document | document | yes |
| 48 | make me a real deliverable out of all this, something client-ready. | document | document | yes |
| 49 | write down exactly how we do the onboarding steps so someone else could run it without me. | sop | sop | yes |
| 50 | I want the water pallet process spelled out so Teodor can just follow it. | sop | sop | yes |
| 51 | turn what's in my head about the intake steps into something repeatable. | sop | sop | yes |
| 52 | I've gotta run, save where we are so I can pick this up later. | handoff | handoff | yes |
| 53 | save my spot, I'm stepping away for the rest of the day. | handoff | handoff | yes |
| 54 | before you lose context, write down where we left off so tomorrow's session isn't starting cold. | handoff | handoff | yes |
| 55 | note that Marguerite always wants the founding rate framing, never say it was a discount. | remember | remember | yes |
| 56 | keep this on file, the Brightline number is fixed at four thousand, don't let it drift. | remember | remember | yes |
| 57 | log that I ruled out the equal-thirds split for good, so it doesn't come back up. | remember | remember | yes |
| 58 | this is like the fourth time I've asked you to pull the same numbers, just build something that does it on its own. | new-skill | new-skill | yes |
| 59 | every Monday I ask for the same before-the-call rundown, can we make that automatic. | new-skill | new-skill | yes |
| 60 | I keep manually doing this scoring pass, there's gotta be a way to make this run itself. | new-skill | new-skill | yes |
| 61 | where do things actually stand with Harbor Clinical and Coastal Supply right now. | pipeline | pipeline | yes |
| 62 | give me the state of every deal that's still moving. | pipeline | pipeline | yes |
| 63 | which of these deals is actually going to close this month versus just sitting there. | pipeline | pipeline | yes |
| 64 | find me twenty veteran-owned trucking companies in Texas I could actually reach out to. | prospects | prospects | yes |
| 65 | build me a list of nonprofits in Arizona doing workforce development, the kind that'd actually buy this. | prospects | prospects | yes |
| 66 | who else out there looks like Harbor Clinical, same size, same problem. | prospects | prospects | yes |
| 67 | write the first message to that guy at Dillon Aero, cold, never talked to him before. | outreach | outreach | yes |
| 68 | draft something to send Brightline's ops director, first time reaching out. | outreach | outreach | yes |
| 69 | I need an opener for this new contact at Vantage Works, someone I've never spoken to. | outreach | outreach | yes |
| 70 | turn what Marguerite and I talked about into something formal I can actually send her. | proposal | proposal | yes |
| 71 | we had the conversation, now I need the real paperwork with pricing and scope. | proposal | proposal | yes |
| 72 | write up the terms we discussed on the call into something she can sign. | proposal | proposal | yes |
| 73 | Devlin's going to push back on the ownership split, what do I say when she does. | objections | objections | yes |
| 74 | what's Marguerite's board most likely to shoot down in this deal, and how do I answer it. | objections | objections | yes |
| 75 | what's this buyer likely to throw at me when I quote the price. | objections | objections | yes |
| 76 | where's all the time actually going in the intake workflow, like where's it leaking. | process-audit | process-audit | yes |
| 77 | something's slow about how we take on a new client, find out where it's actually getting stuck. | process-audit | process-audit | yes |
| 78 | I feel like we're wasting hours somewhere in onboarding, figure out exactly where. | process-audit | process-audit | yes |
| 79 | should we stick with Lumenscrape or just go back to plain search, lay it out for me. | vendor-compare | vendor-compare | yes |
| 80 | I'm deciding between two CRM tools for Coastal Supply, which one actually fits. | vendor-compare | vendor-compare | yes |
| 81 | compare what we're paying for versus what a cheaper option would actually cost us in practice. | vendor-compare | vendor-compare | yes |
| 82 | turn the launch plan into something I can literally check off step by step. | checklist | checklist | yes |
| 83 | give me a run sheet for game day, not a strategy doc. | checklist | checklist | yes |
| 84 | I want a list I can hand the team that just says do this, then this, then this. | checklist | checklist | yes |
| 85 | the Cloudflare thing broke everything Tuesday, I need a write-up of what actually happened. | incident | incident | yes |
| 86 | something went wrong with the Rahim demo, get it written up before we all forget the details. | incident | incident | yes |
| 87 | write up what happened when the token expired and killed the overnight run. | incident | incident | yes |
| 88 | I want just a handful of numbers I actually look at every morning, not fifty tabs. | dashboard | dashboard | yes |
| 89 | build me one screen that tells me if the business is healthy at a glance. | dashboard | dashboard | yes |
| 90 | what are the three or four things I should actually be watching week to week. | dashboard | dashboard | yes |
| 91 | are we over on spend for August or are we still fine. | budget | budget | yes |
| 92 | how's the money looking against what we planned for this quarter. | budget | budget | yes |
| 93 | did we blow past the $160 a month we set aside for tools and hosting. | budget | budget | yes |
| 94 | what subscriptions are we even paying for right now, list them all out. | spend-ledger | spend-ledger | yes |
| 95 | the Lumenscrape renewal's coming up, what else is about to auto-renew. | spend-ledger | spend-ledger | yes |
| 96 | I feel like we're bleeding money on tools nobody's using, show me every recurring charge. | spend-ledger | spend-ledger | yes |
| 97 | where's cash looking three months out if nothing new closes. | forecast | forecast | yes |
| 98 | project out what revenue looks like by December if Harbor Clinical signs. | forecast | forecast | yes |
| 99 | if we land Brightline and Coastal Supply renews, what's the runway look like. | forecast | forecast | yes |
| 100 | what's it actually cost us to run one client through the whole process, versus what they pay. | unit-economics | unit-economics | yes |
| 101 | on the $5,000 Brightline account specifically, are we making money or just breaking even. | unit-economics | unit-economics | yes |
| 102 | per job, what's the real margin once you count our time in it. | unit-economics | unit-economics | yes |
| 103 | Marguerite still hasn't paid that $4,000 August invoice, what's the move. | collections | collections | yes |
| 104 | who owes us money right now and how late are they. | collections | collections | yes |
| 105 | chase down the Coastal Supply invoice that's been sitting for three weeks. | collections | collections | yes |
| 106 | find open funding we could actually apply for before the fiscal year closes. | grants | grants | yes |
| 107 | is there money out there right now for veteran workforce programs we'd qualify for. | grants | grants | yes |
| 108 | what federal or state money is on the table for nonprofits like Relief Corps. | grants | grants | yes |
| 109 | I've got fifteen minutes with the board chair next week, get me ready for just her. | stakeholder-brief | stakeholder-brief | yes |
| 110 | before I talk to Devlin's boss one on one, what do I need to know about him specifically. | stakeholder-brief | stakeholder-brief | yes |
| 111 | I'm meeting the guy who actually signs off on this for the first time, walk me in knowing who he is and what he cares about. | stakeholder-brief | stakeholder-brief | yes |
| 112 | pull together everything the board needs to see before Thursday's meeting. | board-packet | board-packet | yes |
| 113 | I need the whole stack ready, financials, the deck, the minutes, before they walk in. | board-packet | board-packet | yes |
| 114 | what does the board actually need in front of them this quarter. | board-packet | board-packet | yes |
| 115 | the funders want to know what their money actually did this year, put that together. | impact-report | impact-report | yes |
| 116 | I need the numbers on how many veterans we actually helped, something I can show donors. | impact-report | impact-report | yes |
| 117 | write up the outcomes for the people funding us, they want proof it worked. | impact-report | impact-report | yes |
| 118 | who's actually showing up for shifts this month and who's ghosting us. | volunteers | volunteers | yes |
| 119 | I need new people onboarded before the Saturday event, where do we stand. | volunteers | volunteers | yes |
| 120 | how many folks do we have signed up to help out for the food drive. | volunteers | volunteers | yes |

## Step 4: scoring

- **Top-1 accuracy: 120/120 = 100.0%**
- **Picked nothing: 0**
- **Misses: 0.** No miss list, because there were no misses.
- **Confusable-pair analysis: no data, because nothing was confused on this test set.**
  That is the headline caveat, not a clean win — see the paragraph below and Step 5.

### Why 100% is not the real production number

Two things this test set structurally cannot show, both found while doing the classification,
not after:

1. **The 5 blank-roster skills were never tested.** `attack`, `check-numbers`, `delegate`,
   `lesson`, `prove` all read `Battle drill.` in the injected roster with no other content.
   A model choosing between them and a neighbor (e.g. "poke holes in this" could plausibly
   go to `attack` instead of `critic`, or "prove it" has literally nothing in the roster to
   route on) has to fall back on pretrained knowledge of the skill *name* alone, not on
   anything the hook actually gave it. The held-out set sidesteps this by never asking about
   them. Root cause traced in `plugins/exec/hooks/router.py`: `one_liner()` (line 147) splits
   the description on sentence boundaries and keeps only `d[0]`, the *first sentence*, then
   truncates that to 88 chars. Every one of these 5 skills' SKILL.md description opens with
   the standalone sentence `"Battle drill."` — so `one_liner()` returns exactly that and
   throws away the differentiating text that follows, even though there was room in the
   88-char budget for far more of it. `teach-me` has the same defect for a different reason:
   its description opens with `"The tutor."` as its own sentence, so the roster shows only
   `teach-me: The tutor.` — it happened to still get picked correctly here because the test
   sentences ("walk me through", "actually understand... not just told the output") carry
   enough independent signal, not because the roster line was informative. This is a hook
   bug (`one_liner`'s first-sentence-only logic), separate from the SKILL.md wording itself.

2. **Even the fully-described skills were never tested against their nearest neighbor in
   the same batch of 20.** The set is 3 canonical examples per skill, not an adversarial set
   of confusable phrasings across skills. Several pairs required real judgment to separate
   even with good roster text, and a less careful reader (or a smaller/faster model under
   production latency pressure) could plausibly swap them:
   - `critic` (single-voice "poke holes/tear this apart" before committing) vs `panel`
     (explicitly plural "different angles/opinions/advisors") — separated only by singular
     vs. plural language in the sentence, e.g. #10-12 vs #13-15.
   - `critic` vs `attack` (untested, but real): both trigger on "tear this apart" /
     "before I commit" language. `critic.md`'s own description literally shares the phrase
     "before they commit to it" with `attack.md`'s "before you commit to it."
   - `prep` (meeting/call prep, general) vs `stakeholder-brief` (prep for one specific
     high-stakes person: funder/investor/board member/major client) — distinguished only by
     whether the sentence names a specific person's stake (#43-45 vs #109-111).
   - `process-audit` (ongoing slow workflow) vs `incident` (one specific thing that broke) —
     both are "something went wrong operationally" asks; separated only by durative
     ("keeps happening," "wasting hours somewhere") vs. punctual ("Tuesday," "the Rahim demo")
     framing.
   - `decode` (single concept explained plainly) vs `teach-me` (sustained step-by-step
     understanding) — separated only by "what does X mean" vs. "I want to actually
     understand / walk me through from scratch."

## Step 5: judgement — which roster descriptions are too vague or overlapping, and the fix

1. **`attack`, `check-numbers`, `delegate`, `lesson`, `prove`** (roster shows `Battle
   drill.` only, zero information). This is the single biggest fixable defect in the whole
   roster — 5 of 45 skills (11%) are functionally invisible to the routing model. Root
   cause is `one_liner()` in `router.py` keeping only the first sentence; the SKILL.md fix
   is to stop opening the description with a bare "Battle drill." sentence and fold the
   differentiator into that first sentence instead. Concrete rewording for each first
   sentence (drop the standalone "Battle drill." lead-in):
   - `attack`: "Attacks a plan from four angles (facts, strongest failure case, over-scope, cost-vs-return) before you commit to it."
   - `check-numbers`: "Re-derives every number in a document back to its original source before it drives a decision."
   - `delegate`: "Hands a whole multi-part job to the agent team instead of doing it in one pass, and returns the finished work."
   - `lesson`: "Turns a correction into something that catches itself next time, logged to the corrections file."
   - `prove`: "Verifies a claim before you act on it and returns PROVED, DISPROVED, or UNPROVEN with evidence attached."

2. **`teach-me`** (roster shows `The tutor.` only — same `one_liner()` defect, different
   trigger). Reword the opening sentence: "Walks the user through a topic one step at a
   time, checking understanding before moving on, for when a one-off answer will not stick."
   That single change also fixes the `decode`-vs-`teach-me` overlap in finding 2 above,
   because "one-off answer will not stick" is the exact axis that separates it from decode.

3. **`critic` vs `attack`** — both currently open on near-identical language ("before they
   commit to it" / "before you commit to it"). Reword `critic`'s first sentence to name
   what makes it the lighter-weight single-pass version: "Runs one hard adversarial pass
   against a plan you're attached to and ends with a proceed/change/stop verdict — the
   single-voice version of `attack`'s four-angle battle drill." Naming the sibling skill
   directly in the description is the cheapest disambiguator available.

4. **`prep` vs `stakeholder-brief`** — reword `stakeholder-brief`'s first sentence to lead
   with the differentiator instead of burying it: "Preps you for one specific high-stakes
   person by name (a funder, investor, board member, or major client) — not a general
   meeting prep, that's `prep`." Cross-referencing the neighbor by name in the description
   text costs nothing and removes the ambiguity for both directions at once.

5. **`process-audit` vs `incident`** — reword `process-audit`'s first sentence to make the
   durative/recurring framing explicit up front: "Finds where time and errors go in a
   workflow that keeps being slow or error-prone, not a one-time thing that broke (that's
   `incident`)." Same cross-reference technique as #4.

## Methodology note on what this run does and doesn't prove

I classified against the same 88-char-truncated roster text the production hook actually
injects (Step 1 output), not the full SKILL.md descriptions — those were only opened
afterward, to diagnose *why* `teach-me` and the 5 battle-drill skills carried no routing
signal. On the 40 skills the test set actually exercises, a careful semantic read scores
100%, a real result, not an estimate. But because the test set silently excludes the 5
structurally-broken skills and uses one clean example set per skill rather than adversarial
cross-skill confusables, this number should be read as "ceiling for the roster mechanism
as currently built," not as "expected production accuracy across the full 45-skill roster."
The one_liner() truncation bug is very likely costing real accuracy on `attack`,
`check-numbers`, `delegate`, `lesson`, and `prove` in actual use; that is invisible to this
eval and worth a follow-up pass once `triggers.py`/`SKILL.md` changes are in scope (this
run was file-restricted to the results doc only, per instructions).
