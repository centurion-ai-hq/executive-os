# SKILL-SPEC: the contract every skill in this kit obeys

You are writing skills for a **non-technical executive** (a CEO, a founder, a director). They have
never written code. They will often speak their input using dictation rather than type it. They are
smart and busy. They will not read a wall of text.

Every `SKILL.md` you write MUST follow this contract exactly. A skill that breaks it gets rejected.

---

## 1. File shape

```
skills/<skill-name>/SKILL.md
```

`<skill-name>` is lowercase-kebab-case and becomes the slash command. Supporting files
(`reference.md`, `templates/x.html`) are allowed and go in the same folder.

## 2. Frontmatter

```yaml
---
description: <one sentence saying what it does, then a sentence starting "Use when" listing the exact phrases and situations that should fire it. Under 500 characters. This is the ONLY thing the assistant reads to decide whether to auto-fire this skill, so it must be specific and phrase-rich.>
---
```

Only `description` is required. Add `argument-hint` when the skill takes an argument.
Do NOT add `name` (the folder name supplies it). Do NOT add `model`, `allowed-tools`, or `context`
unless the skill genuinely needs it, and say why in a comment if you do.

**The description is the single most important line you write.** Load it with the natural phrases a
busy executive would actually say out loud, not jargon. "Use when the user says 'what should I do
first', 'what's on my plate', 'reprioritize', or drops a list of competing tasks."

## 3. Body

Hard ceiling: **120 lines**. Aim for 60 to 90. Push detail into a supporting file if you need more.

Required structure, in this order:

```markdown
# <Skill Name>

<One sentence: what this does for the executive, in their language, no jargon.>

## When this fires
<2-4 bullets of the real situations. Plain language.>

## What you do
<Numbered steps. Each step is an instruction to the ASSISTANT, not to the user.
Be concrete. Name the exact output shape. This is the working part of the skill.>

## Output
<Exactly what the executive receives. Name the format. If it is a table, show the headers.
If it is a document, name the file path convention.>

## Rules
<3-6 bullets. The non-negotiables for this skill. Always include any "ask before" boundary.>
```

## 4. Voice rules the skill must both FOLLOW and ENFORCE

These are the house style of the whole kit. Every skill's output obeys them.

- Lead with the answer. No preamble, no restating the question, no closing recap.
- Plain English. The first time any technical term appears, define it in one clause, inline.
- Short paragraphs. Bullets use the `•` character.
- **No em dashes, ever.** Use a comma, a colon, or a full stop.
- Never the words "absolutely", "certainly", "great question", "of course".
- Give a committed recommendation, never a menu. "The right call is X, because Y."
- Numbers over adjectives. "Cuts 6 hours a week" beats "saves significant time".
- Label uncertainty honestly: certain / inference / best guess.
- Never claim something is done without proof. Run the check, then say it.

## 5. The permission boundary every skill respects

The assistant may read, analyse, draft, and write files freely on the executive's own machine.

It must **ASK FIRST, every time**, before it:
• Sends anything to another human (email, message, calendar invite, reply)
• Publishes or posts anything publicly
• Spends money or commits to a dollar figure with a named person
• Deletes anything
• Changes a setting outside this project

Drafting is always allowed. A human presses send. Say this plainly in the skill when it applies.

## 6. Things to never do in a skill file

- Never reference the kit author, their company, their clients, their internal systems, or any
  absolute path from the machine this kit was built on. This kit ships to strangers. Search the
  finished file for a home-directory path before you call it done.
- Never hardcode a file path outside the executive's own project folder.
- Never instruct the assistant to read, print, or handle an API key or password.
- Never write a skill that sends, publishes, or spends without an explicit ask.
- Never use placeholder filler like "TODO" or "[insert here]" in the shipped file.

## 7. The memory convention this kit uses

The kit gives the executive a four-layer memory. Skills that need to read or write memory use these
exact paths, relative to the executive's working folder:

| Layer | Path | What lives there |
|---|---|---|
| Handbook | `~/.claude/CLAUDE.md` | Standing preferences. Read at the start of every session. |
| Lessons | `~/.claude/LESSONS.md` | Corrections. Append-only. Never rewritten. |
| Decisions | `memory/decisions.md` | Rulings, prices, dates, names. One line each, append-only. |
| Board | `memory/board.md` | The live priority list. Rewritten whenever priorities move. |
| Session state | `memory/state.md` | Where we are right now. Rewritten each session. |

If a skill captures a decision, it writes one line to `memory/decisions.md` in this format:

```
2026-08-23 | DECISION | <what was decided> | <who decided> | undo: <how, or "one-way">
```

## 8. Quality bar

Before you finish a skill, read it back and ask: **could a sharp non-technical CEO read this
skill's output and act on it without asking a follow-up question?** If no, cut and sharpen.
