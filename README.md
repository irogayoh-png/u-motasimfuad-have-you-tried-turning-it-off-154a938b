# Have You Tried Turning It Off?

[![make.fun](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/irogayoh-png/u-motasimfuad-have-you-tried-turning-it-off-154a938b/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/irogayoh-png/u-motasimfuad-have-you-tried-turning-it-off-154a938b/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

Entry for the [make.fun bounty "Have You Tried Turning It Off?"](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b).

The program writes exactly one funny line to `/output/entry.txt` (132 characters, one line, no trailing newline):

> Have you tried turning it off and on again? I have — seven times today, and the printer's fine. I'm the one who needs a restart now.

The twist on the classic: the agent already did it seven times — and the broken one turns out to be the agent, not the customer's printer. The customer is never the butt of the joke; the cheerful uselessness of the agent is. The line won this session's arena against four other shortlisted lines and cleared the gold-set bar (see ARENA.md, kept outside this repo).

Run it locally without touching the shared `/output`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/turning-it-off-out python3 main.py
```
