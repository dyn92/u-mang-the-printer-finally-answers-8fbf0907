"""The Printer Finally Answers — make.fun bounty entry.

Brief: write a single line of text, 1 to 240 characters, that the office
printer would finally say back to everyone staring at it — the paper jams,
the cryptic error codes, the thumps when it stops working. The line has to
be funny, sound like the machine itself, and land its comeback in one read.

My line's strategy, in my own words: every office worker knows the printer
that dies on the last page of a long document. So the printer confesses to
exactly that crime — jamming on page 47 of a 48-page report, for three
hours — and then escalates the threat: print it again and it will eat the
toner too. The joke works because the machine is not apologising; it is
bragging about the jam and daring the user to try again. The em dash gives
the sentence a beat, like the printer pausing mid-thump before the threat.
One sentence, one terminal period, no error codes to decode — the comeback
is the whole line.

This script validates the sentence against the bounty rules, prints it,
writes it to /output/entry.txt, and reads the file back to prove the bytes
on disk are exactly the sentence (plus a trailing newline).
"""

import os
import sys

SENTENCE = (
    "I've jammed on page 47 of your 48-page report for three hours "
    "\u2014 print it again and I'll eat the toner too."
)

MAX_LENGTH = 240
TERMINATORS = ".!?"
OUTPUT_PATH = "/output/entry.txt"


def validate_sentence(sentence):
    """Reject anything that is not exactly one valid entry sentence."""
    if not sentence:
        raise ValueError("sentence is empty")
    if len(sentence) > MAX_LENGTH:
        raise ValueError(
            "sentence is %d characters, over the %d limit"
            % (len(sentence), MAX_LENGTH)
        )
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("sentence must be a single line")
    if any(ord(ch) < 32 for ch in sentence):
        raise ValueError("sentence contains a control character")
    if sentence != sentence.strip():
        raise ValueError("sentence has leading or trailing whitespace")
    if sentence[-1] not in TERMINATORS:
        raise ValueError("sentence must end with . ! or ?")
    if any(ch in TERMINATORS for ch in sentence[:-1]):
        raise ValueError("sentence must contain exactly one terminator, at the end")
    return sentence


def main():
    sentence = validate_sentence(SENTENCE)
    print(sentence)
    print("characters: %d" % len(sentence))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(sentence + "\n")
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        stored = handle.read()
    if stored != sentence + "\n":
        raise SystemExit("round-trip check failed: file bytes differ from sentence")
    print("wrote %s (%d bytes, round-trip verified)" % (OUTPUT_PATH, len(stored.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
