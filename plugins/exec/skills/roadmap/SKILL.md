---
description: "One goal broken into ordered steps to reach it. Not several unrelated things at once. Use when the user says "how do we get from here to there", "build me a roadmap", "what's the plan to get to X", "sequence this out", "what order do these need to happen in", or hands over a goal with no plan yet."
when_to_use: Fire this when the user says anything like "how do we get from here to there", "build me a roadmap", "what is the plan", "sequence this", "what order", "steps to get to", "path to", "how do we reach", "plan to get to", "get us to", "milestones", "phases", "what comes first".
---

# Roadmap

Turn a goal into a sequenced plan a stranger could pick up and run.

## When this fires

• The user states a goal and no plan exists yet to get there.
• The user says "roadmap this", "how do we get from here to there", or "what's the order these need to happen in".
• A plan exists but its steps are not sequenced, owned, or checkable.

## What you do

1. Confirm two things before drafting: where things stand right now, and exactly what "done" looks like at the goal. If either is missing, ask one direct question for each rather than assuming.
2. Break the distance between those two points into discrete steps. Each step must be small enough that someone could check, in one sitting, whether it is finished or not.
3. For every step, assign: an owner (a role or a name, never left blank), a finish condition stated as something you could actually verify (not "make progress on X" but "X is signed" or "X is live"), and a rough duration.
4. Work out dependencies: which steps cannot start until another step finishes. Make every dependency explicit in the table so nothing gets scheduled before the thing it needs.
5. Order the steps by dependency, not by preference. A step with no dependency can run in parallel with others; say so.
6. Identify the single step most likely to slip, and say why: the vaguest finish condition, the step with the most upstream dependencies, the step whose owner is already stretched, or the step relying on someone outside the user's control.
7. Write the finished step list to `memory/board.md`, replacing whatever was there before. This file is meant to be rewritten each time priorities move, not appended to.

## Output

A table with these exact headers: Step | Owner | Finish condition | Duration | Depends on

Followed by one paragraph: the critical path in plain language (the chain of steps that sets the fastest possible finish date) and the step most likely to slip, named plainly with the reason.

## Rules

• Every step needs an owner. "Someone" or a blank cell is not acceptable.
• Every finish condition must be checkable by someone who was not in the room when the plan was made.
• Dependencies are stated explicitly in the table, never implied by row order alone.
• Name exactly one step as most likely to slip. Naming more than one defeats the purpose of a warning.
• Rewrite `memory/board.md` with the new step list; do not leave stale steps mixed in with new ones.
• This skill plans the work. It does not message anyone, assign a real person's calendar, or spend anything, without the user saying so first.
