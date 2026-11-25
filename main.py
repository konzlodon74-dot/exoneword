#!/usr/bin/env python3
"""Describe Your Ex in One Word — entry for u-puan-describe-your-ex-in-one-word-9fc6ebe7.

The verdict: Unsubscribed. A relationship treated like a service you
cancelled — no drama, no shouting, just quietly opted out. The word
lands because everyone has hit "unsubscribe" on something that stopped
being worth the inbox space.
"""

import os

WORD = "Unsubscribed"


def validate(word: str) -> None:
    """Enforce the bounty rules: exactly one word, 1-111 chars, no tricks."""
    if not word or len(word) > 111:
        raise ValueError("word must be 1-111 characters")
    if word.split() != [word] or not word.isalpha():
        raise ValueError("word must be a single alphabetic word")


def main() -> None:
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
