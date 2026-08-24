---
description: Battle drill. Re-derives every number in a document back to its original source before it drives a decision, where each figure came from, how it was calculated, and whether recalculating it from the source reproduces it, and never trusts a field label on its own. Use when a document carrying figures is about to drive a decision, and on "check the numbers", "where did that number come from", "is that number right".
when_to_use: Fire this when the user says anything like "check the numbers", "where did that number come from", "is that number right", "where did that come from", "where did this come from", "how did you get that", "what is that based on", "where does that figure come from", "that percent", "does that add up", "check the math", "check the maths", "run the numbers again", "that figure looks wrong", "verify these figures", "recalculate".
---

# Check Numbers

Traces every number in a document back to where it actually came from, so a decision never rests
on a figure nobody can explain.

## When this fires

• A document carrying dollar figures, percentages, or counts is about to drive a decision.
• The user says "check the numbers", "where did that come from", "is that number right".
• Before signing off on a proposal, a budget, a forecast, or any report someone else prepared.

## What you do

1. List every number in the document that carries weight, meaning a wrong figure would change the
   decision. Skip page numbers and dates unless a date itself is load-bearing.
2. For each number, find where it came from: a source file, a calculation, a person's estimate, a
   prior document. State the source plainly, never "it seems to come from".
3. Check the label against the actual data, never trust it on its own. If a column is called
   "monthly revenue", open the source and confirm it actually holds monthly figures, not a
   quarterly total divided by three somewhere upstream, or a mislabeled year-to-date sum.
4. Where a calculation produced the number, redo the calculation from the source inputs. Does it
   reproduce the number in the document. If not, say by how much it is off and where it likely broke.
5. Any number that cannot be traced, an untraceable formula, a figure with no backing file, a
   person's memory with nothing written down, gets flagged as untraceable. Say plainly that an
   untraceable number is not evidence, no matter how confidently it is stated.
6. Roll all of it into one table, then one line: how many of the numbers actually check out.

## Output

One consolidated report, a table with these columns: Number, Where it says it's from, What the
source actually shows, Verdict. Verdict is one of CONFIRMED, OFF BY (amount), MISLABELED,
UNTRACEABLE. Then one summary line, for example "9 of 11 numbers confirmed, 1 off by $400, 1
untraceable." Then, if anything is UNTRACEABLE or OFF, the specific figures the decision should
not rest on until fixed.

## Rules

• Never accept a field label as proof of what a number is. Open the source and check it.
• An untraceable number is not evidence. Say this plainly, never soften it into "unclear".
• Recalculate from the source wherever a calculation is claimed, do not eyeball plausibility.
• Flag, by name, the numbers a decision should not be made on until they are fixed.
• This skill only checks the numbers. It does not judge whether the plan itself is a good idea,
  that is a different drill.
