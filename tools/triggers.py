#!/usr/bin/env python3
"""
The trigger table. The phrases an executive actually says, mapped to the skill that should fire.

This is written into each SKILL.md as a `when_to_use` frontmatter field, which Claude reads for
its own native skill matching AND which the router scores against. One source, two layers.

Authored by hand, deliberately, before the held-out evaluation was written. Do not paste
evaluation sentences in here: that turns the score into a measurement of nothing.
"""

TRIGGERS = {
# ---- core: the daily five -------------------------------------------------
"brain-dump": ["brain dump", "everything on my mind", "let me get this all out", "a few things",
  "couple things", "dumping this on you", "sort this out", "here is everything", "lot going on",
  "off the top of my head", "in no particular order", "before I forget", "while I remember",
  "bear with me", "rambling", "a bunch of things", "several things", "three things", "ok so"],
"priorities": ["what should I do first", "what is on my plate", "what matters most",
  "reprioritize", "re prioritise", "what is open", "where are we on everything", "what do I owe",
  "what am I forgetting", "add this to the list", "I am underwater", "what actually matters",
  "too much going on", "what can wait", "what should I drop", "my list", "the board", "my plate",
  "what should I be doing", "what do I do now", "what is next", "where do I start"],
"decide": ["should I do this", "should we do this", "should I go ahead", "what is the call", "help me decide", "which one do I pick",
  "make the call", "yes or no", "go or no go", "I have been sitting on this", "torn between",
  "what would you do", "your recommendation", "pull the trigger", "commit to this", "decision"],
"decode": ["what is", "what does that mean", "explain this", "in plain english", "break it down",
  "eli5", "I do not understand", "what does it do", "never heard of", "what is the difference",
  "translate this", "jargon", "acronym", "decode this", "dumb it down", "simply put"],
"daily-brief": ["what is on my plate today", "morning brief", "daily brief", "bring me up to speed",
  "catch me up", "what is today", "start my day", "what is happening today", "my day",
  "this morning", "before my first meeting", "brief me"],

# ---- thinking -------------------------------------------------------------
"critic": ["poke holes", "talk me out of it", "what am I missing", "devil's advocate",
  "tear this apart", "push back on this", "argue against", "is this actually a good idea",
  "what could go wrong", "stress test this", "be honest with me", "do not agree with me",
  "what is wrong with this", "am I fooling myself"],
"panel": ["run the panel", "second opinion", "what would a board say", "pressure test this",
  "real disagreement", "different perspectives", "multiple viewpoints", "get me other opinions",
  "what would other people say", "I want an argument", "not another yes"],
"roadmap": ["how do we get from here to there", "build me a roadmap", "what is the plan",
  "sequence this", "what order", "steps to get to", "path to", "how do we reach",
  "plan to get to", "get us to", "milestones", "phases", "what comes first"],
"teach-me": ["teach me", "walk me through", "I want to learn", "step by step",
  "help me understand", "tutor me", "I want to actually understand", "how does this work",
  "show me how", "I am new to this", "explain it properly", "go slower"],
"research": ["look this up", "research this", "find out", "who is", "who owns", "dig into",
  "what is the market", "compare the options out there", "is that true", "verify this",
  "what do we know about", "background on", "look into"],

# ---- working --------------------------------------------------------------
"browse": ["look at this page", "this website", "this site", "on my screen", "what I am looking at",
  "pull this off", "navigate this", "help me get through this", "fill this out", "this portal",
  "this dashboard I am on", "walk me through this site", "grab this from the page", "log in and",
  "this web page", "can you see this", "this page", "stuck on this page", "on this site",
  "help me with this page", "reading this page"],
"email": ["draft an email", "write an email", "send something to", "reply to this",
  "compose", "write to", "email them", "email her", "email him", "follow up with",
  "get back to them", "respond to this", "note to"],
"voice": ["does this sound like me", "in my voice", "how I write", "learn my voice",
  "sound like me", "my writing style", "rewrite this so it sounds", "too formal", "too stiff",
  "that is not how I talk", "match my tone"],
"recap": ["here is the transcript", "we just met", "recap this", "what did we agree",
  "summarize this call", "notes from the call", "the meeting", "what was said", "after the call",
  "otter", "recording", "minutes"],
"prep": ["I have a call with", "prep me for", "meeting with", "before I walk in", "pitch to",
  "what do I need to know before", "getting ready for", "call tomorrow", "meeting tomorrow",
  "who am I meeting", "brief me on this meeting"],
"document": ["one pager", "write me a memo", "I need something I can send", "hand to them",
  "put this in a document", "make this presentable", "turn this into a memo", "a brief",
  "something formal", "leave behind", "write this up properly", "a doc", "a pdf"],
"sop": ["turn this into a procedure", "write an sop", "document this process",
  "so someone else can do it", "how we do this", "standard operating", "repeatable",
  "hand this off to someone", "train someone on this", "write down how"],

# ---- system ---------------------------------------------------------------
"handoff": ["save my place", "I have to go", "pick this up later", "pick this up tomorrow",
  "where were we", "continue where we left off", "running out of time", "stop here for now",
  "come back to this", "wrap up for today"],
"remember": ["remember this", "do not forget", "make a note", "from now on", "always do",
  "never do", "I decided", "that is confirmed", "we are going with", "locked in", "note that",
  "keep that in mind", "for the record", "going forward"],
"new-skill": ["turn this into a skill", "I keep asking you", "make this a standing thing",
  "every time I ask", "same thing again", "can you just remember to do this",
  "save this as something", "make this automatic", "do this every time"],

# ---- battle drills: one word fires a whole sequence -----------------------
"attack": ["attack this plan", "grill this", "before I commit", "pressure this plan",
  "rip this apart", "attack it", "war game this", "what would kill this",
  "am I about to make a mistake", "sanity check this plan", "shoot holes in the plan"],
"prove": ["prove it", "is that actually true", "verify this", "did that really happen",
  "are you sure", "show me the evidence", "back that up", "how do you know", "says who",
  "I do not believe that", "check that claim"],
"check-numbers": ["check the numbers", "where did that number come from", "is that number right",
  "where did that come from", "where did this come from", "how did you get that",
  "what is that based on", "where does that figure come from", "that percent",
  "does that add up", "check the math", "check the maths", "run the numbers again",
  "that figure looks wrong", "verify these figures", "recalculate"],
"lesson": ["you did that wrong", "I already told you", "stop doing that", "lesson learned",
  "that is not what I asked", "you keep doing this", "we talked about this",
  "do not do that again", "you got that wrong"],
"delegate": ["have the team do this", "run this properly", "put your people on it",
  "do this end to end", "this is a big one", "give this the full treatment",
  "hand this to the team", "get the team on this", "do the whole thing"],

# ---- lane: sales ----------------------------------------------------------
"pipeline": ["my pipeline", "review the pipeline", "deals are stuck", "deal is stuck", "stuck in the pipeline",
  "stalling", "what should I call about", "this quarter's number", "deal review", "my deals",
  "what is at risk", "close this month", "forecast the deals"],
"prospects": ["prospect list", "find me leads", "who should I target", "who should I be targeting",
  "build me a list", "companies to go after", "new business", "lead list", "who to approach",
  "find companies"],
"outreach": ["outreach message", "cold email", "reach out to", "first touch", "linkedin message",
  "intro message", "cold call script", "approach them", "get in front of them"],
"proposal": ["write a proposal", "scope of work", "sow", "turn this into a proposal",
  "quote them", "put together a proposal", "statement of work", "what we would deliver"],
"objections": ["what pushback", "objections", "what will they say", "how do I answer",
  "they will push back", "what are they going to ask", "prepare for resistance",
  "how do I handle it when they say"],

# ---- lane: ops ------------------------------------------------------------
"process-audit": ["where is the time going", "audit this process", "what should we automate",
  "this takes too long", "too many steps", "where are the bottlenecks", "streamline this",
  "why does this take so long", "wasted time", "manual work"],
"vendor-compare": ["which vendor", "compare these tools", "which one should I pick",
  "worth it versus", "is it worth it", "should we switch", "evaluate these options",
  "which software", "which platform", "buy or build"],
"checklist": ["make this a checklist", "run sheet", "steps I can follow", "checklist for",
  "what do I do in order", "so nothing gets missed", "walk through the launch", "go live steps"],
"incident": ["write up what happened", "incident report", "post mortem", "what went wrong",
  "explain this to the client", "we messed up", "root cause", "it broke", "outage",
  "how do we explain this"],
"dashboard": ["build me a dashboard", "what should I be watching", "key numbers",
  "one page view", "track our metrics", "what numbers matter", "scoreboard", "kpis",
  "at a glance", "how is the business doing"],

# ---- lane: finance --------------------------------------------------------
"budget": ["against budget", "budget review", "where is spend drifting", "over budget",
  "how are we doing on spend", "variance", "cost overrun", "our spending", "p and l", "p&l"],
"spend-ledger": ["what are we paying for", "subscriptions", "recurring charges", "renewing soon",
  "what renews", "vendor charges", "monthly costs", "are we still using", "cancel anything",
  "our software costs"],
"forecast": ["forecast", "run out of money", "cash flow", "project revenue", "next quarter",
  "runway", "model this out", "what happens if", "cash position", "will we make it"],
"unit-economics": ["cost per customer", "margin per", "break even", "unit economics",
  "is this job profitable", "does this make money", "cost to serve", "per job",
  "what does one cost us", "profitable at that price"],
"collections": ["who owes us", "unpaid invoices", "chase this invoice", "chase these",
  "collections", "aging report", "receivables", "they have not paid", "outstanding invoices",
  "late payment", "overdue"],

# ---- lane: mission --------------------------------------------------------
"grants": ["find us grants", "grant opportunities", "what grants are open", "find us funding",
  "funding opportunities", "apply for funding", "non dilutive", "who funds this kind of work",
  "grant deadlines", "open applications"],
"stakeholder-brief": ["brief me on this person", "meeting with the funder", "before I talk to them",
  "who is this person", "what have they backed", "prep me for this call with",
  "investor meeting", "board member meeting", "what do they care about"],
"board-packet": ["board packet", "board meeting", "board materials", "board deck",
  "prep the board", "what the board needs", "board update", "for the board"],
"impact-report": ["impact report", "annual report", "what did we accomplish", "our results",
  "outcomes report", "report to funders", "show our impact", "year in review",
  "what changed because of us"],
"volunteers": ["volunteer", "volunteers", "shift plan", "volunteer onboarding",
  "we need people to help", "recruit helpers", "volunteer roles", "community helpers"],
}

if __name__ == "__main__":
    import sys
    n = sum(len(v) for v in TRIGGERS.values())
    print(f"{len(TRIGGERS)} skills, {n} trigger phrases, {n/len(TRIGGERS):.1f} average")
    dupes = {}
    for skill, phrases in TRIGGERS.items():
        for p in phrases:
            dupes.setdefault(p, []).append(skill)
    clash = {p: s for p, s in dupes.items() if len(s) > 1}
    if clash:
        print("\nPhrases claimed by more than one skill (ambiguity, not necessarily a bug):")
        for p, s in sorted(clash.items()):
            print(f"  {p!r} -> {s}")
    sys.exit(0)
