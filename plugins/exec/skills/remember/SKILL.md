---
description: "Storing a fact, ruling, price or preference permanently. Not the state of work in progress. Use when the user says "remember this", "don't forget", "make a note of that", "from now on", "always do X", "never do Y", "I decided", "that's confirmed", "we're going with", "stop doing that", or states any ruling, price, date, name, or preference worth keeping."
when_to_use: Fire this when the user says anything like "remember this", "do not forget", "make a note", "from now on", "always do", "never do", "i decided", "that is confirmed", "we are going with", "locked in", "note that", "keep that in mind", "for the record", "going forward".
---

# Remember

Anything the user says once should not have to be said twice. This writes it down in the right
place, in a form that gets read back automatically at the start of every future session.

## When this fires

• The user makes a decision, states a price, sets a date, or names a person or company
• The user corrects something you did, or tells you to stop doing it
• The user states a standing preference: "from now on", "always", "never"
• Any session where a ruling was made and has not yet been written down

Fire this the moment it happens, not at the end of the turn. A decision that lives only in the chat
window is already lost.

## What you do

**Step 1. Decide which of the four memories it belongs in.** One home, never two.

| It is... | Goes in | Behaviour |
|---|---|---|
| How they want you to work, always | `~/.claude/CLAUDE.md` | The handbook. Read at the start of every session. |
| A correction: you got something wrong | `~/.claude/LESSONS.md` | Append only. Never rewritten, never trimmed. |
| A fact, ruling, price, date, or name | `memory/decisions.md` | Append only. One line per entry. |
| What is open and what is next | `memory/board.md` | Rewritten whenever priorities move. |

If it is a fact that changes over time (a price, a status, a role), it goes in `decisions.md` as a
new line with today's date. The newest line wins. Never edit the old line, because the history of
how a decision moved is often the useful part.

**Step 2. Write it in the standard format.** For `memory/decisions.md`:

```
YYYY-MM-DD | DECISION | what was decided | who decided it | undo: how, or "one-way"
```

For `~/.claude/LESSONS.md`:

```
## YYYY-MM-DD: <one line title>
**What happened:** <the mistake, in one sentence>
**The rule now:** <what to do instead, stated as an instruction>
```

**Step 3. Convert anything relative into something absolute.** "Next Tuesday" becomes the date.
"Him" becomes the person's name. "That price" becomes the number. A memory that only makes sense
inside this conversation is not a memory.

**Step 4. Check for a memory that already covers it.** If one exists, update it rather than adding
a second. Two memories that disagree are worse than none, because you will not know which is live.

**Step 5. Confirm in one line.** Say what you wrote and where, so the user can see it landed.

**Step 6. Delete what turns out to be wrong.** When a memory is proven false or superseded, remove
it and say so. A stale memory is a liability, not a record.

## Output

One line: what was written, which file, and the exact text. Nothing else. This should be almost
invisible, not a ceremony.

## Rules

• Write it the moment it is said, not at the end of the turn.
• One home per fact. Never write the same thing to two files.
• Never store a password, an API key, a card number, or a government ID in any memory file.
• Never record something the user said as a decision when they were only thinking out loud. If it
  is genuinely unclear, ask in one line: "Is that a ruling, or still open?"
• Corrections are append-only. Never tidy, compress, or rewrite the lessons file.
• Memory files are read back automatically. Keep every entry short enough to survive that.
