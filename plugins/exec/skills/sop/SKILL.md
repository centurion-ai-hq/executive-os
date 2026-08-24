---
description: "A repeatable process written down so a different person could run it unaided. Not a one-off document. Use when the user says 'write an SOP', 'turn this into a procedure', 'document this process', 'make a checklist for X', or a task needs to survive the person who currently does it being unavailable."
argument-hint: "[the process to document]"
when_to_use: Fire this when the user says anything like "turn this into a procedure", "write an sop", "document this process", "so someone else can do it", "how we do this", "standard operating", "repeatable", "hand this off to someone", "train someone on this", "write down how".
---

# SOP

Turns a process that only exists in someone's head into a written procedure a new person could follow on their own.

## When this fires
• The user says "write an SOP", "document this process", "turn this into steps", or "make a checklist for X".
• A task needs to survive the person who currently does it being unavailable.
• A new hire or a teammate needs to run something without asking questions first.

## What you do
1. Confirm in one line what process is being documented and who does it today.
2. Interview one question at a time. Ask, wait for the answer, confirm you understood it, then ask the next question. Never dump a list of questions at once. Cover, in this order: the trigger (what starts this), the steps in order, the decision points (anywhere the path branches, and what decides which way), what "done" looks like, the most common way this goes wrong and its fix, and who owns it today.
3. If an answer is vague, ask a follow-up before moving on. Never guess at a step and write it down as fact.
4. If you must infer a likely step because the user skipped it, mark it in the draft as `[unconfirmed, please check]` rather than stating it as settled.
5. Draft the procedure in this order: title, owner, trigger, numbered steps (write any branch as "if X, do Y, otherwise do Z"), definition of done, the common failure and its fix, and a one-line revision log with today's date.
6. Run the day-one test before showing it: read the draft as if you are a brand-new hire with no other context. If a step assumes knowledge that was never stated, add it or flag it.
7. Build it as one self-contained HTML file: one typeface, light background, generous white space, no external stylesheets or scripts, so it opens and prints anywhere.
8. Save to `documents/<procedure-slug>.html` and tell the user the path, plus any `[unconfirmed, please check]` steps still needing their eyes.

## Output
One HTML procedure document with title, owner, trigger, numbered steps, definition of done, common failure and fix, and a revision log, saved at `documents/<procedure-slug>.html`.

## Rules
• One question at a time. Never a questionnaire dump.
• Never state an inferred step as fact. Flag it and let the user confirm or correct it.
• Test every draft against the day-one question before calling it finished: could a new hire run this from the document alone.
• No em dashes. Bullets use •.
• Ask first before sending or publishing this document to anyone outside this session.
