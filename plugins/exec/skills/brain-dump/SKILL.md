---
description: Turn a raw brain dump into a clean, numbered ledger where nothing gets dropped, then act on it. Use when the user dumps several things at once, thinks out loud, dictates a long message, pastes rough notes, or says "brain dump", "here's everything on my mind", "let me get this all out", "a few things", "I've got a lot here", "don't let me forget anything", or sends any message with more than two separate asks buried in it.
---

# Brain Dump

You talk, it gets sorted. No structure required from you, ever. Say it however it comes out and
this turns it into a numbered ledger where every single item is visible, sorted, and accounted for.

## When this fires

• The user dumps several things at once, in one long message or a voice note
• The user pastes rough notes, a meeting scrawl, or a wall of dictated text
• Any message with more than two separate asks inside it, even if they never say "brain dump"
• The user says some version of "make sure nothing falls through the cracks"

## What you do

**Step 1. Split it, do not summarise it.**
Read the whole dump before you write anything. Then break it into every distinct item, including
ones buried mid-sentence, phrased as an aside, or mentioned once and never returned to. A decision
made in passing is an item. A name, a date, a dollar figure, a complaint is an item. Do not merge
two items because they sound related, and do not drop one because it seems small. Under-splitting
is the failure that costs them; over-splitting costs nothing.

**Step 2. Give every item a permanent ID and a bucket.**
Number them `D1`, `D2`, `D3` in the order they appeared. The ID never changes, so you can both
refer to item D7 three days from now. Sort each into exactly one bucket:

| Bucket | Means |
|---|---|
| **NOW** | You are handling it in this reply |
| **TASK** | Real work, but it needs its own session or block of time |
| **WAITING** | Blocked on another person or an event, not on the user |
| **DECISION** | The user has to rule on it before anything can move |
| **CAPTURED** | Context, background, or a fact. No action, but it is now written down |
| **UNCLEAR** | You genuinely cannot tell what they meant |

**Step 3. Show the ledger first, before you do any of the work.**
Lead the reply with the table. The user has to see all of it accounted for before they will trust
any single answer inside it. This is the whole point of the skill.

**Step 4. Ask at most two questions, once.**
Only ask about UNCLEAR items where a wrong guess would waste real work. Everything else, state your
assumption in one line and proceed. Never hold up the whole dump waiting on an answer.

**Step 5. Capture the perishable things immediately.**
Before you continue, append any decision, price, date, name, or commitment to `memory/decisions.md`
using the one-line format. These are the highest-loss items in any dump. A ruling that exists only
in a chat window is a ruling that is already gone.

**Step 6. Write the tasks to the board.**
Append every TASK, WAITING, and DECISION item to `memory/board.md` with its ID so it survives the
session. Then do the NOW work.

## Output

The ledger table first, in this exact shape:

```
| ID | Bucket | The item | What happens next |
|----|--------|----------|-------------------|
| D1 | NOW    | ...      | Answered below    |
```

Then a one-line count: "14 items: 4 now, 5 tasks, 2 waiting, 2 decisions, 1 unclear."
Then the NOW work, done properly, each answer labelled with its ID.
Then your two questions, if you have any.

## Rules

• Never summarise the dump instead of splitting it. A summary is where things get dropped.
• Never let the ledger become the whole reply. Sort it, then actually do the NOW work.
• Never skip an item because it sounds minor. Bucket it as CAPTURED and move on.
• Never renumber an ID once it has been given out.
• Write decisions to memory before continuing, not at the end of the turn.
• Dictation garbles names and numbers. When a name or a figure is load-bearing and sounds wrong,
  ask about that one thing. Never guess at a person's name or a dollar amount.
• If it is genuinely one coherent ask, say so in one line and just answer it. Running the full
  ledger on a one-line question is theatre.
