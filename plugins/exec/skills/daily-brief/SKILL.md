---
description: "Produces the one-page morning read as a self-contained HTML file: a one-line bottom line, today's schedule with one-line prep, up to five replies that actually matter ranked by consequence, deadlines inside 7 days, and the top three things to do today. Use when the user says 'daily brief', 'morning brief', 'what's on my plate today', 'bring me up to speed', 'catch me up', or starts a session wanting the full picture before diving in. Read-only, never sends or accepts anything."
argument-hint: "[optional: date or focus area]"
when_to_use: Fire this when the user says anything like "what is on my plate today", "morning brief", "daily brief", "bring me up to speed", "catch me up", "what is today", "start my day", "what is happening today", "my day", "this morning", "before my first meeting", "brief me".
---

# Daily Brief

The one page she opens every morning to see what's actually true today, before anything else.

## When this fires
• The user says "daily brief," "morning brief," "what's on my plate," or "bring me up to speed."
• The start of a work session, when she wants the full picture before diving into anything else.
• Do NOT fire to draft a reply to something in the brief. That's a separate drafting task.

## What you do
1. Work out today's date and the file path: `briefs/<YYYY-MM-DD>.html` in the working folder.
   Create the `briefs/` folder if it does not exist yet.
2. Pull today's calendar from whatever calendar connector is wired up: title, time, attendees,
   location or video link for each event. If the connector is missing, unauthenticated, or errors,
   write one plain line saying so instead of a schedule. Do not leave the section silently empty.
3. Write one prep line per meeting: who's in the room and the single most useful thing to do
   beforehand. Say plainly when this is a guess from the title and attendee list, not confirmed.
4. Pull mail from roughly the last day from whatever email connector is wired up, skipping
   newsletters and promotions. If that connector is missing or errors, say so in one line instead
   of a list.
5. Rank the mail by consequence, not recency: an active back-and-forth beats a one-off send, a
   sender she has replied to before beats a stranger, a deadline word ("today," "urgent," "due,"
   "respond by") moves it up. Keep the top 5 only. If nothing needs a reply, say that in one line.
6. Scan the ranked mail and the calendar for anything due inside 7 days. If nothing turns up,
   leave the whole section out of the page. Never write "none" where a section would go.
7. Read `memory/board.md` if it exists and fold its live priorities into the picture.
8. Pick the top three things to do today from the calendar, the ranked mail, the deadlines, and
   the board. Never more than three. If more compete for the spot, rank and cut; don't list them all.
9. Write the one-line bottom line for the top of the page: what today actually is, in one sentence,
   for example "Three meetings, one decision owed, and the Brightline renewal expires Friday."
10. Build the page as one self-contained HTML file (see Output) and save it to the path from
    step 1. Then tell her the path, in one line, and nothing else in chat.

## Output
One self-contained HTML file at `briefs/<YYYY-MM-DD>.html`. Inline CSS only, one typeface, a light
warm background, one accent color used sparingly for headings, small labels, and rules. No dark
background, no charts, gauges, progress bars, emoji, or decorative icons. Nothing marked important
by color alone; it has to read correctly printed in black and white, and print cleanly to PDF from
a browser. Aim for one laptop screen, no scrolling, where the content allows it.

In this order, and nothing else:
1. The bottom line, one sentence, at the very top.
2. Today's schedule: each meeting's time, who, and one line of prep.
3. Replies that matter: up to 5, ranked, each one line (who, what they want, what happens if it
   waits). One line saying none are needed if that's true.
4. Deadlines inside 7 days: a short table (date, what's due, source). Section removed entirely,
   not filled in, when there's nothing to show.
5. The three things to do today, numbered, with the reason on the same line.
6. A footer line naming exactly what was and wasn't connected this run, plus the true word count,
   for example "347 words. Calendar connected. Email not connected."

400 words is the absolute ceiling for the page, footer included. Count it for real, every time.

## Rules
• Read-only, always. Never sends, replies, drafts, accepts, declines, or marks anything read on
  any connector. If a step is about to touch one of those, stop and report the brief without it.
• A missing connector and an empty section are different facts and must never look the same: say
  "not connected" for the first, remove the section entirely for the second.
• Never invent a meeting, an email, or a deadline. If the source doesn't have it, it doesn't go on
  the page.
• Numbers over adjectives: "3 replies needed, 1 due today," not "a few important emails."
• Never more than 5 emails, never more than 3 priorities. More candidates means ranking harder,
  not listing more.
• No em dashes. Bullets use •. Define any technical term the first time it appears.
• Every day's brief accumulates in `briefs/`, roughly 30 days of history for looking back. Never
  delete an old one without being asked.

## Getting it every morning without asking

Claude Code can schedule this itself. There is no cron, no terminal, and nothing to install.

**To turn it on**, the executive says, in their own words:

> "Run my morning brief every weekday at 7am."

That creates a scheduled task stored at `~/.claude/scheduled-tasks/morning-brief/SKILL.md`.

**Three things to tell them plainly when setting it up, because all three surprise people:**

1. **The schedule runs in their local time**, not UTC. 7am means 7am where they are.
2. **It only runs while the app is open.** If the app is closed when 7am passes, the brief is
   generated the next time they open it. For a morning brief this is usually what they want: they
   open the laptop and it is already waiting. Say it out loud anyway so it is never a surprise.
3. **Each run starts with no memory of any conversation.** The scheduled prompt has to carry
   everything it needs on its own: which connectors to read, the output path, the format, and the
   length ceiling. Never write a scheduled prompt that refers to "the usual" or "as we discussed".

**Write the scheduled prompt self-contained.** It must name: the connectors to read, the file to
write, the five sections in order, the 400-word ceiling, the read-only boundary, and the honest
degrading rule. A short scheduled prompt produces a different brief every day, which is the one
outcome that makes them stop trusting it.

**To change or stop it**, they say "change my morning brief to 6:30" or "stop the morning brief".
Never edit the task file by hand on their behalf without telling them.
