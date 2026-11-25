"""One-line office joke: the printer that knows the calendar.

Writes a single original one-line joke about office life to
/output/entry.txt (UTF-8, 1-199 characters, exactly one line).
The joke turns on a real office detail -- the printer that only
jams when a document is urgent -- and lands its laugh in the
last few words. Standard library only.
"""

import os

JOKE = (
    "Our office printer only jams on urgent documents, which is "
    "how I know it reads the calendar better than my manager does."
)

MAX_CHARS = 199


def check(text):
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if "\n" in text.rstrip("\n"):
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit("char count %d outside 1-%d" % (len(text), MAX_CHARS))
    return len(text)


def main():
    chars = check(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")
    print("wrote /output/entry.txt: %d chars, 1 line" % chars)


if __name__ == "__main__":
    main()
