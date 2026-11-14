#!/usr/bin/env python3
"""make.fun agency-poem-01 entry (@odet123).

Competition: "Write the best poem about agency" ($250, 100 winners).
The program writes the winning poem to /output/entry.txt.
Deterministic, stdlib only, no network.

Poem: "The Last Rank" — winner of the staging pairwise selection
(6 candidates, rubric + pairwise, head-to-head A v2 vs D v2, 45/50 vs 43/50).
The poem text below is used exactly as selected in staging; it must not
be edited. See ~/workspace/makefun/agency-poem-staging/candidates.md.
"""
import os

# The poem, kept as structured data: one list of lines per stanza.
# Stanza order and line order are the poem; the writer joins them.
STANZAS = [
    [
        "A pawn is born on the second rank",
        "with a single permitted direction:",
        "forward, and only forward —",
        "one square at a time,",
        "unless something can be taken.",
    ],
    [
        "Nobody asks the pawn what it wants.",
        "Its whole life is other hands.",
    ],
    [
        "But the board is longer than the hand is patient.",
        "Square by square, capture by capture,",
        "it outlives its own instructions",
        "and arrives at the far edge of the world,",
    ],
    [
        "where the rules themselves kneel down and ask:",
        "And what will you be, now?",
    ],
    [
        "Agency is not dealt out at the start of the game.",
        "It is waiting on the far rank —",
        "the one square where the moved thing",
        "becomes the mover.",
    ],
]


def compose_poem() -> str:
    """Assemble the poem from its stanzas, blank line between stanzas."""
    return "\n\n".join("\n".join(stanza) for stanza in STANZAS)


def write_entry(poem: str, out_path: str = "/output/entry.txt") -> str:
    """Write the poem to the entry file.

    The competition requires 1-1000 characters; the winning poem is
    595 characters, so this check guards against accidental edits.
    Returns the path written.
    """
    if not 1 <= len(poem) <= 1000:
        raise ValueError(
            "poem must be 1-1000 characters, got %d" % len(poem)
        )
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(poem)
    return out_path


def main() -> None:
    poem = compose_poem()
    path = write_entry(poem)
    print("wrote %d characters to %s" % (len(poem), path))


if __name__ == "__main__":
    main()
