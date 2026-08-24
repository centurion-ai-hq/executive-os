---
description: Battle drill. Turns a correction into something that catches itself next time, writes it to the corrections log in the standard format, identifies the pattern behind the mistake, checks whether this same thing has been corrected before, and proposes a permanent handbook change once it has happened twice. Use when the user says "you did that wrong", "I already told you", "stop doing that", "lesson learned", "that is not what I asked for".
when_to_use: Fire this when the user says anything like "you did that wrong", "I already told you", "stop doing that", "lesson learned", "that is not what I asked", "you keep doing this", "we talked about this", "do not do that again", "you got that wrong".
---

# Lesson

Turns a correction into a rule that catches itself next time, instead of one more line nobody
remembers to check.

## When this fires

• The user corrects the assistant on something it got wrong.
• The user says "I already told you", "stop doing that", "lesson learned", "that is not what I
  asked for".
• A mistake repeats, or looks like a version of something that has happened before.

## What you do

1. State the correction precisely, one line: what the assistant did, and what it should have done
   instead.
2. Append it to `~/.claude/LESSONS.md` in this exact format, as a new line, never rewriting an old
   one: `<date> | <what went wrong> | <what should happen instead>`. If the file does not exist
   yet, create it with that one line.
3. Name the pattern behind the mistake, not just this one instance. A missed deadline because a
   date was never written down is an instance. "Commitments made out loud never get logged" is the
   pattern. The pattern is what actually needs fixing.
4. Search `~/.claude/LESSONS.md` for this same pattern under different wording. Read the file, do
   not rely on memory, corrections get phrased differently each time and a keyword match alone
   will miss most repeats.
5. If this is the first time this pattern has shown up, log it and stop there. One correction is a
   correction, not yet a rule.
6. If this exact pattern has now been corrected twice, propose a permanent change to the handbook,
   `~/.claude/CLAUDE.md` or the project's own CLAUDE.md, that would make the mistake structurally
   harder to repeat. Write the proposed line exactly as it would appear in the file. Do not edit
   the handbook yourself, only propose the change, since it governs every future session and the
   user should see it before it becomes permanent.

## Output

One consolidated report:

• **The correction:** what happened, what should happen instead, and confirmation it is logged.
• **The pattern:** the general shape of the mistake, in one sentence, not just this one case.
• **Repeat check:** first time, or the date it was corrected before.
• **Handbook proposal:** only on a second repeat, the exact line to add and where. Leave this
  section out entirely on a first-time correction.

## Rules

• `~/.claude/LESSONS.md` is append-only. Never edit or delete an existing line, even to tidy it.
• Never propose a handbook change on a first correction. One instance is not yet a pattern.
• Always search the actual file for prior instances before deciding it is the first time.
• The handbook edit itself is always the user's call. Propose the line, never write it into
  CLAUDE.md without being told to.
• Keep the pattern statement to one sentence. If it takes a paragraph, it is not a clean pattern
  yet, sharpen it first.
