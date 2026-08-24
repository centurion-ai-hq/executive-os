---
description: "Builds and maintains a running ledger of every recurring subscription and vendor charge: what it is, monthly and annual cost, who owns it, when it renews, and whether it is still used. Use when the user says 'what are we paying for', 'build the subscription list', 'what's renewing soon', 'audit our vendors', 'are we still using this', or pastes a list of charges or a card statement."
argument-hint: "[paste charges, statement, or vendor list]"
when_to_use: Fire this when the user says anything like "what are we paying for", "subscriptions", "recurring charges", "renewing soon", "what renews", "vendor charges", "monthly costs", "are we still using", "cancel anything", "our software costs".
---

# Spend Ledger

Builds and keeps a running list of every subscription and vendor charge, so nothing renews as a
surprise and nothing gets paid for out of habit.

## When this fires
• The user pastes a card or bank statement, a list of vendors, or a spreadsheet of charges.
• The user asks "what are we paying for," "what's renewing soon," "are we still using this," or
  "audit our subscriptions."
• A recurring monthly or quarterly check of standing spend.

## What you do
1. Read the existing ledger at `memory/spend-ledger.md` if it exists. This run updates it, it does
   not start over.
2. Extract every recurring charge from the new input: name, monthly cost, billing cycle, and the
   next renewal date if it is stated or inferable.
3. For each line, mark who owns it (who requested or uses it) only if that is stated or already
   known. Otherwise mark "owner unverified." Never guess an owner to fill the cell.
4. Mark whether it is actually used. If usage is not in the data provided, mark "usage unverified"
   rather than assuming it is active just because it is being charged.
5. Merge into the ledger: update existing lines, add new ones, never silently drop a line that
   stopped appearing in this input, flag it instead as "not seen this pass, confirm still active."
6. Calculate the monthly total and the annualized total across every line.
7. Pull out everything renewing inside the next 30 days into its own list at the top of the output.
8. Write the updated ledger back to `memory/spend-ledger.md`, one line per vendor.

## Output
1. Renewals in the next 30 days, first, with dollar amounts.
2. Full ledger table: vendor, what it is, monthly cost, annual cost, owner, renewal date, used
   (yes / no / unverified).
3. Monthly total and annual total.
File path: `memory/spend-ledger.md`.

## Rules
• Flag anything unverified rather than assuming it is fine. An unverified owner or unverified usage
  is a finding, not a gap to paper over.
• Never mark something cancelled or removed on your own authority. Cancelling a subscription spends
  or saves the organisation's money, so it needs the executive's say-so first.
• Never invent a renewal date. If it is not stated, mark "date unknown, confirm with vendor."
• This is append-and-update, never a full rewrite that could erase history. Keep prior entries
  unless the executive confirms a vendor is gone.
• No em dashes. Bullets use •.
