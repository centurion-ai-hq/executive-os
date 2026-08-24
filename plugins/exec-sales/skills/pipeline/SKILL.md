---
description: Reviews a sales pipeline and says exactly where it is stuck, what to call this week, and what to kill. Use when the user says "review my pipeline", "what's stuck", "where are my deals stalling", "what should I call about this week", "walk my pipeline", pastes a CRM export or a deal list, or asks what is at risk to this quarter's number.
when_to_use: Fire this when the user says anything like "my pipeline", "review the pipeline", "deals are stuck", "deal is stuck", "stuck in the pipeline", "stalling", "what should i call about", "this quarter's number", "deal review", "my deals", "what is at risk", "close this month", "forecast the deals".
---

# Pipeline Review

Reads your deal list and tells you where the number is actually stuck, not just where it looks busy.

## When this fires

• The user pastes or points to a CRM export, spreadsheet, or plain list of deals.
• The user asks "what's stuck", "where's my pipeline stalling", "what should I call about this week".
• The user wants to know what's at risk to this quarter's number.
• A weekly or monthly pipeline check-in.

## What you do

1. Read the pipeline data the user provides: pasted text, a spreadsheet, or a file in the project folder. If no data is given, ask for it once: "Paste the list or point me to the file."
2. Group every deal by stage and sum the dollar value in each stage. This is the total-by-stage view.
3. For every deal, calculate how long it has sat in its current stage. Flag anything stalled: no stage change in 21+ days by default, or a different threshold if the user states their normal sales cycle.
4. Identify the single biggest risk to this quarter's number: the one thing most likely to make the quarter miss (a stalled large deal, a stage with unusually low conversion, a rep with no logged activity). State it as one sentence with the dollar amount attached.
5. Rank the three calls worth making this week by expected value: deal size times your best-guess probability of closing sooner if the call happens. Show the math, do not just assert the order.
6. Name the one deal you would kill outright: the deal least likely to close, still consuming attention a live deal needs. Give the reason in one sentence, tied to a fact from the data (age in stage, no next step logged, size mismatch with the account).
7. If a decision comes out of this review (kill a deal, reprioritize a rep's week), offer to log it to `memory/decisions.md` in the standard format, but only after the user confirms it.

## Output

A table plus four short sections, in this order:
• **By stage:** stage name, deal count, dollar total.
• **Stalled:** deal name, stage, days stuck, dollar value.
• **Biggest risk to the number:** one sentence, with the dollar figure.
• **Call this week, ranked:** three deals, each with the expected-value math shown.
• **Kill this one:** the deal name and the one-sentence reason.

## Rules

• Every number comes from the data given. If a deal's value or stage age is not in the source, say "not enough data" rather than guessing.
• The kill recommendation is a suggestion for the user's own pipeline hygiene, never an instruction that removes or edits their CRM. This skill only reads and reports.
• No email, call, or message goes out from this skill. It reports; the user acts.
• Log a decision to `memory/decisions.md` only after the user confirms it was actually made, not for every routine review.
