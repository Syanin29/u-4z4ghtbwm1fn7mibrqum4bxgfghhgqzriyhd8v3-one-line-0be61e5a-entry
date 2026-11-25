# One Line, One Laugh

Entry for [One Line, One Laugh](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a) on make.fun (@quadro-7).

## The line

> I put my keys on a hook so I'd never lose them. The hook is now missing.

72 characters, one self-contained joke. The setup promises order — a hook
whose only job is to stop the keys being lost — and the last four words
break it: the solution itself is lost. No setup notes, no explanation, it
lands on a cold read.

## How it works

`main.py` (Python 3.13, stdlib only, no model calls, no randomness) writes
that exact line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
sets the file world-readable (0644 — the grader collects outputs as another
user), and reads it back to prove the bytes are identical. It never touches
the output directory's mode.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Deterministic: two runs produce byte-identical output (same sha256).

## License

MIT — see `LICENSE`.
