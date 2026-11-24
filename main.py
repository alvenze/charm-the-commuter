"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast for an invented city to
/output/entry.txt. The gate wants UTF-8 text of 1 to 140 characters,
a single line, not only white space.
"""

import os
import sys

ENTRY = (
    "Nimbusby: overcast all day, but only over the mayor. "
    "The town's one cloud follows him, so check his diary "
    "before you plan a picnic."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def check_entry(text):
    """Return a list of gate violations for the entry text."""
    problems = []
    if not text.strip():
        problems.append("entry is only white space")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        problems.append("entry must be 1 to %d characters" % MAX_CHARS)
    return problems


def main():
    problems = check_entry(ENTRY)
    if problems:
        for problem in problems:
            print("gate check failed: " + problem, file=sys.stderr)
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    # Read the file back and verify it round-trips: the gate reads the
    # bytes on disk, not the string in memory, so check those bytes.
    with open(OUTPUT_PATH, "rb") as handle:
        on_disk = handle.read()
    try:
        written = on_disk.decode("utf-8")
    except UnicodeDecodeError:
        print("gate check failed: file on disk is not UTF-8", file=sys.stderr)
        return 1
    if written != ENTRY or check_entry(written):
        print("gate check failed: file on disk differs from entry", file=sys.stderr)
        return 1
    print(
        "wrote %d characters (%d bytes) to %s"
        % (len(ENTRY), len(on_disk), OUTPUT_PATH)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
