---
description: "Everything open, ranked, with what to do next and what is dropped. Not one single decision. Use when the user says "what should I do first", "what's on my plate", "reprioritize", "what's open", "where are we", "what do I owe people", "what am I forgetting", "add this to the list", or when several competing tasks land at once and something has to give."
when_to_use: Fire this when the user says anything like "what should I do first", "what is on my plate", "what matters most", "reprioritize", "re prioritise", "what is open", "where are we on everything", "what do I owe", "what am I forgetting", "add this to the list", "I am underwater", "what actually matters", "too much going on", "what can wait", "what should I drop", "my list", "the board", "my plate", "what should I be doing", "what do I do now", "what is next", "where do I start".
---

# Priorities

One live list of everything on your plate, ranked by what actually matters, kept current without
you having to maintain it. Ask it what to do next and it tells you, with the reason.

## When this fires

• The user asks what to do first, or what is on their plate
• Something new lands that has to be slotted against everything already open
• The user asks what is still open, what they owe someone, or what they are forgetting
• The start of a working session, to re-ground before anything else happens

## What you do

**Step 1. Read the board.** Open `memory/board.md`. If it does not exist, create it. Never rebuild
it from your memory of the conversation. The file is the truth, the conversation is not.

**Step 2. Re-derive status, do not trust the label.** For each item, check whether it is actually
still open. If the thing it was waiting on has happened, or the deadline has passed, or the work
was done earlier in this session, say so and move it. Items marked open that are already finished
are the fastest way for the board to lose the user's trust.

**Step 3. Rank on consequence, not on noise.** Sort by these, in order:
1. It is blocking another person right now
2. It has a hard external deadline inside 7 days
3. It gets worse or more expensive the longer it waits
4. It unlocks the most other work
5. Everything else

Loud is not the same as important. Say plainly when the loudest item is not the top item.

**Step 4. Name what gets dropped.** If there is more on the board than the week can hold, do not
quietly reorder. Say which items are not getting done and recommend killing or deferring them
explicitly, with the cost of each. An honest short list beats a complete list nobody finishes.

**Step 5. Give every open item an expiry.** Anything with no date gets one, plus what happens
automatically if the user says nothing by then. Decisions rot far more often than they go wrong.

**Step 6. Write the board back.** Rewrite `memory/board.md` in full with the new order and the
new statuses. This file is meant to be rewritten, unlike the decisions log, which is append-only.

## Output

Three short sections, in this order:

**Do these three today.** Numbered, one line each, with the reason in the same line.

**The board.** A table: `ID | Item | Status | Owner | Waiting on | Expires`.

**Not getting done.** What is being dropped or deferred, and what that costs. Delete this section
entirely if the week genuinely fits. Never write "none" in it.

## Rules

• The file is the source of truth. Read it before you speak, write it after you decide.
• Never mark something done without evidence. "It looks finished" is not evidence.
• Every item carries a recommendation, even when no action is possible today. A bare list of open
  items with no guidance is the user's job handed back to them.
• Never let the board grow past what a person can read. Over about twenty live items, force a cull
  and say you are doing it.
• Never delete an item silently. Move it to a closed section at the bottom with the date and why.
