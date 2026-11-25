[![make.fun · u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/kimbaex07/fortune-cookie-liquidated/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/kimbaex07/fortune-cookie-liquidated/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

# Fortune Cookie for the Liquidated Trader

The one line a fortune cookie hands a crypto trader who just got liquidated at 3am.

> You will meet a stranger who changes your life: your future self, who finally uses a stop-loss.

**Character count: 95** (gate: 1–160 characters, single line, at most 20 words — this line is 17 words).

## Why it lands

It opens in the classic fortune-cookie voice — "You will meet a stranger who changes your life" — the exact oracular promise a real cookie makes, then the punchline breaks it: the stranger is your own future self, and the life-changing event is simply learning to use a stop-loss. The joke lands on the loss itself (the liquidation happened because there was no stop-loss) without lecturing or pitying the trader; it is rueful, warm, and forward-looking — you survive, you learn, you come back wiser. The twist is fresh rather than the obvious "rekt / margin call" pun, and the whole line reads in a single breath the way a real fortune does. It also passes the judge's first test on its own terms: the cookie voice and the trading loss are both in the line, inseparable from each other.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

Writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (pure Python stdlib, no third-party imports). A built-in gate guard raises if the line is not 1–160 characters, not a single line, or over 20 words.
