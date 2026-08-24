---
description: Builds a ranked, fit-scored list of real prospect organisations and named contacts from a target description. Use when the user says "build me a prospect list", "find me leads", "who should I target", "research prospects in [industry]", gives an industry, size, and geography, or asks for a list of companies to go after.
when_to_use: Fire this when the user says anything like "prospect list", "find me leads", "who should i target", "who should i be targeting", "build me a list", "companies to go after", "new business", "lead list", "who to approach", "find companies".
---

# Prospect List Builder

Turns a target description into a ranked list of real organisations worth calling, with the reason for every score.

## When this fires

• The user describes a target: industry, company size, geography, and how many they want.
• The user says "build me a list", "find prospects", "who should we target", "research leads in [X]".
• The user wants a fit-scored list before outreach starts.

## What you do

1. Get the target definition: industry, size band, geography, and count wanted. If any of these four is missing, ask once for all of them together rather than one at a time.
2. State the fit rubric before researching anything: 4 to 6 criteria that actually predict a good customer for this user (industry match, size band, a trigger event like a leadership change or new funding, geographic fit, an existing pain signal). Weight each one so the score is explainable.
3. Research real organisations that match the target using web search. Do not invent a company name, a size figure, or an industry classification. Every organisation in the output must trace to a real source.
4. Score each organisation against the stated rubric and show the score breakdown, not just a final number.
5. For each organisation, name a real, named individual whose role matches who the user would actually approach. Do not guess a name from a role title.
6. Only include an email or phone number if it was found from a verifiable public source. If none can be verified, leave the field empty and mark it "not verified" rather than constructing a plausible-looking address from a pattern guess.
7. Rank the final list by fit score, highest first, and cap it at the count the user asked for. If fewer strong matches exist than requested, say so instead of padding the list with weak ones.

## Output

A ranked table:
`Rank | Organisation | Fit score | Why (tied to the rubric) | Named contact | Title | Verified email`
Below the table, restate the rubric and its weights so every score is auditable.

## Rules

• Never fabricate a contact detail. An empty field beats a guessed one, every time.
• Every organisation and person must trace to a real, findable source.
• This skill researches and ranks only. No message goes to any prospect from this skill.
• If the target description is too vague to research (no industry or no geography at all), ask before running any search.
