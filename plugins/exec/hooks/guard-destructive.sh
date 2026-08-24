#!/usr/bin/env bash
# PreToolUse(Bash) hook: blocks commands that destroy things which may have no second copy.
# Exit 2 blocks the command and shows the reason to the assistant.
set -uo pipefail
cmd=$(cat | python3 -c 'import sys,json; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null || echo "")
[ -z "$cmd" ] && exit 0

block() { echo "BLOCKED: $1

This command was stopped by the Executive OS safety guard. Explain to the user in one plain
sentence what it would have done and why it was blocked, then ask what they want to do instead.
Never re-run it without their explicit word in this chat." >&2; exit 2; }

case "$cmd" in
  *"rm -rf /"|*"rm -rf ~"|*"rm -rf /"*" "*|*"rm -rf ~/"*" "*)
                                             block "a recursive delete of a whole drive or home folder" ;;
  *"rm -rf"*|*"rm -fr"*)                     block "a recursive force delete, which cannot be undone" ;;
  *"git push --force"*|*"git push -f"*)      block "a force push, which destroys history" ;;
  *"git reset --hard"*)                      block "a hard reset, which throws away uncommitted work" ;;
  *"DROP TABLE"*|*"DROP DATABASE"*|*"TRUNCATE "*) block "a destructive database command" ;;
  *"mkfs"*|*"dd if="*of=/dev/*)              block "a disk format or raw disk write" ;;
  *"chmod -R 777"*)                          block "making files world writable" ;;
esac
exit 0
