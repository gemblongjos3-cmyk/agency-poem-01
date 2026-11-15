#!/usr/bin/env python3
"""make.fun agency-poem-01 entry (@odet123).

Competition: "Write the best poem about agency" ($250, 100 winners).
The program writes the winning poem to /output/entry.txt.
Deterministic, stdlib only, no network.

Poem: "In Her Own Hand" — winner of the staging round-2 pairwise
selection (3 candidates, rubric + pairwise, 46/50 vs 44/50 vs 43/50),
final text set by the user (981 characters). Revision of the round-1
entry "The Last Rank" (judge 66,3%): the old poem was 595 characters
of abstract chess metaphor; the revision is a concrete human scene
at the length of the leaderboard's top cluster (950-990 characters),
closing on an aphorism instead of an explanation.
The poem text below reproduces the user-approved final file exactly;
it must not be edited. See
~/workspace/makefun/agency-poem-staging/final-in-her-own-hand.txt and
candidates-r2.md.
"""
import os

# The poem, kept as structured data: one list of lines per stanza.
# Stanza order and line order are the poem; the writer joins them.
STANZAS = [
    [
        'The nurse slid the form across and, kindly, reached to steady her hand.',
        '"I\'m not dead yet," Marla said, and took the pen alone.',
    ],
    [
        'For sixty years other hands had signed her name.',
        "Her father's, when she was a girl who needed permission.",
        "Her husband's, when the marriage made one signature do for two.",
        "Her son's, these last soft years, while she watched her own name",
        'come out of his pen neat, quick, and nothing like her.',
    ],
    [
        'Her hand shook. The M leaned like a fence post after weather.',
        'The a trailed off the line and had to be gathered back.',
        'It took her a full minute to write what he wrote in two seconds,',
        "and the nurse's kind hand hovered the whole time, unlanded.",
        'The pen felt heavier than any pen she had held.',
    ],
    [
        'When she finished, the name on the form was crooked,',
        'and slow, and spelled in a hand nobody else alive could write.',
    ],
    [
        'She put the pen down like a flag going into ground she had just taken.',
    ],
    [
        'It was the worst signature of her life.',
        'It was the first one that was only hers.',
    ],
]


def compose_poem() -> str:
    """Assemble the poem from its stanzas, blank line between stanzas."""
    return "\n\n".join("\n".join(stanza) for stanza in STANZAS)


def write_entry(poem: str, out_path: str = "/output/entry.txt") -> str:
    """Write the poem to the entry file.

    The competition requires 1-1000 characters; the winning poem is
    981 characters, so this check guards against accidental edits.
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
