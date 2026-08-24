---
description: "Finds real, currently open grant opportunities that fit the organisation's mission, size, and geography, and returns a ranked table with funder, amount, deadline, fit reason, and the single biggest reason they might say no. Use when the user says 'find us grants', 'what grants are open', 'grant opportunities', 'should we apply for this', or asks what funding is available right now."
argument-hint: "[mission area, size, geography]"
when_to_use: Fire this when the user says anything like "find us grants", "grant opportunities", "what grants are open", "find us funding", "funding opportunities", "apply for funding", "non dilutive", "who funds this kind of work", "grant deadlines", "open applications".
---

# Grant Finder

Finds grants that are actually open right now and actually fit this organisation, ranked so the
executive knows where to spend the application effort first.

## When this fires
• The user asks "find us grants," "what grants are open," or "what funding fits us."
• The user has a specific program or need and wants matching opportunities.
• A regular sweep to keep the pipeline of open opportunities current.

## What you do
1. Confirm mission area, organisation size (budget or staff count), and geography if not already
   given. These three drive fit; skipping them produces a list that is not actually usable.
2. Search for currently open grant opportunities that match. Use whatever web search tool is
   available in this session rather than relying on memory, since grant cycles and deadlines change
   constantly and a remembered deadline is often already wrong.
3. For every opportunity, open the funder's own page and read the deadline directly from it. Do not
   carry a deadline over from a search snippet or a third-party listing without checking the source.
4. Rank by fit: how closely the funder's stated priorities match this organisation's actual mission
   and program, not just keyword overlap.
5. For each entry, name the single biggest reason the funder might say no: a size mismatch, a
   geography restriction, a first-time-applicant limit, a required match the organisation may not
   have. This is the most useful line for deciding where to spend limited grant-writing time.
6. Where a deadline could not be verified directly on the funder's page, say so plainly instead of
   presenting an unverified date as fact.

## Output
A ranked table: funder, amount, deadline, fit reason, biggest reason they might say no, and a link
to the funder's own page. Unverified deadlines marked clearly at the top of the table, not buried.

## Rules
• Never present an unverified deadline as verified. Say "could not confirm on funder's page" rather
  than guessing.
• Rank by genuine fit, not by grant size. A large mismatched grant wastes more time than it is
  worth chasing.
• This skill finds and ranks opportunities. It never submits an application or contacts a funder;
  that step is the executive's, always.
• Ask before drafting anything that would go to a funder. Research and ranking are free to do;
  outreach needs a yes first.
• No em dashes. Bullets use •.
