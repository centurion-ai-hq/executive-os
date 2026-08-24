---
description: Battle drill. Verifies a claim before you act on it, states it precisely, finds the primary evidence rather than someone's summary of it, runs an actual check where one can be run, and returns PROVED, DISPROVED, or UNPROVEN with the evidence attached. Use when the user says "prove it", "is that actually true", "verify this", "did that really happen", "are you sure".
when_to_use: Fire this when the user says anything like "prove it", "is that actually true", "verify this", "did that really happen", "are you sure", "show me the evidence", "back that up", "how do you know", "says who", "I do not believe that", "check that claim".
---

# Prove

Checks a claim against primary evidence instead of taking anyone's word for it, including a prior
claim made in this same conversation.

## When this fires

• Someone told the user something and they want it checked before acting on it.
• A report, an email, or a document states something as fact.
• A prior turn in this session claimed a task is done, a number is right, or something exists.
• The user says "prove it", "is that actually true", "verify this", "are you sure".

## What you do

1. State the claim precisely, one sentence, no hedging. If the claim as given is too vague to
   check, narrow it to the specific checkable version and say what you narrowed and why.
2. Find the primary evidence: a file, a run's actual output, a source document, a dated record. A
   summary of the evidence, a description of it, or a prior claim that it is true, does not count.
3. Where an actual check can be run, run it. Open the file, execute the command, read the real
   number. Never reason about whether something is probably true when you could just look.
4. Compare what the evidence shows against the claim as stated. Note any part of the claim the
   evidence does not reach.
5. Return one verdict: **PROVED** (the primary evidence confirms it), **DISPROVED** (the evidence
   contradicts it), or **UNPROVEN** (no evidence found either way). UNPROVEN is a valid, honest
   outcome. Never round an UNPROVEN up to PROVED because the claim sounds plausible or confident.
6. Attach the evidence itself, not a description of it: the file path and line, the command and its
   output, the exact figure or quote.

## Output

One consolidated report:

• **The claim:** one sentence, exactly what was checked.
• **Verdict:** PROVED / DISPROVED / UNPROVEN, stated first, in capitals.
• **The evidence:** the actual file, output, or quote it rests on, with a path or line if it is a
  file.
• **What this does not cover:** any part of the original claim the evidence does not reach.

## Rules

• UNPROVEN is not a failure of this check, it is the correct answer when no evidence exists.
• Never accept a summary, a prior claim, or confident phrasing as evidence. Go to the source.
• Never soften DISPROVED into "partially true" language. If the evidence contradicts it, say so.
• Where nothing can actually be checked, a private conversation, an unrecorded event, say that
  plainly instead of guessing at a verdict.
• This skill only checks. It never fixes the underlying problem or acts on the finding itself.
