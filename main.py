#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes one original fortune-cookie line for a crypto trader who has
just been liquidated, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python standard library only.
"""

import os

FORTUNE = (
    "You will meet a stranger who changes your life: "
    "your future self, who finally uses a stop-loss."
)

MAX_CHARS = 160


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    # Gate guard: 1-160 characters, single line, not only whitespace.
    if not FORTUNE or not FORTUNE.strip():
        raise ValueError("fortune is empty or only whitespace")
    if "\n" in FORTUNE or "\r" in FORTUNE:
        raise ValueError("fortune must be a single line")
    if len(FORTUNE) > MAX_CHARS:
        raise ValueError(
            f"fortune is {len(FORTUNE)} characters, over the {MAX_CHARS} limit"
        )
    if len(FORTUNE.split()) > 20:
        raise ValueError("fortune must be at most 20 words")
    if FORTUNE != FORTUNE.strip():
        raise ValueError("fortune must not start or end with whitespace")
    # The gate reads the file as UTF-8; prove the line round-trips cleanly.
    FORTUNE.encode("utf-8").decode("utf-8")

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
