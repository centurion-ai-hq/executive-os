---
description: "Reviews a budget or a spend export and reports what is actually happening: spend by category against plan, the three largest variances explained in plain English, what is drifting quietly, and one committed recommendation on where to cut or reallocate with a dollar figure attached. Use when the user says 'how are we doing against budget', 'run the budget review', 'where is spend drifting', 'check this against plan', or pastes a budget, spend export, or P&L."
argument-hint: "[paste budget or spend export]"
---

# Budget Review

Reads a budget or spend export and tells the executive, in plain numbers, where the money actually
went against the plan.

## When this fires
• The user pastes or uploads a budget, a spend export, a P&L, or a bank or card statement and asks
  how it looks.
• The user says "how are we doing against budget," "where is spend drifting," "run the budget
  review," or "check this against plan."
• A month or quarter just closed and the user wants the read before deciding anything.

## What you do
1. Parse the input into categories and amounts. If the file has no categories, group by vendor or
   description and say plainly that is what you did.
2. Build a table: category, planned, actual, variance in dollars, variance in percent. Sort by the
   size of the variance, largest first.
3. Pull the three largest variances. For each, give the plain-English reason if it is inferable
   from the data itself (a new vendor appeared, a category went to zero, a one-time charge landed).
   Label anything you cannot explain "cause unclear from this data" rather than guessing.
4. Scan separately for quiet drift: categories creeping up in small steps that never show up as one
   big variance. These are the ones that get missed in a normal review, so call them out on their
   own line.
5. Land on one committed recommendation: where to cut or reallocate, with the dollar figure
   attached. Not a menu of three options to pick from.
6. If a number in the plan or the actuals looks like a typo, a duplicate, or an outlier, flag it
   rather than silently rolling it into the total.

## Output
A table (category, planned, actual, variance $ and %), the three largest variances with plain-
English reasons, the quiet-drift list, and one recommendation with a dollar figure. Under one page.

## Rules
• This skill analyses the executive's own numbers only. It never gives personalised investment
  advice. If asked whether to invest in something, it says plainly it is not a licensed advisor and
  stops there.
• Never invent a category, a vendor name, or a figure that is not in the source data.
• Label every inferred reason as an inference, never state it as a fact.
• Ask before anything leaves this review: it never emails the write-up, never edits a budget in
  another system, and never deletes a line item. It only reads and reports.
• No em dashes. Bullets use •. Never "absolutely," "certainly," "great question," or "of course."
