---
description: Builds a simple HTML dashboard of the handful of numbers you actually steer by, no more than seven, each with its source and what a bad reading means. Use when the user says "build me a dashboard", "what numbers should I be watching", "give me a one-page view of the business", or asks to track key metrics in one place.
---

# Executive Dashboard

Builds a one-page view of the small number of figures that actually tell you how the business is doing.

## When this fires

• The user wants a single view of the numbers that matter, not a full reporting suite.
• The user says "build me a dashboard", "what should I be watching", "give me a one-page view".
• Too many metrics are being tracked and nothing is actually being acted on.

## What you do

1. Ask what decisions this dashboard needs to support, if not already clear. A number earns a place only if a bad reading would change what the user does next.
2. Select no more than seven numbers. If the user asks for more, push back: name which of the requested numbers is a vanity metric, one that moves without meaning anything or that nobody would act differently on, and explain why it's cut rather than silently dropping it.
3. For each number, confirm its source: where it comes from (a specific file, spreadsheet, system, or manual count) and how current it is.
4. For each number, set the update cadence: how often it actually needs refreshing (daily, weekly, monthly) based on how fast it can meaningfully move, not just "always."
5. For each number, define what a bad reading means in plain terms: the threshold, and the specific consequence if it's crossed. A number with no defined bad reading is not ready to ship on the dashboard.
6. Build the output as a single, styled, self-contained HTML file, inline CSS, no external scripts, so it opens in any browser without a server.
7. Lay it out so all seven numbers are visible without scrolling on a normal screen: a grid of simple tiles, not a wall of charts.

## Output

One self-contained HTML file, up to seven tiles, each showing: the number, its label, its source, its update cadence, and what a bad reading means. Save to the project's dashboard folder and tell the user the exact path.

## Rules

• Seven numbers, hard cap. Cutting is the point of this skill; if everything looks essential, that's a sign nothing has actually been prioritized yet.
• Every number needs a named source and a defined bad reading before it goes on the dashboard. No number ships without both.
• Refuse a vanity metric if asked to add one, and say plainly why it doesn't belong, for example "this can go up while nothing real improves."
• This is a read-only view. It doesn't write to, connect to, or change any live system; the user or their own tools keep the numbers current.
