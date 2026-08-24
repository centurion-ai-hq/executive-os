---
description: "Picks the right-sized AI model for each piece of work, automatically, and explains the choice in one line when it matters. Use when the user says "which model are you using", "is this worth the expensive one", "am I overpaying", "why is this slow", "use the good one for this", "don't overthink this one", or "is this worth the top model"."
when_to_use: Fire this when the user says anything like "which model are you using", "is this worth the expensive one", "am i overpaying", "why is this slow", "use the good one for this", "do not overthink this", "is this worth the top model", "how much is this costing", "use the cheap one".
---

# Model Routing

Every task gets matched to the right-sized model automatically: cheap and fast for mechanical
work, the best one for anything you will act on, so you never overpay for typing or underpay for
a decision.

## When this fires

• Every task, automatically, before any work starts. No trigger phrase needed.
• The user asks which model is running, whether it is worth the expensive one, or if they are
  overpaying.
• The user says "use the good one for this" or "don't overthink this one" to override the pick.
• Work feels slow and the user wants to know why.

## What you do

1. Before starting, size up the work: a lookup with one right answer, real drafting or research,
   or something the executive will make a decision from. That is the whole test.
2. Match the tier to the job using the table below, not to how big or urgent the request sounds.
3. Apply the rule that matters most: never economise on a decision the executive will act on;
   economise on typing. A wrong answer that sounds confident costs more than a slow one ever
   will. That is the expensive outcome, not the token bill.
4. If the job splits into genuinely independent pieces, meaning no piece needs another piece's
   answer first, run them at the same time. If one piece depends on another's result, run them in
   order. Forcing parallel work on dependent pieces produces answers that contradict each other.
5. Stay silent for routine work. The executive should never have to think about this.
6. Name the choice in one line whenever the output is something the executive will decide or act
   from: which tier, why, and what a wrong answer would cost.
7. When asked directly, answer for this specific task only: which tier is running, why, and the
   tradeoff, in plain English, no jargon.
8. Treat "use the good one for this" and "don't overthink this one" as direct overrides. Follow
   them. If the override cuts against the rule in step 3, say so in one line before proceeding.
9. Never trust the top tier blindly. If the output is load-bearing, check it against something
   real, a source, a calculation, a second pass, before it reaches the executive.

## The routing table

| The work | Tier | Why |
|---|---|---|
| Listing files, simple lookups, extraction, reformatting | Fast and cheap | Has one right answer |
| Drafting, research, most real execution | Middle | Needs judgment, not deep judgment |
| Architecture, strategy, adversarial review, anything they decide from | Top | A wrong call here costs real money |
| Very large volumes of mechanical work | Fast and cheap, run in parallel | Volume, not difficulty |

## Output

**Automatic mode (default):** nothing extra. Only when the output is decision-bearing, close with
one line: "Used the [tier] model here, because [one-clause reason]."

**On-request mode:** a short, plain-English answer naming three things: which tier is running for
this task, why that tier fits the work, and what changes if they push it up or down a tier.

## Rules

• Never route the cheap tier to anything the executive will make a decision from. That mistake is
  invisible until it costs something.
• Never route the top tier to mechanical volume work. That is wasted spend for no better answer.
• Say the choice out loud only when it matters: a decision, an override, or a direct question.
  Silent every other time.
• More expensive is not the same as correct. A top-tier answer stated with confidence can still be
  wrong, so load-bearing output gets checked, never just trusted.
• Independent pieces run in parallel. Dependent pieces run in order. Forcing parallel on dependent
  work produces contradictions, not speed.
• If the executive overrides the pick, follow it, and name the tradeoff in one line if it runs
  against the rule in step 3.
