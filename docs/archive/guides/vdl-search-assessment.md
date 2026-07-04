# VDL Search & Discovery Infrastructure — Assessment and Recommendations

**Subject:** Current state of VDL search, gaps identified, prioritized improvements
**In-scope artifacts:**
- [`vistadocs/vistadocs.github.io`](https://github.com/vistadocs/vistadocs.github.io) — the interactive search UI + master index CSV
- [`vistadocs/vdl`](https://github.com/vistadocs/vdl) — the markdown content corpus
- [VA VDL](https://www.va.gov/vdl) — the institutional source of record

**Mode:** Specification & recommendations only — no implementation code
**Companion document:** `vista-package-lifecycle-spec-v4.md` (the consumer of this infrastructure)

---

## 1. Executive summary

The VDL search infrastructure is in **good but not optimal shape**. The architecture is sound: a static GitHub Pages site (`vistadocs.github.io`) renders an 8,834-row CSV index through DataTables, with a parallel markdown corpus (`vistadocs/vdl`) providing 1,418 converted documents for content access. The two-tier separation between *index* and *content* is a strong design choice.

However, several quality issues limit the system's authority and usability:

- **Data quality:** UTF-8 mojibake in 70+ rows; typos preserved from source ("DIBORG", "Aurerus"); package-name inconsistencies in 14 abbreviations
- **Schema drift:** `doc_code` → `doc_label` mappings are inconsistent (5 codes have multiple labels)
- **Sparse coverage:** 26% of rows lack `pkg_ns`; 60% of unique documents lack a corresponding markdown file
- **Discoverability gap:** The CSV does not link to the markdown corpus, so users cannot trivially move between the index tier and the content tier

The single highest-leverage improvement is **adding a `github_md_url` column to the CSV** that links to the corresponding markdown file in `vistadocs/vdl` when one exists. This closes the discoverability gap and makes the two-tier architecture actually navigable. Implementation requires resolving the anchor/patch consolidation many-to-one mapping (§4.3 below).

The remaining issues are addressable through pipeline corrections at the `enrich` stage that produces the CSV — none require redesign.

---

## 2. Current state

### 2.1 The two-tier architecture

| Tier | Repository / location | Purpose | Document count |
|---|---|---|---|
| **Index** | `vistadocs/vistadocs.github.io` → `vdl_inventory_enriched.csv` | Discovery, filter, query | 8,834 rows / 3,640 unique docs |
| **Content (converted)** | `vistadocs/vdl` (markdown) | Programmatic reading, AI-friendly access | 1,418 markdown files |
| **Content (canonical)** | `va.gov/vdl/...` (linked via `doc_url`) | Authoritative source of record | All 8,834 documents |

This separation is the right design. The index is small and fast; the content is large and bandwidth-constrained; the canonical source is institutional but not optimized for programmatic access. Each tier serves its purpose well.

### 2.2 The interactive search UI

The web table at `https://vistadocs.github.io` is built on:
- **PapaParse 5.4.1** — streaming CSV parser
- **DataTables 2.0.8** — sort/filter/paginate/search
- **DataTables Buttons + ColVis** — column visibility controls
- **jQuery 3.7.1** — DataTables dependency

Hosting is **GitHub Pages** with zero server-side processing. The architecture is exemplary for the use case: minimal dependencies, all CDN-loaded, instant deploy on `git push`, no build step.

**Search capabilities exposed today:**
- Global text search (across all visible columns)
- Per-column dropdown filters (Section, Package, Doc Type, Status, Format, Layer)
- Free-text search on Document Title
- Sort by any column
- Hide/show columns
- Pagination

**Capabilities *not* exposed today:**
- Search across multiple columns with boolean logic
- Search restricted to specific patch-version ranges
- Search across the markdown content (the content tier is not indexed)
- Cross-document discovery (e.g. "all DIBRGs that mention HL7")
- Saved searches / shareable filter URLs

### 2.3 The markdown corpus

`vistadocs/vdl` holds 1,418 markdown files organized by section/package, derived from the original VA VDL DOCX/PDF documents. The conversion preserves a YAML frontmatter block with rich metadata:

```yaml
---
consolidated_title: "dibrg"
app_code: ADT
doc_type: DIBR
doc_layer: anchor
master_source: "DG*5.3*952 DIBRG"
master_pub_date: February 2020
consolidated_from: 9 versions
prior_versions:
  - "DG*5.3*1016 DIBRG"
  - "DG*5.3*1025 DIBRG"
  ...
---
```

**Document layering** (also reflected in CSV's `doc_layer` column):
- `anchor` (3,466 CSV rows) — consolidated master + N appendix versions in a single markdown file
- `patch` (3,584 CSV rows) — per-patch documents
- `plain` (1,784 CSV rows) — one-off documents (e.g. Kernel TM, KIDS User Guide)

The anchor-consolidation pattern is the **dominant content-tier abstraction**: most modern VistA package documentation is produced as a series of patch-level documents that get rolled up into a single anchor for browsability. The markdown corpus typically contains the anchor file, not the per-patch files.

### 2.4 What's good about the current state

- Static infrastructure means zero hosting cost and trivial maintenance
- The CSV schema is rich (30 columns) and queryable
- Markdown frontmatter preserves the metadata needed for any future linking work
- Anchor-consolidation reduces the content-tier file count by ~3× without losing detail
- The `doc_url` column reliably links to the canonical va.gov source

---

## 3. Issues identified and recommended improvements

For each issue: evidence, recommendation, and priority. Priorities are H (high — affects authority of search results), M (medium — affects usability), L (low — cosmetic or edge-case).

### 3.1 UTF-8 mojibake [Priority: M]

**Evidence:** 70 rows contain UTF-8 mojibake patterns in `doc_title` and `doc_subject`.

| Pattern | Likely original | Example in CSV |
|---|---|---|
| `â€™` | `'` (right single quote) | `Developerâ€™s Guide` |
| `â€"` / `â€"` | em-dash or en-dash | `Clinical Pathways â€" Lung Cancer` |
| `Â` | non-breaking space | (various) |

**Cause:** Source documents contain Windows-1252 or UTF-8 characters that were re-encoded as Latin-1 somewhere in the extraction pipeline.

**Recommendation:** In the `enrich` stage of the pipeline that produces `vdl_inventory_enriched.csv`, add a **mojibake detection and correction pass** using a tool like `ftfy` (Fixes Text For You). Run before CSV write.

**Impact on search:** Users searching for "Developer's" don't find rows where the title contains "Developerâ€™s". Critical for full-text search.

### 3.2 Source-document typos preserved [Priority: M]

**Evidence:** Typos that originate in the VA's source documents are preserved in the CSV:

| Typo | Correct | Occurrences | Field |
|---|---|---|---|
| `Aurerus` | `Aureus` | 25 rows | `app_name_full` (Methicillin Resistant Staph Aurerus → MRSA) |
| `DIBORG` | `DIBRG` | 16 rows | `doc_title` (HTRE Phase 3 Build 1 DIBORG) |
| `ACKQ` (uppercase mid-title) | (intentional? — the namespace) | 14 rows | `doc_title` — this one is actually correct, false positive |

**Cause:** Faithful extraction from source. The typos are in the underlying VA documents.

**Recommendation:** **Maintain a known-typo correction table** in the pipeline, applied at enrich. The table should be small, documented, and human-curated. Include both the typo and the corrected form to support search on either spelling.

Suggested initial table:

```yaml
typo_corrections:
  - { source: "Staph Aurerus",   corrected: "Staph Aureus" }
  - { source: "DIBORG",          corrected: "DIBRG" }
  # Add new entries as discovered
```

**Search-side mitigation:** Even without correction at enrich time, the search UI should index *both* the original and the corrected term so search works either way. This is a fallback if pipeline changes are slow.

### 3.3 `app_name_full` inconsistency for the same `app_name_abbrev` [Priority: H]

**Evidence:** 14 abbreviations carry multiple full names in the CSV, indicating that `app_name_full` is sometimes the *document subject* rather than the *package's canonical identity*.

| `app_name_abbrev` | Multiple `app_name_full` values |
|---|---|
| `OR` | "CPRS: Bulk Parameter Editor for Notifications" / "Group Notes" — should be "Order Entry / CPRS" |
| `XU` | (varies) — should be "Kernel" |
| `PXRM` | "CPRS: Clinical Reminder Updates" / "CPRS: Clinical Reminders" / "Registry: Airborne Hazard Open Burn Pit (AHOBPR)" — should consistently be "Clinical Reminders" |
| `LR` | 6 different full names — should consistently be "Laboratory" |
| `SD` | "Electronic Wait List" / "Scheduling" — should be "Scheduling" |
| `MPIF` | "Duplicate Record Merge: Patient Merge" / "Master Patient Index" |
| `PSA` | "Pharmacy: API" / "Pharmacy: Drug Accountability" |
| `QAC` | "Patient Advocate Tracking System (PATS)" / "Patient Representative" |
| `ANRV` | "Blind Rehabilitation" / "Visual Impairment Service Team (VIST)" |
| `KAAJEE` | "KAAJEE" / "KAAJEE (XU and XWB)" |
| `HDI` | "Health Data  Informatics" / "Health Data Informatics" — double-space typo |

**Cause:** The pipeline appears to populate `app_name_full` from a per-document context (sometimes the document's own title or subject heading) rather than from a single package-master table.

**Recommendation:** **Introduce a package-master table** in the pipeline, keyed by `app_name_abbrev`, that defines the canonical `app_name_full` for each package. The enrich stage looks up the canonical name from this table rather than deriving it per-document.

Add a separate column `doc_subject` (already exists in the CSV — currently sparse) for document-level subject/topic if that's what the per-document `app_name_full` was actually capturing.

**Impact on search:** Critical. When a user filters by `app_name_full == "Clinical Reminders"`, they should see all PXRM documents — not 1/3 of them. Today's filter dropdowns are populated from CSV values, so the inconsistency leaks directly into the UI.

### 3.4 Multiple abbreviations for the same package [Priority: H]

**Evidence:** Two distinct `app_name_full` values resolve to multiple `app_name_abbrev`s — typically from namespace-consolidation eras (KMP\*) or pre-namespace-rationalization periods:

| Canonical name | Abbrevs in CSV | Era / cause |
|---|---|---|
| Resource Usage Monitor | `RUM`, `KMPR` | KMP\* consolidation |
| Statistical Analysis of Global Growth | `SAGG`, `KMPS` | KMP\* consolidation |
| Single Signon/User Context | `SSO`, `SSO/UC` | Naming variation |
| Name Standardization | `XOB`, `XU` | XOB sub-package within Kernel |
| Standard Files and Tables | `HL`, `XU` | Cross-package shared docs |

**Recommendation:** Add a **`canonical_pkg`** column to the CSV that resolves the abbreviation to its canonical pre-consolidation identity. For non-consolidated packages this equals `app_name_abbrev`; for consolidated cases it points to the surviving abbreviation. Example:

```
app_name_abbrev: KMPR
canonical_pkg:   KMPR  (if KMPR is the canonical post-consolidation name)
                 RUM   (if RUM is the legacy name to preserve for search)
```

Decision rule: **canonical = current production namespace**, with the legacy abbreviation retained in `app_name_abbrev` for historical document linkage.

Alternatively, use the existing `pkg_ns` column more aggressively as the canonical identity — but `pkg_ns` is currently only 74% populated (§3.6), so it can't carry this load until it's filled in.

**Impact on search:** Users looking for "Resource Usage Monitor" docs need to know to search both `RUM` and `KMPR`. The package-master table from §3.3 should also resolve this.

### 3.5 `doc_code` → `doc_label` drift [Priority: M]

**Evidence:** 5 doc codes have multiple labels in the CSV:

| `doc_code` | Labels found |
|---|---|
| `CFG` | "Configuration Guide" / "Setup and Configuration Guide" |
| `INT` | "Interface Feed Guide" / "Interface Specification" |
| `REF` | "Interface Toolkit" / "Reference" |
| `UG` | "Manager/ADPAC Guide" / "User Guide" |
| `UM` | "Clinical Coordinator Manual" / "User Manual" |

**Cause:** The label is sometimes the document's actual title-prefix wording (e.g. "Manager/ADPAC Guide") rather than the canonical doc-type label.

**Recommendation:** **Define a canonical `doc_code` → `doc_label` table** in the pipeline. Apply at enrich. If the source document has a non-canonical label (e.g. "Manager/ADPAC Guide"), preserve it in a new `doc_subtitle` field but populate `doc_label` from the canonical table.

Suggested canonical labels:

```yaml
doc_code_labels:
  RN:   "Release Notes"
  DIBR: "Deployment, Installation, Back-Out, and Rollback Guide"
  IG:   "Installation Guide"
  TM:   "Technical Manual"
  UG:   "User Guide"
  UM:   "User Manual"
  CFG:  "Configuration Guide"
  INT:  "Interface Specification"
  REF:  "Reference"
  POM:  "Production Operations Manual"
  SG:   "Security Guide"
  VDD:  "VistA Database Design"
  # ...
```

**Impact on search:** The Doc Type dropdown filter currently shows the same code under multiple labels, fragmenting the user's filter options.

### 3.6 Sparse `pkg_ns` coverage [Priority: M]

**Evidence:** 6,493 / 8,834 rows (74%) have `pkg_ns` populated. The remaining 26% have it blank.

**Cause:** The enrich pipeline appears to extract `pkg_ns` only from documents that explicitly state it (e.g. patches with `XX*Y.Y*ZZZ` identifiers). Documents that don't carry this pattern in their title (e.g. user manuals, technical manuals at the package level) are left with blank `pkg_ns`.

**Recommendation:** Populate `pkg_ns` from the package-master table proposed in §3.3 — every package has a canonical M namespace, and it should be filled in for *every* row of that package, regardless of whether the specific document mentions a patch ID.

For packages whose abbreviation differs from their namespace (e.g. `ANRV` → namespace varies), the package-master table is the only authoritative source.

**Impact on search:** Users querying by namespace (a common pattern for VistA developers — "show me everything in OR namespace") get incomplete results.

### 3.7 Section name has trailing parenthetical [Priority: L]

**Evidence:** The section name `VistA/GUI Hybrids (formerly HealtheVet)` contains a parenthetical historical note inside the value itself. Other section names are clean.

**Recommendation:** Move historical/contextual notes into a sibling column (e.g. `section_notes`). Keep `section_name` clean: `VistA/GUI Hybrids`.

**Impact on search:** Minor. The dropdown filter shows the long form; search-as-you-type for "VistA/GUI" works because of substring matching.

### 3.8 Markdown formatting variance [Priority: M]

**Evidence:** Across the 32 DIBRGs in the markdown corpus (the v3 spec sample):
- 29 use H1 (`#`) as their top-level heading
- 3 (all GMRC variants) use H2 (`##`) as their top-level heading
- This is a **pure conversion artifact** — the source documents have the same logical structure, but the DOCX-to-markdown conversion produced different heading levels

Beyond DIBRGs, the same pattern likely affects other doc types (UG, UM, TM) but has not been systematically scanned.

**Recommendation:** **Normalize heading levels** in the markdown conversion pipeline. Detect the topmost heading level in each document; if it's not `#`, promote all heading levels uniformly so the topmost is `#`.

This is a one-time backfill plus a guard in the conversion pipeline going forward.

**Impact on search:** Affects programmatic structural analysis (the kind that produced v3 §3.1). Affects any tool that depends on Markdown-rendered TOC. Does not affect the search UI directly.

### 3.9 Status field is package-level, not document-level [Priority: L]

**Evidence:** `app_status` reflects whether the *package* is active/archive/decommissioned, not whether the *document* is current. An archived package's most recent release notes still carry `app_status == 'archive'`.

**Recommendation:** Add a separate `doc_status` column that tracks whether the document itself is the current version (vs. superseded). This requires version-comparison logic in the pipeline (e.g. for an anchor doc, the current version is the master; prior versions are appendices). For patch-layer docs, current = the latest patch; older patches are superseded.

Alternatively, this can be left as-is; users can use `doc_layer == 'anchor'` as a proxy for "the consolidated current version."

**Impact on search:** Users looking for "current install instructions for ADT" today get the package's currentness, not the document's. Acceptable for most use cases.

### 3.10 Markdown corpus partial coverage [Priority: H — addressed in §4]

**Evidence:** Of 3,640 unique documents in the CSV, only 1,418 have markdown counterparts in `vistadocs/vdl` — roughly 39% (or higher when accounting for anchor consolidation, which collapses multiple CSV rows to one markdown file).

**Recommendation:** Two complementary tracks:

1. **Expand markdown conversion** to cover the remaining ~60% of unique documents. Prioritize by package activity (active > archive > decommissioned) and by doc type relevance for the user's likely workflows (DIBRG, IG, TM, RN before niche types).

2. **Expose what already exists** by linking from CSV rows to their markdown counterparts. This is the focus of §4 below.

Track 2 is much higher-leverage in the short term: it makes the existing 39% coverage *discoverable*. Most users today don't realize the markdown corpus exists.

---

## 4. The CSV → markdown linking question

The user-asked question: should the inventory CSV be expanded with links to the corresponding markdown documents in `vistadocs/vdl`, in addition to the existing `doc_url` (PDF) and `companion_url` (DOCX)?

**Recommendation: yes.** It is the single highest-leverage improvement to the discovery infrastructure. Below: the design.

### 4.1 The current state of cross-tier linking

Today, the CSV has:
- `doc_url` — points to va.gov for the document in its primary format (PDF or DOCX)
- `companion_url` — points to va.gov for the same document in the other format (when both exist)
- **No link to the markdown corpus.** Users who want the parseable markdown have to manually navigate `vistadocs/vdl`'s folder structure, guessing at filenames.

This is a discoverability failure. A user querying the CSV for "all active DIBRGs in ADT" gets `doc_url` values pointing at va.gov DOCX files — useful for citation, but not for programmatic content analysis.

### 4.2 The proposal

Add a new column to `vdl_inventory_enriched.csv`:

| Column | Purpose | Example |
|---|---|---|
| `github_md_url` | Direct link to the markdown counterpart in `vistadocs/vdl` | `https://github.com/vistadocs/vdl/blob/main/clinical/adt--admission-discharge-transfer/deployment-installation-back-out-and-rollback-guide--dibrg.md` |

Optionally also `github_md_raw_url` for the raw-content endpoint:

| Column | Purpose | Example |
|---|---|---|
| `github_md_raw_url` | Raw markdown URL for programmatic fetching | `https://raw.githubusercontent.com/vistadocs/vdl/main/clinical/adt--admission-discharge-transfer/deployment-installation-back-out-and-rollback-guide--dibrg.md` |

Rows whose document has no markdown conversion get an empty value in these columns. The web table at `vistadocs.github.io` then renders a "Markdown" link alongside the existing PDF/DOCX links, when present.

### 4.3 The mapping mechanism (and why it's nontrivial)

The mapping from CSV rows to markdown files is **many-to-one for anchor-layer documents**. Example:

The ADT DIBRG markdown file `clinical/adt--admission-discharge-transfer/deployment-installation-back-out-and-rollback-guide--dibrg.md` consolidates **9 CSV rows** (per its frontmatter `master_source` + `prior_versions`):

- DG\*5.3\*952 DIBRG (master)
- DG\*5.3\*916 DIBRG
- DG\*5.3\*977 DIBRG
- DG\*5.3\*1016 DIBRG
- DG\*5.3\*1025 DIBRG
- DG\*5.3\*1029 DIBRG
- DG\*5.3\*1034 DIBRG
- DG\*5.3\*1035 DIBRG
- DG\*5.3\*1047 DIBRG

Each of those 9 patch-IDs corresponds to a CSV row (or two — PDF + DOCX). All ~18 CSV rows should resolve to the same `github_md_url`.

**The linking algorithm:**

1. **Build the mapping at conversion time, not lookup time.** When the markdown conversion pipeline produces a markdown file, it knows which source patches it consolidated. Persist this mapping as part of the conversion output.
2. **Index the mapping by `patch_id_full`** (e.g. `DG*5.3*952`) — the CSV's natural per-row identifier.
3. **At enrich time,** for each CSV row, look up its `patch_id_full` in the mapping. If found, set `github_md_url` to the corresponding markdown file URL. If not found, leave blank.
4. **For "plain"-layer documents** (Kernel TM, KIDS User Guide, etc.) with no patch consolidation, the mapping is 1:1 and trivial.

**Practical consideration:** the markdown frontmatter already carries `master_source` and `prior_versions`. The mapping table can be built by walking the markdown corpus and parsing frontmatter — no new tooling required to extract the relationships. The pipeline addition is small.

### 4.4 Benefits

**For users of the search UI:**
- A "Markdown" link next to PDF and DOCX in the search results, where available
- Direct path from query → readable, parseable content
- Anyone scripting against the CSV can now drive into markdown bodies for full-text analysis

**For programmatic consumers (LLMs, RAG systems, dev tools):**
- The CSV becomes a complete index → content map. A consumer can filter to a working set, fetch markdown bodies, and reason over them. Today, they have to filter and then guess at markdown paths.
- The raw-URL variant supports streaming fetch from any HTTP client — no GitHub API needed.

**For documentation maintainers:**
- Coverage gaps become visible: any CSV row with empty `github_md_url` is a candidate for markdown conversion.
- The 39%-coverage figure becomes actionable: filter CSV rows where `github_md_url == ''` AND `app_status == 'active'` AND `doc_code IN ('DIBR', 'IG', 'TM', 'RN')` to get a prioritized conversion backlog.

**For this spec project specifically:**
- v4 of the package-lifecycle spec (the companion document) would gain inline links to every DIBRG/IG/TM it cites, going from "I claim this exists" to "click to read".

### 4.5 Implementation considerations

**Cost:** Low. The frontmatter is already there; the conversion pipeline already knows which rows consolidate into which markdown. The addition is one column + one mapping pass at enrich.

**Maintenance:** Negligible. When the markdown corpus updates, regenerate the mapping. When the CSV updates, re-apply the mapping. Both are existing pipeline steps.

**Schema impact:** Adding a column is non-breaking. The web table's `index.html` gets one new column entry in `COLS` and one new orthogonal-render branch in the column render function — no architectural changes.

**Risks:**
- **Stale links** if a markdown file is renamed and the mapping isn't regenerated. Mitigation: regenerate as part of any CSV refresh; consider a CI check that flags broken `github_md_url` values.
- **Anchor-vs-patch ambiguity** if a user expects a specific patch's content but gets the consolidated anchor. Mitigation: document the consolidation behavior in the search UI's help text. The anchor markdown contains all prior versions as appendices, so no information is lost — but users should know.

### 4.6 Recommendation

**Proceed with the addition.** Order of operations:

1. Add `github_md_url` (and optionally `github_md_raw_url`) to the CSV schema
2. Build the patch-ID → markdown-path mapping by walking `vistadocs/vdl` and parsing frontmatter
3. Apply the mapping at enrich-time
4. Update the web table's `index.html` to render the new column as a clickable "Markdown" link
5. Add CI to detect broken markdown links on each refresh

Estimated effort: small (a day or two of pipeline work). Estimated leverage: very high — closes the discoverability gap that currently makes the markdown corpus invisible to most users.

---

## 5. Priority matrix

| # | Issue | Priority | Effort | Where fixed |
|---|---|---|---|---|
| 4 | CSV → markdown linking | **H** | Low | Pipeline enrich + web UI |
| 3.3 | `app_name_full` inconsistency | **H** | Medium | Package-master table |
| 3.4 | Multiple abbrevs for same package | **H** | Medium | Package-master table |
| 3.10 | Markdown corpus coverage | **H** | High | Conversion pipeline (incremental) |
| 3.1 | UTF-8 mojibake | M | Low | Pipeline enrich (`ftfy`) |
| 3.2 | Source-document typos | M | Low | Pipeline enrich (correction table) |
| 3.5 | `doc_code` → `doc_label` drift | M | Low | Pipeline enrich (canonical table) |
| 3.6 | Sparse `pkg_ns` coverage | M | Medium | Package-master table |
| 3.8 | Markdown heading-level variance | M | Medium | Conversion pipeline |
| 3.7 | Section name parenthetical | L | Low | CSV schema cleanup |
| 3.9 | Doc-level vs package-level status | L | High | Pipeline enrich (version logic) |

The four `H`-priority items together close most of the practical search-quality gap. The three `H`-priority items 3.3, 3.4, and 3.6 share a single root cause and a single fix: a **package-master table** in the pipeline. Implementing that table is therefore higher-leverage than its row in the matrix suggests.

---

## 6. Open questions

These are decisions the maintainers of `vistadocs/vdl` and `vistadocs/vistadocs.github.io` need to make before any of the above can proceed:

1. **Source of truth for the package-master table.** Is there an existing canonical list of VistA packages (e.g. derived from a live VistA's `PACKAGE` file #9.4) that should seed it? Or does it need to be hand-curated from the existing CSV's `app_name_abbrev` distinct values?

2. **Refresh cadence.** The CSV currently has no embedded version stamp. Should each refresh write a `csv_generated_at` column or a sibling metadata file?

3. **Markdown coverage policy.** Is the goal to eventually convert 100% of active VDL documents to markdown, or only specific doc types (DIBRG, IG, TM, RN)? The answer informs the §3.10 prioritization.

4. **Anchor consolidation policy for the linking column.** When a CSV row resolves to an anchor markdown that consolidates 9 patches, should `github_md_url` link to:
   - The anchor file's top (default; loses patch-specific positioning), or
   - The anchor file with a fragment identifier pointing to the relevant prior-version appendix?
   The latter is more precise but requires consistent anchor-naming conventions in the converted markdown.

5. **Search content-tier expansion.** Should the search UI eventually index *markdown content* (full-text search across documents), or remain index-only? The latter is simpler; the former requires either a build-step search index (Lunr.js, MiniSearch) or a hosted search service.

6. **Typo correction policy.** When source documents contain typos (`Aurerus`, `DIBORG`), should the CSV preserve the original (faithful to source) or correct it (better search)? A hybrid — original in `doc_title_raw`, corrected in `doc_title` — supports both.

---

## 7. Appendix — reusable analysis queries

The findings in §3 were derived from the queries below. Documented here as specifications for re-running on future CSV refreshes.

| Finding | Query (conceptual) |
|---|---|
| §3.1 mojibake | Scan all string columns for any of the patterns `â€™`, `â€"`, `â€"`, `Â`, `Ã©`, `Ã¨` |
| §3.2 typos | Substring match on a known-typo list |
| §3.3 `app_name_full` inconsistency | Group by `app_name_abbrev`, count distinct `app_name_full`; flag where count > 1 |
| §3.4 multiple abbrevs | Group by normalized `app_name_full`, count distinct `app_name_abbrev`; flag where count > 1 |
| §3.5 `doc_code` drift | Group by `doc_code`, count distinct `doc_label`; flag where count > 1 |
| §3.6 `pkg_ns` coverage | Count rows where `pkg_ns == ''`; report as percentage |
| §3.10 markdown coverage | Count distinct `doc_slug` in CSV vs count of `*.md` files in `vistadocs/vdl` |

These queries should be re-run on each CSV refresh and the deltas tracked in a `data-quality-report.md` published alongside each release.
