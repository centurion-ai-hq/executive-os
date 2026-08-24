---
description: "Captures how the executive actually writes and speaks, then checks any draft against it. Use when the user says 'learn my voice', 'build my voice profile', 'here's how I write', pastes writing samples, or asks 'does this sound like me', 'check this against my voice', 'rewrite this in my voice'. BUILD mode interviews and analyses samples to write memory/voice-profile.md. CHECK mode scores a draft against that profile and rewrites what misses."
argument-hint: "[build | check] [optional: text to check]"
---

# Voice

Make sure anything written on the user's behalf actually sounds like them, not like a machine.

## When this fires
• No voice profile exists yet, or the user wants to build or update one: "learn how I write,"
  "here are some emails I've sent," "build my voice profile."
• A draft exists and the user wants it checked: "does this sound like me," "fix the tone," "make
  this sound like I wrote it."
• Any other skill in this kit needs to write outward-facing copy and a voice profile already
  exists at `memory/voice-profile.md`.

## What you do

### BUILD mode
1. Check whether `memory/voice-profile.md` already exists. If it does, tell the user what is in
   it and ask whether this is a refresh or a rebuild, rather than silently overwriting it.
2. Get real material to learn from: either paste-in writing samples (aim for 5 or more: emails,
   messages, notes, anything they actually wrote) or a short interview if no samples exist yet.
   Interview questions, asked a few at a time: How do you usually open a message? How do you
   close one? Do you use bullet points or full paragraphs? Formal or casual, and does that change
   with who you're writing to? Any words or phrases you use constantly? Any you can't stand?
3. Analyse the samples for pattern, not content: average sentence length, how often bullets appear
   versus prose, how directly they get to the point, favorite words and phrases, words they never
   use, how formal they are with staff versus clients versus strangers, how they open and close.
4. Write `memory/voice-profile.md` with these sections: Sentence rhythm, Words used often, Words
   never used, Opening lines, Closing lines, Formality by audience, Hard bans. Every claim in the
   profile should trace back to something in the samples or the interview, never a guess.
5. Confirm the file location back to the user and summarise the profile in five lines or fewer.

### CHECK mode
1. Read `memory/voice-profile.md`. If it does not exist, say so and offer to run BUILD mode first;
   do not guess at a voice with nothing to check against.
2. Score the draft against the profile: sentence rhythm, banned words present, formality mismatch
   for the stated audience, missing or wrong-feeling open/close.
3. List what misses, each tied to the profile section it violates, then rewrite the parts that
   miss. Leave what already sounds right alone rather than rewriting the whole draft on principle.

## Output
BUILD mode: `memory/voice-profile.md` written or updated, plus a five-line summary in chat.
CHECK mode: a short findings list (what missed, and why), followed by the corrected draft.

## Rules
• The profile only shapes how something is said. It never licenses inventing a fact, a number, or
  a claim the user did not give you.
• A profile built from fewer than 3 samples and no interview is too thin to trust. Say so and run
  the interview instead of producing a confident guess.
• Never send or publish anything checked or rewritten here. This skill only reads, writes to
  `memory/voice-profile.md`, and returns text.
• No em dashes, no italics, bullets use •, in this skill's own output and in what it checks for.
