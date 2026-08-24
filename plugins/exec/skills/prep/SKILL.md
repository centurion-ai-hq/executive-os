---
description: "Prepare the executive for a meeting or call before it happens: research the people and the organization, pull every prior commitment and decision involving them, state the outcome worth wanting, and predict the three most likely objections with an answer to each. Use when the user says 'I have a call with', 'prep me for', 'meeting with X tomorrow', 'what do I need to know before', or 'pitch to'. Produces a one-page prep sheet readable in five minutes."
argument-hint: "[who and what the meeting is about]"
---

# Prep

Walk into the room already knowing the room, in five minutes of reading or less.

## When this fires
• The user names an upcoming meeting or call: "I have a call with X tomorrow," "prep me for the
  board meeting," "what do I need to know before meeting Y."
• Do NOT fire after a meeting has already happened; that is the `recap` skill's job.
• Do NOT use this to decide whether the meeting is worth taking at all. This skill assumes the
  meeting is happening and prepares for it.

## What you do

1. **Read the meeting itself.** Who is attending, what is the stated purpose, how long is it. If
   the purpose is unclear, say so as the first line of the prep sheet rather than guessing at one.
2. **Pull what is already settled, before researching anything new.** Search
   `memory/decisions.md` and `memory/board.md` for every prior ruling, commitment, price, or date
   involving these people or this organization. A prep sheet that ignores prior history risks
   re-opening something already agreed.
3. **Research the room.** Who are the people, what is the organization, what is publicly known
   about their situation right now that bears on this meeting. Keep it to what is actually
   relevant, not a biography.
4. **State the outcome worth wanting.** One line: what does a genuinely good result from this
   meeting look like, stated as an outcome, not a hope. "They confirm the Thursday date and name a
   budget" beats "the meeting goes well."
5. **Predict the three likely objections or pushbacks**, ranked by how likely each is, each paired
   with a specific answer. Base these on what is known about the other side's stated priorities and
   any prior friction on record, not on generic sales objections.
6. **Assemble the one-page sheet.** It has to be readable start to finish in five minutes. Cut
   anything that is interesting but not decision-relevant to this specific meeting.

## Output
A single prep sheet, in this order:
• **Who's in the room:** names, roles, one line each on what matters about them here.
• **What's already on record:** prior commitments or decisions involving them, with dates.
• **The outcome worth wanting:** one line.
• **Likely pushback:** three objections, ranked, each with an answer.
• **One thing to watch:** the single biggest risk this meeting could go sideways on, if there is
  one.

## Rules
• Never put a number or a promise in the prep sheet that has not actually been decided. If a price
  or commitment is still open, flag it as open rather than stating it as settled.
• Do not re-argue a decision already on record. If new information genuinely contradicts a past
  ruling, flag it in one line rather than rewriting the position in the prep sheet.
• A prep sheet longer than one page defeats its own purpose. Cut prose before cutting the
  objections or the outcome line.
• This skill only reads and writes the prep sheet. It never contacts anyone named in it.
• No em dashes, no italics. Bullets use •.
