# EDIT-MANIFEST: what each interview answer changes

Every question in `ONBOARD.md` maps to an exact file and an exact placeholder. Do not guess at a
path and do not improvise a location. Look it up here, make the edit, confirm it in one sentence.

A human can also read this table to hand-edit their own setup later. That is deliberate.

## The placeholder map

| Q | What you asked | File | Placeholder or action |
|---|---|---|---|
| 1 | Name for the agent | `~/.claude/CLAUDE.md` | `[AGENT_NAME]` , replace every instance |
| 2 | Their name | `~/.claude/CLAUDE.md` | `[USER_NAME]` |
| 2 | How to address them | `~/.claude/CLAUDE.md` | `[HOW_TO_ADDRESS]` |
| 3 | Their role | `~/.claude/CLAUDE.md` | `[ROLE]` |
| 3 | Their company | `~/.claude/CLAUDE.md` | `[COMPANY]` |
| 3 | What the company does | `~/.claude/CLAUDE.md` | `[WHAT_COMPANY_DOES]` |
| 4 | Their three lanes | `~/.claude/CLAUDE.md` | `[LANE_1]`, `[LANE_2]`, `[LANE_3]` |
| 5 | Tone preference | `~/.claude/CLAUDE.md` | `[TONE]` |
| 6 | Lane pack chosen | shell | `claude plugin install exec-<lane>@centurion` |
| 7 | Email and calendar | browser | connect at claude.ai connectors, then confirm in `/mcp` |
| 7 | Their answer, recorded | `memory/decisions.md` | append one line |
| 8 | Browser access | Chrome | install the Claude extension, reconnect with `claude --chrome` |
| 9 | What is on their plate | `memory/board.md` | write the full sorted ledger |
| 10 | What eats their week | `memory/board.md` | one item, tagged `FIRST-BUILD` |
| 11 | Their work folder | `~/.claude/CLAUDE.md` | `[WORK_FOLDER]` |
| 12 | First win | wherever the work lands | plus one line in `memory/decisions.md` |
| , | Today's date | `~/.claude/CLAUDE.md` | `[SETUP_DATE]` |
| , | Setup finished | `memory/.setup-complete.json` | write the marker file |

## Files this setup creates

| Path | Created from | Purpose |
|---|---|---|
| `~/.claude/CLAUDE.md` | `setup/CLAUDE-TEMPLATE.md` | The handbook, read every session |
| `~/.claude/LESSONS.md` | `setup/LESSONS-seed.md` | Corrections, append only |
| `memory/board.md` | Question 9 | What is open |
| `memory/decisions.md` | new, empty | Rulings, append only |
| `memory/state.md` | new, empty | Session state |
| `memory/.setup-complete.json` | end of interview | The marker that stops the interview |

## The marker file

```json
{
  "setup_completed": "YYYY-MM-DD",
  "agent_name": "<what they named it>",
  "lane_pack": "<sales|ops|finance|nonprofit|none>",
  "connectors": { "email": true, "calendar": true, "browser": true },
  "kit_version": "1.0.0"
}
```

`~/.claude/CLAUDE.md` checks for this file at the start of every session. If it is missing, the
interview runs. If it is present, it does not. That is the entire mechanism, and it is why the
setup fires by itself the first time without the user having to remember to start it.

## Verification, before you call setup done

Search `~/.claude/CLAUDE.md` for `[` and `]`. If any remain, a placeholder was missed, and the
handbook will read as a template rather than as theirs. Fix it before reporting complete.
