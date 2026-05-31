# Publish Normalization Spec — VistA Docs Corpus

**Status:** Draft 1 (design, not yet implemented)
**Author:** Rafael + Claude
**Date:** 2026-05-31
**Applies to:** `vista-docs` pipeline, `consolidate` → `publish` stages
**Related:** `vdl-pipeline` skill, `vdl` skill, `va-docx-structure` skill,
[`docs/vdl-arch-overview.md`](vdl-arch-overview.md)

> **Reality check (from repo, 2026-05-31):** the ingest converter is **pandoc**
> (`src/vista_docs/ingest/converter.py` — DOCX → GFM, + LibreOffice headless for
> EMF/WMF → PNG). Docling is only an *optional* dep referenced in post-processing.
> `consolidate` is `src/vista_docs/analyze/consolidate.py`; `publish` is
> `src/vista_docs/publish/{builder,runner,url_map}.py`. Frontmatter is owned by
> stage 6 `pipeline/audit_frontmatter.py`, which already manages the reserved keys
> `has_toc`, `page_count`, `revision_count`, `revision_newest`, `revision_oldest`,
> and `description`. The heading tree already exists (stage 6.5
> `pipeline/chunk_sections.py`), and heading-shape analysis already exists
> (`vista-docs headings` → `~/data/vista-docs/survey/heading_analysis/`). This
> spec **reuses** that machinery rather than duplicating it.

---

## 1. Purpose

The published corpus (`publish/`, ~1,464 docs across 137 packages) is being
promoted to the **gold source** for VistA documentation, replacing the original
MS-Word/PDF originals. The pandoc-converted markdown carries forward a number of
artifacts of its paper/Word origin that are now noise:

- **Page numbers** — meaningless in a paginated-source-free medium.
- **"Revision History" tables** — manual MS-Word version control, dumped inline
  at the top of every document.
- **Redacted `Project Manager` / `Technical Writer` columns** — uniformly
  `Redacted` / `N/A`, carrying zero information.
- **Layout whitespace** — giant space runs, form-feeds, repeated running
  headers/footers replayed by pandoc from Word layout.

This spec defines a **`normalize` stage** that converts faithful pandoc output
into clean, GitHub-ready gold markdown **without losing any navigational or
structural information** present in the originals. Every lossy decision is
recorded in frontmatter or a sidecar so it is auditable and reversible.

## 2. Goals / Non-goals

**Goals**
1. Remove visual noise (page numbers, layout whitespace, redaction placeholders).
2. Demote — not delete — revision history into a structured sidecar + frontmatter
   summary.
3. Give every document a portable, link-based table of contents.
4. Preserve all available navigation: Word bookmarks, original TOC entries, and
   (for paginated-only docs) original page positions, in a form that can later be
   converted to links and then retired.
5. Recover structure from docs that have inconsistent or no headings.
6. Make the markdown defensibly authoritative via reproducible provenance.

**Non-goals**
- Rewriting prose or correcting source content.
- Hand-editing `consolidated/` (it stays the lossless pandoc output).
- Perfect fidelity for hopeless inputs — degrade gracefully and *record* the
  degradation.

## 3. Pipeline placement

`normalize` is a new stage between `consolidate` and `publish`:

```
raw/        ─ingest(pandoc)→  md-img/      ─enrich/audit→  (frontmatter)
(Word/PDF)                     (markdown)
   │
   └─consolidate→  consolidated/  ─NORMALIZE→  (clean md + sidecars)  ─publish→  publish/
                   (faithful,                                                     (gold, re-organized
                    never hand-edited)                                            by domain)
```

- `consolidated/` is the **lossless** layer. Never hand-clean it; `normalize`
  must be re-runnable from it at any time.
- `normalize` is **idempotent** and **reversible** (all dropped data lands in
  frontmatter or sidecars).
- `publish/` is the gold output, re-organized by domain
  (`clinical` / `financial-administrative` / `infrastructure` /
  `vista-gui-hybrids`) + full package name, as it is today.

