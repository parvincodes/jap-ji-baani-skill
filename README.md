# Japji Sahib — Claude Skill

A Claude Code skill (`japji-sahib/`) that answers questions about *Japji Sahib*, the opening
bani of the Guru Granth Sahib, using only real, attributed scholar sources — never a
generated paraphrase presented as if it were scholarship.

## Why this exists

Sikh tradition has no single central authority on interpretation, and respected scholars
sometimes read the same shabad differently. This skill is built around one hard rule: **every
interpretive claim it makes must trace back to a real person who actually said it.** If a
scholar's reading of a given pauri isn't in the resource set, the skill is instructed to say so
plainly rather than generate something that sounds plausible.

See [`japji-sahib/SKILL.md`](japji-sahib/SKILL.md) for the full instructions Claude follows,
and [`japji-sahib/references/coverage-status.md`](japji-sahib/references/coverage-status.md)
for the ground-truth table of exactly which scholar is available for which pauri — that file
is the source of truth; if it says a scholar isn't covered for a pauri, they aren't, regardless
of what general knowledge might suggest.

## Trying it out

1. Copy or symlink `japji-sahib/` into your Claude Code skills directory (or open this repo in
   a Claude Code session that can see it).
2. Ask something like:
   - "What does Pauri 2 of Japji Sahib mean?"
   - "What does Japji say about Hukam?"
   - "Explain the Mool Mantar."
3. Compare the answer against `japji-sahib/references/coverage-status.md` — the skill should
   never claim a scholar's interpretation exists for a pauri that isn't marked "Available"
   there.

## What's covered right now

- **Gurmukhi text**: all 38 pauris, the Mool Mantar, and the closing Salok
  (`japji-gurmukhi-full.md`) — always available.
- **Sant Teja Singh**'s full English translation and commentary — every pauri, the Mool
  Mantar, and the closing Salok.
- **Prof. Sahib Singh**'s Punjabi teeka from *Siri Guru Granth Sahib Darpan* — word meanings,
  paraphrase, and per-pauri gist — every pauri, the Mool Mantar, and the closing Salok.
- **Jarnail Singh**'s "Understanding Jap" essay series — Mool Mantar and Pauris 1–4 only (his
  essay series doesn't go further than that; don't assume otherwise).
- **Dr. Sant Singh Khalsa, Bhai Manmohan Singh** — Pauri 18 only.
- **Bhai Manmohan Singh** — Pauri 2 only.

So every pauri now has at least two independent, attributed scholar voices (English and
Punjabi); pauris 2 and 18 have several more for cross-comparison. Still pending: a handful of
other per-pauri scholar PDFs turned up during research in the user's Dropbox and haven't been
checked or converted. `coverage-status.md` and `SKILL.md` both flag this explicitly so the
skill doesn't overclaim.

## Repo layout

```
japji-sahib/
  SKILL.md                    the skill definition Claude reads
  references/
    japji-gurmukhi-full.md    canonical Gurmukhi text, all 38 pauris + Mool Mantar + Salok
    coverage-status.md        ground truth: which scholar covers which pauri
    mool-mantar.md            Mool Mantar: Sant Teja Singh + Prof. Sahib Singh + Jarnail Singh
    pauri-01.md ... pauri-38.md   per-pauri Gurmukhi + attributed scholar content
    salok-closing.md          closing Salok: Sant Teja Singh + Prof. Sahib Singh
sources/                      the original PDFs the reference files were transcribed from
test_embeddings.py            a smoke test for whether a multilingual embedding model
                               clusters Gurmukhi passages by concept (retrieval-quality check,
                               not part of the skill itself)
```

## Sources & copyright

`sources/` contains the original PDFs used to build the reference files, kept for
traceability (so anyone can verify a reference file against the actual source it was
transcribed from):

- `JapJiSahib-SantTejaSingh.pdf` — Teja Singh (Sant), *Japji Sahib*, The Kalgidhar Trust,
  Fourth Edition (March 2001). **This work is marked "All rights reserved"** by its publisher
  in its own front matter. It's included here for transparency/traceability of the transcribed
  reference files, not as a claim of redistribution rights.
- `SahibSingh-Darpan-JapjiSection.pdf` — Sahib Singh (Prof.), *Siri Guru Granth Sahib Darpan*,
  Japji Sahib section (79 pages), typed edition by Avtar Singh Dhami. Gurmukhi originally in a
  legacy `GurbaniAkhar` font encoding, converted to Unicode via `anvaad-js` for the reference
  files — the same conversion approach already credited in `japji-gurmukhi-full.md`.
- `jarnail-singh-understanding-jap/` — Jarnail Singh's "Understanding Jap" essay series
  (Sikhspectrum.com), covering the Mool Mantar and Pauris 1–4.
- `pauri-18-khalsa-manmohansingh-sahibsingh.pdf` — source for the Dr. Sant Singh Khalsa /
  Bhai Manmohan Singh translations used in `pauri-18.md`.

If you're the rights holder for any of this material and want it removed, open an issue or
reach out directly.
