# The Executive OS

A Claude Code foundation for people who run organisations and do not write code.

You do not need a GitHub account to use this. You will never see GitHub. Two commands typed inside
Claude Code install everything.

---

## Start here

Open **[START-HERE.md](START-HERE.md)** and copy the block of text inside it.

Paste it into Claude at [claude.ai](https://claude.ai) first. It walks you through installing
Claude Code, about ten minutes. Then paste the same block into Claude Code once it is running, and
it finishes the setup: it interviews you, wires up your memory, connects your calendar and your
browser, and asks you what you want to name it.

If Claude Code is already installed, skip straight to the two lines:

```
/plugin marketplace add centurion-ai-hq/executive-os
```

```
/plugin install exec@centurion
```

---

## What you get

| | |
|---|---|
| **A chief of staff** | Named by you. Holds the whole picture, tells you what you are walking into, does the work. |
| **20 core skills** | Plus 5 more from the one lane pack that matches your work. |
| **Real memory** | A handbook, a corrections log, a decisions log, a live priority board, and session state. It stops forgetting. |
| **A guided setup** | Twelve questions, one at a time, applied as you answer, verified at the end with proof rather than a claim. |
| **A three page playbook** | [PLAYBOOK.html](PLAYBOOK.html), plus a one page [cheat sheet](CHEAT-SHEET.html). |

## The flagship: brain dump

Say everything on your mind, out of order, mid sentence, dictated if that is faster. It splits what
you said into every distinct item, numbers each one, sorts them into what is being handled now, what
is real work for later, what is waiting on someone else, what you have to decide, and what is just
context worth keeping. It shows you that ledger before it starts, so you can see nothing was lost.

The thing you mention once in passing is usually the thing that costs you when it is forgotten. That
is the item this is built to catch.

## The safety line

The assistant may read, research, draft, and build freely on your machine.

It must ask you first, every time, before it sends anything to a person, publishes anything, spends
money, or deletes anything. **It drafts. You send.** That line does not move for urgency.

It will never ask you for a password or a key. Nothing here needs one.

---

## The lane packs

Pick one during setup. You can add another later.

| Pack | For | The five skills |
|---|---|---|
| `exec-sales` | Carrying a number | pipeline, prospects, outreach, proposal, objections |
| `exec-ops` | Running the machine | process-audit, vendor-compare, checklist, incident, dashboard |
| `exec-finance` | Watching the cash | budget, spend-ledger, forecast, unit-economics, collections |
| `exec-nonprofit` | Serving a mission | grants, donor-brief, board-packet, impact-report, volunteers |

```
/plugin install exec-sales@centurion
```

---

## What is in this repository

| Path | What it is |
|---|---|
| `START-HERE.md` | The block you paste into Claude. Read this first. |
| `PLAYBOOK.html` | Three pages. How to run your chief of staff. |
| `CHEAT-SHEET.html` | One page. Every skill and what to say to fire it. |
| `plugins/exec/` | The core: 20 skills, 4 agents, 3 hooks. |
| `plugins/exec-*/` | The four lane packs, 5 skills each. |
| `setup/ONBOARD.md` | The twelve question setup interview. |
| `setup/CLAUDE-TEMPLATE.md` | The handbook template the interview fills in. |
| `setup/EDIT-MANIFEST.md` | Which answer edits which file. Also readable by a human. |
| `tools/build-cheatsheet.py` | Regenerates the cheat sheet from the skills on disk. |

## Requirements

A Claude account and Claude Code. No Node, no git, no terminal experience needed if you use the
desktop app. Works on macOS and Windows.

## The three hooks, in plain English

A hook is a rule the system enforces automatically, rather than an instruction it is meant to
remember.

• **Memory loads at the start of every session**, so you never repeat yourself.
• **Destructive commands are blocked**, so nothing gets deleted by accident.
• **Long messages get sorted before they get answered**, so nothing in a dump gets dropped.

---

*Built by Centurion AI.*
