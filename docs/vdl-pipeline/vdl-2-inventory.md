# VDL Pipeline — Stage 2: Inventory

**Date:** 2026-03-30
**Module:** `vista_docs/enrich_inventory.py`
**Output:** `~/data/vista-docs/inventory/vdl_inventory_enriched.csv`

---

## Table of Contents

1. [Overview](#1-overview)
2. [Problem Statement — The Raw Inventory](#2-problem-statement--the-raw-inventory)
3. [Stepwise Enrichment Approach](#3-stepwise-enrichment-approach)
4. [Pass 1 — Structural Normalization](#4-pass-1--structural-normalization)
5. [Pass 2 — Document Type Classification](#5-pass-2--document-type-classification)
6. [Pass 3 — Label Gap Resolution](#6-pass-3--label-gap-resolution)
7. [Pass 4 — Patch Identity Extraction](#7-pass-4--patch-identity-extraction)
8. [Pass 5 — Noise Identification](#8-pass-5--noise-identification)
9. [Pass 6 — doc_layer Stratification](#9-pass-6--doc_layer-stratification)
10. [Pass 7 — App Abbreviation Normalization](#10-pass-7--app-abbreviation-normalization)
11. [Pass 8 — System Classification](#11-pass-8--system-classification)
12. [Output Schema](#12-output-schema)
13. [Idempotency and Determinism](#13-idempotency-and-determinism)
14. [Coverage and Results](#14-coverage-and-results)

---

## 1. Overview
[↑ Table of Contents](#table-of-contents)

The inventory stage takes the raw VDL crawl output — a flat CSV of every document listed on the VA Documentation Library — and transforms it into a fully normalized, classified, and enriched data table suitable for downstream pipeline stages.

**Input:** `~/data/vista-docs/inventory/vdl_inventory.csv` (raw crawl output, ~8,834 rows)
**Output:** `~/data/vista-docs/inventory/vdl_inventory_enriched.csv` (29 columns, fully normalized)

The enrichment script (`enrich_inventory.py`) runs in a single deterministic pass over the raw CSV. Every transformation is a pure function of the input row — no external lookups, no AI, no stateful side effects. The script can be run any number of times and will always produce identical output from identical input.

The pipeline that follows depends on this table for:
- Document download selection (fetch stage)
- Markdown file naming (ingest stage)
- Frontmatter initialization (ingest and enrich stages)
- The interactive web browser at `vistadocs.github.io`

---

## 2. Problem Statement — The Raw Inventory
[↑ Table of Contents](#table-of-contents)

The raw crawl output has five systematic problems that make it unusable for analysis or downstream processing without normalization:

### Problem 1 — Unlabelled documents (741 rows, 8.4%)

The VDL assigns most documents a document type (`doc_code` / `doc_label`). 741 rows have no `doc_code` — the VDL lists the document without classifying it. This is not random: the unlabelled documents include entire application suites, specialized adjunct documents, and documents whose titles use non-standard vocabulary.

Of the 741 unlabelled rows:
- 272 are unique documents (the rest are PDF/DOCX duplicates)
- They represent 9.5% of the downloadable corpus
- They span every `doc_layer` tier (179 patch, 215 anchor, 347 plain)

Without a `doc_code`, these documents appear as "Uncategorized" in navigation, filtering, and corpus analysis. The gap is significant enough to require a multi-step resolution strategy (see §6).

### Problem 2 — No structural stratification (flat list)

The VDL presents each application's documents as a flat list. A Technical Manual for PSO Version 7 and a DIBR patch supplement for `PSJ*5*381` sit side by side with no structural distinction. For the pipeline to serve documents usefully — to select canonical references, identify superseded versions, and navigate the corpus by documentation tier — the flat list must be stratified.

The raw inventory has no `doc_layer` field. It must be derived from title structure.

### Problem 3 — No system-level classification

The VDL does not distinguish VistA packages from non-VistA systems. A core MUMPS clinical package, a COTS product with a VistA interface, a VA enterprise service, and a VBA benefits tool all appear in the same catalog with no type marker. The raw inventory has no `system_type` field.

Without classification, analysis of "VistA documentation" necessarily commingles fundamentally different kinds of systems.

### Problem 4 — Boilerplate noise rows (1,341 rows, 15%)

The VDL attaches a fixed set of boilerplate documents to every application entry, regardless of relevance. These include:
- **1,192 VBA form rows** — the same 8 benefit forms (VA-22, VA-21, etc.) repeated for every application
- **149 VA reference rows** — Strategic Plan documents and similar VA-wide publications attached to sections, not packages

These noise rows inflate document counts and pollute analysis. They must be identified and flagged.

### Problem 5 — Inconsistent app abbreviations

58 applications in the VDL have no machine-parseable abbreviation — the application name does not include a parenthetical abbreviation (the convention used for the other 166 apps). Without an abbreviation, grouping by application is unreliable.

Some abbreviations that do appear are ambiguous: `app_name_abbrev` and `pkg_ns` differ in 27 apps (16%) — the namespace used in KIDS patches is not always the same as the VDL organizational grouping key.

---

## 3. Stepwise Enrichment Approach
[↑ Table of Contents](#table-of-contents)

The enrichment script processes the raw inventory in eight sequential passes. Each pass adds or normalizes one set of fields, building on the results of the previous pass. All passes are pure and deterministic.

```
Pass 1: Structural normalization  → field renames, type casting, whitespace cleaning
Pass 2: Document type classification → doc_code, doc_label from title patterns
Pass 3: Label gap resolution      → four-step strategy for the 741 unlabelled rows
Pass 4: Patch identity extraction → patch_ver, patch_num, patch_id, patch_id_full, multi_ns
Pass 5: Noise identification      → noise_type (vba_form, va_ref, empty)
Pass 6: doc_layer stratification  → anchor / patch / plain from patch identity fields
Pass 7: App abbreviation normalization → app_name_abbrev (100% fill)
Pass 8: System classification     → system_type, cots_dependent
```

The passes are ordered so that each builds on the previous: classification (Pass 2) requires clean titles (Pass 1); doc_layer (Pass 6) requires patch identity fields (Pass 4); and noise tagging (Pass 5) is a prerequisite for meaningful coverage statistics.

---

## 4. Pass 1 — Structural Normalization
[↑ Table of Contents](#table-of-contents)

**Gap:** The raw crawl output uses inconsistent field names, mixed types, and non-normalized strings.

**Fix:** Rename fields to canonical names; cast numeric fields to integers; strip leading/trailing whitespace from all string fields; normalize file extensions to lowercase format without dot.

### Field renames

| Source field | Enriched field | Reason |
|---|---|---|
| `filename` | `doc_filename` | Avoid confusion with VistA FileMan "files" (database tables, not filesystem files) |
| `file_ext` | `doc_format` | Normalize to lowercase, drop dot; `doc_format` is cleaner than `doc_file_ext` |
| `app_name` | `app_name_full` | Clarifies this is the full name after stripping the parenthetical abbreviation |
| `vista_pkg_ns` | `pkg_ns` | Shorter; namespace concept is clear from context |

### Fields dropped from source

| Dropped field | Reason |
|---|---|
| `doc_type` | Identical to `doc_file_ext` (uppercase, no dot); had 1,341 nulls vs 0 in `doc_file_ext` |
| `doc_file_ext` | Redundant with `doc_format` (same values, leading dot); `doc_format` is cleaner for YAML |
| `doc_date` | Only 26 of 8,834 rows populated; free-form text from title parentheticals; not sortable |
| `app_code` | Identical to `app_name_abbrev` in all 166 named apps; `app_name_abbrev` fills 2 additional gaps |

### Type normalization

- `patch_ver_major`, `patch_ver_minor`, `patch_num` — cast to integer; leading zeros stripped
- `doc_format` — lowercase, dot stripped: `PDF` → `pdf`, `.docx` → `docx`
- All string fields — `.strip()` applied; Unicode whitespace normalized to ASCII space

**Result:** 8,834 rows with consistent field names, types, and whitespace. No rows added or removed.

---

## 5. Pass 2 — Document Type Classification
[↑ Table of Contents](#table-of-contents)

**Gap:** 741 rows (8.4%) have no `doc_code` / `doc_label` from the VDL crawl.

**Fix:** Classify `doc_code` and `doc_label` by matching the document title against `DOC_TYPE_PATTERNS` in `enrich_inventory.py`.

### Classification mechanism

```python
DOC_TYPE_PATTERNS = [
    # (regex, doc_code, doc_label) — ordered most-specific to least-specific
    (r'Deployment,?\s+Installation,?\s+Back.?Out', 'DIBR',
        'Deployment, Installation, Back-Out, and Rollback Guide'),
    (r'\bDIBR\b',   'DIBR', 'Deployment, Installation, Back-Out, and Rollback Guide'),
    (r'Release\s+Notes?',  'RN',   'Release Notes'),
    (r'Technical\s+Manual','TM',   'Technical Manual'),
    (r"User.?s?\s+Guide",  'UG',   'User Guide'),
    (r"User\s+Manual",     'UM',   'User Manual'),
    (r"Installation\s+Guide", 'IG','Installation Guide'),
    # ... (25 total patterns)
]

def classify_doc_type(title: str) -> tuple[str, str]:
    for pattern, code, label in DOC_TYPE_PATTERNS:
        if re.search(pattern, title, re.IGNORECASE):
            return code, label
    return '', ''
```

Patterns are applied in order. The first match wins. More specific patterns (e.g., `DIBR` before generic `Guide`) appear before broader ones.

### Ordering rule

Patterns are grouped by doc type family and ordered within each group from most-specific to least-specific. The generic `\bGuide\b` catchall is last. This prevents "Deployment Guide" from matching the `TG` (Technical Guide) pattern before reaching the `IG` pattern.

### Result

After Pass 2: approximately 8,093 rows have `doc_code` filled (91.6% coverage). The remaining 741 rows enter the gap resolution stage (Pass 3).

---

## 6. Pass 3 — Label Gap Resolution
[↑ Table of Contents](#table-of-contents)

**Gap:** 741 rows remain without `doc_code` after title-pattern matching. Root causes fall into three categories:

| Cause | Docs | Description |
|---|---|---|
| A — Title pattern gap | ~100 | Title has a recognizable doc-type keyword that `DOC_TYPE_PATTERNS` does not cover (possessives, acronyms, phrase variants) |
| B — Filename encodes type, title does not | ~80 | VA naming convention uses `_pom`, `_dg`, `_wf` etc. as filename suffixes, but `enrich_inventory.py` classifies by title only |
| C — No lexical signal anywhere | ~92 | Descriptive titles with no standard VA doc-type keyword and no clean filename suffix |

Resolution uses four steps in priority order. Each step acts only on rows still empty after the previous step.

### Step 3.1 — Fix title pattern gaps (~90 docs resolved)

Add or fix patterns in `DOC_TYPE_PATTERNS` to cover missing vocabulary:

| Pattern added / fixed | doc_code | Docs resolved | Root cause |
|---|---|---|---|
| `User.?s?\s+Guide` (fix existing) | UG | 18 | Possessive ("User's Guide") broke original `User\s+Guide` regex |
| `Administrator.?s?\s+Guide` | AG | 11 | Pattern present in `rules.py` but absent from `DOC_TYPE_PATTERNS` |
| `Developer.?s?\s+Guide` | DG | 12 | Same — present in rules but absent from enrich_inventory |
| `System.?s?\s+Management` | SM | 19 | Pattern absent from `DOC_TYPE_PATTERNS` entirely |
| `Deployment\s+Guide` | IG | 7 | Present in `rules.py` only |
| `Troubleshooting\s+Guide` | SUP | 15 | Pattern absent; troubleshooting guides are adjunct documents |
| `Productions?\s+Operations?\s+Manual` | POM | 9 | "Productions" typo variant; "Operations Manual" without "Production" prefix |
| `\bPOM\b` standalone | POM | 31 | Trailing whitespace or encoding artifact in JLV titles caused existing `\bpom\b` to not fire |
| `\bHandbook\b` | UG | 1 | Not in patterns; handbooks are user-facing reference documents |
| `\bMenu\b` | UM | 1 | Standalone menu reference; corpus validates UM 100% for this pattern |
| `^\d{3}:` | SUP | ~10 | LR numbered procedure series (`001: Bacteriology`, `002: Blood Bank`, etc.) |

**Key implementation detail — `\bPOM\b` investigation:** The 31 JLV Release POM titles failed to match the existing `\bpom\b` pattern. Inspection of raw bytes revealed trailing non-breaking space characters (`\u00a0`) in the VDL title field. Fix: strip all Unicode whitespace (not just ASCII space) in Pass 1 before classification in Pass 2.

**Estimated net unique docs resolved: ~90**

### Step 3.2 — Filename suffix classification (~50 docs resolved)

The VA document naming convention encodes document type as the last `_`-separated segment of the filename stem. `enrich_inventory.py` is extended with a secondary classification pass using the `doc_slug` field (URL-safe filename stem).

```python
_SLUG_SUFFIX_RE = re.compile(r'[_\-]([a-z]{2,8})$', re.I)

DOC_FILENAME_SUFFIX_MAP = {
    'pom':     ('POM',  'Production Operations Manual'),
    'raci':    ('POM',  'Production Operations Manual'),
    'tg':      ('TRG',  'Training Guide'),        # NOT Technical Guide — 100% corpus validation
    'dg':      ('DG',   'Developer Guide'),
    'ag':      ('AG',   "Administrator's Guide"),
    'wf':      ('WF',   'Workflow Guide'),
    'kda':     ('SUP',  'Supplement'),             # Known Defects and Anomalies
    'sp':      ('SUP',  'Supplement'),
    'sm':      ('SM',   'Site Manual / Systems Management Guide'),
    'ig':      ('IG',   'Installation Guide'),
    'dibrg':   ('DIBR', 'Deployment, Installation, Back-Out, and Rollback Guide'),
    'dibr':    ('DIBR', 'Deployment, Installation, Back-Out, and Rollback Guide'),
    'bckout':  ('DIBR', 'Deployment, Installation, Back-Out, and Rollback Guide'),
    'rn':      ('RN',   'Release Notes'),
    'readme':  ('RN',   'Release Notes'),
    'notes':   ('RN',   'Release Notes'),
    'tm':      ('TM',   'Technical Manual'),
    'sg':      ('SG',   'Security Guide'),
    'qr':      ('QRG',  'Quick Reference Guide'),
    'tut':     ('TRG',  'Training Guide'),
    'tutorial':('TRG',  'Training Guide'),
    'addendum':('UG',   'User Guide'),
    'pm':      ('API',  'API / Programmer Manual'),
    'ddd':     ('SUP',  'Supplement'),
    'glossary':('SUP',  'Supplement'),
    'rs':      ('RS',   'Requirements Specification'),
    'plan':    ('DIBR', 'Deployment, Installation, Back-Out, and Rollback Guide'),
    # app-specific disambiguation:
    # '_signed' → POM for PRC; → RS for TMP (handled in classify_by_filename)
}
```

Applied **after** the title pass. Title classification always takes precedence. Suffix classification is invoked only when `doc_code` is still empty.

**Critical note on `_tg`:** In VA naming convention, `_tg` suffix means **Training Guide** (TRG), not Technical Guide (TG). The labelled corpus validates this at 100% (8/8 docs). The correct mapping is `tg → TRG`. Any mapping of `_tg` to TG is incorrect.

**Known anomalies requiring app-specific disambiguation:**

| doc_slug pattern | App | Suffix says | Title says | Correct code | Rule |
|---|---|---|---|---|---|
| `mag_cx_*_ag_pom` | MAG | `_pom` | "CVIX Administrator's Guide" | AG | Title takes precedence; `_pom` is a VDL cataloguing error |
| `gmrc_*_57rn` | GMRC | `_rn` | "Suicide Hotline Consult Setup" | IG | Setup document; VDL mislabelled as RN |
| `hc_hl7_messaging_pom_ecms_signed` | PRC | `_signed` | "HL7 Messaging POM" | POM | `_signed` → POM for PRC |
| `tmp_*_signed` | TMP | `_signed` | "Requirements" | RS | `_signed` → RS for TMP |

These are handled by an `APP_SPECIFIC_OVERRIDES` dict in `enrich_inventory.py` keyed by `doc_slug` prefix, checked before the generic suffix map.

**Corpus-validated suffix statistics (suffixes with ≥4 labelled occurrences, ≥80% consensus):**

| Suffix | doc_code | Consensus | n |
|---|---|---|---|
| `_are` | FORM | 100% | 1,043 |
| `_dibrg` | DIBR | 100% | 594 |
| `_rn` | RN | 96% | 1,112 |
| `_um` | UM | 97% | 315 |
| `_tm` | TM | 97% | 262 |
| `_ug` | UG | 94% | 265 |
| `_notes` | RN | 99% | 210 |
| `_vdd` | VDD | 99% | 147 |
| `_manual` | TM | 82% | 166 |
| `_addendum` | UG | 100% | 94 |
| `_pom` | POM | 100% | 40 |
| `_tg` | **TRG** | **100%** | 8 |

**Estimated net unique docs resolved (beyond Step 3.1): ~50**

### Step 3.3 — Group key peer inference (~20 docs resolved)

For rows still empty after Steps 3.1 and 3.2, look up sibling documents in the same `group_key` (i.e., documents belonging to the same application version group).

```python
def infer_from_peers(row, by_group):
    gk = row.get('group_key')
    if not gk:
        return '', ''
    peers = [p for p in by_group[gk]
             if p['doc_code'] and p['doc_slug'] != row['doc_slug']]
    if not peers:
        return '', ''
    peer_codes = Counter(p['doc_code'] for p in peers)
    # Only apply if ALL labelled peers agree on the same doc_code
    if len(peer_codes) == 1:
        code = list(peer_codes.keys())[0]
        label = peers[0]['doc_label']
        return code, label
    return '', ''
```

Peer inference is only applied when:
1. All labelled siblings in the `group_key` agree on a single `doc_code`, AND
2. The unlabelled doc's title contains no contradiction (e.g., a title containing "workflow" is not assigned `IG` from a peer group)

Rows classified by peer inference are flagged with `doc_code_source = 'peer'` for downstream review.

**Estimated net unique docs resolved: ~20**

### Step 3.4 — Residual (154 unique docs accepted as unlabelled)

After all three automated steps, 154 unique documents (1.7% of the 8,834-row inventory) remain without `doc_code`. These are genuinely outside the reach of lexical or structural heuristics:

| Category | Count | Description |
|---|---|---|
| A — Patch-prefix descriptive | 42 | Patch docs whose titles describe clinical content with no standard doc-type keyword |
| B — Numbered series | 0 | Fully resolved by `^\d{3}:` pattern |
| C — Plain/anchor specialist | 57 | Anchor-layer docs with idiosyncratic VA-internal titles |
| D — Peripheral / non-VistA apps | 55 | Apps with non-standard naming (CAPRI workflows, NOIS admin docs, etc.) |

These 154 documents are retained in the inventory with `doc_code = ''`. They appear as "Uncategorized" in navigation and are excluded from type-distribution statistics. They are not errors — they are genuine gaps in the VDL's own classification scheme.

A `MANUAL_OVERRIDES` dict in `enrich_inventory.py`, keyed by `doc_slug`, provides a mechanism for targeted manual resolution of specific documents without modifying the heuristic rules.

---

## 7. Pass 4 — Patch Identity Extraction
[↑ Table of Contents](#table-of-contents)

**Gap:** The raw inventory has no structured patch identity fields. Patch IDs are embedded in document titles as free-text strings in `NS*V*P` format.

**Fix:** Parse patch identity from document title and filename using a deterministic regex pipeline.

### Parsing logic

```python
# Pattern: NS*V*P (e.g., PSO*7*500, DG*5.3*1057)
_PATCH_RE = re.compile(
    r'\b([A-Z][A-Z0-9]{0,5})\*(\d+(?:\.\d+)?)\*(\d+)\b'
)

# Pattern: NS*V (anchor doc — version without patch number)
_ANCHOR_RE = re.compile(
    r'\b([A-Z][A-Z0-9]{0,5})\*(\d+(?:\.\d+)?)\b'
)
```

For each row, the parser tries `_PATCH_RE` first. If it matches, `pkg_ns`, `patch_ver`, and `patch_num` are extracted. If not, `_ANCHOR_RE` is tried to extract `pkg_ns` and `patch_ver` for anchor-layer documents.

### Fields produced

| Field | Description | Example |
|---|---|---|
| `pkg_ns` | MUMPS namespace extracted from patch ID | `PSO` |
| `patch_ver` | Version string as-is (do not sort as string) | `7`, `5.3`, `22.2` |
| `patch_ver_major` | Integer major version | `7` |
| `patch_ver_minor` | Integer minor version; `0` when major-only | `0` |
| `patch_num` | Patch sequence number as integer (leading zeros stripped) | `500` |
| `patch_id` | Canonical patch ID: `NS*V*P` for patch docs; `NS*V` for anchor docs | `PSO*7*500` |
| `patch_id_full` | Full raw prefix for multi-namespace patches | `DG*5.3*554/TIU*1*184/USR*1*27` |
| `multi_ns` | `1` if title contains multiple `NS*V*P` segments; `0` otherwise | `0` |
| `group_key` | Functional group ID: `app_name_abbrev:pkg_ns:patch_ver` | `PSO:PSO:7` |

### Version sorting

**Never sort `patch_ver` as a string.** `"5.3"` sorts after `"10"` lexicographically. Always use the integer fields:

```sql
ORDER BY patch_ver_major ASC, patch_ver_minor ASC, patch_num ASC
```

### Multi-namespace patches

48 rows have titles containing multiple `NS*V*P` segments (e.g., `DG*5.3*554/TIU*1*184/USR*1*27`). These are KIDS builds that install into multiple namespaces simultaneously. For these rows:
- `patch_id` is set to the first parsed `NS*V*P` segment
- `patch_id_full` is set to the full raw prefix string
- `multi_ns = 1`

---

## 8. Pass 5 — Noise Identification
[↑ Table of Contents](#table-of-contents)

**Gap:** 1,341 rows (15.2%) are boilerplate documents attached to every VDL section, not genuine package documentation.

**Fix:** Classify each row into `noise_type` using title and URL signals.

| noise_type | Rows | Detection rule |
|---|---|---|
| `vba_form` | 1,192 | Title matches VA form number pattern (`\bVA\s+Form\b` or `\b2[12]-\d+`) OR `doc_url` points to `benefits.va.gov` |
| `va_ref` | 149 | Title matches Strategic Plan patterns OR `doc_url` contains `va.gov/vapubs` |
| `''` (empty) | 7,493 | All other rows — genuine package documentation |

**Standard analysis filter:** All substantive analysis applies `WHERE noise_type = ''`. Forms and VA reference docs inflate counts and are not package documentation.

The 1,192 `vba_form` rows are the same 8 VA benefit forms attached to every application's VDL entry — VA Forms 22-1990, 21-22, 21-4142, etc. They are not VistA documentation.

The 149 `va_ref` rows are VA-wide strategic planning documents attached to section headers, not to specific packages.

---

## 9. Pass 6 — doc_layer Stratification
[↑ Table of Contents](#table-of-contents)

**Gap:** The raw VDL presents each application's documents as a flat, undifferentiated list. Without structural stratification, the pipeline cannot distinguish canonical reference manuals from per-patch supplements.

**Fix:** Assign `doc_layer` deterministically from the patch identity fields produced in Pass 4.

### Assignment rules

| Condition | doc_layer | Meaning |
|---|---|---|
| `patch_ver` set AND `patch_num` empty | `anchor` | Canonical versioned reference document for this package version |
| `patch_num` set (with or without version) | `patch` | Per-patch supplement — documents one specific KIDS patch |
| Neither `patch_ver` nor `patch_num` set | `plain` | No parseable version or patch signal — version-ambiguous document |

### Why `doc_layer` is not re-derivable

`doc_layer` is computed once from `patch_ver` and `patch_num` during enrichment. **Do not re-derive it at query time** from those fields — the derivation depends on the parsing context and edge-case handling in the enrichment script. Use `doc_layer` directly.

### Distribution

| doc_layer | Count | Description |
|---|---|---|
| `patch` | 3,584 | Per-patch change documents |
| `plain` | 3,332 | No version or patch signal |
| `anchor` | 1,918 | Stable versioned base documents |

### The `plain` tier

`plain` is a residual category. It includes:
- Genuinely versionless documents (cross-cutting guides, glossaries, policy docs)
- Very old documents predating the version-in-title convention
- Documents whose titles were too idiosyncratic for the parser to extract version info

`plain` does not mean unimportant. The PSO Technical Manual with no version in the title may be the most current one. The 741 unlabelled `doc_code` rows are overwhelmingly `plain`, reflecting the same parsing gap — titles without structured signals resist both doc-type classification and layer assignment.

---

## 10. Pass 7 — App Abbreviation Normalization
[↑ Table of Contents](#table-of-contents)

**Gap:** 58 of 196 VDL applications have no machine-parseable abbreviation. The VDL convention of embedding abbreviations in parentheses (`Pharmacy Patient Safety (PSJ)`) is followed by 166 apps but not the remaining 58.

Without an abbreviation, `app_name_abbrev` would be empty for 58 apps, making application-level grouping unreliable.

**Fix:** A three-tier fallback strategy produces 100% fill for `app_name_abbrev`.

### Tier 1 — VDL-assigned (166 apps, authoritative)

Extracted from trailing parentheses in `app_name_full` using:
```python
_ABBREV_RE = re.compile(r'\(([A-Z][A-Z0-9]{0,6})\)\s*$')
```

This is the authoritative VDL abbreviation. It is stable across crawl runs.

### Tier 2 — Curated fallback map (58 apps, derived)

A `APP_ABBREV_FALLBACK` dict in the script provides manually curated abbreviations for all 58 apps that lack VDL-assigned abbreviations:

| App name (partial) | Fallback abbrev | Notes |
|---|---|---|
| CPRS: Clinical Reminder Updates | PXRM | Delivered under the Clinical Reminders package |
| KAAJEE | KAAJEE | No standard namespace; use full name |
| HL7 (VistA Messaging) | HL7 | Not a KIDS package; no namespace |
| Patient Record Flags | PRF | Clinical flags namespace |
| ... | ... | ... |

**These are not VDL-assigned.** They are derived abbreviations. Do not treat fallback abbrevs as authoritative VDL identifiers.

### Tier 3 — pkg_ns last resort

For any remaining rows after Tiers 1 and 2, `app_name_abbrev` falls back to `pkg_ns`. This covers only a handful of edge cases.

**Result:** `app_name_abbrev` is 100% filled as of the March 2026 enrichment.

### app_name_abbrev vs pkg_ns

These fields differ in 27 apps (16% of the catalog). They answer different questions:

- `app_name_abbrev` = **VDL organizational grouping key** — how the VDL groups documents under an application
- `pkg_ns` = **MUMPS package namespace** — the namespace used in KIDS patch IDs

Examples of divergence:
| app_name_abbrev | pkg_ns | Explanation |
|---|---|---|
| ACR | SD | Ambulatory Care Reporting is delivered inside the Scheduling package |
| ADT | ADT, DG | ADT uses both namespaces |
| ASU | USR | Authorization/Subscription Utility uses the USR namespace |

Use `app_name_abbrev` for VDL-level grouping and navigation. Use `pkg_ns` for linking to KIDS patch history.

---

## 11. Pass 8 — System Classification
[↑ Table of Contents](#table-of-contents)

**Gap:** The VDL does not distinguish VistA packages from non-VistA systems. All 196 applications appear in the same catalog with no system-type marker. Without classification, analysis of "VistA documentation" necessarily commingles fundamentally different kinds of systems.

**Fix:** `classify_vista_type.py` (invoked as a post-processing step after the main enrichment) assigns `system_type` and `cots_dependent` to every row.

### Working definition of VistA

A system is VistA if and only if it:
1. Is implemented in MUMPS/M
2. Is deployed via the Kernel Installation and Distribution System (KIDS)
3. Runs as server-side M code on VA server nodes

This is the **KIDS test**: if a system does not install via KIDS, it is not VistA. If it does, it is VistA (or a hybrid containing VistA).

### Classification scheme (11 categories)

| system_type | Apps | Description |
|---|---|---|
| VistA | 127 | Pure MUMPS/M package deployed via KIDS — canonical VistA |
| VistA + GUI | 2 | KIDS MUMPS server + dedicated GUI client under one VDL entry (CPRS, MAG) |
| VistA + COTS | 3 | KIDS MUMPS integration layer + COTS system (MD, YS, ROI) |
| VistA + middleware | 1 | KIDS MUMPS component + non-VistA connector layer (XOBV/VistALink) |
| Web client | 20 | Web/mobile app accessing VistA data; no MUMPS server component |
| Integration middleware | 10 | Adapter between VistA and external systems; no clinical/admin function |
| VA enterprise service | 23 | National VA platform VistA interfaces with; not part of VistA |
| VBA system | 1 | Veterans Benefits Administration tool (CAPRI) |
| COTS product | 3 | Commercial software with no VistA MUMPS component (BMS, CRMS, VPS) |
| Data patch | 4 | KIDS build whose payload is reference data, not M code (CPT, ICD, DRG, LEX) |
| Program documentation | 2 | VA program docs, not software (EHM, MON) |

### VistA vs. non-VistA summary

| | Apps | % | Rows | % |
|---|---|---|---|---|
| VistA (all four VistA categories) | 133 | 68% | 6,674 | 76% |
| Non-VistA | 63 | 32% | 2,160 | 24% |

### cots_dependent field

For applications with a named commercial product dependency, `cots_dependent` names the specific COTS product. Empty string if none.

| app_name_abbrev | cots_dependent |
|---|---|
| MD | COTS bedside device vendors |
| YS | Netsmart Mental Health Suite |
| ROI | Ciox / DSSI ROI system |
| CPT | AMA CPT code set |
| DRG | 3M DRG grouper |
| PREM | Multum drug database (MOCHA) |

### Implementation

`classify_vista_type.py` reads `vdl_inventory_enriched.csv`, calls `classify_row(row) → (system_type, cots_dependent)` for each row, and inserts the two new columns after `app_status`. The classification function is a deterministic if/elif chain against `app_name_abbrev` — no AI, no external lookups.

The script is idempotent: if `system_type` and `cots_dependent` columns are already present, it overwrites them. The column positions are fixed by insertion point, not by column order in the input.

---

## 12. Output Schema
[↑ Table of Contents](#table-of-contents)

The enriched inventory is a 29-column CSV. Column order is fixed and canonical.

```
section_name, section_code,
app_name_full, app_name_abbrev, app_status,
system_type, cots_dependent,
decommission_date,
pkg_ns, patch_ver, patch_ver_major, patch_ver_minor, patch_num,
patch_id, patch_id_full, multi_ns,
group_key,
doc_code, doc_label, doc_layer,
doc_title, doc_filename, doc_slug, doc_format, doc_subject,
noise_type,
app_url, doc_url, companion_url
```

### Field reference — quick summary

| Field | Fill | Key notes |
|---|---|---|
| `section_name` | 100% | CLI, FIN, INF, GUI, MON |
| `section_code` | 100% | Short code for grouping; use this, not section_name |
| `app_name_full` | 100% | Full application name, parens stripped |
| `app_name_abbrev` | 100% | Primary app grouping key; 100% fill after Pass 7 |
| `app_status` | 100% | `active`, `archive`, `decommissioned` |
| `system_type` | 100% | 11-category system classification |
| `cots_dependent` | sparse | Named COTS dependency; empty if none |
| `decommission_date` | 1.3% | `YYYY-MM` format; sparse — do not use as completeness signal |
| `pkg_ns` | 56.4% | MUMPS namespace; differs from `app_name_abbrev` in 27 apps |
| `patch_ver` | 61.3% | Version string — sort by integer fields, not this string |
| `patch_ver_major` | 61.3% | Integer major version |
| `patch_ver_minor` | 61.3% | Integer minor version |
| `patch_num` | 40.6% | Patch sequence number as integer |
| `patch_id` | 56.4% | Canonical `NS*V*P` or `NS*V` patch ID |
| `patch_id_full` | 0.5% | Full multi-namespace prefix (48 rows) |
| `multi_ns` | — | `1` for multi-namespace patches |
| `group_key` | 61.3% | `app_name_abbrev:pkg_ns:patch_ver` — groups anchor + patch docs |
| `doc_code` | 91.6% | Normalized doc type abbreviation |
| `doc_label` | 91.6% | Full canonical doc type label |
| `doc_layer` | 100% | `anchor`, `patch`, `plain` — use directly, do not re-derive |
| `doc_title` | 100% | Original title as listed on VDL — do not clean or normalize |
| `doc_filename` | 100% | Document filename (named `doc_filename` to avoid FileMan confusion) |
| `doc_slug` | 100% | URL-safe stable identifier; PDF/DOCX pairs share the same slug |
| `doc_format` | 100% | `pdf`, `docx`, `doc` |
| `doc_subject` | ~68% | Best-effort subject qualifier stripped from title |
| `noise_type` | 100% | `''` genuine; `vba_form`; `va_ref` — exclude non-empty from analysis |
| `companion_url` | 84% | URL of paired format (PDF↔DOCX); empty if no pair |
| `app_url` | 100% | VDL application page URL |
| `doc_url` | 100% | Direct document file URL |

### Standard analysis filters

Always apply when computing documentation coverage or gap statistics:

```sql
WHERE noise_type = ''        -- exclude VBA forms and VA reference docs
AND   app_status = 'active'  -- unless studying archive/decommissioned
```

Version sorting — always use integers:
```sql
ORDER BY patch_ver_major ASC, patch_ver_minor ASC, patch_num ASC
```

---

## 13. Idempotency and Determinism
[↑ Table of Contents](#table-of-contents)

The inventory enrichment pipeline is fully idempotent and deterministic:

**Idempotent:** Running `enrich_inventory.py` multiple times on the same input always produces the same output. No state is accumulated between runs. The output CSV is completely replaced each run.

**Deterministic:** Every enrichment decision is a pure function of the input row. No AI, no random seeds, no external lookups, no network calls. Given the same raw CSV, the same script version always produces the same enriched CSV.

**Reproducible:** The enrichment script is version-controlled. The raw inventory CSV is version-controlled. Together they reproduce any historical version of the enriched inventory.

**What is NOT deterministic:** The raw crawl output depends on what is currently published on the VDL website. If VA adds, removes, or retitles documents between crawls, the enriched output will differ. This is expected — it reflects actual changes to the catalog, not pipeline non-determinism.

**Re-run safety:** The enrichment can be re-run any time:
- When new patterns are added to `DOC_TYPE_PATTERNS`
- After the raw inventory is re-crawled
- When `classify_vista_type.py` classification is updated
- As a verification step to confirm output has not drifted

---

## 14. Coverage and Results
[↑ Table of Contents](#table-of-contents)

Final state of `vdl_inventory_enriched.csv` after all eight passes:

| Metric | Value |
|---|---|
| Total rows | 8,834 |
| Unique applications | 196 |
| Columns | 29 |
| `doc_code` filled | 8,093 (91.6%) |
| `doc_code` empty | 741 (8.4%) |
| Noise rows | 1,341 (15.2%) |
| Substantive rows | 7,493 (84.8%) |
| `app_name_abbrev` filled | 8,834 (100%) |
| `doc_layer` filled | 8,834 (100%) |
| `system_type` filled | 8,834 (100%) |
| `noise_type` filled | 8,834 (100%) |

### doc_code distribution (substantive labelled rows)

| doc_code | doc_label | Count |
|---|---|---|
| RN | Release Notes | 1,570 |
| DIBR | Deployment, Installation, Back-Out, and Rollback Guide | 1,316 |
| FORM | VBA Form *(noise)* | 1,192 |
| UM | User Manual | 871 |
| UG | User Guide | 814 |
| IG | Installation Guide | 785 |
| TM | Technical Manual | 707 |
| CRU | Clinical Reminder Update | 336 |
| VDD | Version Description Document | 145 |
| IG-IMP | Implementation Guide | 88 |
| POM | Production Operations Manual | 66 |
| SG-SET | Setup Guide | 54 |
| SG | Security Guide | 44 |
| INT | Interface Specification | 36 |
| QRG | Quick Reference Guide | 24 |
| API | API / Programmer Manual | 24 |
| CFG | Configuration Guide | 16 |
| TG | Technical Guide | 15 |
| TRG | Training Guide | 10 |
| REF | Reference | 8 |
| PDD | Patch Description Document | 8 |
| APX | Appendix | 4 |
| FAQ | Frequently Asked Questions | 4 |
| DESC | Description Document | 4 |
| CVG | Conversion Guide | 2 |

### Projected label gap resolution (Steps 3.1–3.3)

| Step | Mechanism | Unique docs resolved | Cumulative | Remaining |
|---|---|---|---|---|
| Baseline | — | — | 0 | 272 |
| Step 3.1 — title patterns | 11 new/fixed patterns | ~90 | ~90 | ~182 |
| Step 3.2 — filename suffixes | Suffix map secondary pass | ~50 | ~140 | ~132 |
| Step 3.3 — peer inference | 100%-consensus peers | ~20 | ~160 | ~112 |
| Step 3.1b — `^\d{3}:` pattern | LR numbered series | ~5 | ~165 | ~107 |
| **Projected residual** | | | | **~107 docs (~3.7%)** |

The projected residual of ~107 documents represents genuinely atypical VA documentation outside the standard vocabulary: purely descriptive patch titles, VA-internal administrative notices, and non-VistA apps with idiosyncratic naming. These cannot be reliably classified without reading the document content.

---

*End of report.*
