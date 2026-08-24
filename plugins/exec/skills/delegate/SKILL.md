---
description: Battle drill. Hands a whole multi-part job to the agent team, chief-of-staff, researcher, drafter, and reviewer, instead of doing it in one pass, and returns the finished work plus two lines on what each worker contributed. Use when the user says "have the team do this", "run this properly", "this is a big one", "put your people on it", "do this end to end".
when_to_use: Fire this when the user says anything like "have the team do this", "run this properly", "put your people on it", "do this end to end", "this is a big one", "give this the full treatment", "hand this to the team", "get the team on this", "do the whole thing".
---

# Delegate

Hands a big job to a team of specialist workers instead of doing it all in one pass, then hands
back the finished result.

## When this fires

• The job has more than one real part: research, then writing, then a check, not one single step.
• The user says "have the team do this", "run this properly", "this is a big one", "put your
  people on it", "do this end to end".
• A job is big enough that doing it in a single pass risks skipping the checking step.

## What a sub-agent is

A sub-agent is a separate worker with one job and a clean head, meaning it never saw the rest of
this conversation. It cannot get tired or dragged off course by something said five minutes ago in
an unrelated part of the chat. It is like handing one piece of a project to a specialist who only
hears the brief for their piece, not the whole meeting. That focus is what makes the output better
than one generalist trying to do everything at once.

## What you do

1. Restate the job in one line so the user knows it was understood correctly before it goes out.
2. Hand the whole job to `chief-of-staff` using the Task tool. `chief-of-staff` is the only one of
   the four agents that delegates further, it is the lead.
3. `chief-of-staff` splits the job and routes the pieces:
   • `researcher` gathers the facts and sources the job actually needs, and returns evidence, not
     opinions.
   • `drafter` writes the first full version from that research, one committed draft, not options.
   • `reviewer` attacks the draft for gaps, wrong numbers, and anything overclaimed before it
     comes back.
4. Wait for `chief-of-staff` to assemble the pieces into one result. Do not intervene mid-flight
   and do not start doing the work yourself in parallel, that defeats the point of delegating it.
5. When it comes back, check the finished work actually answers the job as restated in step 1. If
   a piece is missing, send it back to `chief-of-staff` once, naming what's missing, before
   showing anything to the user.

## Output

One consolidated report:

• **The finished work:** the actual deliverable, not a summary of it.
• **What each worker contributed:** two lines each, only for the workers actually used. For
  example: "Researcher pulled current pricing from three source documents. Drafter wrote the memo
  from that pricing and flagged one open assumption on volume."
• Nothing narrated step by step while the team is working. One result, at the end.

## Rules

• Only `chief-of-staff` delegates. Never call `researcher`, `drafter`, or `reviewer` directly from
  here, that skips the assembly step and the team stops being a team.
• The team is visible, not magic. Always name what each worker actually did, in plain terms,
  never "the team handled it".
• Sending, publishing, spending, or deleting anything outside this project still needs the user's
  own go-ahead, no matter which worker produced it.
• If the job turns out to be one simple step, say so and just do it. Running the whole team on a
  one-line ask is theatre.
• Never claim a worker checked something it did not actually check. If reviewer was not used,
  do not imply that it was.