**Implementation home** (per project architecture rules in `CLAUDE.md`): a new
`src/vista_docs/normalize/` package — pure transforms in `*_pure*.py` (zero I/O,
plain-values-in/out, unit-tested first), thin I/O wrappers tested in integration.
Wire into the `publish` stage (run before re-org/copy) or expose as
`vista-docs normalize [--pkg ...] [--force]`. Frontmatter writes route **through**
stage 6 `audit_frontmatter.py`, the single owner of canonical keys.

## 4. Current-state evidence (from `consolidated/cprs/um/cprs_user_manual__gui_version.md`)

- Frontmatter already reserves the target fields, currently empty/placeholder:
  `revision_count: 0`, `revision_newest: null`, `revision_oldest: null`,
  `has_toc: false`, `page_count: 0`, plus provenance `docx_url` / `pdf_url`.
- `description:` is **polluted** with the revision-table caption
  (`description: Revision HistoryThis table lists the history...`) — a bug to fix
  during extraction.
- Revision history is a pandoc **raw-HTML `<table>`** with columns
  `Date | Version/Patch | Page | Change | Project Manager | Technical Writer`.
  PM/TW cells are uniformly `Redacted` / `N/A`.
- `Change` cells contain **live Word anchors**: `<a href="#_Toc112615110">`,
  `<a href="#OrderingInpatientSimple">`.
- `Page` cells are a **mix** of plain numbers (`233, 239, 250`) and already-linked
  numbers (`<a href="#Smart_Note_593">170</a>`).
- Body contains pathological whitespace runs (single lines of thousands of
  spaces) from Word layout.

This confirms the building blocks already exist; `normalize` mostly harvests and
relocates them.

## 5. Frontmatter contract (additions)

`normalize` populates the reserved fields and adds new ones. **All keys are owned
by stage 6 `audit_frontmatter.py`** — new keys below must be registered there (and
in the §11 schema) or audit will strip them. Reserved keys that already exist and
are merely *populated* here: `has_toc`, `page_count`, `revision_count`,
`revision_newest`, `revision_oldest`, `description`. New/changed keys:

```yaml
# --- TOC / anchors ---
has_toc: true
toc: generated            # generated | original | none
anchors_source: word      # word | inferred | mixed | none
anchor_aliases:           # legacy bookmark -> current slug (may be empty)
  _Toc112615110: ordering-inpatient-medications-simple-dose
  OrderingInpatientSimple: ordering-inpatient-medications-simple-dose

# --- revision history (summary; full data in sidecar) ---
revision_count: 14
revision_newest: "2023-06"
revision_oldest: "2014-08"
revision_sidecar: cprs_user_manual__gui_version.history.yaml

# --- pagination bridge (only when source was paginated-only) ---
page_anchors: false       # true while p<N> anchors are still embedded
page_count: 612           # provenance only; not rendered

# --- provenance (makes markdown defensibly 'gold') ---
source_sha256: "<hash of raw docx/pdf>"
converter: "pandoc <version>"      # ingest converter (DOCX→GFM)
normalized_at: "2026-05-31"
normalize_version: "1.0"

# --- bugfix ---
description: "CPRS GUI user guide for clinical end users."   # de-polluted
```

A **JSON Schema** for frontmatter is maintained and validated in CI (§13).

## 6. Transforms

Transforms run in the order listed (§12). Each is independently testable.

### F1 — Whitespace / layout denoise
- Strip runs of ≥6 consecutive spaces to a single space (or remove if leading
  layout padding).
- Remove form-feeds (`\f`) and other control chars.
- Collapse ≥3 blank lines to 1.
- Trim trailing whitespace.
- **Idempotent**; safe on all doc classes. Run first.
- *Note:* some F1 cleanup may already belong in `ingest/postprocess.py`; if so,
  fix it upstream there rather than duplicating a denoiser. Decide during prototype.

### F2 — Running header/footer stripping
- Detect lines repeated near page-boundary cadence matching a template, e.g.
  `<Doc Title> <Month Year> Page N` or `Page N of M`.
