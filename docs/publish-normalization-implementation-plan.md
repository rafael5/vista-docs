# Publish Normalization — Implementation Plan

**Tracks:** [`docs/publish-normalization-spec.md`](publish-normalization-spec.md) (Draft 1, 2026-05-31)
**Plan status:** In progress — 2026-05-31. Pure transform layer (F1–F10 + F3a
unwrap + F8 dead-link sweep), classifier, orchestrator, runner, CLI, CI lint
helpers, and the P0.2 census all built & green (98% cov). See the tracking table
for per-stage status and the Change Log / Lessons #13–14 for the corpus-shape
findings. **Census:** 236 docs → A=122, B=108, C=4, D=2. **The full corpus now validates
`hard=0`** through the publish/push gate (P0–P7 done; P6.3/P7.3 wired). **Remaining:**
PDF page-bridge I/O (P4.1, 4 docs), the P8 rollout (prototype review → lock
`normalize_version 1.0` → batch publish-push), and docs/skills (P9).
**Home:** new `src/vista_docs/normalize/` package; wired before `publish`.
**Conventions:** TDD hard rule (failing test first), pure/IO split, `.venv/bin/`
tools, `make check` (95% cov) before every commit, frontmatter writes route
through stage 6 `pipeline/audit_frontmatter.py` (single owner of canonical keys).

> **How to use this doc.** The tracking table below is the single source of
> truth for progress — update a row's **Status** as you work. Append a dated
> entry to the **Change Log** (§Change Log) for every stage you start/finish,
> in narrative form. Add to **Lessons Learned** whenever the pipeline surprises
> you. Keep the spec (`publish-normalization-spec.md`) as the *what*; this doc
> is the *how* and the *record*.

---

## Tracking Table

**Status legend:** `TODO` not started · `WIP` in progress · `DONE` complete &
verified · `BLOCKED` waiting on a decision/dependency · `REUSE` infrastructure
already exists (from the 2026-05-31 frontmatter-guardrails work) and can be
extended rather than built.

