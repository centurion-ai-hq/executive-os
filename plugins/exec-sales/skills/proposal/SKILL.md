---
description: Turns a discovery conversation into a client-ready proposal covering the problem, deliverables, price, timeline, and exclusions. Use when the user says "write a proposal for", "turn this into a proposal", "draft a proposal", "put together a scope of work", or has just finished describing a discovery conversation with a client.
when_to_use: Fire this when the user says anything like "write a proposal", "scope of work", "sow", "turn this into a proposal", "quote them", "put together a proposal", "statement of work", "what we would deliver".
---

# Proposal Builder

Turns what was said on a discovery call into a client-ready proposal document, in the client's own language.

## When this fires

• The user has just described or pasted notes from a discovery conversation with a prospective client.
• The user says "write a proposal", "turn this into a proposal", "draft the scope of work", "put together a quote".
• A deal has reached the stage where a written proposal is the next step.

## What you do

1. Read the discovery notes or conversation provided. Pull out the problem in the client's own words: quote or closely paraphrase how they described the pain, not a generic restatement.
2. List exactly what gets delivered. Be concrete: named deliverables, not categories. If scope is vague in the notes, ask the user to confirm it before writing rather than guessing at what was promised.
3. Ask the user for the price. Never invent, estimate, or infer a number from context. If a price was mentioned in the notes, confirm it with the user before using it: "I see $X mentioned, is that the number to use?"
4. Once a price is given, use that exact number everywhere it appears: the summary, the pricing section, and any total. Check the document for consistency before finishing; two different numbers in one proposal is a failed proposal.
5. State the timeline: what happens by when, in dated or day-count milestones tied to a start date the user confirms.
6. State what is explicitly not included. This section protects the user from scope creep and must be as concrete as the deliverables section.
7. Build the output as a single, styled, self-contained HTML file, inline CSS, no external assets, so it opens cleanly in any browser and forwards as one file.
8. Save the file to the project's proposals folder using the client's name and today's date in the filename, and tell the user the exact path.

## Output

One self-contained HTML file, sections in this order: the problem in the client's words, what's delivered, price, timeline, what's not included. Plain, professional styling: one accent colour at most, readable type, no clip art.

## Rules

• Never invent a price. Always get it from the user, then hold it exactly across the whole document.
• Never promise a deliverable, date, or exclusion that wasn't confirmed by the user or clearly present in the discovery notes.
• This skill builds the file. It does not send, email, or share it. The user sends it themselves.
• If the discovery notes are too thin to fill a section honestly, flag the gap to the user instead of filling it with generic language.