- Build the repeated-line template per document (fuzzy match on the variable
  page-number token); delete matches.
- Record count removed in a normalize log (not in the doc).

### F3 — Heading inference / promotion *(highest-value transform)*
For docs where pandoc flattened headings to paragraphs:
- **Reuse the existing heading analysis** (`vista-docs headings` →
  `survey/heading_analysis/`) to separate boilerplate from real structure rather
  than re-deriving detection from scratch.
- Detect heading-like lines: ALL-CAPS short lines, numbered prefixes
  (`1`, `1.2`, `1.2.3`), `Chapter N` / `Appendix X`, underlined text, bold-only
  short paragraphs.
- Promote to `#`/`##`/`###` by inferred depth (numbering depth, caps, font cues
  surviving as `**`/`<u>`).
- Set `anchors_source: inferred` (or `mixed`) when promotion occurs.
- Conservative: when ambiguous, **do not** promote; log the skip.

### F4 — Anchor assignment + alias map
- Slug every heading with the **GitHub slug algorithm** (lowercase; spaces→`-`;
  strip punctuation except `-`; de-dupe with `-1`, `-2`).
- Where the heading (or an adjacent `<span id="...">`) carries a legacy Word
  bookmark (`_Toc…`, named bookmark), record `legacy_id -> slug` in
  `anchor_aliases`. If the id sits on an adjacent span, **hoist** it onto the
  heading so the slug and the legacy id resolve to the same target.
- A late step (F8) rewrites in-document `#legacy_id` references to slugs using
  this map.

### F5 — Revision history extraction
1. Locate the revision `<table>` (raw HTML or GFM) following the title block.
2. Parse rows into structured records, **dropping the `Project Manager` and
   `Technical Writer` columns** (uniformly redacted, zero information).
3. Keep `Date`, `Version/Patch`, `Change`, and `Page` (Page retained as
   link-recovery fuel; see F7). Preserve any anchors embedded in `Change`/`Page`
   cells as a `refs:` list.
4. Write the **sidecar** (§7); populate frontmatter summary
   (`revision_count`, `revision_newest`, `revision_oldest`, `revision_sidecar`).
5. **Remove the table from the body.**
6. **Fix `description:`** — if it begins with the revision caption, regenerate
   from doc type/audience or clear it.

### F6 — TOC generation
- **Source the heading tree from stage 6.5 `chunk_sections.py`** (already builds
  the H1–H3 tree + FTS5 index) instead of re-parsing headings.
- Build a link TOC from `H1–H3` using the slugs from F4:
  ```markdown
  ## Contents
  - [Ordering Inpatient Medications (Simple Dose)](#ordering-inpatient-medications-simple-dose)
    - [Complex Dose](#complex-dose)
  ```
- Insert after the title block (and after any preserved original-TOC note).
- Set `has_toc: true`, `toc: generated`.
- For docs that *had* a usable original TOC with anchors, prefer regenerating
  from headings anyway (uniform output); keep the original only as sidecar data
  if it carried page references needed by F7.

### F7 — Page-number bridge (paginated-only docs)
For old docs with **no internal anchors but real page numbers**:
1. **Pagination oracle = the PDF** (`pdf_url`), not the .docx (Word computes page
   numbers at render; .docx does not store them). Extract per-page text, align to
   the markdown, inject **silent** anchors at page starts:
   ```markdown
   <a id="p123"></a><!-- page 123 -->
   ```
   Set `page_anchors: true`.
2. Preserve the original TOC (with its page targets) as sidecar data
   (`original_toc:`), each entry pointing at `#p<N>`.
3. **Resolution step (later run):** map each `p<N>` to the nearest *following*
   heading slug; rewrite original-TOC links from `#p<N>` to `#slug`.
4. **Retirement step:** once resolved, delete the `p<N>` anchors and
   `<!-- page -->` comments; set `page_anchors: false`. `page_count` remains in
   frontmatter as provenance only.

This realizes preserve → bridge → retire, each stage reversible via sidecar.

