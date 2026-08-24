---
description: "Saving the state of work in progress before stopping. Not a standing fact to remember. Use when the user says 'I have to go, save my place', 'let's pick this up later', 'where were we', or a new session needs to catch up on what already happened."
when_to_use: Fire this when the user says anything like "save my place", "i have to go", "pick this up later", "pick this up tomorrow", "where were we", "continue where we left off", "running out of time", "stop here for now", "come back to this", "wrap up for today".
---

# Handoff

Saves exactly where things stand so the next session, or the next person, can pick up clean instead of re-explaining everything from scratch.

## When this fires
• The user says "I have to go, save my place", "let's pick this up later", or "save where we are".
• A session is ending, running low on time, or about to be handed to someone else.
• A new session is starting and needs to catch up on what already happened.

## What you do
Work out which half you're in before doing anything.

### Closing a session (save)
1. Write `memory/state.md`, fully replacing whatever was there before, with exactly these five things: what we were doing, what got finished and how you know (a file, a number, a result, not just a claim), what's still open and what each open item is waiting on, the single next action stated specifically enough to start cold, and any decision still owed by the user, named plainly.
2. Any ruling made this session, a price agreed, a date set, a yes to go ahead, a name chosen, gets appended as one line to `memory/decisions.md` in this exact format: `<date> | DECISION | <what was decided> | <who decided> | undo: <how, or "one-way">`. Do this even if nobody asked. A decision that isn't written down gets re-decided from zero next time.
3. Tell the user in one line that their place is saved, plus the single next action, so they know it worked without opening a file.

### Opening a session (resume)
1. Read `memory/state.md`. If it doesn't exist, say so plainly and start fresh rather than guessing at history.
2. Before doing anything else, restate your understanding back in five lines or fewer: what we were doing, what's done, what's open, the next action, and anything you need from the user first.
3. If anything in state.md looks stale, an old date, a next action that no longer makes sense, check with the user before acting on it.

## Output
Either an updated `memory/state.md`, with lines appended to `memory/decisions.md` where a ruling was made, or a five-line restatement read back to the user at the start of a session.

## Rules
• `memory/state.md` is always fully rewritten, never appended to. It describes right now.
• `memory/decisions.md` is always appended to, never rewritten or trimmed.
• Never mark something "finished" without saying how you know.
• If nothing got done this session, say that plainly instead of padding the file.
• This skill only reads and writes local files in the project folder. It never sends anything to anyone.
