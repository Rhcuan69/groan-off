"""groan-off: one original one-line dad joke for make.fun's The One-Liner Groan-Off.

Pure stdlib. Deterministic: the same line every run.
Writes the joke to <OUTPUT_DIR>/entry.txt (default /output).
"""

import os

JOKE = "I asked my toaster for life advice, and it said to stop pressing me and just pop up when I'm ready."


def main():
    line = JOKE.strip()
    if not line:
        raise SystemExit("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not (1 <= len(line) <= 140):
        raise SystemExit("entry must be 1-140 characters, got %d" % len(line))
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