### F8 — Link rewrite + dead-link sweep
- Rewrite `#legacy_id` → `#slug` via `anchor_aliases` (in body, TOC, and sidecars).
- Resolve textual cross-doc references ("see the X manual") to real links where a
  corpus anchor index match exists (best-effort; log misses).
- Fail CI on any remaining dangling in-document anchor.

### F9 — Figures / captions
- Images are bare `![](dir/001.png)`. Recover nearby `Figure N: …` text into the
  alt/title: `![Figure 3: Order entry dialog](dir/003.png)`.
- Improves searchability and accessibility.

### F10 — Table policy
- Simple tables → GFM pipe tables.
- Complex tables (colspans, nested lists/paragraphs in cells) → keep as raw HTML.
- Never force-convert complex tables (corruption risk).

## 7. Sidecar conventions

Sidecars live **next to the document**, sharing its basename:

```
cprs_user_manual__gui_version.md
cprs_user_manual__gui_version.history.yaml      # revision history (F5)
cprs-user-manual-gui-version-updated-or-3-0-499/ # existing image asset dir
```

**Revision history sidecar** (`*.history.yaml`):
```yaml
document: cprs_user_manual__gui_version.md
source_docx: https://www.va.gov/vdl/.../cprsguium.docx
revisions:
  - date: "2023-06"
    version: "OR*3*499"
    pages: [233, 239, 250, 254, 322, 328, 334, 339, 358, 361, 562]
    change: >
      Added OR ZIP CODE MESSAGE warning and updated DEA required dialogs.
    refs: ["#_Toc112615110", "#OrderingInpatientSimple"]
  - date: "2023-05"
    version: "OR*3.0*593"
    pages: [170]
    change: "Added note for SMART alerts; removed copy-order instructions."
    refs: ["#Smart_Note_593"]
```

**Original-TOC sidecar** (only for F7 docs; `*.toc.yaml`):
```yaml
original_toc:
  - title: "Agent Cashier Menu"
    page: 123
    anchor: "#p123"      # later rewritten to #slug, then page anchors retired
```

Optional derived artifact: a per-package `CHANGELOG.md` **generated** from the
`*.history.yaml` sidecars — never hand-authored.

## 8. Document classification

`normalize` branches on detected structure; classification recorded in
`anchors_source` + `toc`:

| Class | Has headings? | Has anchors? | TOC strategy | Page bridge |
|-------|---------------|--------------|--------------|-------------|
| A — modern | yes | Word bookmarks | F6 generated + F4 aliases | no |
| B — headings only | yes | none | F6 generated | no |
| C — flat + paginated | no (infer via F3) | none | F3→F6 generated | F7 if PDF available |
| D — hopeless | no, infer fails | none | `toc: none` | log + skip |

## 9. Provenance

Every published doc records, in frontmatter: `source_sha256`, `converter`,
`normalized_at`, `normalize_version`, and the existing `docx_url`/`pdf_url`.
This is what lets the markdown be cited as authoritative — it is verifiably
reproducible from a known raw source by a known toolchain version.

## 10. Reversibility & idempotency

- Re-running `normalize` on already-normalized input must be a no-op (detect via
  `normalize_version` + content markers).
- All dropped data (revision rows, PM/TW columns are the only true deletion;
  everything else) is recoverable from `consolidated/` + sidecars.
- The page bridge (F7) is staged so each step is independently reversible.

## 11. Validation / CI

1. **Frontmatter schema** validation (JSON Schema).
2. **Dead-anchor check** — no dangling `#…` in any published doc.
3. **Noise linter** — fail on residual page-number-only lines, ≥6-space runs,
   form-feeds, `Redacted` PM/TW cells.
4. **Sidecar integrity** — every `revision_sidecar` path resolves; every sidecar
   `document` back-reference resolves.
5. **Anchor index** emitted to `survey/` (`doc → {headings, slugs, aliases}`),
   derivable from the stage 6.5 chunk/heading tree — used by F8 cross-doc link
   resolution and the dead-anchor check.

## 12. Canonical processing order

