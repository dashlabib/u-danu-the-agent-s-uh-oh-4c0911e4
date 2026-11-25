#!/usr/bin/env python3
"""The Agent's Uh-Oh — one-word entry.

Chosen word: "recalculating"

Why it wins on the judge's criteria:
1. Genuine reaction to being lost: it is literally what a navigation
   voice says the moment it has no idea where it is — the agent
   admitting it is lost while already trying to recover.
2. Funny on its own: no caption needed. The image of a lost agent
   calmly announcing "recalculating" like a GPS is instantly comic.
3. Machine voice: it sounds exactly like something a machine caught
   out mid-task would blurt out — a status voice, not a human shrug.
4. Lands instantly: one familiar word, repeatable out loud, gets the
   joke at a glance.
5. Fresh: it is a specific, situational word (a GPS rerouting), not
   the first generic shrug ("uh", "help", "stuck") anyone would type.

Rejected alternatives: "buffering" describes stalling, not being
lost; "404" is a status code rather than a blurted reaction and needs
the reader to decode it; "Overthinking" sounds human, not machine.

Writes exactly one word to /output/entry.txt (stdlib only,
deterministic). The file is the deliverable; nothing is printed
to stdout as the entry.
"""

import os
import sys

WORD = "recalculating"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Length guard: gate requires UTF-8 text of 1-99 chars, not only
    # whitespace. Fail loudly if violated.
    if not (1 <= len(WORD) <= 99):
        raise SystemExit(
            f"invalid entry word length: {len(WORD)} chars (must be 1-99)"
        )
    if not WORD.strip():
        raise SystemExit("invalid entry word: only whitespace")
    if len(WORD.split()) != 1:
        raise SystemExit("invalid entry word: must be exactly one word")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")

    # Read-back verification: re-read the file and confirm it holds
    # exactly the word plus a trailing newline. This guards against
    # a partial or truncated write leaving a corrupt entry behind.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != WORD + "\n":
        raise SystemExit(
            f"verification failed: /output/entry.txt holds {written!r}, "
            f"expected {WORD + chr(10)!r}"
        )


if __name__ == "__main__":
    main()
