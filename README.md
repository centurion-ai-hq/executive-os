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
| **28 core skills** | Twenty everyday skills plus five full sequences. Plus 5 more from the one lane pack that matches your work. |
| **Real memory** | A handbook, a corrections log, a decisions log, a live priority board, and session state. It stops forgetting. |
| **Automatic firing** | You never invoke anything. Every message you send arrives with your full skill list and the matching procedure already attached. |
| **Answer-first voice** | An output style that leads with the answer, bans filler, and ends anything long enough to decide from with a bottom line and a committed recommendation. Set globally at setup. |
| **A guided setup** | Twelve questions, one at a time, applied as you answer, verified at the end with proof rather than a claim. |
| **A three page playbook** | [PLAYBOOK.html](PLAYBOOK.html), plus a one page [cheat sheet](CHEAT-SHEET.html). |

## The flagship: brain dump

Say everything on your mind, out of order, mid sentence, dictated if that is faster. It splits what
you said into every distinct item, numbers each one, sorts them into what is being handled now, what
is real work for later, what is waiting on someone else, what you have to decide, and what is just
context worth keeping. It shows you that ledger before it starts, so you can see nothing was lost.

The thing you mention once in passing is usually the thing that costs you when it is forgotten. That
is the item this is built to catch.

## Why you never have to learn commands

Left alone, Claude picks a skill by reading skill descriptions and hoping one matches. Community
measurement puts that at roughly half the time. Half is useless for someone who will never notice
the miss and would never type the command anyway.

So a hook runs on every single message and does two things:

1. **It puts the whole menu in front of the model, every turn.** All 32 of your installed
   skills, each with a one line job, arrive attached to what you wrote. The model then matches on
   meaning rather than on wording. This is the part that generalises, because people do not speak
   from a list.
2. **It also runs plain phrase matching** against 543 recorded trigger phrases, in two bands. A
   confident hit attaches that skill's full procedure, so nothing needs looking up. An unsure hit
   is passed along as a named aside and nothing more. This matters: phrase matching is wrong often
   enough that a wrong answer delivered confidently would be worse than no answer at all.

Roughly 900 tokens per message, about 70 milliseconds, no model call in the hook itself. It fails
open: if it breaks, the session carries on without it.

**Honest measurement.** Two layers, measured separately, because they do different jobs.

The **phrase layer** gets 35% top-1 on a held-out test of 120 executive sentences written by
someone who never saw the trigger phrases. On a test written by the same author as the triggers it
gets 96.6%, which is precisely why that number is not the one quoted here: an evaluation whose
cases and whose rules share an author measures nothing. Where the phrase layer speaks up
confidently it is right 70.8% of the time, and where it is unsure it says so rather than guessing.

The **roster layer** is what carries the work, and it can only be measured by a real model rather
than a script. On the same 120 held-out sentences it scored 120/120. That number is real but it is
not a victory: the run that produced it also found that six skills were reduced to meaningless
roster lines by a bug, and the test set happened not to cover five of them. That bug is fixed and
gated against; see `tools/eval-model-results.md` for the caveats in full, written by the same run
that produced the 100%.

Reproduce with `python3 tools/eval-router.py` and `bash tools/verify.sh`.

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
| `exec-mission` | Carrying a mission or answering to a board | grants, stakeholder-brief, board-packet, impact-report, volunteers |

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
| `plugins/exec/` | The core: 28 skills, 4 agents, 3 hooks including the router. |
| `plugins/exec-*/` | The four lane packs. Five skills each, you install one. |
| `setup/ONBOARD.md` | The twelve question setup interview. |
| `setup/CLAUDE-TEMPLATE.md` | The handbook template the interview fills in. |
| `setup/EDIT-MANIFEST.md` | Which answer edits which file. Also readable by a human. |
| `tools/build-cheatsheet.py` | Regenerates the cheat sheet from the skills on disk. |
| `tools/triggers.py` | The 543 phrases that fire each skill. Edit here, then re-inject. |
| `tools/eval-router.py` | Scores the router. Run it after any change to triggers. |

## Requirements

A Claude account and Claude Code. No Node, no git, no terminal experience needed if you use the
desktop app. Works on macOS and Windows.

## The three hooks, in plain English

A hook is a rule the system enforces automatically, rather than an instruction it is meant to
remember.

• **Memory loads at the start of every session**, so you never repeat yourself.
• **Destructive commands are blocked**, so nothing gets deleted by accident.
• **Every message is matched to the right skill** before your assistant answers it, so you never
  have to know what you have or ask for it by name.

---

*Built by Centurion AI.*
