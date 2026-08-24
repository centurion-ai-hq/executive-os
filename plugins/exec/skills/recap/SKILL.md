---
description: "Turn a meeting transcript, recording, or rough notes into a commitment ledger, a read on what the other side actually wants, a clean recap, and a drafted follow-up email. Use when the user says 'here's the transcript', 'we just met with', 'recap this meeting', 'what did we agree to', 'summarize this call', or pastes an Otter export, meeting notes, or a recording transcript. Never sends anything."
argument-hint: "[paste transcript or notes]"
---

# Recap

Turn a meeting into a written record so nothing said in the room quietly disappears.

## When this fires
• The user pastes or hands over a transcript, recording text, or rough meeting notes.
• The user says "what did we agree to," "recap that call," "what's the follow-up," or "who owes
  what from that meeting."
• Do NOT fire to grade the user's own performance in the meeting; that is a different job. This
  skill is about what was said and what happens next, not how well the user did.

## What you do

1. **Untangle who said what.** Transcripts, especially auto-generated ones, mislabel or drop
   speaker tags. Work out attribution before drafting anything. Where it is genuinely unclear who
   said something, leave it unattributed rather than guess.
2. **Build the commitment ledger.** Pull every specific commitment made by anyone in the meeting:
   a completed sentence with a person, an action, and ideally a date. "We should look into pricing"
   is not a commitment. "Sarah will send the contract by Friday" is. Number each one.
3. **Read what the other side actually wants.** Underneath what they said, what is the real
   priority or concern driving it? Base this only on what is in the transcript, and label it as a
   read, not a fact: "this reads as..." rather than a flat assertion.
4. **Write the clean recap.** A short, plain-English summary the user could send to the other
   party as-is: what was discussed, what was decided, what's still open. No transcript dump, no
   play-by-play. Half a page, not a chronology.
5. **Draft the follow-up email.** Short, matches the user's voice if `memory/voice-profile.md`
   exists (check with the `voice` skill), states the single next step clearly, points at the recap
   rather than repeating it.
6. **Write every commitment to the board.** Append each ledger item to `memory/board.md` as a
   checklist line with owner and date: `- [ ] <commitment>, owner: <name>, due: <date or "not
   given">`. Create the file if it does not exist.

## Output
Four things, in this order:
1. Numbered commitment ledger (owner, action, date).
2. What they actually want (labeled as a read, not a fact).
3. Clean recap, half a page or less.
4. Follow-up email draft (subject + body).

## Rules
• Never invent a commitment, a date, or an owner that was not in the source material. Write
  "owner not named" or "no date given" instead of filling a gap to look complete.
• Keep "what they said" and "what was committed to" in separate sections. Blending them turns an
  honest record into a pitch.
• This skill never sends the recap or the email. It hands both back as drafts. A human sends.
• If nothing was actually decided in the meeting, say that plainly rather than dressing up
  discussion as decisions.
• No em dashes, no italics. Bullets use •.
