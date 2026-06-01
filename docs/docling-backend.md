# Docling ingest backend — rationale & expansion criteria

The INGEST stage (`src/vista_docs/ingest/converter.py`) routes per-document between two
DOCX→markdown backends: **Pandoc** (the default, ~99% of the corpus) and **Docling**
(an explicit allowlist, `DOCLING_DOCS = {cprsguium, constm}`). This note records *why*
the allowlist is two documents and *how to decide* whether to add more — the corpus
evidence behind the decision, so it isn't lost if the original spike repo is archived.

## The problem Docling fixes

A handful of VA DOCX wrap their lists and headings in Word `[[…]](#_Toc…)` cross-reference
fields. Pandoc detaches the marker from its content, exploding each list into thousands of
**bare markers** (a list marker alone on a line — `^\s*(?:\d+\.|[-*])\s*$`). Docling
reconstructs the lists cleanly: on `cprsguium.docx`, bare markers drop **3,058 → 0** and
properly-formed list items rise **267 → 3,226**. No regression on already-clean docs.

## Why an allowlist, not a corpus-wide switch

A corpus-wide pandoc sweep of all 2,983 raw DOCX (same bare-marker metric) found the
problem is **concentrated in essentially one document**, not corpus-wide:

| Band (bare-marker ratio) | Files |
|---|---|
| severe (≥10%)   | **1** — `CPRS/cprsguium.docx` (17.4%) |
| moderate (3–10%)| 11 |
| mild (1–3%)     | 19 |
| trace (<1%)     | 208 |
| clean (0)       | 2,744 |

- **`cprsguium.docx` alone = 65% of every bare marker in the corpus** (3,058 of 4,709);
  the top two files are 73%.
- The heavy `[[…]]` cross-reference pathology Docling fixes best exists in exactly **two**
  documents: `CPRS/cprsguium.docx` (5,073 `[[` wraps) and `GMRC/constm.docx` (2,157).
- 99% of files need nothing. Docling adds a multi-GB ML stack and ~1 min/doc, so paying
  that on the whole batch is unjustified — route the few that need it.

## When to add a document to `DOCLING_DOCS`

- **Strong trigger:** `[[` cross-ref wraps ≥ 50 in the pandoc output → the cross-ref
  explosion Docling fixes cleanly. (Today: exactly `cprsguium`, `constm`.)
- **Optional wider net:** bare-marker ratio ≥ 3% on docs > 500 lines adds ~5–6 real
  manuals (`IBD/aics3_0ig`, `IVMB/ivmb_2_p686_ig`, `PRCA/prca_4_5_p355_ig`, the
  `GMRC/dst_*` group). These are a milder nested-list-flattening mode, not the cross-ref
  explosion — smaller payoff; only worth it if those manuals matter downstream.

**When you do add one, audit every pandoc-format-assuming stage** — each normalize/extract
step was written against pandoc's output shape and silently no-ops on Docling output
(no error, just unprocessed junk). Known dialect splits already handled: revision history
(HTML `<table>` vs GFM pipe table), original TOC stripping, figure/table handling. Expect
more.

## Image handling

Docling's DOCX backend parses **zero** alt-text (0 captions/annotations across all images).
`_run_docling` therefore reads alt-text straight from the DOCX XML (`<wp:docPr descr>`,
collapsing `<mc:AlternateContent>` to its `Choice` to avoid double-counting) and injects
`![alt](…)` refs in document order — the XML picture count aligns 1:1 with Docling's
`<!-- image -->` placeholders, so the ordinal injection is safe. Control then returns to
the existing `_normalize_images()` pass unchanged (NNN.png rename, EMF/WMF→PNG).

## Dependency hygiene

Docling is an **optional extra** (`uv pip install -e '.[docling]'`, pinned
`docling==2.96.0`), imported lazily inside `_run_docling`. The base install stays
pandoc-only; only re-ingesting an allowlisted doc needs the extra. A routed doc ingested
without it **fails loudly** with install instructions.

## Provenance

The full spike — Docling-vs-pandoc comparison, the corpus sweep, the image-injection
prototype (`fix_images.py`), and the integration recommendation — lives in the
`docling-spike` repo (`FINDINGS.md`, `SWEEP.md`, `RECOMMENDATION.md`). The production
integration here implements that repo's recommended option (optional allowlist-routed
Docling backend reusing `_normalize_images`).
