---
description: "Assembles the board meeting packet as a styled, self-contained HTML document: an executive summary leading with what the board must decide, the numbers with the story behind them, risks stated honestly, and each requested decision written as a card with a recommendation and a deadline. Use when the user says 'build the board packet', 'prep the board meeting', 'board deck', 'put together the board materials', or a board meeting is coming up."
argument-hint: "[meeting date and topics]"
when_to_use: Fire this when the user says anything like "board packet", "board meeting", "board materials", "board deck", "prep the board", "what the board needs", "board update", "for the board".
---

# Board Packet

Builds the whole board meeting packet as one document, decisions first, detail behind them, so the
board can act instead of just reading.

## When this fires
• A board meeting is coming up and materials need assembling.
• The user says "build the board packet," "prep the board meeting," or "put together the board
  materials."
• The user has numbers, updates, and open decisions that need turning into one coherent document.

## What you do
1. Gather what exists: financials, program updates, any open decisions the executive wants the
   board to weigh in on. Ask for whatever is missing rather than filling a gap with a guess.
2. Write the executive summary first, and lead it with what the board must actually decide this
   meeting, not a recap of the last one. If there is nothing to decide, say that plainly.
3. Present the numbers with the story behind them: not just a balance, but why it moved. A number
   with no story is not useful to a board making a call.
4. State risks honestly. A packet that hides a risk to look better in the room fails the board's
   actual job, which is oversight.
5. Write every decision the board is being asked to make as its own card: the decision, a committed
   recommendation, the deadline it needs to be made by, and what happens by default if the board
   does not act.
6. Enforce the length ceiling: keep the front section, summary plus decision cards, short enough to
   read in one sitting. Move supporting detail, backup numbers, and full program reports into a
   clearly labeled appendix rather than cutting them.
7. Render the final packet as one self-contained, styled HTML file.

## Output
One self-contained HTML file: executive summary and decision cards up front, numbers with their
story, risks stated plainly, full supporting detail in an appendix. File path convention:
`board-packet-<meeting-date>.html` in the project's output folder.

## Rules
• Decisions go on the front page. Depth moves to the appendix, nothing gets cut to hit a length
  target.
• Every risk gets stated, not softened. A board that is not told the real risk cannot do its job.
• Every decision card carries a recommendation and a deadline. A card with neither is not finished.
• Ask before this packet is sent or shared with any board member. It is a draft document until the
  executive says otherwise.
• No em dashes. Bullets use •.
