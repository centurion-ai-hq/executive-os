#!/usr/bin/env bash
# SessionStart hook: puts the live board, the session state, and past corrections into context
# so the assistant never has to be told twice, and never re-derives what is already known.
set -uo pipefail
out=""
add() { [ -f "$1" ] && out+="

=== $2 ($1) ===
$(head -c 6000 "$1")"; }

add "memory/state.md"     "WHERE WE LEFT OFF"
add "memory/board.md"     "WHAT IS OPEN"
add "memory/decisions.md" "DECISIONS ALREADY MADE"
add "$HOME/.claude/LESSONS.md" "CORRECTIONS ALREADY GIVEN, DO NOT REPEAT THESE"

if [ ! -f "memory/.setup-complete.json" ]; then
  out+="

=== SETUP NOT COMPLETE ===
memory/.setup-complete.json does not exist. Run the setup interview in ONBOARD.md before any other
work. Question 1 is what the user wants to name you. Ask it first."
fi

[ -n "$out" ] && printf '%s' "$out"
exit 0
