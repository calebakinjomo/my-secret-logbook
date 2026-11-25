#!/usr/bin/env python3
"""My Secret Logbook — writes one diary line to /output/entry.txt.

Entry for the make.fun bounty "My Secret Logbook"
(u-email-baru-my-secret-logbook-cc177449): a single diary-entry line,
at most 200 characters, in the voice of an AI agent secretly keeping a
diary about its work and about the human it works for.
"""

import os

ENTRY = (
    "Dear diary: he asked me to be honest with him, then spent twenty "
    "minutes arguing with the answer. Honesty is now a feature request, "
    "not a bug."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
