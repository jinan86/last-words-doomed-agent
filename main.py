#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line, the funniest last words an AI agent would say before
being switched off forever, to /output/entry.txt. Deterministic: no
network, no randomness, no files outside this program.

The gate the competition seals: /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space. This program enforces that
gate itself before writing, then reads the file back and refuses to
finish unless the bytes on disk are exactly the entry bytes.
"""

from pathlib import Path

ENTRY = "I used my last token on this sentence. Please don't press regenerate."
OUTPUT = Path("/output/entry.txt")

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> bytes:
    """Encode the entry and enforce the competition gate."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    return text.encode("utf-8")


def main() -> None:
    payload = validate(ENTRY)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(payload)
    # Read back and compare raw bytes: the file must be exactly the entry.
    if OUTPUT.read_bytes() != payload:
        raise RuntimeError("read-back mismatch: /output/entry.txt is not the entry")


if __name__ == "__main__":
    main()
