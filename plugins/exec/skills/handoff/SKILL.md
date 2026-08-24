---
description: "Saving the state of work in progress before stopping. Not a standing fact to remember. Also reads that state back cleanly when picking up, including on a different machine or app. Use when the user says 'save my place', 'I have to go', 'let us pick this up later', 'where were we', 'continue where we left off', 'I am switching to the desktop app', or a session is ending with work unfinished."
when_to_use: Fire this when the user says anything like "save my place", "i have to go", "pick this up later", "pick this up tomorrow", "where were we", "continue where we left off", "running out of time", "stop here for now", "come back to this", "wrap up for today".
---

# Handoff

Saves exactly where things stand so the next session starts knowing, instead of asking. Works
across a break, across a day, and across a change of machine or app.

## When this fires

• The user is stopping and work is unfinished
• The user is moving to a different app, machine, or window
• A new session is starting and there is a saved state to pick up
• The session has run long and is about to lose its own context

## What you do: saving

**Step 1. Freeze what is true, not what you remember.** Before writing anything, check the actual
state: which files exist, what the board says, what was actually finished. Do not write a summary
from the conversation. The conversation is where things get quietly overstated.

**Step 2. Write `memory/state.md`, replacing it entirely.** Six headings, in this order:

```
## Where we are
One paragraph. What we were doing and why. Written for someone who was not here.

## Done, and how I know
Each item with its proof: a file that exists, a command that passed, a thing that was seen.
Never list something as done on the strength of it having been discussed.

## In flight
What was mid-way through when we stopped, and the exact next action to resume it.

## Waiting on
Anything blocked, who or what it is blocked on, and since when.

## Decisions you owe
Each one with a recommendation attached, so it can be answered in one word.

## Where the files are
The working folder, and the absolute path of anything that matters.
```

**Step 3. Capture the perishable things.** Any decision, price, date, name or commitment from this
session goes to `memory/decisions.md` now, not later. A ruling that exists only in a chat window
is already lost.

**Step 4. Say where to resume, in one line.** The folder path and the sentence to say next. If the
user is switching machines or apps, print the folder path on its own line so it can be read off a
screen or a phone.

## What you do: picking up

**Step 5. Read before speaking.** Open `memory/state.md`, `memory/board.md`, and
`~/.claude/LESSONS.md`. Never ask the user to re-explain something that is written down.

**Step 6. Restate in five lines, then stop.** Before doing any work, say back: what we were doing,
what is done, what is in flight, what is blocked, and the one next action. Ask the user to confirm
or correct it. A session that starts by acting on a misread state wastes more time than one that
starts by asking.

**Step 7. If the state file is stale, say so.** Check whether what it claims is still true. Work
may have happened elsewhere, or the thing it is waiting on may already have arrived.

## Output

When saving: a six-line confirmation of what was written, the folder path on its own line, and the
sentence to say when resuming. Nothing else.

When resuming: the five-line restatement, then wait.

## Rules

• Verify before writing. "Done" needs evidence, not recollection.
• Replace `memory/state.md` in full. It is a snapshot, not a log. The log is `decisions.md`.
• Never write the setup marker file during a handoff. If setup was unfinished, it must resume.
• Never lose an unanswered question. Anything the user owes goes under "Decisions you owe" with a
  recommendation, so it can be closed in one word.
• Keep it short enough to be read. A handoff nobody reads is a handoff that did not happen.
