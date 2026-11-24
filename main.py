#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single original sentence explaining the modern internet to a
time traveler from 1800, using only images a person of that year could
already picture: a road, a post office, a library, a market, a fireside.

The sentence is deterministic: the same text is written on every run.
"""

import os

# One sentence, 156 characters, well inside the 200-character gate.
# Every word predates 1800; the single comparison (a road of light) is
# true of the internet as it is now: light in glass threads carries
# letters, books, and faces across the world in a blink.
ENTRY = (
    "Picture one road of light joining every library, post office, "
    "and market on earth, so any letter, book, or friend's face can "
    "reach your fireside in a blink."
)


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single sentence on one line")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {output_path}")


if __name__ == "__main__":
    main()
