#!/usr/bin/env python3
"""One Line, One Laugh — writes exactly one funny line to entry.txt.

The line is a fixed, hand-written one-liner (no model calls, no randomness,
stdlib only). It writes to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)
and verifies the written bytes are identical to the line.

The joke: a clean inversion — the very system built to stop losing things
is itself lost. Setup promises order, the last four words break it.
"""

import os
import sys

LINE = "I put my keys on a hook so I'd never lose them. The hook is now missing."

# Gate: the bounty requires UTF-8 text of 1 to 140 characters, not only
# whitespace. 72 characters, one line, self-contained.
assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
assert LINE.strip(), "line must not be only whitespace"
assert "\n" not in LINE, "line must be a single line"
assert LINE.isascii(), "line must be plain ASCII text"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get(
        "OUTPUT_DIR", "/output"
    )
    # Never chmod the output directory (the grader owns it); only create
    # it if it does not exist.
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # The collector runs as another user: the file must be world-readable.
    os.chmod(path, 0o644)
    # Read back and prove the written file is byte-identical to LINE.
    with open(path, "rb") as f:
        assert f.read() == data, "written entry.txt differs from LINE"
    return 0


if __name__ == "__main__":
    sys.exit(main())
