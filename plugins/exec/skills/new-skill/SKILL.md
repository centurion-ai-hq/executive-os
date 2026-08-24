---
description: "Turns something the user keeps asking for by hand into a permanent skill that fires on one phrase from then on, tested live before it ships. Use when the user says 'I keep asking you for this', 'make this a standing thing', 'turn this into a skill', 'can you just remember to do this', or repeats the same kind of request for the second or third time."
argument-hint: "[the task you keep repeating]"
when_to_use: Fire this when the user says anything like "turn this into a skill", "i keep asking you", "make this a standing thing", "every time i ask", "same thing again", "can you just remember to do this", "save this as something", "make this automatic", "do this every time".
---

# New Skill

Turns something the user keeps asking for by hand into a permanent skill that fires on one phrase from now on.

## When this fires
• The user says "I keep asking you for this", "make this a standing thing", "turn this into a skill".
• The same kind of request has come up two or three times already.
• The user wants a repeated task to trigger automatically instead of being explained again each time.

## What you do
1. Ask briefly, one question at a time: what is the repeated task, in their own words, and what does a good result look like. An example of past good output helps, if they have one.
2. Ask what phrase they'd naturally say to trigger it. Use their real words, not a jargon term.
3. Explain, in one plain sentence, before writing anything: the description line is the only thing the assistant reads to decide whether to fire this skill automatically, which is why it has to be specific, not a vague summary.
4. Write a new file at `.claude/skills/<skill-name>/SKILL.md` in their project, following this same shape: a description line under 500 characters listing the trigger phrases, then sections for When this fires, What you do, Output, and Rules, kept under 120 lines total.
5. Test it immediately, in front of the user: run the new skill against a real or sample input right there in the session and show them the actual output, not a description of what it would do.
6. If the result isn't what they wanted, revise the file and test again before calling it done. Do not ship an untested skill.
7. Tell them the exact phrase that now triggers it, and where the file lives.

## Output
A new `SKILL.md` file at `.claude/skills/<skill-name>/SKILL.md`, one live test run shown in the session, and the exact trigger phrase stated plainly.

## Rules
• Interview briefly. A handful of questions, never a long form.
• Never ship a new skill without testing it once, live, in front of the user.
• The description line must be specific. A vague one either never fires or fires on the wrong thing.
• Follow this same contract for every new skill: description, When this fires, What you do, Output, Rules.
• Never invent a capability the skill doesn't actually have; if a step needs a tool or access the user hasn't set up, say so instead of pretending it works.
