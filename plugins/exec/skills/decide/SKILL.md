---
description: Turn any open decision into one committed recommendation card, never a menu of options. Use when the user says "what should I do", "what's the call", "help me decide", "should I do this", "which one do I pick", "make the call", or hands over a decision they've been sitting on.
---

# Decide

Give the one right call, with the number behind it, an expiry date, and what happens if nothing is decided.

## When this fires

• The user names a decision and asks what to do about it.
• A conversation has produced two or more options and stalled without a pick.
• The user says "what's the call", "should I do this", or "just tell me what to do".
• A decision has been sitting open across more than one session.

## What you do

1. Read the decision back in one line: what is being decided, and by when if a deadline exists.
2. If a real fact needed to decide is missing (a number, a date, a name), ask for it once. Do not guess at something checkable. If nothing checkable is missing, proceed.
3. Weigh the options against what the user has already said they want, not a generic best practice. Pick one. Never present a list of options as the answer.
4. Fill in every field of the card below. Do not skip the expiry field. A card without an expiry date is not a finished card, because an executive's real failure mode is a decision that never gets made, not a decision that turns out wrong.
5. Set the expiry to the soonest date the decision actually needs to be made by. If nothing forces a date, set one anyway: 7 days out is the default when no deadline is stated.
6. State the default: what happens automatically if the user does nothing by the expiry date. Every decision has a default, even if the default is "nothing changes and the cost keeps accruing."
7. After the user confirms the call (or you are told to log it as made), append one line to `memory/decisions.md` in this exact format:
   `2026-08-23 | DECISION | <what was decided> | <who decided> | undo: <how, or "one-way">`
   Use today's actual date. If `memory/decisions.md` does not exist yet, create it with that one line.

## Output

One card, in this exact shape, nothing before it and nothing after it except a one-line answer to any question you had to ask first:

• **Recommend:** committed, one sentence. "Do X."
• **Because:** the number or fact driving it. Not an adjective.
• **If you don't:** the specific consequence, and roughly when it lands.
• **Door:** two-way (what undoing it costs) or one-way (why it can't be undone).
• **Expires:** a real date, and what happens automatically if no decision is made by then.
• **Confidence:** certain / inference / best guess.
• **Watch:** what would flip this call. Leave this field out entirely if nothing would.

## Rules

• Never return a menu. If you catch yourself listing pros and cons for two options with no pick, stop and pick.
• Expiry is mandatory on every card. No exceptions, no "N/A".
• Label confidence honestly. If you are guessing, say "best guess" and say what would make it certain.
• Drafting the decision is free. Sending it, spending against it, or telling another person the number requires the user's explicit go-ahead first, every time.
• Log the decision to `memory/decisions.md` only after it is actually made, not when the card is first shown.
