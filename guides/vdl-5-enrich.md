# VDL Pipeline — Stage 4: Enrich

**Date:** 2026-03-30
**Module:** `vista_docs/enrich/`
**Output:** YAML frontmatter in each markdown file

---

## Table of Contents

1. [Overview](#1-overview)
2. [Architecture](#2-architecture)
3. [Frontmatter Management](#3-frontmatter-management)
4. [Enrichment Cycles](#4-enrichment-cycles)
5. [Inventory Sync](#5-inventory-sync)
6. [Canonical Field Order](#6-canonical-field-order)
7. [Coverage and Results](#7-coverage-and-results)

---

## 1. Overview
[↑ Table of Contents](#table-of-contents)

The enrich stage reads every markdown document in the corpus and extracts structured metadata from its content, writing the extracted fields into the YAML frontmatter block at the top of each file. This transforms the corpus from a set of plain markdown files into a machine-readable knowledge base where every document carries its own complete metadata record.

**Input:** `~/data/vista-docs/markdown/<app_code>/<doc>.md` (2,240 files)
**Output:** Updated YAML frontmatter in each `.md` file (30–35 fields per document)

The enrich stage ran in seven sequential cycles, each adding a new set of fields. At the end of all cycles:
- **2,240 documents** with complete frontmatter (100% coverage)
- **2,220 documents** with word count metadata
- **1,897 documents** with page count metadata
- **14,881,751 words** read and analyzed across the corpus

---

## 2. Architecture
[↑ Table of Contents](#table-of-contents)

The enrich stage is split into pure and I/O layers:

- **`enrich/frontmatter.py`** — pure; all frontmatter manipulation functions; fully unit-tested
- **`enrich/inventory_fields.py`** — pure; builds an index from the inventory CSV; looks up inventory fields for each document; fully unit-tested
- **`enrich/sync.py`** — I/O; walks the markdown directory; reads files; calls `rebuild_frontmatter`; writes back
- **`enrich/runner.py`** — I/O; orchestrates enrichment cycles; calls the AI extraction engine

The AI extraction engine reads each document's full markdown text and returns a structured dict of field values. The runner writes these into frontmatter via `rewrite_frontmatter`.

### Idempotency

Each enrichment cycle checks whether its target fields are already present in the frontmatter before processing. If all target fields for a cycle are present and `--force` is not set, the document is skipped. This means:
- Re-running a completed cycle is a no-op
- A cycle interrupted partway through resumes from the last unprocessed document
- Specific documents can be re-enriched with `--force` without affecting others

---

## 3. Frontmatter Management
[↑ Table of Contents](#table-of-contents)

### Two Distinct Functions

`enrich/frontmatter.py` provides two frontmatter update functions with different contracts:

#### `rewrite_frontmatter(md, new_fields)`

Used during enrichment cycles. Merges new fields into the existing frontmatter block, preserving the existing field order for fields already present. New fields are appended after existing ones.

- Does not reorder existing fields
- Does not retire obsolete fields
- Safe to call on partially-enriched documents

#### `rebuild_frontmatter(md, extra_fields=None)`

Used during the inventory sync stage. Applies the canonical field order (`CANONICAL_FIELD_ORDER`), removes fields in `RETIRED_FIELDS`, and merges any extra inventory fields.

- Reorders ALL fields into canonical order
- Removes retired fields
- Use only when a clean canonical rewrite is desired (sync stage, not incremental enrichment)

### YAML Safety

All string values written to YAML frontmatter are double-quoted. Values containing `:`, `#`, `[`, `]`, `{`, or `}` would produce malformed YAML if unquoted. The serialization layer enforces quoting universally rather than testing each value.

---

## 4. Enrichment Cycles
[↑ Table of Contents](#table-of-contents)

Seven enrichment cycles were run across the corpus. Each cycle targeted a distinct set of fields.

### Cycle 1 — Document Identity

Target fields extracted from document title, headers, and opening sections:

| Field | Description |
|---|---|
| `title` | Canonical document title as stated in the document |
| `doc_type` | Document type category |
| `doc_label` | Human-readable document type label |
| `doc_layer` | Documentation tier: patch, anchor, plain |
| `doc_subject` | Subject/version string |
| `app_code` | Application code |
| `app_name` | Application full name as stated in document |
| `section` | VDL section |
| `app_status` | Application status |
| `pkg_ns` | MUMPS namespace prefix |
| `patch_ver` | Package version |
| `patch_id` | KIDS patch identifier |
| `group_key` | Multi-patch group key |

These fields cross-validate inventory values against what the document itself states. Discrepancies were flagged for manual review.

### Cycle 2 — Package Identity

Target fields extracted from Technical Manual introductory sections:

| Field | Description |
|---|---|
| `pkg_name` | Canonical package name as stated in document |
| `pkg_namespace` | Confirmed MUMPS namespace prefix |
| `pkg_version` | Version string as stated in document |
| `audience` | Intended reader (clinician, developer, system manager, IRM, ADPAC, etc.) |
| `figure_count` | Total figures in the document |

The `audience` field distinguishes user manuals (clinical staff, ADPAC) from technical manuals (IRM, developers, system managers). This drives document selection logic when serving documents to specific reader types.

### Cycle 3 — Document Structure

Target fields extracted from document content analysis:

| Field | Description |
|---|---|
| `word_count` | Total word count of the markdown document |
| `is_stub` | Boolean: document is a stub (< 500 words, no substantive content) |
| `has_toc` | Boolean: document contains a table of contents |
| `patch_number` | Numeric patch sequence extracted from title or body |
| `description` | One-sentence description of document purpose |
| `file_numbers` | FileMan file numbers referenced (e.g., `[#2]`, `[#4.001]`) |
| `security_keys` | VistA security keys defined or referenced in the document |
| `menu_options` | Count of VistA menu options documented |

`is_stub` identifies documents that converted to nearly empty markdown — typically scanned PDFs or documents whose content is entirely in tables that Docling could not extract. Stubs are excluded from word-count statistics and corpus analysis.

`file_numbers` and `security_keys` are VistA-specific architectural metadata that appear consistently in Technical Manuals and are valuable for cross-package dependency analysis.

### Cycle 4 — Extended Structure

Target fields extracted from document length and revision history:

| Field | Description |
|---|---|
| `page_count` | Equivalent page count |
| `section_count` | Number of top-level sections |
| `table_count` | Number of tables |
| `appendix_count` | Number of appendices |
| `pub_date` | Publication or revision date extracted from document text |
| `revision_count` | Number of revision history entries |
| `revision_newest` | Date of most recent revision in the document |
| `revision_oldest` | Date of earliest revision in the document |

`page_count` is derived from word count using a document-density heuristic calibrated to VA technical documentation (approximately 300–350 words per page for text-heavy documents; adjusted for table-heavy documents).

`pub_date` is extracted from the document text, not the filename or URL. VA documents include explicit publication dates in their title pages and revision histories.

### Cycles 5–7 — Validation and Cross-Reference

These cycles performed quality assurance on the earlier extraction:

**Cycle 5 — Cross-validation against inventory**
- Compared extracted `app_code`, `title`, `patch_id` against inventory values
- Flagged mismatches for review
- Corrected systematic errors introduced by Docling parsing artifacts in specific document types

**Cycle 6 — Date format normalization**
- Normalized `pub_date`, `revision_newest`, `revision_oldest` to ISO-8601 format (`YYYY-MM-DD`)
- Resolved ambiguous date formats (MM/DD/YY vs. DD/MM/YY) using context from patch IDs and known release dates

**Cycle 7 — Namespace and version string normalization**
- Normalized `pkg_ns` values to uppercase, trimmed leading/trailing whitespace
- Normalized `pkg_version` to consistent format (e.g., `7.0` → `7`)
- Retired obsolete fields from earlier extraction attempts: `patch`, `patch_number`, `package_name`, `package_namespace`, `package_version` (replaced by canonical names)

---

## 5. Inventory Sync
[↑ Table of Contents](#table-of-contents)

The inventory sync step merges fields from `vdl_inventory_enriched.csv` into the frontmatter of every matching markdown document. This ensures that inventory-level metadata (section, app_status, VDL URLs, decommission dates) stays synchronized with the CSV.

### Matching Logic

`enrich/inventory_fields.py` builds an index from the inventory CSV:

```python
def build_inventory_index(rows: list[dict]) -> dict[tuple[str, str], dict]:
    """
    Build index keyed by (app_name_abbrev, doc_title).
    Excludes noise rows.
    When DOCX and PDF rows both exist for the same doc, prefers the DOCX row.
    """
```

```python
def fields_for_doc(
    index: dict,
    app_code: str,
    title: str
) -> dict | None:
    """
    Look up inventory fields for a document.
    Returns None if not found (unmatched document).
    """
```

`enrich/sync.py` walks the markdown directory and calls `rebuild_frontmatter` with the inventory fields for each document.

### Skip Condition

Sync skips a document if the `section` field is already present in its frontmatter and `--force` is not set. `section` is used as the sentinel because it is always populated by a successful sync.

---

## 6. Canonical Field Order
[↑ Table of Contents](#table-of-contents)

`CANONICAL_FIELD_ORDER` in `enrich/frontmatter.py` defines the authoritative order of all 34 frontmatter fields, organized into seven groups:

```python
CANONICAL_FIELD_ORDER = [
    # Group 1: Document identity
    "title", "doc_type", "doc_label", "doc_layer", "doc_subject",

    # Group 2: Application identity
    "app_code", "app_name", "section", "app_status",

    # Group 3: Package identity
    "pkg_ns", "pkg_name", "pkg_namespace", "pkg_version",

    # Group 4: Patch identity
    "patch_ver", "patch_id", "patch_num", "group_key",

    # Group 5: Document structure
    "word_count", "page_count", "section_count", "table_count",
    "appendix_count", "figure_count", "has_toc", "is_stub",

    # Group 6: Content metadata
    "audience", "description", "pub_date",
    "revision_count", "revision_newest", "revision_oldest",
    "file_numbers", "security_keys", "menu_options",

    # Group 7: Pipeline metadata
    "doc_format", "doc_filename",
]
```

`RETIRED_FIELDS` lists fields from earlier extraction attempts that have been superseded:

```python
RETIRED_FIELDS = {
    "patch",            # replaced by patch_id
    "patch_number",     # replaced by patch_num
    "package_name",     # replaced by pkg_name
    "package_namespace", # replaced by pkg_namespace
    "package_version",  # replaced by pkg_version
}
```

---

## 7. Coverage and Results
[↑ Table of Contents](#table-of-contents)

After all seven cycles, the corpus metadata coverage:

| Metric | Count | % |
|---|---|---|
| Documents with complete frontmatter | 2,240 | 100% |
| Documents with `word_count` | 2,220 | 99.1% |
| Documents with `page_count` | 1,897 | 84.7% |
| Documents with `pub_date` | 1,943 | 86.7% |
| Documents with `description` | 2,198 | 98.1% |
| Documents flagged `is_stub = true` | 42 | 1.9% |

The 20 documents without `word_count` are stubs whose conversion produced content too minimal to count. The ~300 documents without `page_count` are those where word count alone was insufficient to calibrate the page-count heuristic (primarily short patch documents of 1–3 pages where the heuristic margin of error exceeds the document length).

---

*End of report.*
