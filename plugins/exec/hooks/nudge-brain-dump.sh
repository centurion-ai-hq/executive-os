#!/usr/bin/env bash
# UserPromptSubmit hook: when a message carries several separate asks, remind the assistant to
# sort it before answering, so nothing buried mid-sentence gets dropped. Advisory, never blocks.
set -uo pipefail
prompt=$(cat | python3 -c 'import sys,json; print(json.load(sys.stdin).get("prompt",""))' 2>/dev/null || echo "")
words=$(printf '%s' "$prompt" | wc -w | tr -d ' ')
[ "${words:-0}" -lt 90 ] && exit 0
printf '%s' "[MULTI-ASK CHECK] This message is long and may carry several separate asks. Before
answering: split it into every distinct item, number them, sort each into NOW / TASK / WAITING /
DECISION / CAPTURED / UNCLEAR, and show that ledger first. Then do the NOW work. Write any decision,
price, date or name to memory/decisions.md immediately, not at the end of the turn. If it is
genuinely one coherent ask, say so in one line and just answer it."
exit 0