| ID | Phase / Stage | Spec ref | Module / artifact | Status | Tests | Notes |
|----|---------------|----------|-------------------|--------|-------|-------|
| **P0** | **Discovery & scaffolding** | §13, §3, §12a | — | WIP | — | only FM JSON-schema (P0.4) left |
| P0.1 | Verify open questions (anchor span-vs-heading; PDF availability; pandoc version) | §13 | survey notes | DONE | — | resolved: `[[…](#_Toc)]` = nav wrapping, not headings (Lesson #13). `converter:` still literal "pandoc" — capture real version |
| P0.2 | Corpus classification census (Class A/B/C/D counts) | §8 | `survey/normalize_census.csv` | DONE | — | 236 docs → **A=122, B=108, C=4, D=2**; 76 have nav-wrapping; 4 C-docs all have PDFs (F7 effort small). `scripts/normalize_census.py` |
| P0.3 | `normalize/` package skeleton + CLI stub + `[tool.coverage.run] omit` for I/O | §3, §12a | `src/vista_docs/normalize/` | DONE | unit | runner/io/pdf_reader omitted; one test file per pure module |
| P0.4 | Register new frontmatter keys in `audit_frontmatter.py` + JSON-schema scaffold | §5, §11 | `audit_frontmatter.py`, `validate/schema.py` | DONE | ✓ unit | keys registered in audit + validate; `FRONTMATTER_SCHEMA` + committed `frontmatter.schema.json` (drift-guarded) + pure `validate_against_schema` |
| **P1** | **Denoise & boilerplate (F1–F2)** | §6 F1–F2 | — | DONE | — | run first; idempotent |
| P1.1 | F1 whitespace/layout denoise (≥6-space runs, `\f`, ≥3 blank lines, trailing ws) | F1 | `denoise_pure.py` | DONE | ✓ unit | idempotent verified |
| P1.2 | Decide F1-in-ingest vs normalize; reconcile with `ingest/postprocess.py` | F1 note | postprocess vs normalize | BLOCKED | — | F1 lives in normalize for now; upstream-fix decision still open |
| P1.3 | F2 running header/footer strip (per-doc fuzzy template) | F2 | `boilerplate_pure.py` | DONE | ✓ unit | repeated-line + Page-N + isolated-number rules |
| **P2** | **Structure recovery (F3, F4, F6)** | §6 | — | DONE | — | + F3a unwrap added (Lesson #13) |
| P2.1 | F3 heading inference/promotion + F3a unwrap dead `[[…](#_Toc)]` nav wrapping | F3 | `heading_infer_pure.py`, `delink_pure.py` | DONE | ✓ unit | F3a recovers text + kills dead anchors; real headings often lost upstream |
| P2.2 | F4 anchor assignment: GitHub slug algo + `anchor_aliases` | F4 | `anchors_pure.py` | DONE | ✓ unit | alias map (+F8 rewrite) used instead of span-hoist; 122 docs carry Word anchors |
| P2.3 | F6 TOC generation (+ remove original pandoc TOC) | F6 | `toc_pure.py` | DONE | ✓ unit | generates a fresh TOC AND `remove_original_toc` drops the original (slug-resolution signal: a >=6-item link run with >=50% targets = real headings), sweeping its malformed/polluted entries. **Deviation:** sources `extract_headings`, not the stage-6.5 chunk tree |
| **P3** | **Revision history (F5) + sidecars** | §6 F5, §7 | — | DONE | — | 10 docs have revision tables |
| P3.1 | F5 parse revision `<table>`, drop PM/TW cols, structured records + `refs` | F5 | `revision_pure.py` | DONE | ✓ unit | +M/D/YY date handling; CPRS = 243 rows |
| P3.2 | Sidecar writer (`*.history.yaml`) + frontmatter summary | §7, F5.4 | `io.py`/`runner.py` | DONE | (integ) | `revision_count/newest/oldest/sidecar` set |
| P3.3 | `description` de-pollution | F5.6, §13.3 | in F5 path | DONE | ✓ unit | clears revision-caption pollution |
| **P4** | **Page-number bridge (F7)** — Class C | §6 F7 | — | WIP | — | pure parts done; PDF I/O left; only 4 C-docs need it |
| P4.1 | PDF text extraction I/O (eval `pypdf`/`pdfplumber`; `uv lock`) | F7.1 | `pdf_reader.py` | TODO | integration | not built; 4 C-docs all have a PDF |
| P4.2 | Inject silent page anchors (+`original_toc` sidecar) | F7.1–2 | `page_bridge_pure.py` | WIP | ✓ unit | `inject_page_anchors` done; `original_toc` sidecar writer not built |
| P4.3 | Resolution step: map `p<N>` → nearest following heading slug | F7.3 | `page_bridge_pure.py` | DONE | ✓ unit | `map_pages_to_slugs` + `rewrite_page_toc` |
| P4.4 | Retirement step: delete `pN` anchors; `page_anchors: false` | F7.4 | `page_bridge_pure.py` | DONE | ✓ unit | `retire_page_anchors`, idempotent |
| **P5** | **Figures, tables, link rewrite (F9, F10, F8)** | §6 | — | DONE | — | F8 runs last |
| P5.1 | F9 figure caption recovery into alt/title | F9 | `figures_pure.py` | DONE | ✓ unit | caption before/after image |
| P5.2 | F10 table policy (simple→GFM, complex→raw HTML) | F10 | `tables_pure.py` | DONE | ✓ unit | never force-converts complex |
| P5.3 | F8 link rewrite + dead-link sweep | F8 | `linkfix_pure.py` | DONE | ✓ unit | rewrite + `sweep_dead_links` (after aliasing; handles bracketed text, footnotes, nested links to a fixpoint → **235/236 docs end with 0 dead anchors**). **Open:** cross-doc resolve not built; 1 doc has a malformed unescaped-`]` link left for the CI flag |
| **P6** | **Orchestration & classification** | §8, §12 | — | DONE | — | idempotent pipeline |
| P6.1 | Document classifier A/B/C/D → `anchors_source`/`toc` | §8 | `classify_pure.py` | DONE | ✓ unit | drives census |
| P6.2 | `normalize` runner (F1→…→F8) + idempotency | §10, §12 | `normalize_pure.py`, `runner.py` | DONE | ✓ unit | **deviation:** idempotency via `consolidated/`→`normalized/` regen (sibling tree), not an in-place `normalize_version` guard |
| P6.3 | CLI `vista-docs normalize`; wire into `publish` | §3 | `cli/main.py`, `publish/{runner,builder}.py` | DONE | ✓ unit | CLI done (stage 9.5); **publish consumes `normalized/` bodies** when present (per-doc fallback to consolidated; images still from consolidated; `normalized_candidate` pure+tested). Smoke: 10 CPRS bodies swapped, images intact |
| **P7** | **Provenance & validation/CI** | §9, §11 | — | WIP | — | builds on guardrails session |
| P7.1 | Provenance fields (`source_sha256`, `converter`, `normalized_at`, `normalize_version`) | §9 | runner + audit keys | DONE | ✓ unit | sha256 best-effort from `raw/` |
| P7.2 | Extend validator: dead-anchor, noise linter, sidecar integrity, FM JSON-schema, anchor-index emit | §11 | `lint_pure.py`, `index_pure.py`, `index_runner.py`, `validate/schema.py` | DONE | ✓ unit | noise + dead-anchor + sidecar-integrity + anchor-index emit + **FM JSON-schema** all DONE; `validate_normalized` aggregates all five into `survey/normalize_validation_flags.csv`, wired into the `normalize` CLI |
| P7.3 | Plug normalize checks into hard publish/push gate + corpus CI | §11 | `index_runner.py`, `cli/main.py` | DONE | ✓ unit | gate wired into `vista-docs normalize` AND the shared `_run_validation_gate` (publish + push), which now also validates `normalized/` (correct scope — sidecars live there) and refuses on any normalize hard failure. (Corpus `.ci/` mirror = optional follow-up) |
| **P8** | **Rollout** | §14 | — | WIP | — | prototype done; batch pending |
| P8.1 | Prototype CPRS GUI UM end-to-end | §14.1 | review artifact | DONE | manual | 2491 nav-links unwrapped, 0 dangling anchors, 27% smaller, idempotent (Change Log) |
| P8.2 | Class-C prototype with PDF (exercise F7) | §14.2 | review artifact | TODO | manual | needs P4.1 |
| P8.3 | Lock `normalize_version: 1.0` | §14.4 | constant | TODO | — | constant set to "1.0"; not yet review-signed-off |
| P8.4 | Batch run + `validate` gate + per-domain spot audit + publish-push | §14.5 | corpus | TODO | gate | force-push `vistadocs/vdl` |
| **P9** | **Docs & skills** | §15 | — | WIP | — | same-commit doc rule |
| P9.1 | Update `src/vista_docs/README.md`, `pipeline/README.md`, `CLAUDE.md` stage list | §15 | docs | WIP | — | `src/…/README.md` DONE; `pipeline/README.md` correctly scoped to 6–6.7 (no change). **`CLAUDE.md` stage list deferred** — it has another session's uncommitted edits; don't entangle |
| P9.2 | Update `docs/vdl-arch-overview.md` flow + `vdl-pipeline`/`va-docx-structure` skills + memory | §15 | docs/skills | WIP | — | arch-overview (intro + Mermaid + stage table) DONE; memory DONE; **`vdl-pipeline`/`va-docx-structure` skills TODO** |

---

## Plan detail (per phase)

### P0 — Discovery & scaffolding
**Why first:** three spec decisions (anchor location, PDF oracle viability, where
F1 lives) change the shape of later code. Resolve them before writing transforms.
- **P0.1** On the CPRS GUI prototype doc, confirm whether pandoc emitted `_Toc…`
  ids *on* headings or on adjacent `<span id="…">` (spec evidence says spans).
  F4's hoist logic forks on this. Capture pandoc version for `converter:`.
- **P0.2** Walk `consolidated/`, tag each doc Class A/B/C/D (headings? anchors?
  page numbers? PDF present?) → `survey/normalize_census.csv`. Drives effort
  sizing (esp. how many Class-C docs need the F7 bridge).
- **P0.3** Create `src/vista_docs/normalize/` with empty pure modules + a thin
  `runner.py`; add `runner.py` (and any I/O wrappers) to `[tool.coverage.run]
  omit` *immediately* (coverage gate is 95%).
- **P0.4** Add the §5 keys to `audit_frontmatter.py`'s `CANONICAL_KEYS` (and the
  shared `CANONICAL_KEY_ORDER` in `validate/frontmatter.py`) + a JSON-schema
  file. **Unregistered keys are stripped by audit** — the spec calls this out.

### P1 — Denoise & boilerplate (F1, F2)
Pure, idempotent, run first. **P1.2 is a real decision:** F1 cleanup may belong
in `ingest/postprocess.py` (so md-img is clean for *all* consumers, not just
publish). Prototype both; prefer fixing upstream once, then normalize only does
publish-specific work. F2 reuses the boilerplate frequencies already computed by
`vista-docs headings` (`survey/heading_analysis/`).

### P2 — Structure recovery (F3, F4, F6)
The payoff phase. F3 (heading inference) is the highest-value transform and the
riskiest — keep it conservative (skip+log on ambiguity; never invent structure).
F6 must consume the stage-6.5 heading tree (`chunk_sections.py`), not re-derive
headings, so the TOC matches the chunk index and anchors stay consistent.

### P3 — Revision history (F5) + sidecars
Harvest the revision `<table>`, drop only the uniformly-redacted PM/TW columns,
write `*.history.yaml`, summarize into frontmatter, remove the table from the
body, and fix the `description:` pollution. Reuse the `sanitize_scalar` +
guarded-serializer machinery already shipped.

### P4 — Page-number bridge (F7)
Only for Class-C (flat + paginated). **The PDF is the pagination oracle** — .docx
does not store rendered page numbers. Preserve→bridge→retire, each step
reversible via the `*.toc.yaml` sidecar. Gated on P0.1/P0.2 finding enough
usable PDFs; otherwise fall back to non-linked original-TOC text.

### P5 — Figures, tables, link rewrite (F9, F10, F8)
F9/F10 are local. **F8 runs last** in the whole pipeline because it needs every
anchor finalized; it rewrites legacy ids → slugs, resolves cross-doc references
against the emitted anchor index, and fails CI on any dangling `#…`.

### P6 — Orchestration & classification
The classifier (§8) picks the transform set per doc. The runner enforces the
canonical order (§12) and the idempotency guard (`normalize_version` + content
markers) so re-runs are no-ops. Expose as `vista-docs normalize` and call it
inside `publish` before the domain re-org/copy.

### P7 — Provenance & validation/CI  *(largest reuse of prior work)*
The 2026-05-31 guardrails session already shipped the validator module
(`src/vista_docs/validate/`), the `vista-docs validate` stage, the hard
publish/push gate, and the corpus-repo CI + pre-push hook + self-contained
`.ci/validate_frontmatter.py`. P7 **extends** these with normalize-specific
rules (dead-anchor, noise linter, sidecar integrity, frontmatter JSON-schema,
anchor-index emission) rather than building new infrastructure.

### P8 — Rollout
Prototype two docs end-to-end (one Class-A with anchors+redacted table, one
Class-C with a PDF), review the diffs, lock `normalize_version: 1.0`, then batch
with the hard gate in front of the push.

### P9 — Docs & skills
Update the stage lists, arch overview, README files, and the `vdl-pipeline` /
`va-docx-structure` skills + memory in the same commits, per the CLAUDE.md rule.

---

## Change Log

> Append one entry per stage you start or finish. Narrative form — capture *what
> changed, what you discovered, and any deviation from this plan*. Newest first.

### 2026-05-31 — Original-TOC removal → whole corpus validates clean (unblocks P8)
The one doc the gate blocked on (`psn`) had a malformed TOC entry — a heading
slug fused with an image + paragraph, inside the *original* pandoc TOC that
normalize was keeping. Per spec F6 ("prefer regenerating from headings; don't
keep the original TOC"), added `toc_pure.remove_original_toc`: a contiguous run
of >=6 list-item links where >=50% of targets resolve to real heading slugs is
the document's TOC and is removed (slug-resolution signal, not position — the psn
TOC sits *after* `# Revision History`). This sweeps up the block's malformed
entries in one shot. Wired into F6 (after `_strip_existing_toc`, before
re-extracting headings); idempotent (verified: psn drops 61 TOC items, regenerates
a clean one, second pass == first).

**Result: the full 235-doc corpus now validates `hard=0, total=0`** (noise=0,
dead-anchor=0, sidecar=0, schema=0). The publish/push gate passes corpus-wide —
P8 batch rollout is no longer blocked on a data defect.

### 2026-05-31 — P7.3 fold normalize gate into publish/push
`_run_validation_gate` (shared by `publish`, `push`, and `validate`) now also
runs `validate_normalized` over `normalized/` and refuses to publish/push on any
normalize hard failure (dangling anchors, residual noise, broken sidecars, hard
schema), alongside the existing frontmatter gate. **Scope decision:** validate
`normalized/`, not the publish tree — sidecars (`*.history.yaml`) live in
`normalized/` and aren't copied to publish, so checking the publish tree would
false-flag every revision doc as a missing sidecar. The check is skipped when
`normalized/` doesn't exist (backward compatible). With the current corpus the
gate correctly blocks on the 1 malformed `psn` doc until it's fixed.

### 2026-05-31 — P6.3 publish consumes normalized/ bodies
Wired the normalize output into `publish` with a surgical, backward-compatible
change:
- `publish/builder.normalized_candidate(src_md, consolidated_dir, normalized_dir)`
  — pure path math (unit-tested) for where a doc's normalized body would live;
  returns `None` for patch docs (under md-img/, no normalized mirror).
- `run_publish(..., normalized_dir=None)`: per anchor doc, copies the normalized
  body when it exists, else the consolidated original. **Images are still copied
  from the consolidated tree** (normalize doesn't duplicate images), so refs
  resolve unchanged. Returns a new `normalized_bodies` count.
- CLI `publish` auto-detects `DATA_DIR/normalized` and reports usage; with no
  normalized tree it transparently falls back to consolidated bodies.

Smoke (CPRS, `--pkg CPRS`): 10 normalized anchor bodies swapped in (all carry
`normalize_version`), 59 patch docs fell back, 69 image dirs copied intact.
TODO (P7.3 remainder): run the normalize hard gate over the publish output inside
`_run_validation_gate`.

### 2026-05-31 — P7.3 hard validation gate (+ noise-linter consistency fix)
Wired a hard gate into `vista-docs normalize`: after emitting the anchor index +
validation report, it exits non-zero on any **hard** issue
(`NormalizedValidation.hard` = noise + dead-anchor + sidecar + hard-schema;
advisory `schema:soft` excluded), printing the offending flags; `--no-validate`
bypasses for inspection.

**Measured the gate against the whole corpus before enforcing it** (235 docs
normalized → validated) and fixed two noise-linter false-positive sources it
exposed:
- **22 `redacted_cell`** were legitimate redactions in *non*-revision tables. F5
  deterministically removes the revision table (PM/TW columns), so remaining
  `Redacted`/`N/A` cells are real source content — dropped the check.
- **6 `page_number_line`** were bare numbers that are *content* (e.g. table data
  `cytopath / 8 / 86-04`), which F2 correctly leaves. Made the linter consistent
  with F2: only flag a numeric line *isolated* by blanks on both sides.

After the fixes the corpus validates with **noise=0, sidecar=0, schema=0**; the
gate fails on exactly **1** doc — the genuinely malformed `psn` unescaped-`]`
link (a real source defect for human review), which is the intended §11 outcome.
TODO: fold the gate into the publish/push path (needs P6.3) + corpus CI.

### 2026-05-31 — P0.4 frontmatter JSON-schema (completes P7.2)
- `validate/schema.py`: `FRONTMATTER_SCHEMA` (source-of-truth dict, every key
  typed; `section`/`toc`/`anchors_source` enums) mirrored to the committed
  `validate/frontmatter.schema.json` (drift-guarded by a unit test). Pure,
  dependency-free `validate_against_schema` for the JSON-Schema subset used
  (required/type/enum/additionalProperties). Severities: missing-required +
  bad-enum = hard; type mismatch + unknown key = soft. The enforced gate stays
  `validate_frontmatter`; this is a layered cross-check.
- `null` is treated as "unset" (skip type/enum) — 101/235 docs legitimately have
  `doc_subject: null`, so flagging them would be pure noise.
- Wired into `validate_normalized` (advisory `schema:` flags) + the CLI summary.
  Smoke on real docs: 0 schema flags after the null-skip fix.

### 2026-05-31 — P7.2 anchor-index emit + sidecar integrity
Built the remaining §11 validation pieces (except the FM JSON-schema):
- `index_pure.py` (pure, TDD): `anchor_index_entry(doc, body, aliases)` →
  `{doc, headings[{level,text,slug}], slugs, aliases}` and `build_anchor_index`
  (the `doc → {headings,slugs,aliases}` map of §11.5, used by F8 cross-doc
  resolution + the dead-anchor check).
- `lint_pure.sidecar_violations` (pure, TDD): every `revision_sidecar` resolves
  to an existing file and that sidecar's `document` back-reference matches (§11.4).
- `index_runner.py` (I/O, omitted): `emit_anchor_index` → `survey/anchor_index.json`;
  `validate_normalized` runs noise + dead-anchor + sidecar checks over
  `normalized/`, writing `survey/normalize_validation_flags.csv`. Both wired into
  the `vista-docs normalize` CLI, which now prints index size + a flags summary.

End-to-end smoke (3 docs incl. CPRS): index emitted, sidecar back-refs resolve,
**0 validation flags**. Still open in P7.2: FM JSON-schema (P0.4); P7.3 (plug
these checks into the hard publish/push gate) remains TODO.

### 2026-05-31 — F8 sweep robustness (bracketed text, footnotes, nested links)
Hardened `sweep_dead_links` against three real-corpus forms the census surfaced
(docs with residual dead anchors: **15 → 1**):
1. **Bracketed link text** — `_MD_LINK_RE` text now allows escaped chars
   (`\[CODE\]`), so VistA TOC entries like `[### Check Files \[LRCHKFILES\]](#…)`
   are swept; still stops at the first *unescaped* `]` so adjacent links never merge.
2. **Footnotes** — `valid_anchor_ids` now recognizes an `id=` on *any* element
   (not just `<span>`/`<a>`) plus pandoc `{#id}`. Pandoc footnotes define
   `<li id="fn1">` / `<a id="fnref1">`; the old span/a-only rule made `#fn1` look
   dead, so the sweep stripped the citation `<a>` (which also *defined* `fnref1`),
   leaving the back-link dangling. Now all footnote links resolve.
3. **Nested dead links** — the sweep iterates to a fixpoint; stripping a dead
   *outer* link reveals a dead *inner* one (`[… [11-10](#_Ref) …](#outer)`) that a
   single `re.sub` pass skips.

**Census after fixes: 235/236 docs end with 0 dead anchors.** The lone remaining
doc (`psn/.../national_drug_file_-_user_manual.md`) has a genuinely
malformed-markdown artifact — a heading + image + paragraph fused into one link
whose text contains an *unescaped* `]`, so it is not a well-formed link the sweep
should touch; it is correctly left for the §11 dead-anchor CI flag to surface for
human review.

### 2026-05-31 — P0.2 corpus census (Class A/B/C/D)
Ran `scripts/normalize_census.py` over all **236** consolidated docs (reuses the
pure orchestrator + classifier; writes `survey/normalize_census.csv`):

| Class | Count | Meaning |
|-------|-------|---------|
| A | **122** | headings + Word anchors (healthy; top doc has 905 headings / 161 anchors) |
| B | **108** | headings, no anchors |
| C | **4**   | flat+paginated — **all 4 have a PDF**, so F7 effort is small |
| D | **2**   | hopeless (CPRS GUI release notes, KAAJEE quick-setup) |

Other signals: **76** docs carry the dead nav-link wrapping (F3a), **10** have a
revision table, **221/236** end with **0 dead anchors** after the F8 sweep.
**Takeaway:** the corpus is far healthier than the CPRS prototype implied — only
6 docs are C/D, and F7 (PDF bridge) is needed for just 4. The CPRS GUI UM is an
outlier in degradation, not the norm.

**Census-surfaced follow-up (F8 robustness):** the 15 docs that still report dead
anchors are internal TOC cross-references whose link *text* contains `]` (e.g.
`[### Check Files … \[LRCHKFILES\]](#slug)`), so `sweep_dead_links`'s `[^\]]+`
text guard skips them; some also have slug mismatches between the TOC entry and
the recovered heading. Fix: let the sweep handle bracketed link text + reconcile
cross-ref slugs. Tracked under P5.3 Notes.

### 2026-05-31 — F8 dead-link sweep (closes the dangling-anchor gate)
Added `linkfix_pure.sweep_dead_links(body, valid_ids)` and wired it as the final
F8 step, **after** `rewrite_legacy_links` (so an alias-resolvable ref is already a
valid slug and is never stripped). A markdown `[text](#dead)` collapses to `text`;
an html `<a href="#dead">inner</a>` collapses to `inner` (keeps inline markup);
links to a valid target and external links are untouched. `valid_ids` =
`lint_pure.valid_anchor_ids` (heading slugs ∪ explicit `id=` anchors), recomputed
on the post-rewrite body. TDD, `linkfix_pure` 100% cov, 8 new tests; idempotent.

**Prototype impact (CPRS GUI UM):** the 169 inline dead nav links (incl. the
remaining `#_Toc17877476` refs) are now neutralized → **0 dangling anchors**
(`lint_pure.dead_anchors` returns `[]`), so the doc passes the spec §11
dead-anchor CI gate. Body now **27% smaller**; still idempotent + deterministic.
This resolves the inline-residue follow-up from the F3a entry below.

### 2026-05-31 — F3a unwrap transform (`delink_pure`) + corrected P0.1 reading
**Correction to the earlier same-day entry:** the `[[text](#_Toc)]` form is **not**
a heading encoding at all. Deeper analysis of the CPRS doc: there are **zero**
anchor *definitions* in the body (`<a id>`/`[]{#id}`/`{#id}` all 0; the only defs
are 86 `<span id>` figure anchors), and **all** 925 double-link + 927 single-link
lines point to the *same* undefined anchor `_Toc17877476` ("return to TOC"),
wrapping **prose** (and a few empty bookmark markers). So they are dead
navigation-link wrapping pandoc replays on every paragraph — not section headings.

**Built `normalize/delink_pure.py` (F3a, TDD, 100% cov, 12 tests):**
- `unwrap_toc_links(body, defined=None)`: a global lazy `[[…](#a)](#b)` → inner
  text sub (the double `](#..)](#..)` close is unambiguous, so it safely handles
  blockquote/list prefixes, inline, and multi-line wrappers + preserves an inner
  inline `[x](#y)`), plus a whole-line single `[text](#dead)` → text pass that
  only fires when the target is **undefined** (so legit cross-refs and generated
  TOC links to real heading slugs survive — `defined` = explicit ids ∪ heading
  slugs).
- `defined_anchor_ids(body)`: the resolvable-target set.
- Wired into `normalize_body` right after F1 denoise, before F2/F3. Added a
  trailing-whitespace trim to `_finalize` (unwrapping an empty blockquote left
  `> ` which pass-2 denoise trimmed to `>` — an idempotency break, now fixed).

**Prototype impact (CPRS GUI UM, real doc):** **2491** nav links unwrapped,
`[[` wrappers **0** remaining, body **26% smaller** (816k→601k chars), unique
dead anchors down to **4**, output **idempotent** + deterministic. The doc now
classifies **B** (was ~D). Remaining: **166 inline** links to the single dead
`_Toc17877476` nav anchor are intentionally left (whole-line/double only) — per
spec §11 dead anchors are a CI **flag** (`lint_pure.dead_anchors` reports them),
not a silent strip. A follow-up F8 dead-link sweep (run *after* F4 aliasing, so
it never strips an aliasable ref) could neutralize those if desired. Real
headings are still not recoverable from this doc (they were lost upstream); F3
promoted 1. The census (P0.2) should now measure how many docs carry this nav
wrapping.

### 2026-05-31 — P0–P7 core build (WIP) + prototype discovery
**Built (TDD, all green; 97.6% cov on `normalize/`, `make`-gate passes):**
- `src/vista_docs/normalize/` package with pure transforms, one test file each:
  `denoise_pure` (F1), `boilerplate_pure` (F2), `heading_infer_pure` (F3),
  `anchors_pure` (F4: GitHub slug + `Slugger` de-dup + `build_anchor_aliases`),
  `revision_pure` (F5: parse/summarize/remove + `depollute_description`),
  `toc_pure` (F6), `page_bridge_pure` (F7 inject/resolve/retire — pure parts),
  `linkfix_pure` (F8), `figures_pure` (F9), `tables_pure` (F10 simple→GFM,
  complex→raw), `classify_pure` (§8 A/B/C/D), `lint_pure` (§11 noise + dead-anchor).
- `normalize_pure.normalize_body` — orchestrator composing F1→F8 in canonical
  order (§12); deterministic, idempotent (verified twice == once).
- I/O layer (coverage-omitted): `io.py` (sha256, `*.history.yaml` sidecar writer,
  raw-source locator), `runner.py` (`consolidated/` → `normalized/`, provenance
  stamps, routes FM through `safe_dump_frontmatter`), CLI `vista-docs normalize`.
- Registered the §5 keys in `audit_frontmatter.CANONICAL_KEYS` +
  `validate.frontmatter.CANONICAL_KEY_ORDER` (P0.4); reserved `runner/io/pdf_reader`
  in `[tool.coverage.run] omit`.

**Deviation — architecture fix mid-build:** first runner wrote frontmatter *in
place* into `consolidated/`. That violates §3 ("lossless layer, never hand-edited,
re-runnable from it"). Refactored to read `consolidated/` and write a separate
`normalized/` tree. This also fixed an idempotency bug: a second in-place pass
recomputed `revision_count` from the (already-removed) table and clobbered it to 0.

**Prototype run (CPRS GUI UM, real consolidated doc) — resolves P0.1 with a
surprise:** revision extraction works end-to-end (243 rows → sidecar;
`revision_newest 2023-06`, `revision_oldest 2002-05` after adding M/D/YY date
handling; `description` de-polluted; `consolidated/` untouched; deterministic
re-run). **But** the doc has effectively **no recoverable headings**: pandoc did
*not* leave `_Toc…` ids on headings or on `<span id>` siblings (the spec's two
hypotheses). Instead section titles are encoded as **self-referential
`[[Heading Text](#_TocNNN)](#_TocMMM)` links**, regular paragraphs are wrapped in
`[[…]]`, and numbered lists are exploded into bare `1.`/`2.` lines. So F3/F4/F6
find nothing to promote and the doc classifies as ~D. This is upstream
ingest/consolidation damage, not just publish noise.

**Follow-ups created:**
1. Add an F3/F4 sub-transform to recover headings from the
   `[[text](#_Toc)](#_Toc)` self-link form and alias the `_Toc` ids to the new
   slug. Distinguish heading self-links (double-anchor / TOC entries) from
   paragraph `[[…]]` wrapping — non-trivial; prototype on this doc.
2. Investigate fixing the `[[…]]` wrapping + exploded-list artifacts **upstream**
   in `ingest/postprocess.py` (per P1.2) so all consumers get clean md, then
   normalize only does publish-specific work.
3. Run the P0.2 Class A/B/C/D census now that we know the real shapes — quantify
   how many docs are this degraded vs clean.
4. Still TODO: PDF page-bridge I/O (P4.1), FM JSON-schema (P0.4/§11), sidecar
   integrity + anchor-index emit (P7.2), wire `normalize` into `publish` + the
   hard gate (P6.3/P7.3), batch rollout (P8).

### 2026-05-31 — Plan created
- Authored this implementation plan from `publish-normalization-spec.md` Draft 1.
  Decomposed the 10 transforms (F1–F10) + classification + sidecars + provenance
  + CI into 9 phases / 31 tracked stages, mapped to the spec's §12a module
  layout and the repo's pure/IO TDD conventions.
- Marked P7 (`validation/CI`) as **REUSE**: the frontmatter-guardrails work
  landed earlier today (pipeline branch `harden-frontmatter-guardrails`
  `a2783b0`; corpus `vistadocs/vdl` `5f9ba78`) already provides the validator
  module, `validate` CLI stage, hard publish/push gate, and corpus CI + pre-push
  hook — normalize plugs into these instead of rebuilding them.
- Flagged P1.2 (F1 location: ingest vs normalize) as **BLOCKED on a decision**
  to avoid a double-denoiser, and P0.1/P4.1 as gated on the spec's open
  questions (anchor location, PDF availability).
- No code written yet. Next action: **P0.1** (verify anchor location + pandoc
  version on the CPRS GUI prototype) and **P0.2** (Class A/B/C/D census).

<!-- Template for new entries:
### YYYY-MM-DD — P<n>.<m> <stage name> (<WIP|DONE>)
- What was implemented / changed (files, functions).
- Test evidence (failing-first → green; `make check` result).
- Surprises / deviations from plan / decisions taken.
- Follow-ups created.
-->

---

## Lessons Learned (pipeline nuances — carry forward & reuse)

> Seeded from the 2026-05-31 frontmatter-guardrails work on this same pipeline.
> Add to this list as normalize implementation surfaces new nuances.

1. **One serializer, with a round-trip guard.** The pipeline historically had
   *two* frontmatter serializers: audit's `yaml.safe_dump` and enrich's
   hand-rolled `_quote` — the hand-rolled one double-quoted values without
   escaping backslashes and emitted unparseable YAML (`(ACKQ\3.0\3)` →
   *"unknown escape character"*). **Route every frontmatter write through the
   single guarded serializer** `validate.frontmatter.safe_dump_frontmatter`,
   which round-trips its own output through strict `safe_load` and raises on
   failure. Do **not** add a third serializer for normalize.
2. **Audit owns the canonical keys and runs last.** Any key not registered in
   `audit_frontmatter.py` (`CANONICAL_KEYS`) / `validate.frontmatter`
   (`CANONICAL_KEY_ORDER`) is silently dropped on the next audit. Register
   normalize's new keys (`toc`, `anchors_source`, `anchor_aliases`,
   `revision_sidecar`, `page_anchors`, `source_sha256`, `converter`,
   `normalized_at`, `normalize_version`) **before** writing them anywhere.
3. **`enrich --force` re-derives `description` from the body.** A leading
   `---…---` block left in the body gets captured as `description` (this is
   exactly how the DVBA doc got corrupted — its real frontmatter ended up
   double-wrapped in the body). F5's body edits and F3's restructuring must be
   **idempotent** and must not leave fence-like or table-caption text at the top
   of the body, or a later enrich will re-pollute `description`.
4. **Stage order constrains where a field can be filled.** `enrich → sync →
   audit → consolidate → manifest → publish`. Inventory-derived fields must be
   set at **sync** (join key is `(app_code, title)`, *not* slug); content-derived
   fields at **enrich/audit**. `normalize` sits **after consolidate, before
   publish** — so it can rely on canonical frontmatter already being present, but
   anything it changes in frontmatter should go back through audit's serializer.
5. **`publish` drops docs with empty `app_code`.** A normalize bug that blanks
   `app_code` will *silently remove* the doc from the deliverable (that's how the
   DVBA stub stays out of publish). Treat empty required keys as a hard failure,
   not a silent drop.
6. **Determinism is required and easy to break.** `consolidate` is deterministic
   via stable sort; audit stamps only a *dated* `audit_applied`, so same-day
   reruns are byte-identical. Keep normalize deterministic: sorted iteration, no
   wall-clock/random content (only a dated `normalized_at` stamp), stable slug
   de-dup ordering. Verify with a second run + `md5sum` diff.
7. **`ftfy` uncurls quotes as a side effect of mojibake repair.** `sanitize_scalar`
   is safe for prose (`description`, `audience`) but will alter literal
   punctuation. **Never run it on checksums, version strings, anchors, or slugs.**
   Sanitize prose; copy structured tokens verbatim.
8. **Keep tables and maps YAML-safe.** Tables belong in the markdown **body**,
   not frontmatter. The one map normalize puts *in* frontmatter (`anchor_aliases`)
   must stay safe — keys with colons/`*`/leading `-` need the guarded serializer
   (it handles this; bespoke string-building does not).
9. **The hard gate already exists — lean on it.** `publish`/`push` refuse to run
   on any hard validation failure (`_run_validation_gate`), the corpus repo has
   `.ci/validate_frontmatter.py` + a CI workflow + a pre-push hook, and
   `run_publish` preserves `.git/.gitignore/.github/.ci` across `--force`. Add
   normalize's CI checks (dead-anchor, noise linter, sidecar integrity) into this
   path; don't invent a parallel gate.
10. **The converter is pandoc, not Docling.** Page numbers are **not** in the
    .docx — F7 must read them from the **PDF** (`pdf_url`). Set `converter:`
    from the actual pandoc version.
11. **Source docs are off-limits to hand-editing.** The auto-mode classifier
    blocks overwriting non-git-controlled `md-img/`/`consolidated/` docs — and it
    should. **Every fix must be generator-level** (a transform + a test), which
    is exactly what this spec mandates. A one-off "just fix this file" is both
    blocked and non-reproducible.
12. **Coverage discipline.** New I/O wrappers go into `[tool.coverage.run] omit`
    in `pyproject.toml` the moment they're created; pure transforms must have a
    failing unit test before implementation (TDD hard rule) and stay at/above the
    95% gate. Verify a scoped commit builds in isolation with a throwaway
    `git worktree` + `PYTHONPATH=…/src pytest` when the working tree contains
    unrelated in-progress files.
13. **The consolidated corpus is more degraded than the spec's evidence (P0.1),
    and the `[[…](#_Toc)]` form is nav wrapping, not headings.** The spec assumed
    pandoc left clean headings with `_Toc…` ids on the heading or an adjacent
    `<span id>`. Reality on the CPRS GUI UM doc: **zero** anchor *definitions*
    exist, and ~1850 lines wrap **prose** in dead "return-to-TOC" links all
    pointing at the *same* undefined `_Toc` anchor. The fix is to **unwrap** them
    (`delink_pure`, F3a) — recovering text + killing dead anchors (2491 unwrapped,
    26% smaller, idempotent) — *not* to promote them to headings. Real headings
    were lost upstream; F3 can only infer the few that survive as text. **Always
    prototype against a real consolidated doc, and re-verify your read of the data
    before building — the first "self-referential heading link" hypothesis was
    itself wrong.** Census (P0.2) should measure how widespread the wrapping is.
14. **Normalize writes a sibling tree, never `consolidated/`.** Read
    `consolidated/` (lossless), write `normalized/`. Mutating `consolidated/` in
    place breaks re-runnability *and* idempotency (the revision summary gets
    recomputed from the already-removed table and zeroed). The pure orchestrator
    is date-free; only the runner stamps `normalized_at`.
