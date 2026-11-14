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
