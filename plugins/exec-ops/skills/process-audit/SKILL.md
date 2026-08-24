---
description: "A recurring workflow that keeps wasting time or producing errors, every time it runs. For something that broke once, this is the wrong skill. Use when the user says "audit this process", "where is the time going", "what should we automate first", "walk me through fixing this workflow", or describes a recurring process that feels slow or error-prone."
when_to_use: Fire this when the user says anything like "where is the time going", "audit this process", "what should we automate", "this takes too long", "too many steps", "where are the bottlenecks", "streamline this", "why does this take so long", "wasted time", "manual work".
---

# Process Audit

Takes a workflow you describe and tells you exactly which step to fix first, and how many hours a month you get back for it.

## When this fires

• The user describes a recurring workflow or process, step by step.
• The user says "audit this process", "where's the time going", "what should we automate first".
• A process feels slow, error-prone, or expensive, but no one has broken down why.

## What you do

1. Get the workflow described step by step: what happens, who does it, roughly how long each step takes, and how often it runs (daily, weekly, per transaction).
2. If the user has not given time estimates, ask for a rough number per step rather than guessing; an audit built on invented numbers is worthless.
3. Calculate hours consumed per month for each step: time per instance times how often it runs times how many people touch it. Show the math.
4. Rank every step by hours consumed per month, highest first.
5. For each step, judge whether it is genuinely automatable (structured or predictable input, a rule-based decision) or only looks automatable (it actually needs judgment, exceptions dominate, or the feeding data is inconsistent). State which, and why, in one sentence per step.
6. Give one committed recommendation: the single step to fix first. It must be the best combination of hours recovered and real automatability, not just the biggest number on the list. Explain the tradeoff if the biggest time sink wasn't the pick.
7. State the hours per month the recommended fix gives back, and what the fix actually is in concrete terms, not "automate this" but the specific change.

## Output

• **Steps ranked by hours/month:** table with step, owner, hours/month, automatable (yes / looks-like-it-but-no / no).
• **Fix first:** one committed recommendation, the specific change, and the hours/month it recovers.
• **Why not the biggest number instead:** one sentence, only if the top time sink wasn't picked.

## Rules

• Every hours figure traces back to a number the user gave. Label anything estimated as "estimate" rather than presenting it as a measured fact.
• "Automatable" means something specific: rule-based, structured input, a low exception rate. A step is not automatable just because it is repetitive.
• This is a recommendation, not an executed change. Building or wiring the automation is a separate step the user requests afterward.
