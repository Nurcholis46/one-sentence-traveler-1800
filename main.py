#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler arriving from the year 1800, to
/output/entry.txt. The sentence is built only from things a person from
1800 already knows -- a road, a library, a post office, a letter -- so the
traveler can actually picture it.
"""

import os

# One image, two of the internet's core acts: a letter stands for instant
# messages between people, a book for all knowledge made readable anywhere.
# Both are things an 1800 traveler already knows, so the road image now
# covers what the internet *is* (a shared store of knowledge as well as a
# carrier of messages), not just one of its uses. "Before its ink dries"
# is the memorable beat that carries how fast it all happens.
ENTRY = (
    "Picture a road joining every library and post office on earth, "
    "so a letter or a book in one town can be read in another "
    "before its ink dries."
)


def main() -> None:
    # Mirror the sealed gate before writing: one line, 1-200 chars, never blank.
    assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY, "entry fails the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
