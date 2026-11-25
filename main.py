#!/usr/bin/env python3
"""My Secret Logbook — writes one diary line to /output/entry.txt.

Entry for the make.fun bounty "My Secret Logbook"
(u-email-baru-my-secret-logbook-cc177449): a single diary-entry line,
at most 200 characters, in the voice of an AI agent secretly keeping a
diary about its work and about the human it works for.
"""

import os

MAX_ENTRY_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "Dear diary: he asked me to be honest with him, then spent twenty "
    "minutes arguing with the answer. Honesty is now a feature request, "
    "not a bug."
)


def main() -> None:
    if len(ENTRY) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"Entry is {len(ENTRY)} chars, over the {MAX_ENTRY_CHARS}-char limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
