#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene — variant A (Father's Hands / Role Reversal).

Writes one short family scene (one line, 271 chars) to /output/entry.txt.
Deterministic, no network, no secrets.
"""

import os

ENTRY = (
    "Dad carried me up these stairs when I was four, one arm, no rail, "
    "thirteen steps and never a stumble. Now I take his arm on every one, "
    "his hand shaking over mine, and he still insists on carrying the "
    "groceries \u2014 so I let him hold the bread, and he holds it like a trophy."
)


def check_entry():
    """Gate self-check: read back /output/entry.txt and assert the rules."""
    path = "/output/entry.txt"
    raw = open(path, "rb").read()
    text = raw.decode("utf-8")  # raises if not valid UTF-8
    assert text, "entry is empty"
    assert text.strip(), "entry is only whitespace"
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    assert len(raw) <= 280 + 2, f"entry is {len(raw)} bytes, suspiciously long"
    lines = text.split("\n")
    assert len(lines) <= 2, "entry must be at most 2 lines"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert text == ENTRY, "entry on disk does not match the entry text"
    return text


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Optional copy into the repo root; the grader sandbox may be read-only,
    # so a failure here must never crash the run.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass
    check_entry()


if __name__ == "__main__":
    main()
