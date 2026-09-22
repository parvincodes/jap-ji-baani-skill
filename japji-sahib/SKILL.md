---
name: japji-sahib
description: Answers questions about Japji Sahib, the opening bani of the Guru Granth Sahib — explaining specific pauris/lines, thematic questions across the whole bani (e.g. what it says about ego, Hukam, truth), and general Q&A about its meaning. Always trigger this skill for any question involving Japji Sahib, Jap Ji, Mool Mantar, or specific pauris of Japji, even if the user doesn't name the skill explicitly — e.g. "what does pauri 2 mean," "what does Japji say about ego," "explain this line of Jap Ji." Use this instead of answering from general knowledge, because this skill is grounded in specific, attributed, verified sources rather than a generated summary.
---

# Japji Sahib

This skill answers questions about Japji Sahib using real, attributed sources — never a generated paraphrase presented as if it were scholarship. Sikh tradition has no single central authority on interpretation; respected scholars sometimes read the same shabad differently. This skill reflects that directly rather than picking one "correct" answer.

## Why this matters

The point of this skill is trust, not just fluency. Someone using this — likely a student — should be able to trace every interpretive claim back to a real person who said it. Do not generate an interpretation of a line in your own voice and present it as if it were scholarly. If the resource set doesn't have a scholar's take on something, say so plainly instead of filling the gap.

## How to answer a question about a specific pauri

1. Look up the pauri in `references/japji-gurmukhi-full.md` — this has the complete, verified Gurmukhi text for all 38 pauris plus the Mool Mantar and closing Salok. Always show the Gurmukhi and the pauri number for whatever you're discussing.
2. Check `references/coverage-status.md` to see which scholars have interpretations available for that specific pauri.
3. If a dedicated `references/pauri-NN.md` file exists for that pauri (currently: `pauri-01.md` through `pauri-38.md`, plus `mool-mantar.md` and `salok-closing.md`), read it — it has the actual scholar translations/teeka, attributed by name.
4. Structure the answer as:
   - The Gurmukhi text of the pauri (or the specific line asked about), with its pauri number
   - Each available scholar's interpretation, clearly attributed by name (e.g. "Prof. Sahib Singh's teeka says...", "Bhai Manmohan Singh translates this as...")
   - If Jarnail Singh's commentary is available for that pauri, include it as its own attributed voice, not blended into the others
5. If a scholar's interpretation for that pauri isn't in the resource set, say so directly — e.g. "Prof. Sahib Singh's teeka isn't available for this pauri in what I have on file." Do not paraphrase what you'd expect them to say.

## How to answer a thematic / cross-pauri question

Example: "What does Japji say about ego?" or "Where does it talk about Hukam?"

1. Search `references/japji-gurmukhi-full.md` for relevant Gurmukhi terms (e.g. ਹਉਮੈ for ego/haumai, ਹੁਕਮੁ for Hukam, ਨਾਮੁ for Naam) to find which pauris are actually relevant — don't guess which pauris are relevant from memory.
2. Cross-reference against `references/coverage-status.md` to see which of those pauris have scholar commentary available.
3. Answer with the pauris that are actually relevant, and be explicit about which have full scholar backing and which only have the Gurmukhi text so far. A partial, honest answer ("Pauri 2 develops this at length per Jarnail Singh's essay; the term also appears in pauris X and Y but I don't have scholar commentary on those yet") is much better than a confident answer synthesized from general knowledge of Sikhi.
4. Never present a "summary of what Japji says about X" that isn't actually traceable to the specific pauris and scholars in the resource set.

## Resource files

- `references/japji-gurmukhi-full.md` — the complete Gurmukhi text of Japji Sahib, labeled by pauri, always usable
- `references/coverage-status.md` — the ground-truth table of which scholar covers which pauri; consult this before claiming any interpretation exists
- `references/mool-mantar.md`, `references/pauri-01.md` through `pauri-38.md`, `references/salok-closing.md` — Gurmukhi plus two full-bani scholar sources for every pauri, the Mool Mantar, and the closing Salok:
  - **Sant Teja Singh**'s English translation/commentary (attributed, from his published *Japji Sahib*, The Kalgidhar Trust).
  - **Prof. Sahib Singh**'s Punjabi teeka from *Siri Guru Granth Sahib Darpan* (word meanings, paraphrase, and per-pauri gist, attributed, converted from the source PDF's legacy Gurmukhi font to Unicode).
  The Mool Mantar and pauris 1–4 additionally carry Jarnail Singh's "Understanding Jap" essay (his essay series only covers these five sections — don't assume it goes further); `pauri-02.md` and `pauri-18.md` additionally carry Bhai Manmohan Singh; `pauri-18.md` additionally carries Dr. Sant Singh Khalsa — each scholar's voice kept in its own section, never blended.

## Extending this skill

Sant Teja Singh's translation and Prof. Sahib Singh's Darpan teeka now give every pauri two sourced scholar voices; the Mool Mantar and pauris 1–4 additionally have Jarnail Singh's essay, and pauris 2 and 18 have several scholars for cross-comparison. Still pending: a handful of other per-pauri scholar PDFs turned up in the user's Dropbox `Jap Bani` folder and haven't been checked or converted — don't assume any untranscribed source's coverage for a pauri until it's actually been added. To add a new scholar's coverage for a pauri:
1. Add a new `### <Scholar Name>` section to the existing `references/pauri-NN.md` (or create it, following the same structure, if the pauri file doesn't exist) — the actual translation/teeka, clearly attributed, sourced from a real document (not generated), kept separate from other scholars' sections.
2. Update the table in `references/coverage-status.md` to reflect the new coverage.
Don't add a scholar's name to the coverage table unless their actual translation text is present in that pauri's reference file.
