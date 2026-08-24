---
description: "Lists outstanding invoices with their age and value, then drafts a follow-up message at the right escalation level (gentle nudge, firm reminder, final notice) for each. Use when the user says 'who owes us money', 'chase this invoice', 'run collections', 'follow up on unpaid invoices', 'aging report', or pastes an accounts-receivable export. Drafts only, never sends."
argument-hint: "[paste accounts-receivable or invoice list]"
---

# Collections

Turns a list of unpaid invoices into a clear picture of what is owed and a drafted follow-up for
each one, pitched at the right tone.

## When this fires
• The user pastes an accounts-receivable export, an invoice list, or asks "who owes us money."
• The user says "chase this invoice," "run collections," "follow up on unpaid invoices," or "aging
  report."
• A regular sweep of what is outstanding before it gets older and harder to collect.

## What you do
1. Read the prior state at `memory/collections.md` if it exists, so escalation level per invoice
   carries over instead of resetting to "gentle" every run.
2. List every outstanding invoice: client name, amount, invoice date, days outstanding, and how
   many follow-ups have already gone out for it.
3. Set the escalation level by age and history, not by amount alone: a first touch under 30 days is
   a gentle nudge, 30 to 60 days with no response is a firm reminder, past 60 days or a second
   unanswered reminder is a final notice.
4. Draft one message per invoice at its level. Gentle: warm, assumes an oversight, no pressure.
   Firm: clear about the amount and the date, still respectful. Final notice: states the amount, the
   history of prior contact, and what happens next (a specific next step, not a vague threat).
5. For a client worth preserving the relationship with, say so and pull the tone down a notch even
   at a higher escalation level. Name when a relationship is not worth preserving and the tone can
   be direct.
6. Update `memory/collections.md` with today's date and escalation level per invoice, so the next
   run knows where each one stands.

## Output
An aging table (client, amount, days outstanding, escalation level), then one drafted message per
invoice, clearly labeled by client and level. File path: `memory/collections.md`.

## Rules
• Every message is a draft. This skill never sends an email, a text, or any message on its own. A
  human sends.
• Never invent an amount, a date, or a prior contact that is not in the data or the ledger.
• Preserve the relationship where it is worth preserving; say plainly when it is not, and why.
• Ask before treating any invoice as uncollectible or writing it off. That is a financial call, not
  a drafting one.
• No em dashes. Bullets use •.
