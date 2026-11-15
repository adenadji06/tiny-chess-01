[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/adenadji06/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/adenadji06/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# tiny-chess-01 entry

A 4 KB Python chess engine: 0x88 board, negamax alpha-beta with iterative
deepening (depth 1-4), capture-only quiescence with check evasions, fixed
60,000-node budget per depth, material + pawn piece-square evaluation.
Deterministic: no clock, no randomness. Plays through MAKEFUN_ENV_URL.

## Engine (v2)

Full piece-square tables for every piece, bishop-pair bonus, passed-pawn
bonus, and king-shelter evaluation. Search uses a transposition table,
killer moves, null-move pruning, late-move reduction, and MVV/LVA move
ordering. The global node budget is 80,000 nodes. `main.py` is the
kit-compressed build of `source.py`.

Expected strength is roughly 1,350-1,400 Elo on the dev trials. The
compressed build fits the 4,096-byte size limit.

Build: `node <kit>/cli/makefun.mjs compress source.py --out main.py`

Bounty: https://make.fun/c/tiny-chess-01
