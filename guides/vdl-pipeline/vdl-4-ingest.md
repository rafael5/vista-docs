# VDL Pipeline — Stage 3: Ingest (Pandoc)

**Date:** 2026-03-31
**Replaces:** `vdl-4-ingest-docling.md` (Docling-based pipeline, archived)
**Module:** `vista_docs/ingest/`
**Output:** `~/data/vista-docs/md-img/<app_code>/`

---

## Table of Contents

1. [Overview](#1-overview)
2. [Why Pandoc](#2-why-pandoc)
3. [Architecture](#3-architecture)
4. [Batch Conversion](#4-batch-conversion)
5. [Image Handling](#5-image-handling)
6. [Post-Processing Pipeline](#6-post-processing-pipeline)
7. [YAML Frontmatter Initialization](#7-yaml-frontmatter-initialization)
8. [Known Limitations](#8-known-limitations)
9. [Problems Encountered and Fixed](#9-problems-encountered-and-fixed)
10. [Lessons Learned](#10-lessons-learned)

---

## 1. Overview

[↑ Table of Contents](#table-of-contents)

The ingest stage converts every downloaded DOCX file into structured markdown with embedded image references. The output is a tree of `.md` files — each with YAML frontmatter initialized from the inventory — paired with sibling image directories containing all figures extracted from the source document.

**Input:** `~/data/vista-docs/raw/<app_code>/` (DOCX files fetched from VDL)
**Output:** `~/data/vista-docs/md-img/<app_code>/` (markdown + images)

### Output layout

```
md-img/
  CPRS/
    cprs-technical-manual-gui-version.md
    cprs-technical-manual-gui-version/
      001.png
      002.png
      ...
  PSO/
    outpatient-pharmacy-version-7-user-manual.md
    outpatient-pharmacy-version-7-user-manual/
      001.png
      ...
```

### Results (2026-03-31)

| Metric | Value |
|---|---|
| Documents converted | 2,858 |
| Packages covered | 137 |
| Conversion errors | 51 |
| Images extracted | 59,226 |
| Documents with images | 2,714 |
| Total words | 26,650,008 |

This is a significantly larger corpus than the prior Docling run (2,240 documents, 44 packages), because the fetch stage was expanded and the Pandoc pipeline is more tolerant of structural variation in DOCX files.

---

## 2. Why Pandoc

[↑ Table of Contents](#table-of-contents)

The original ingest stage used **Docling** (IBM Research), an AI-powered document intelligence library. Pandoc replaced it as the primary DOCX converter for the following reasons.

### The decisive issue: numbered lists

VistA technical documentation uses numbered, lettered, and roman-numeral lists extensively — particularly in installation procedures, menu option hierarchies, and security key tables. These lists use Word's `<w:numPr>` numbering mechanism (the native OOXML auto-numbering system).

**Docling** performs layout analysis on the visual rendering of the document. It sees the auto-numbered list rendered as "1.", "2.", "3." but loses the list structure when converting to markdown — producing either plain paragraphs or inconsistently-formatted bullet lists. The list hierarchy and continuation logic are not recovered.

**Pandoc** reads the OOXML XML directly — specifically `<w:numPr>` (per-paragraph numbering properties) and `<w:abstractNum>` (the numbering definition, including format type: decimal, lowerLetter, lowerRoman). It reconstructs the complete list hierarchy faithfully, including mixed nesting (e.g., numbered section containing a lettered sub-list containing a roman-numeral sub-sub-list).

For VistA installation guides and technical manuals, this difference is decisive. A Docling-converted installation guide may have all the text but the procedure steps appear as undifferentiated paragraphs. A Pandoc-converted guide preserves the numbered steps exactly as authored.

### Tool comparison

| Capability | Pandoc 3.1.3 | Docling ≥2.81 |
|---|---|---|
| Auto-numbered lists (decimal/alpha/roman) | ✓ Full fidelity | ✗ Lost |
| Nested list hierarchy | ✓ Preserved | ✗ Flattened |
| Tables | ✓ GFM pipe tables | ✓ Good |
| Headings | ✓ Exact | ✓ Good |
| Image extraction | ✓ `--extract-media` | ✓ |
| EMF/WMF vector images | Requires LibreOffice | ✓ Converts natively |
| DOCX heading styles | ✓ Maps to `#` levels | ✓ |
| Page count metadata | ✗ Not available | ✓ |
| Scanned PDF support | ✗ DOCX only | ✓ With OCR backend |
| Speed (per document) | ~0.5s | 10–300s |
| Memory footprint | Minimal | 2–8 GB peak |

### Speed

Pandoc converts a typical VistA DOCX in under one second. The full corpus of 2,858 documents converted in under 15 minutes sequentially. The Docling pipeline took hours on a smaller corpus (2,240 documents) and required careful management of memory limits to avoid process kills on large files.

### Scope change: DOCX only

The Pandoc pipeline ingests DOCX files only. The VDL fetch stage prefers DOCX when available; PDF-only documents are recorded as fetch errors and not ingested. The prior Docling pipeline accepted both DOCX and PDF. The practical impact is minimal: PDF-only VDL documents are rare and tend to be older scanned documents with little machine-readable content.

---

## 3. Architecture

[↑ Table of Contents](#table-of-contents)

The ingest module follows the project's pure/I/O separation principle.

```
vista_docs/ingest/
  converter.py    — I/O: run Pandoc, extract and rename images
  postprocess.py  — pure: all markdown transforms (no I/O)
  prepare.py      — pure: assemble frontmatter + apply full post-processing pipeline
  runner.py       — I/O: orchestrate one document end-to-end, write output
```

### Data flow

```
raw/<app_code>/doc.docx
        │
        ▼  converter.convert_docx()
   [temp dir]  pandoc → doc.md + raw-images/
        │
        ▼  converter._normalize_images()
   out_img_dir/  001.png  002.png  ...
        │
        ▼  (markdown text returned as string)
        │
        ▼  prepare.build_markdown()
   frontmatter + post-processed body
        │
        ▼  runner writes
   md-img/<app_code>/doc.md
```

### `converter.py` — I/O layer

Runs Pandoc in a temporary directory, normalizes images, returns `(markdown_text: str, n_images: int)`. The temporary directory is cleaned up automatically; on any failure, no partial output is left in `md-img/`.

```python
def convert_docx(source_path: Path, out_img_dir: Path) -> tuple[str, int]:
    with tempfile.TemporaryDirectory() as tmp:
        _run_pandoc(source_path, md_path, raw_img_dir)
        n_images = _normalize_images(md_path, raw_img_dir, out_img_dir)
        text = md_path.read_text(encoding="utf-8")
    return text, n_images
```

### `postprocess.py` — pure layer

All markdown transform functions. Takes a string, returns a string. No file I/O, no Pandoc dependency. Fully unit-testable. Functions are organized by stage:

- Artifact stripping: `strip_artifacts`, `strip_back_links`, `strip_word_toc`
- Content linking: `link_figure_captions`
- Heading normalization: `strip_outline_numbering`, `cap_heading_depth`, `format_callouts`, `strip_boilerplate`
- Whitespace: `normalize_whitespace`
- TOC generation: `gfm_anchor`, `build_toc`, `insert_toc`
- Navigation: `insert_back_links`
- Compaction: `compact_lists`, `compact_reference_sections`

### `prepare.py` — pure layer

Assembles final document: constructs frontmatter from `ManifestEntry`, applies the full post-processing pipeline in order, returns the complete markdown string. No I/O.

### `runner.py` — I/O layer

Orchestrates one document: validates source exists, calls `convert_docx`, calls `build_markdown`, writes output file, returns updated `ManifestEntry` with `ingest_status`, `markdown_path`, `ingest_error`.

---

## 4. Batch Conversion

[↑ Table of Contents](#table-of-contents)

```bash
vista-docs ingest [--pkg ACKQ] [--force]
```

For each entry in `pipeline.db` with `fetch_status = ok`:

1. Skip if `ingest_status = ok` and output file exists (unless `--force`)
2. Determine output paths: `md-img/<app_code>/<output_filename>` and `md-img/<app_code>/<stem>/`
3. Run `convert_docx(src, out_img_dir)` → `(raw_md, n_images)`
4. Run `build_markdown(entry, raw_md)` → `md_content`
5. Write `md_content` to output path
6. Update `ingest_status`, `markdown_path`, `ingest_error` in `pipeline.db`

The `--pkg` flag restricts conversion to a single package namespace. The `--force` flag re-converts already-converted documents (required when switching output directories or updating post-processing rules).

### Idempotency

The ingest stage is idempotent by default: it skips any document whose output file already exists in `md-img/` and whose `ingest_status` is `ok`. Interrupted runs resume from the last unprocessed document.

---

## 5. Image Handling

[↑ Table of Contents](#table-of-contents)

### Extraction

Pandoc's `--extract-media=<dir>` flag writes all images embedded in the DOCX to a scratch directory. Images may be:

- **JPEG / PNG** — embedded raster images, written as-is
- **EMF / WMF** — Windows vector formats embedded by Microsoft Office or Visio diagrams
- **Other** — SVG, BMP, TIFF (rare in VistA documents)

### EMF/WMF conversion

EMF and WMF are Windows-native vector formats that do not render in browsers or markdown viewers. They are converted to PNG via **LibreOffice headless**:

```bash
soffice --headless --convert-to png --outdir <dir> <file.emf>
```

If LibreOffice conversion fails (timeout or process error), the original EMF/WMF file is copied with its original extension as a fallback. These fallback files are not renderable but preserve the source material.

### Naming convention

Images are renamed from Pandoc's internal scratch names (e.g., `media/image1.jpeg`) to a clean sequential scheme. Both markdown image syntax `![alt](src)` and HTML `<img src="...">` (used when Word images have explicit dimensions) are detected and renamed.

```
md-img/
  CPRS/
    cprs-gui-user-manual/
      001.png    ← first image in document order
      002.png
      003.png
      ...
```

The image folder is named identically to the markdown file (without extension). Images are numbered by their position in the document (byte offset in the markdown source), so `001.png` is always the first image the reader encounters.

### Image references in markdown

After renaming, image references in the markdown are updated to relative paths:

```markdown
![Figure 3-1. CPRS Main Screen](cprs-gui-user-manual/001.png)
```

The path is relative to the sibling markdown file, so the documents are self-contained and portable — moving the `<app_code>/` folder preserves all references.

### Documents without images

If a document contains no images, no image directory is created. The `_normalize_images` function cleans up the Pandoc scratch directory and returns `n_images = 0`.

---

## 6. Post-Processing Pipeline

[↑ Table of Contents](#table-of-contents)

Pandoc produces high-fidelity GFM but raw output from VistA DOCX files requires systematic cleaning. All transforms are applied in `prepare.build_markdown()` in this fixed order.

### Mandatory Pandoc flags

```bash
pandoc <input.docx> -f docx -t gfm --wrap=none --standalone \
       --extract-media=<raw-images/> -o <output.md>
```

`--wrap=none` is non-negotiable. Without it, Pandoc wraps long lines at 80 characters, inserting hard line breaks mid-sentence. Every downstream regex pattern — list detection, heading detection, TOC stripping, back-link insertion — would break on wrapped lines. This flag was discovered to be essential during initial testing.

`--standalone` ensures the output is a complete document (not a fragment). Without it, Pandoc omits the YAML metadata block it would normally generate from DOCX properties.

### Stage 1: Artifact stripping

`strip_artifacts(text)` removes HTML comment artifacts left by Word track-changes, field codes, and revision marks:

- HTML comments: `<!-- ... -->` — Word embeds field codes as HTML comments in Pandoc output
- Empty bold/italic markers: `** **`, `* *` — left when bold/italic runs contain only whitespace
- Stray empty blockquotes: `>   ` on an otherwise blank line — left after blockquote TOC headers are removed

`strip_back_links(text)` removes any `<!-- back-to-toc -->` back-link lines from a prior ingest run, making the pipeline idempotent on re-runs with `--force`.

### Stage 2: Figure caption linking

`link_figure_captions(text)` promotes figure captions into image alt text and renders them as italicized lines. VistA documents typically place figure captions as a paragraph immediately after the figure, separated by a blank line:

```markdown
<!-- Before -->
![](cprs-gui/001.png)

Figure 3-1. CPRS Main Screen

<!-- After -->
![Figure 3-1. CPRS Main Screen](cprs-gui/001.png)

*Figure 3-1. CPRS Main Screen*
```

Matched caption prefixes: `Figure`, `Fig.`, `Exhibit`, `Chart`, `Diagram`, `Illustration`, `Plate`, `Table`.

### Stage 3: Word TOC stripping

`strip_word_toc(text)` removes the original Word TOC artifact. Pandoc renders the Word TOC field in one of three forms depending on how the source document was styled.

**Form 1 — Plain bare link lines** (default Word TOC field style):

```markdown
[Introduction [4](#introduction)](#_TOC13979763)
[Chapter 1 [8](#chapter-1)](#_TOC13979764)
```

Detection: a block of 3 or more consecutive lines where each line matches `^\[.+\]\(#[^)]+\)\s*$`. The minimum of 3 prevents false positives on occasional bare links in document body. Also strips any preceding `> Table of Contents` blockquote header.

**Form 2 — Bullet list under a heading** (TOC styled as a body section):

```markdown
## Table of Contents

- [Introduction](#introduction)
  - [Background](#background)
```

Detection: `## Table of Contents` (case-insensitive) followed by list content up to the next same-level heading. The entire section is removed.

**Form 3 — Heading-level link lines** (TOC entries styled as Heading 1):

```markdown
# Table Of Contents
# [Preface [ii](#preface)](#preface)
# [Chapter 1 [2](#chapter-1)](#chapter-1)
```

Detection: A `# Table Of Contents` heading followed by lines matching `^#{1,6}\s+\[.+\]\(#[^)]+\)\s*$`. Rare but observed in ACKQ documents.

### Stage 4: Heading normalization

Three transforms applied in sequence:

**`strip_outline_numbering`** — removes auto-outline prefixes from headings. Some DOCX documents use heading styles that include the outline number as text:

```
# 1.2.3 Installation Prerequisites  →  # Installation Prerequisites
```

**`cap_heading_depth`** — limits headings to H4. H5 and H6 are rare in VistA documents and often arise from Word's minor heading styles mapping to deep levels. Capping at H4 keeps the document navigable.

**`format_callouts`** — converts `NOTE:`, `WARNING:`, `CAUTION:`, `IMPORTANT:`, `REMINDER:` paragraphs into blockquotes:

```
NOTE: This requires Kernel patch XU*8*680.
→ > **NOTE:** This requires Kernel patch XU*8*680.
```

**`strip_boilerplate`** — removes recurring VA title-page lines: "Department of Veterans Affairs", "Veterans Health Administration", "Office of Information", "Washington, DC", "Version X.X", "Revised Month YYYY", "This page intentionally left blank".

### Stage 5: Whitespace normalization

`normalize_whitespace(text)` collapses 3 or more consecutive blank lines to 2 and ensures a single trailing newline. Keeps the document compact without collapsing intentional paragraph breaks.

### Stage 6: TOC generation

After body cleanup, a linkable Table of Contents is generated from the document's headings and inserted after the H1 title (or after the frontmatter block if there is no H1).

**GFM anchor generation** (`gfm_anchor`) follows GitHub Flavored Markdown rules exactly:

1. Decode HTML entities (`&amp;` → `&`)
2. Strip inline markdown (links, `code`, **bold**, _italic_)
3. Lowercase
4. Remove all characters except alphanumeric, spaces, hyphens
5. Replace spaces with hyphens, collapse consecutive hyphens
6. Deduplicate: second occurrence of an anchor gets `-1` suffix, third gets `-2`, etc.

This matches GitHub's rendering so anchor links work correctly when documents are published to GitHub Pages or viewed on github.com.

**TOC depth:** headings up to H3 only. H4+ headings are omitted from the TOC to keep it readable in documents with 100+ sections.

**Insertion point:** immediately after the H1 heading line (absorbing any blank lines), before the body. If no H1 exists, the TOC is inserted after the YAML frontmatter block.

```markdown
# CPRS Installation Guide

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
  - [Hardware Requirements](#hardware-requirements)
  - [Software Requirements](#software-requirements)
- [Installation](#installation)
  ...

## Introduction
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
```

### Stage 7: Back-to-TOC navigation links

`insert_back_links(text)` inserts a `[↑ Table of Contents](#table-of-contents)` link after every H1, H2, and H3 heading in the document body, except the generated TOC heading itself.

The link is prefixed with `<!-- back-to-toc -->` so it can be stripped and re-inserted idempotently on `--force` re-runs.

### Stage 8: List compaction

`compact_lists(text)` removes blank lines between list items, making all lists tight (single-spaced). Applies to bulleted (`-`, `*`, `+`), numbered (`1.`, `2)`), lettered (`a.`, `B)`), and roman numeral (`i.`, `iv.`) lists at any nesting depth.

**Detection regex:**

```python
_LIST_ITEM_RE = re.compile(
    r'^\s*(?:'
    r'[-*+]'                                              # bullet
    r'|\d+[.)]'                                          # numbered
    r'|[A-Za-z][.)](?!\S)'                               # lettered (negative lookahead prevents abbreviations)
    r'|(?:i{1,3}|iv|vi{0,3}|viii|ix|x{1,3}|xl|l)[.)]'  # roman numeral
    r')\s'
)
```

**Boundary rule:** a blank line is removed only when both the preceding and following non-blank lines are list items or list continuations. This prevents merging a list into an adjacent paragraph.

Fenced code blocks are never compacted — blank lines inside ```` ``` ```` blocks are always preserved.

### Stage 9: Reference section compaction

`compact_reference_sections(text)` applies single-spacing within reference sections that are inherently list-of-entries content: Index, Table of Contents, Glossary, List of Tables/Figures/Illustrations/Abbreviations/Exhibits/Plates, Abbreviations, Acronyms, Bibliography, References, List of Effective Pages, List of Changes.

Within these sections, blank lines between plain content lines are removed. Blank lines around back-to-TOC markers and sub-headings are preserved. This produces a compact, readable reference section without losing structure.

---

## 7. YAML Frontmatter Initialization

[↑ Table of Contents](#table-of-contents)

Each markdown file is initialized during ingest with a minimal YAML frontmatter block sourced from the `ManifestEntry` (which is itself built from the inventory CSV and pipeline state):

```yaml
---
title: CPRS Installation Guide
doc_type: installation-guide
app_code: CPRS
docx_url: "https://www.va.gov/vdl/documents/..."
pdf_url: "https://www.va.gov/vdl/documents/..."
---
```

The `patch` field is added if present. `docx_url` and `pdf_url` are optional; `pdf_url` is omitted if only a DOCX was fetched.

### Titles with colons

YAML treats unquoted colons as key-value separators. Document titles like `ADT Version 5.3: PIMS Technical Manual` would produce malformed YAML if written unquoted. The `_quote()` helper in `make_frontmatter` double-quotes any value containing a colon.

### Downstream enrichment

The minimal ingest frontmatter is a seed. Two subsequent pipeline stages complete the frontmatter:

1. **`vista-docs enrich`** — extracts 22 fields from document content: `pub_date`, `word_count`, `page_count`, `is_stub`, `has_toc`, `revision_count`, `revision_oldest`, `revision_newest`, `appendix_count`, `table_count`, `section_count`, `figure_count`, `patch_number`, `description`, `file_numbers`, `security_keys`, `menu_options`, `keywords`, `package_name`, `package_namespace`, `package_version`, `audience`

2. **`vista-docs sync`** — applies canonical field order, retires temporary enrich fields (`patch_number`, `package_name`, `package_namespace`, `package_version`), and merges authoritative inventory fields: `doc_label`, `doc_layer`, `doc_subject`, `app_name`, `section`, `app_status`, `pkg_ns`, `patch_ver`, `patch_id`, `group_key`, `app_url`

After both stages, a complete frontmatter record looks like:

```yaml
---
title: CPRS Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: plain
doc_subject:
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns:
patch_ver:
patch_id:
group_key:
file_numbers: []
security_keys: []
menu_options: 0
description:
audience:
keywords:
  - order
  - cprs
  - installation
  - contents
page_count: 0
word_count: 20156
section_count: 32
table_count: 21
figure_count: 0
appendix_count: 2
has_toc: false
is_stub: false
pub_date: April 2007
revision_count: 17
revision_newest: 4/30/07
revision_oldest: 10/14/98
docx_url: "https://www.va.gov/vdl/documents/Clinical/..."
pdf_url: "https://www.va.gov/vdl/documents/Clinical/..."
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---
```

---

## 8. Known Limitations

[↑ Table of Contents](#table-of-contents)

### Page count always zero

The `extract_page_count` extractor estimates page count from tab-separated page numbers in the original Word TOC (e.g., `Introduction\t4`). The Pandoc pipeline strips the Word TOC and replaces it with a GFM anchor-based TOC. The original page numbers are discarded.

**Result:** `page_count: 0` for all Pandoc-converted documents.

**Impact:** The page count field is available in `vdl_inventory_enriched.csv` (sourced from VDL metadata) and can be synced into frontmatter via the inventory sync stage. The extractor-based approach was a workaround for the old pipeline that is now unnecessary.

**Resolution:** Sync `page_count` from the inventory CSV during the sync stage rather than extracting it from document content.

### PDF documents not supported

Pandoc converts DOCX only. PDF-only documents (those without a DOCX equivalent on VDL) are not ingested. They are recorded in the manifest with `ingest_status = skipped`.

### EMF/WMF fallback images

When LibreOffice fails to convert an EMF or WMF vector image (timeout, missing font, unsupported drawing primitives), the original vector file is copied with its original extension. These files appear in the image directory but do not render in browsers or markdown viewers. This affects a small fraction of documents, primarily those with Visio diagrams.

### Word tables with HTML attributes

Some DOCX documents use advanced table formatting (merged cells, column widths, row spans). Pandoc renders these as HTML `<table>` blocks rather than GFM pipe-table syntax when the table structure cannot be expressed in GFM. These HTML tables render in GitHub and most markdown viewers but may not parse cleanly in all markdown processors.

---

## 9. Problems Encountered and Fixed

[↑ Table of Contents](#table-of-contents)

### Problem 1: `--wrap=none` is mandatory

**Symptom:** Initial test run without `--wrap=none` produced markdown where long lines were broken at column 80. List detection, heading detection, TOC stripping, and all other line-oriented regex patterns failed silently — they matched the first fragment of a line but not the continuation.

**Root cause:** Pandoc's default wrapping mode inserts hard line breaks at 80 characters for readability in plain-text terminals. This is the right default for human-readable text but destructive for programmatic processing.

**Fix:** `--wrap=none` added to all Pandoc invocations. This is now documented as a hard requirement. The flag is set in `_run_pandoc()` and cannot be overridden by callers.

### Problem 2: Word TOC not stripped (Form 1 — plain link lines)

**Symptom:** After conversion, documents contained lines like `[Title [4](#intro)](#_TOC13979763)` at the top — not inside any list or heading structure. The TOC stripper was looking for bullet list syntax (`- [Title]`) and did not match these bare link lines.

**Root cause:** When a Word document uses the default TOC field style, Pandoc renders each TOC entry as a plain line containing a markdown link with an embedded page-number sub-link. Three different styles produce three different output forms.

**Fix:** Added Form 1 detection: a block of 3 or more consecutive lines matching `^\[.+\]\(#[^)]+\)\s*$` is recognized as a TOC block and removed. Minimum of 3 prevents false positives on isolated bare links in document body.

### Problem 3: Word TOC not stripped (Form 3 — heading-level links)

**Symptom:** ACKQ documents had heading lines like `# [Preface [ii](#preface)](#preface)` appearing in the generated TOC, creating doubled entries.

**Root cause:** Some ACKQ documents style their TOC entries using the Heading 1 paragraph style rather than the built-in TOC style. Pandoc converts these to `#` headings whose entire text is a markdown link. The Form 1 and Form 2 detectors did not match this pattern.

**Fix:** Added Form 3 detection: a `# Table Of Contents` heading followed by heading lines matching `^#{1,6}\s+\[.+\]\(#[^)]+\)\s*$`. The entire block (title heading + all following heading-link lines) is stripped.

### Problem 4: HTML `<img>` tags not renamed

**Symptom:** After image normalization, some documents still contained `<img src="raw-images/media/image3.png" style="width:2.8in;height:1.2in">` tags. The raw-images scratch directory was not being cleaned up for these documents.

**Root cause:** When a Word image has explicit width/height dimensions set, Pandoc emits it as an HTML `<img>` tag rather than markdown `![alt](src)` syntax. The image normalization code was only scanning for markdown image syntax.

**Fix:** Added `html_img_re` pattern to detect `<img src="...">` tags. Both patterns are collected, sorted by byte offset in the document (to guarantee sequential numbering matches document order), and processed together.

### Problem 5: Stray empty blockquote after Form 1 TOC strip

**Symptom:** After stripping the Form 1 bare-link TOC block, an empty `>   ` line remained in the document. This rendered as an empty blockquote in GitHub markdown.

**Root cause:** Form 1 TOCs are sometimes preceded by a `> Table of Contents` blockquote header line. The header line was detected and removed, but any following empty `>` continuation lines were not.

**Fix:** Added `re.sub(r'^>\s*$', '', text, flags=re.MULTILINE)` to `strip_artifacts()`, which removes all stray empty blockquote lines regardless of their cause.

### Problem 6: Lettered list items matching abbreviations

**Symptom:** Lines like `e.g., this is an example` were incorrectly detected as lettered list items (matching `e.` pattern). This caused blank lines before such lines to be suppressed by `compact_lists`.

**Root cause:** The initial lettered list pattern `[A-Za-z][.)]` matched single-letter abbreviations followed by a period.

**Fix:** Added a negative lookahead: `[A-Za-z][.)](?!\S)`. The lookahead requires that the character after `.` or `)` is whitespace (or end of line), not a non-whitespace character. `e.g.` fails because `g` immediately follows the first `.`; `a. First item` passes because a space follows `.`.

---

## 10. Lessons Learned

[↑ Table of Contents](#table-of-contents)

**Read the OOXML, not the render.** Docling analyzes the visual layout of a Word document. Pandoc reads the XML structure. For structured content like numbered lists, the XML is authoritative — the visual rendering is a lossy projection of the underlying structure. The right tool for structured DOCX conversion reads OOXML.

**Line-based regex requires `--wrap=none`.** Any pipeline that processes Pandoc GFM output with line-oriented patterns must disable line wrapping. Without it, every multi-word heading, every long list item, every URL is broken across lines. Discovering this late costs debugging time across every downstream function. It should be the first flag set, not the last bug fixed.

**Three TOC forms is not obvious — it must be discovered empirically.** The Word TOC field can render in at least three structurally different forms in Pandoc GFM output, depending on the paragraph style applied to TOC entries in the source document. No single detection pattern handles all three. Testing on a representative sample of the actual corpus (not just one or two documents) is essential.

**Collect HTML `<img>` and markdown `![]()` together, sort by byte offset.** Image normalization must handle both image syntaxes. The sort by byte offset guarantees that `001.png` is always the first image the reader encounters in the document — not the first image in the markdown syntax, which may differ from document order when HTML and markdown images are interleaved.

**Temp directory for Pandoc output.** Running Pandoc into a temporary directory means that on any conversion failure, no partial output is left in the final output directory. The caller gets a `RuntimeError` and the output tree remains clean. Simpler than rollback logic.

**Sequential conversion is fast enough.** Pandoc converts a VistA DOCX in under one second. The full 2,858-document corpus converted in under 15 minutes, sequentially, on a development machine. There is no need to parallelize. Parallelism adds complexity; sequential conversion with idempotent state tracking is simpler and reliable.

**The sync stage owns canonical frontmatter.** Ingest should write minimal frontmatter. Enrich should add extracted fields. Sync should apply canonical ordering and add authoritative inventory fields. These are three distinct concerns and should remain in three distinct stages. Trying to frontload more fields into ingest couples the converter to the inventory schema and makes both harder to change.

---

*End of report.*
