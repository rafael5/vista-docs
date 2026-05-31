# VDL Pipeline — Stage 1: Crawl

**Date:** 2026-03-30
**Module:** `vista_docs/crawl/`
**Output:** `~/data/vista-docs/inventory/vdl_inventory.csv`

---

## Table of Contents

1. [Overview](#1-overview)
2. [VDL Site Structure](#2-vdl-site-structure)
3. [Parser Design](#3-parser-design)
4. [Output Schema](#4-output-schema)
5. [Patch Identifier Normalization](#5-patch-identifier-normalization)
6. [Noise Detection](#6-noise-detection)
7. [Known Quirks](#7-known-quirks)

---

## 1. Overview
[↑ Table of Contents](#table-of-contents)

The crawl stage enumerates the complete VA VDL catalog at `va.gov/vdl` and produces a structured CSV containing one row per document listing. It is the first and foundational stage of the pipeline — every downstream stage works from its output.

The crawler operates as a 3-level traversal:

```
Level 1: VDL index page      → enumerate 5 sections
Level 2: VDL section pages   → enumerate all applications per section
Level 3: VDL app pages       → extract document records per application
```

**Output:** `vdl_inventory.csv` — 8,834 rows, 196 applications, 29 base columns.

---

## 2. VDL Site Structure
[↑ Table of Contents](#table-of-contents)

The VDL presents its content as nested HTML tables. Each level has a distinct structure.

### Level 1 — Index Page

`va.gov/vdl` lists five sections with links to each section page:

| Section Code | Section Name |
|---|---|
| CLI | Clinical |
| FIN | Financial-Administrative |
| INF | Infrastructure |
| GUI | VistA/GUI Hybrids (formerly HealtheVet) |
| MON | Monograph |

### Level 2 — Section Pages

Each section page lists applications as table rows. Each row contains:
- Application full name
- Application abbreviation code (in parentheses)
- Application status (Active / Archive / Decommissioned)
- Link to the application page

### Level 3 — Application Pages

Each application page presents a table of documents. Each document row contains:
- Document title (cell text)
- Document type code and label
- One or more download links labeled with the format ("DOCX", "PDF", "DOC")
- Optional companion document link

**Critical quirk:** The link text is the format label, NOT the document title. The document title is in the preceding table cell. Many generic scrapers get this backwards. See [Section 7: Known Quirks](#7-known-quirks) for the detection logic.

---

## 3. Parser Design
[↑ Table of Contents](#table-of-contents)

The crawler is split into a pure parser and an I/O layer:

- **`crawl/parser.py`** — pure functions; accepts HTML strings; returns structured dicts
- **`crawl/crawler.py`** — I/O layer; fetches pages via `requests`; calls parser functions

### Pure Parser (`crawl/parser.py`)

```python
def parse_section_list(html: str) -> list[dict]:
    """Extract section codes and URLs from VDL index page."""

def parse_app_list(html: str, section_code: str) -> list[dict]:
    """Extract application records from a section page."""

def parse_app_page(html: str, app_record: dict) -> list[dict]:
    """Extract document records from an application page."""
```

The parser uses BeautifulSoup4. All BeautifulSoup `tag["href"]` accesses are cast to `str()` to satisfy mypy, which types them as `str | list[str]`.

### Title vs. Format Detection

```python
FORMAT_LABELS = {"DOCX", "PDF", "DOC", "ZIP", "TXT", "WORD"}

for link in row.find_all("a"):
    link_text = link.get_text(strip=True).upper()
    if link_text in FORMAT_LABELS:
        doc_format = link_text.lower()
        doc_url = str(link["href"])
    else:
        doc_title = link.get_text(strip=True)
```

This pattern correctly identifies the format from the link text and the document title from the non-link cell text.

### DOCX + PDF Row Collapsing

The VDL frequently lists both a DOCX and a PDF for the same document on separate rows. The `build_entries_from_rows` function in `manifest/builder.py` collapses these pairs into a single `ManifestEntry` with both `docx_url` and `pdf_url`. DOCX is always preferred for fetch and ingest; PDF is retained as `companion_url`.

---

## 4. Output Schema
[↑ Table of Contents](#table-of-contents)

The crawl produces `vdl_inventory.csv` with one row per document and the following columns:

**Application identity (from level 2):**
- `section_name`, `section_code`
- `app_name_full`, `app_name_abbrev`, `app_status`
- `decommission_date` (if status is Decommissioned)
- `app_url`

**Document metadata (from level 3):**
- `doc_code`, `doc_label`
- `doc_title`, `doc_filename`, `doc_slug`
- `doc_format`
- `doc_subject` (version/subject metadata from VDL)
- `doc_url`, `companion_url`
- `noise_type` (set during crawl if document matches known noise patterns)

**Derived fields (computed during crawl):**
- `pkg_ns` — MUMPS namespace parsed from patch identifier or app metadata
- `patch_ver`, `patch_ver_major`, `patch_ver_minor`, `patch_num`, `patch_id`, `patch_id_full`
- `multi_ns`, `group_key`
- `doc_layer` — heuristic tier assignment (see Section 5 of the Inventory Guide)

---

## 5. Patch Identifier Normalization
[↑ Table of Contents](#table-of-contents)

VistA document titles frequently contain KIDS patch identifiers in `NS*V*P` format (e.g., `DG*5.3*1057`). The crawler extracts and normalizes these into structured fields.

### Extraction Rules

For each document title, the parser applies regex patterns to extract:

1. `patch_id` — the full structured identifier: `DG*5.3*1057`
2. `patch_ver` — the full version string: `5.3`
3. `patch_ver_major` — major version: `5`
4. `patch_ver_minor` — minor version: `3`
5. `patch_num` — patch sequence number: `1057`
6. `pkg_ns` — the namespace prefix: `DG`

Multi-patch titles (e.g., `PSO*7*500 with PSO*7*499`) set the `multi_ns` flag and populate `group_key` with a normalized grouping identifier.

`patch_id_full` preserves the raw patch string before normalization, capturing multi-patch and non-standard formats.

### `doc_layer` Assignment

Assigned deterministically after patch extraction:

| `patch_ver` | `patch_num` | `doc_layer` |
|---|---|---|
| present | absent | `anchor` — canonical version document |
| present or absent | present | `patch` — patch-level supplement |
| absent | absent | `plain` — version-ambiguous |

---

## 6. Noise Detection
[↑ Table of Contents](#table-of-contents)

The crawler detects and flags two categories of boilerplate noise during the crawl:

### `vba_form`

Eight VA benefit and claims forms appear attached to every active application section regardless of relevance. They are identified by matching against a known list of form titles:

- VA Form 24-0296 (Direct Deposit)
- SF 1199A (Direct Deposit Sign-Up)
- VA Form 21-526 (Disability Compensation)
- VA Form 10-5345 (Request for and Authorization to Release Health Information)
- VA Form 10-5345a (Individuals' Request for a Copy of Their Own Health Information)
- VA Form 10-0493 (Patient Notification Letter)
- VA Form 10-0137 (VA Advance Directive)
- VA Form 10-7959c (Other Health Insurance Certification)

These 8 forms × 149 active applications = 1,192 noise rows.

### `va_ref`

The VA Strategic Plan FY 2014–2020 appears attached to many applications. Identified by exact title match. 149 noise rows.

Noise rows are retained in the inventory with `noise_type` set — they are not deleted. Substantive analysis filters on `noise_type = ''`.

---

## 7. Known Quirks
[↑ Table of Contents](#table-of-contents)

### Link Text Is Format, Not Title

The single most important parsing rule. On VDL application pages:
- Link text = format label ("DOCX", "PDF")
- Document title = cell text adjacent to the link

A parser that uses link text as the title will produce 7,493 rows with titles like "DOCX".

### `app_name_abbrev` Is NOT a MUMPS Namespace

The VDL displays a short code in parentheses after the application name: `Admission Discharge Transfer (ADT)`. This `app_name_abbrev` is the **VDL display code**, not the MUMPS namespace prefix.

| VDL app_code | MUMPS namespace |
|---|---|
| ADT | DG |
| CPRS | OR |
| Pharmacy: Outpatient | PSO |

The pipeline uses `app_name_abbrev` throughout (e.g., `--pkg ADT` not `--pkg DG`). The `pkg_ns` column stores the actual MUMPS namespace where known.

### Duplicate Rows for DOCX + PDF

When both a DOCX and PDF exist for the same document, the VDL lists them on separate rows. The inventory CSV preserves both rows (with different `doc_format` values). The `build_entries_from_rows` function in `manifest/builder.py` collapses them before the fetch stage.

### `app_status` Casing

Application status is not consistently capitalized across VDL sections. The crawler normalizes all status values to lowercase: `active`, `archive`, `decommissioned`.

### `SSO/UC` App Code Slash

The application `Single Signon/User Context` has `app_name_abbrev = "SSO/UC"`. This slash causes issues in file paths. The pipeline sanitizes slashes in app codes when constructing directory names: `SSO/UC` → `sso_uc`. The same issue affects `AR/WS`.

---

*End of report.*
