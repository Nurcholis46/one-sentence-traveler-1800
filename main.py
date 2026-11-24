#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler arriving from the year 1800, to
/output/entry.txt. The sentence is built only from things a person from
1800 already knows -- a road, a library, a post office, a letter -- so the
traveler can actually picture it.
"""

import os

ENTRY = (
    "Picture a road joining every library and post office on earth, "
    "so a letter written in one town can be read in another "
    "before its ink dries."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