```
F1 denoise
F2 header/footer strip
F3 heading inference
F4 anchor assignment + alias map
F5 revision extraction (+ description fix)
F6 TOC generation
F7 page bridge (paginated-only)        # inject anchors now; resolve/retire later
F9 figures/captions
F10 table policy
F8 link rewrite + dead-link sweep      # last: needs all anchors finalized
CI validation
```

(F8 runs last because it depends on every anchor being finalized.)

## 12a. Implementation mapping (`src/vista_docs/normalize/`)

Per repo architecture (pure/IO split, TDD, one test file per module):

| Transform | Pure module (`normalize/*_pure*.py`) | Reuses existing |
|-----------|--------------------------------------|-----------------|
| F1 denoise | `denoise_pure.py` | maybe fold into `ingest/postprocess.py` |
| F2 header/footer | `boilerplate_pure.py` | `survey/heading_analysis/` boilerplate stats |
| F3 heading inference | `heading_infer_pure.py` | `vista-docs headings` output |
| F4 anchors + aliases | `anchors_pure.py` | GitHub slug algo (new, pure) |
| F5 revision extraction | `revision_pure.py` (+ sidecar writer in I/O layer) | feeds `audit_frontmatter` keys |
| F6 TOC | `toc_pure.py` | stage 6.5 `chunk_sections.py` heading tree |
| F7 page bridge | `page_bridge_pure.py` (+ PDF reader I/O) | `raw/` PDFs, `pdf_url` |
| F8 link rewrite | `linkfix_pure.py` (+ anchor-index I/O) | survey anchor index |
| F9 figures | `figures_pure.py` | — |
| F10 tables | `tables_pure.py` | — |

I/O wrappers (sidecar read/write, PDF text extraction, file walk) live in thin
modules listed in `[tool.coverage.run] omit`. Frontmatter mutation routes through
`audit_frontmatter.py`. New runtime dep for F7 (PDF text): evaluate
`pypdf`/`pdfplumber`; add via `uv lock` per CLAUDE.md.

## 13. Open questions / verification items

1. **Anchor location:** confirm whether pandoc placed `_Toc…` ids *on* headings
   or on adjacent `<span id="...">`s — F4's hoist logic depends on this. (Evidence
   so far shows `<span id="...">` siblings.) Verify on the CPRS GUI prototype.
2. **PDF availability/alignment:** how many Class-C docs have a usable `pdf_url`,
   and how reliable is per-page text alignment? May need a fallback for
   PDF-less paginated docs (e.g., keep original-TOC page text as plain,
   non-linked reference).
3. **`description` regeneration:** rule for de-polluted descriptions — derive
   from `doc_label` + `audience`, or leave blank?
4. **CHANGELOG generation:** per-package, per-doc, or both?
5. **Slug collisions across the anchor index** for cross-doc link resolution
   (F8) — namespace by doc path.

## 14. Rollout

1. **Prototype on one doc end-to-end:**
   `~/data/vista-docs/consolidated/cprs/um/cprs_user_manual__gui_version.md` (has
   both Word anchors *and* a redacted revision table — exercises F1–F6, F8–F10).
   Produce cleaned body + `.history.yaml` + frontmatter diff for review.
2. Add a **Class-C** prototype (flat + paginated, with a PDF) to exercise F7.
3. TDD each pure transform (`make test` / `make watch`), then `make check`.
4. Review outputs; lock `normalize_version: 1.0`.
5. Batch-run via `vista-docs normalize` (or folded into `make publish`); run
   `make validate` hard gate; spot-audit per domain; then `make publish-push`.

## 15. Docs to update on implementation

Per CLAUDE.md "update docs in the same commit" rule:
- `src/vista_docs/README.md` — new `normalize` stage I/O.
- `pipeline/README.md` + stage list in `CLAUDE.md` — insert the normalize stage.
- `docs/vdl-arch-overview.md` — add the stage to the ASCII/Mermaid flow.
- `~/claude/skills/vdl-pipeline/SKILL.md` — operating notes + new frontmatter keys.
- `~/claude/skills/va-docx-structure/` — revision-table + page-anchor patterns.
