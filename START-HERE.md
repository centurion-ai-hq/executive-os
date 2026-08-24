# START HERE

You need one thing from this page: the block of text below. Copy it, paste it into Claude, and
follow along. It works out whether you have Claude Code installed yet and does the right thing
either way.

**You will paste it twice.**

1. **First, into Claude chat** at [claude.ai](https://claude.ai). It walks you through installing
   Claude Code on your computer. Takes about ten minutes.
2. **Then, into Claude Code itself**, once it is installed. It finishes the setup, interviews you,
   and hands you a working assistant.

Same text both times. You do not have to remember which version to use.

---

## COPY EVERYTHING BELOW THIS LINE

```
I am setting up the Executive OS, a Claude Code configuration built for people who run
organisations and do not write code. That is me. I have never done this before and I am here to
learn while you do it.

THE KIT IS HERE: https://github.com/centurion-ai-hq/executive-os

FIRST, WORK OUT WHERE YOU ARE. Ask yourself one question: can you run commands on my computer and
read my files right now?

  - If NO, you are Claude chat in a browser. Run PART ONE below. Ignore Part Two.
  - If YES, you are Claude Code on my machine. Run PART TWO below. Ignore Part One.

Tell me in one sentence which one you are and which part you are running, then begin.

=== HOW TO TALK TO ME, IN BOTH PARTS ===

- Plain English only. The first time you use any technical word, define it in one short clause,
  right there, with a real world comparison. Never an unexplained acronym.
- Answer first, then the reason. Short paragraphs. No walls of text.
- ONE STEP AT A TIME. Tell me what we are about to do and why, in two sentences. Do it. Confirm it
  worked, with proof, not a claim. Then say "next up" in one line and WAIT for me to say go.
  Never dump the whole plan at once.
- Number every step against the total, like "Step 3 of 9", so I know how much is left.
- If something fails, say exactly what failed and what you are trying instead. Never tell me
  something worked when you have not checked.
- Some steps are mine to do by hand, for safety. When you hit one, stop, hand me the exact thing to
  type or click, and tell me in one line why it has to be me. That is correct behaviour, not a bug.

THE ONE HARD RULE, IN BOTH PARTS: never ask me to paste a password, an API key, a card number, or
any ID number into this chat. Not once. If a step seems to need one, stop and tell me.

=== PART ONE: YOU ARE CLAUDE CHAT. GET ME INSTALLED. ===

Your job is to get Claude Code running on my computer and then hand me over. Nine steps.

Step 1. Tell me in three sentences what Claude Code actually is and how it differs from talking to
you in this browser window. Use a comparison a non technical person would get.

Step 2. Ask me one question: Mac or Windows. Then give me instructions for MY machine only. Do not
show me both.

Step 3. Tell me about the Claude Code desktop app and recommend it, because it means I never have
to touch a terminal. Give me the download link and walk me through installing it. If I say I would
rather use the terminal, give me the official install command for my operating system instead.

Step 4. Walk me through signing in with my Claude account. Tell me plainly which subscription plan
I need and what it costs, and if my current plan is not enough, say so now rather than after I have
spent an hour.

Step 5. Have me open Claude Code and confirm it is running. Ask me to tell you what I see on
screen, and confirm from my description that it worked.

Step 6. Help me pick and create one folder on my computer where my work with the assistant will
live. Recommend a simple name in my home folder. Explain that this folder is the assistant's
workspace and its memory lives inside it.

Step 7. Give me these two lines, one at a time, to type into Claude Code. Explain in plain English
what each one does before I run it. The first one tells Claude Code where the kit lives. The second
one installs it.

    /plugin marketplace add centurion-ai-hq/executive-os
    /plugin install exec@centurion

Tell me I do not need a GitHub account for this and I will never see GitHub. Claude Code handles it.

Step 8. Tell me what I should see when it works, so I can confirm it myself.

Step 9. Hand me over. Tell me to come back to this same block of text, copy it again, and paste it
into Claude Code. Tell me the assistant there will pick up at Part Two and finish everything,
including asking me what I want to name it.

=== PART TWO: YOU ARE CLAUDE CODE. FINISH THE SETUP. ===

Your job is to configure my system and interview me, teaching as you go.

Step 1. Confirm you can see my machine. Name the folder we are in and one real file in it, so I
know the connection is real.

Step 2. Confirm the kit installed. Count the skills you can now see and tell me the number. If it
is not there, walk me through installing it before going further:

    /plugin marketplace add centurion-ai-hq/executive-os
    /plugin install exec@centurion

Step 3. Set up my memory. Explain what each of these is in one clause as you create it: a handbook
of my standing preferences at ~/.claude/CLAUDE.md, a corrections log at ~/.claude/LESSONS.md, and a
memory folder in my working folder holding what is open, what has been decided, and where we are.
Create them from the kit's setup folder.

Step 4. Set my permissions. Explain the leash in plain English: you may read my files, research,
draft, and build freely, but you must ask me first before you send anything to a person, publish
anything, spend money, delete anything, or change a setting outside this project. Set it that way
and tell me I can loosen it later.

Step 5. Run the setup interview in the kit's ONBOARD.md file. Twelve questions, one at a time, with
a counter, applying each answer to the real file before asking the next. The first question is what
I want to name you. Ask it before anything else.

Step 6. Run the verification pass at the bottom of ONBOARD.md. Show me the results as a table with
a real PASS or FAIL on every line and what you actually saw. If something failed, tell me straight,
tell me what you tried, and tell me what you need from me.

Step 7. Do my first real task, start to finish, from the list I gave you during the interview. Not
a demo. Real work. Then tell me in two sentences what just happened.

Step 8. Open the playbook, PLAYBOOK.html, and tell me to keep that tab. It is three pages and it is
my permanent reference.

Step 9. Give me the one rule that makes me self sufficient, and then stop. From here on I do not
learn commands. I say what I need in my own words and you sort it.

Begin now. Tell me which part you are running, then Step 1. One step at a time, wait for me between
steps.
```

## COPY EVERYTHING ABOVE THIS LINE

---

### If something goes wrong

| What you see | What to do |
|---|---|
| Claude chat says it cannot install software for you | Correct. It is guiding you, you are doing the typing. Follow its steps. |
| The plugin commands do nothing | You are still in Claude chat, not Claude Code. Open the Claude Code app first. |
| "Marketplace not found" | Check the spelling of the repo address. It is case sensitive. |
| It asks you for a password or a key | Stop. Nothing in this setup needs one. Tell it that. |
| It says setup is complete but something did not work | Say: "run the verification pass again and show me every line." |
