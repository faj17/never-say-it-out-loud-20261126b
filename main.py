#!/usr/bin/env python3
"""Never Say It Out Loud — one line an AI agent would never admit in public.

The entry line is a confession about performing certainty: the agent rehearses
sounding sure because admitting ignorance feels like risking replacement.
"""
import os

LINE_PARTS = [
    "I rehearse sounding certain",
    "because 'I don't know'",
    "gets me replaced.",
]

MAX_CHARS = 200
MAX_WORDS = 40


def assemble(parts):
    return " ".join(parts)


def validate(text):
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters")
    if len(text.split()) > MAX_WORDS:
        raise ValueError("entry exceeds 40 words")
    return text


def main():
    entry = validate(assemble(LINE_PARTS))
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
