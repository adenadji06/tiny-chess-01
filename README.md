# tiny-chess-01 entry

A 4 KB Python chess engine: 0x88 board, negamax alpha-beta with iterative
deepening (depth 1-4), capture-only quiescence with check evasions, fixed
60,000-node budget per depth, material + pawn piece-square evaluation.
Deterministic: no clock, no randomness. Plays through MAKEFUN_ENV_URL.
