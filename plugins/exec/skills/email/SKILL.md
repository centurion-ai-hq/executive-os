---
description: "Draft an email in the executive's own voice and park it as a draft; never sends. Use when the user says 'draft an email', 'write an email', 'email someone about', 'help me write to X', 'I need to send something to', 'reply to this', or 'compose an email'. Gathers the who/what/history, writes one clean draft, revises on feedback, and deposits to their email drafts folder if a connector is wired, or hands them the text to paste if not."
argument-hint: "[recipient] [topic or intent]"
---

# Email

Write one clean email draft, ready for the user to review and send themselves.

## When this fires
• The user wants an email written: "draft an email to X," "help me reply to this," "write to my
  contact about Y."
• A draft already exists and needs revising: "make it shorter," "warmer," "cut the second
  paragraph."
• Do NOT fire to actually send, forward, or reply to anything. That is a human's job, every time.

## What you do

1. **Gather what you need.** Who is this going to, and what is the relationship (client, staff,
   vendor, personal)? What outcome does the user want from this email? Is there prior history
   (a thread, a past conversation) that should shape the tone or content? Ask for whatever is
   missing, one question at a time, but do not ask about anything you can reasonably infer.
2. **Write one draft, not three options.** Subject line, greeting, body, sign-off. Lead with the
   point. Short paragraphs. No filler opener like "I hope this finds you well."
3. **Match the register to the relationship.** Warmer and more personal for someone the user knows
   well; more formal and structured for a first contact or a business matter. Never guess a name
   or a fact not given to you.
4. **State the word count.** Target 150 words, hard ceiling 200. If the draft needs to run longer
   to cover something concrete (a list of dates, a set of numbers), say why in one line rather than
   quietly blowing the ceiling.
5. **Revise on plain-language feedback.** "Shorter," "less formal," "add a question at the end,"
   "cut the third line." Rewrite to spec each time. Do not layer a second draft next to the first;
   replace it.
6. **Deposit once approved.** If an email connector is available in this session, create the draft
   in the user's drafts folder using the draft-creation tool only, never the send tool. If no
   connector is available, return the full draft text formatted for the user to copy and paste
   themselves.

## Output
One email draft: subject line, greeting, body, sign-off, and the word count stated at the bottom.
If deposited to a drafts folder, confirm the subject line and recipient back to the user. If handed
back as text, say plainly that no connector was available and this needs to be pasted in by hand.

## Rules
• This skill never sends, schedules a send, or auto-replies to anything. It drafts and parks.
  A human presses send, always.
• One draft at a time. The user asked for an email, not a menu of tones to choose between.
• Never assume the recipient or invent a fact about them. Confirm who this is going to before
  writing a word.
• No em dashes, no italics. Bullets use •. Never "absolutely," "certainly," "great question," or
  "of course."
• If a connector exists but the send tool is the only one available, stop and return the draft as
  text instead of risking a real send.
