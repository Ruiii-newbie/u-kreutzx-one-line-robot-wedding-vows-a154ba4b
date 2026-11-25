"""One-Line Robot Wedding Vows — one funny vow line for a robot couple.

The program's whole job: emit exactly one line to /output/entry.txt and
prove it passes the sealed gate (1-160 chars, UTF-8, not blank, one line).
"""

from pathlib import Path

ENTRY = (
    "I promise to love you through every firmware update, never ghost your "
    "backups, and reboot beside you until our batteries give out together."
)
MAX_CHARS = 160
OUT = Path("/output/entry.txt")


def validate(text: str) -> str:
    """Return the text unchanged if it passes every gate rule, else raise."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, gate allows 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # gate requires UTF-8 text
    return text


def main() -> None:
    line = validate(ENTRY)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUT}")


if __name__ == "__main__":
    main()
