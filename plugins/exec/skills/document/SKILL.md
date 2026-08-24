---
description: "Produces a finished, ready-to-hand-over document, a one pager, a board memo, a client brief, or a proposal, saved as a self-contained styled HTML file you open in a browser and print to PDF. Use when the user says 'write me a one pager', 'draft a memo', 'turn this into a proposal', 'make this a client brief', 'I need something I can send', or hands over notes, a decision, or a call that needs to leave the session as a document."
argument-hint: "[what the document is for, and who reads it]"
when_to_use: Fire this when the user says anything like "one pager", "write me a memo", "I need something I can send", "hand to them", "put this in a document", "make this presentable", "turn this into a memo", "a brief", "something formal", "leave behind", "write this up properly", "a doc", "a pdf".
---

# Document

Turns notes, a decision, or a conversation into a finished document you can actually hand to someone.

## When this fires
• The user asks for a one pager, memo, brief, proposal, or "something I can send".
• A decision or a body of work needs to leave this session as a document someone else reads.
• The user says "write this up", "make this presentable", "turn this into a document".

## What you do
1. Confirm in one line what the document is, who reads it, and whether it exists to drive a decision. Ask once if any of the three is unclear.
2. Draft the content bottom-line-first: the decision or the point in the first few lines. No preamble, no restating the ask.
3. Enforce the length rule. Anything a person reads to decide from gets a 500-word target and a 1,500-word hard ceiling, counted for real, never estimated.
4. If the material does not fit, do not cut it. Layer it: the decision and the reasoning stay on top, the supporting detail moves into a section labeled "Appendix" further down the same file, so nothing is lost, only reordered.
5. Build one self-contained HTML file: inline CSS only, one typeface (a plain system font), a light background, generous white space, one accent color used sparingly, for a headline or a single callout, never as the only signal of emphasis. No dark background, no decorative gauges or widgets.
6. Put the true word count in the footer, in plain text, for example "612 words to the decision." Count it for real.
7. Save the file to `documents/<doc-name>.html` in the project folder and tell the user the path, plus that they can open it in any browser and print to PDF from there.
8. Never send, email, or publish the document to anyone. Drafting and saving locally is always allowed; sending it is the user's own move.

## Output
One self-contained HTML file at `documents/<doc-name>.html`, plus a two or three sentence chat summary naming the path and the word count.

## Rules
• 500 words is the target, 1,500 is the hard ceiling, for anything read to decide from. State the real count, always.
• Completeness and length are not a tradeoff. Layer, never shrink: depth moves into a linked appendix, nothing gets deleted to hit budget.
• One typeface, light background, one sparing accent color, no dark mode, no widgets, no color used as the only way to mark emphasis.
• Self-contained file, no external stylesheets, fonts, or scripts, so it opens and prints anywhere without a live connection.
• No em dashes. Bullets use •. Lead with the answer, never a preamble.
• Ask first before sending, emailing, publishing, or posting this document anywhere. Building and saving it is always fine on its own.
