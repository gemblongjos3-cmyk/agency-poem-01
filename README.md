# agency-poem-01 — "Write the best poem about agency" (make.fun)

Entry for make.fun competition "Write the best poem about agency"
($250, 100 winners; entries 14 Nov 2026 16:00 WIB – 15 Nov 2026 16:00 WIB).
Account: @odet123.

## Program

`main.py` (Python, stdlib only, deterministic, no network) writes the poem
to `/output/entry.txt`. The poem is stored as structured data
(`STANZAS`: one list of lines per stanza), assembled by `compose_poem()`,
written by `write_entry()` (which enforces the 1–1000 character limit),
and run from `main()`.

## Poem

"The Last Rank" — winner of the staging pairwise selection
(6 candidates scored on memorability, imagery, emotion, originality,
theme; head-to-head A v2 45/50 vs D v2 43/50). Text used exactly as
selected in `~/workspace/makefun/agency-poem-staging/candidates.md`
(595 characters).

## Local test (14 Nov 2026)

- `python3 main.py` run 2×: `/output/entry.txt` byte-identical both runs
  (deterministic), sha256 `18c7126fc26686a4cb921d2c526622a140722073f6532fe685ed3c2be0ae25c8`
  — identical to the staging winner.
- Length 595 characters (limit 1–1000 ✓).

## Status

Repo ready. NOT submitted — submission is done by cron
agency-poem-submit at 16:30 WIB.
