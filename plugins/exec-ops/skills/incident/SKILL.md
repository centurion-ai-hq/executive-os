---
description: Produces the honest account of what went wrong, the timeline, the real cause versus what got blamed, who was affected, and the fix that stops it recurring. Use when the user says "write up what happened", "do an incident report", "we need to explain this to the client", "post-mortem this", or something has broken and needs a clean written account.
when_to_use: Fire this when the user says anything like "write up what happened", "incident report", "post mortem", "what went wrong", "explain this to the client", "we messed up", "root cause", "it broke", "outage", "how do we explain this".
---

# Incident Report

Writes the honest account of what broke, why it actually broke, and what changes so it doesn't happen again.

## When this fires

• Something went wrong, an outage, an error, a missed commitment, a data problem, and needs a written account.
• The user says "write up what happened", "do a post-mortem", "we need to explain this to the client or board".
• A cause is being assumed or blamed without having actually been checked.

## What you do

1. Gather what is actually known: what happened, when it was noticed, who reported it, and any logs, messages, or records available. Do not start writing from assumption.
2. Build a timeline: what happened and when, in order, using timestamps where they exist. Mark any gap where the exact time isn't known rather than inventing one.
3. Separate what actually caused the problem from what got blamed for it. These are often different. State the real cause only if it is evidenced by something concrete (a log, a message, a specific action); otherwise say the cause is unconfirmed and name what would confirm it.
4. List who was affected and how, specific enough to be useful (which clients, how many users, what they experienced), without exposing anything the user hasn't cleared for a wider audience.
5. State what was done in response, in the order it was done, including anything that did not work before the actual fix was found.
6. Name the one specific change that stops this from recurring. It must be a concrete action, a check added, a step removed, a person now confirming something, not a vague intention like "we'll be more careful."
7. Write the whole thing so it could be read by a board or a client without embarrassment: honest about the mistake, specific about the fix, no defensive language, no invented cause to make the story tidier.

## Output

Five sections, in order: What happened, Timeline, Real cause (versus what was assumed or blamed), Who was affected, What changes now. Plain prose, short paragraphs, no jargon.

## Rules

• Never state a cause that isn't evidenced. "Unconfirmed" is an honest answer; a guessed cause dressed up as fact is not.
• Name what actually changes, not an intention. A fix with no specific mechanism isn't a fix.
• This document may go to a client or a board. It is a draft until the user reviews it; the user decides who receives it and sends it themselves.
• No blame language directed at a named individual unless the user explicitly confirms that's accurate and wants it included.
