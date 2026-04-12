# DOCX to Markdown Pipeline — Implementation Guide

**Date:** 2026-03-30
**Script:** `~/data/vista-docs/docx-to-md/docx2md-pandoc.py`
**Specification:** `~/data/vista-docs/guides/docx-to-markdown-guide.md`
**Test directory:** `~/data/vista-docs/docx-to-md/`

---

## Table of Contents

1. [Overview](#1-overview)
2. [Environment and Dependencies](#2-environment-and-dependencies)
3. [Output Conventions](#3-output-conventions)
4. [Pipeline Architecture](#4-pipeline-architecture)
5. [Layer 1 — Pandoc Conversion](#5-layer-1--pandoc-conversion)
6. [Layer 2 — Image Normalization](#6-layer-2--image-normalization)
7. [Layer 3 — Post-Processing](#7-layer-3--post-processing)
8. [Layer 4 — TOC and Navigation](#8-layer-4--toc-and-navigation)
9. [Python Library Reference](#9-python-library-reference)
10. [Regex and Pattern Reference](#10-regex-and-pattern-reference)
11. [Rules and Axioms](#11-rules-and-axioms)
12. [Test Files and Results](#12-test-files-and-results)
13. [Deviations from Specification](#13-deviations-from-specification)
14. [Known Limitations](#14-known-limitations)

---

## 1. Overview

The pipeline converts `.docx` files to GitHub Flavored Markdown with full structural fidelity. It is implemented as a single self-contained Python script (`docx2md-pandoc.py`) with no external Python dependencies beyond the standard library. All heavy lifting is delegated to system tools (Pandoc, LibreOffice).

### What the pipeline produces

For each input `docname.docx`:

```
output/
├── docname-pandoc.md          # Converted markdown
└── docname-images/
    ├── docname-001.png        # Figures in document order
    ├── docname-002.png
    └── ...
```

### Structural elements preserved

| Element | Status | Method |
|---|---|---|
| Chapter headings (H1) | ✓ | Pandoc Word style → `#` |
| Section headings (H2–H6) | ✓ | Pandoc Word style → `##`–`######` |
| Auto-numbered lists (1, 2, 3) | ✓ | Pandoc reads `<w:numPr>` + `<w:abstractNum>` |
| Lettered lists (a, b, c) | ✓ | Same OOXML numbering definitions |
| Roman numeral lists | ✓ | Same OOXML numbering definitions |
| Bulleted lists (nested) | ✓ | Pandoc; blank lines between items removed |
| Tables | ✓ | GFM pipe tables (simple) or HTML tables (complex) |
| Figures / inline images | ✓ | Extracted as `docname-NNN.png`, linked |
| Figure captions | ✓ | Detected by prefix pattern, attached as alt text |
| Bold / italic | ✓ | `**bold**` `*italic*` |
| Footnotes | ✓ | Pandoc inline footnote syntax `[^n]` |
| Code blocks | ✓ | Fenced ` ``` ` blocks |
| Appendices | ✓ | Preserved as H1 headings |
| Linkable TOC | ✓ | Generated fresh from heading structure |
| Back-to-TOC links | ✓ | Inserted under every H1/H2/H3 |
| YAML frontmatter | ✓ | `--standalone` flag in Pandoc |
| Index / Glossary spacing | ✓ | Single-spaced by `compact_reference_sections()` |
| All list spacing | ✓ | Single-spaced by `compact_lists()` |

---

## 2. Environment and Dependencies

### System requirements

| Component | Version | Install |
|---|---|---|
| Python | 3.12.3 | system (`/usr/bin/python3`) |
| Pandoc | 3.1.3 | `sudo apt install pandoc` |
| LibreOffice headless | system | `sudo apt install libreoffice-headless` |

### Python standard library modules used

| Module | Purpose |
|---|---|
| `argparse` | CLI argument parsing (`inputs`, `--out-dir`) |
| `html` | Decode HTML entities in heading text for GFM anchor generation |
| `re` | All pattern matching: headings, lists, images, TOC detection, anchors |
| `shutil` | Copy image files, remove scratch directories (`rmtree`) |
| `subprocess` | Invoke Pandoc and LibreOffice as child processes |
| `sys` | Exit codes, stderr output |
| `pathlib.Path` | All filesystem operations |

**No third-party Python packages are required.** The script runs with the system Python 3.12 installation, no virtual environment needed.

### Verify installation

```bash
python3 --version        # Python 3.12.3
pandoc --version         # pandoc 3.1.3
soffice --version        # LibreOffice (any recent version)
```

---

## 3. Output Conventions

### File naming

| Input | Markdown output | Image directory |
|---|---|---|
| `some-doc.docx` | `some-doc-pandoc.md` | `some-doc-images/` |
| `CPRS User Manual.docx` | `CPRS User Manual-pandoc.md` | `CPRS User Manual-images/` |

The `-pandoc` suffix distinguishes Pandoc output from Docling output (`-docling.md`) when both converters are run on the same file for comparison.

### Image naming

Images are named `{doc_slug}-{NNN}.png` where:
- `doc_slug` = `docx_path.stem.lower().replace(" ", "-")`
- `NNN` = zero-padded 3-digit sequence number (001, 002, ...) in document order

Example: `cprsguium_ro-001.png`, `cprsguium_ro-032.png`

### Scratch directory

Pandoc extracts images to a temporary `{stem}-raw-images/` directory. This is cleaned up automatically at the end of Layer 2. If the script crashes mid-run, this directory may need manual cleanup.

---

## 4. Pipeline Architecture

The pipeline executes four sequential layers per document:

```
Input: document.docx
       │
       ▼
┌─────────────────────────────────────────────┐
│  Layer 1 — run_pandoc()                     │
│  Pandoc: DOCX → raw GFM + raw image files  │
│  Output: stem-pandoc.md (raw)               │
│          stem-raw-images/image1.png ...     │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│  Layer 2 — normalize_images()               │
│  Rename → docname-NNN.png                   │
│  Convert EMF/WMF → PNG via LibreOffice      │
│  Update img refs in markdown                │
│  Delete stem-raw-images/ scratch dir        │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│  Layer 3 — post-processing (text transforms)│
│  strip_artifacts()                          │
│  strip_back_links()   ← idempotent reset    │
│  link_figure_captions()                     │
│  strip_word_toc()                           │
│  normalize_whitespace()                     │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│  Layer 4 — structure insertion              │
│  insert_toc()                               │
│  insert_back_links()                        │
│  compact_lists()                            │
│  compact_reference_sections()               │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
Output: docname-pandoc.md (final)
        docname-images/docname-NNN.png
```

### Execution order rationale

- Layer 3 strips TOC artifacts **before** Layer 4 inserts the regenerated TOC — inserting before stripping would create a loop.
- `strip_back_links()` runs before `insert_back_links()` — makes the pipeline idempotent on re-runs.
- `compact_lists()` runs after `insert_back_links()` — the back-link line must be in place before list spacing is evaluated so the compactor can correctly identify non-list special lines.
- `compact_reference_sections()` runs last — it operates on already-compacted list content within reference sections.

---

## 5. Layer 1 — Pandoc Conversion

### Function: `run_pandoc(docx_path, md_path, raw_img_dir)`

Invokes Pandoc as a subprocess. The raw markdown is written to `md_path`; extracted images go to `raw_img_dir`.

### Pandoc command

```python
subprocess.run([
    "pandoc", str(docx_path),
    "-f", "docx",
    "-t", "gfm",
    "--wrap=none",
    "--standalone",
    f"--extract-media={raw_img_dir}",
    "-o", str(md_path),
])
```

### Flag reference

| Flag | Value | Effect |
|---|---|---|
| `-f` | `docx` | Explicit input format — OOXML parser |
| `-t` | `gfm` | GitHub Flavored Markdown output: pipe tables, fenced code |
| `--wrap` | `none` | No hard line wraps — paragraphs stay on one line |
| `--standalone` | — | Emit YAML frontmatter with title, author, date from document properties |
| `--extract-media` | `{raw_img_dir}` | Extract all embedded images to this directory |
| `-o` | `{md_path}` | Output file path |

### Why `--wrap=none` is mandatory

Without it, Pandoc inserts hard line breaks at 80 characters inside paragraphs. These breaks corrupt every downstream regex that matches heading text, caption text, or list items — all of which assume a heading or item occupies one line. This flag is non-negotiable.

### Why `--standalone`

Produces YAML frontmatter from Word document properties:

```yaml
---
title: "CPRS Read-Only User Guide"
author: "Department of Veterans Affairs"
date: "December 2023"
---
```

Without `--standalone`, this metadata is lost. The frontmatter is preserved through all downstream steps.

### What Pandoc preserves from DOCX

| Word feature | OOXML element | Markdown output |
|---|---|---|
| `Heading 1` style | `<w:pStyle w:val="Heading1">` | `# text` |
| `Heading 2`–`6` | `<w:pStyle w:val="Heading2">` etc. | `## text` – `###### text` |
| Auto-numbered list | `<w:numPr>` + `<w:abstractNum>` | `1.` `2.` etc. reconstructed |
| Bulleted list | `<w:numPr>` (bullet type) | `- item` |
| Bold | `<w:b/>` | `**text**` |
| Italic | `<w:i/>` | `*text*` |
| Table | `<w:tbl>` | GFM pipe table or HTML `<table>` |
| Embedded image | `word/media/imageN.*` | `![alt](path)` or `<img src="...">` |
| Footnote | `<w:footnote>` | `[^1]: text` |
| Code/preformatted | `<w:rFonts>` Courier/monospace | ` ``` ` fenced block |

### What Pandoc does NOT preserve

- Auto-numbered section prefixes (1., 1.1, 1.1.1) when numbers are generated by `<w:abstractNum>` list definitions — the numbers are computed at render time and not stored as text in OOXML
- Manual formatting used as headings (bold + large font without Heading style)
- Merged table cells (GFM pipe tables have no cell span syntax)

### Error handling

- Non-zero Pandoc exit code raises `RuntimeError` — document is skipped with an error message
- Pandoc warnings are printed to stdout but do not abort conversion

---

## 6. Layer 2 — Image Normalization

### Function: `normalize_images(md_path, raw_img_dir, out_img_dir, doc_slug)`

Finds all image references in the raw markdown (both markdown and HTML syntax), extracts the source files, renames them to the `doc_slug-NNN.png` convention, converts vector formats to PNG, updates the markdown references, and deletes the scratch directory.

### Two image reference syntaxes

Pandoc outputs images in one of two forms depending on whether the source image in Word has explicit dimensions set:

**Form A — Standard markdown** (image with no explicit size):
```markdown
![alt text](raw_images/media/image1.png)
```

**Form B — HTML img tag** (image with explicit width/height in Word):
```html
<img src="raw_images/media/image1.png" style="width:2.8in;height:1.5in" alt="VistA logo" />
```

Both forms are detected and normalized to markdown `![alt](docname-images/docname-NNN.png)`.

### Regex patterns

```python
# Form A — markdown image
md_img_re = re.compile(r'(!\[[^\]]*\])\(([^)]+)\)')

# Form B — HTML img tag (handles both self-closing and non-self-closing)
html_img_re = re.compile(
    r'<img\s[^>]*\bsrc="([^"]+)"[^>]*(?:alt="([^"]*)")?[^>]*/?>',
    re.IGNORECASE | re.DOTALL,
)
```

### Processing order

Image references are collected from both patterns, sorted by their byte position in the document (ascending), and processed in document order. This guarantees that `docname-001.png` is the first image in the document, `docname-002.png` is the second, etc. regardless of which syntax form was used.

### EMF/WMF conversion

Windows vector image formats (`.emf`, `.wmf`) are extracted by Pandoc but cannot be displayed in web browsers or most markdown renderers. They are converted to PNG via LibreOffice headless:

```python
EMF_FORMATS = {".emf", ".wmf"}

subprocess.run([
    "soffice", "--headless",
    "--convert-to", "png",
    "--outdir", str(tmp_dir),
    str(emf_path),
], timeout=30)
```

Conversion uses a temporary subdirectory (`_lo_tmp/`) that is always cleaned up via `finally`. If LibreOffice conversion fails or times out (30s limit), the original file is copied with its original extension rather than silently dropping the image.

### Fallback behavior

If a referenced image file cannot be found (source path does not resolve), the reference is left unchanged in the markdown and the sequence counter is still incremented. This prevents sequence number collisions on partial failures.

---

## 7. Layer 3 — Post-Processing

Layer 3 applies five text transforms in sequence to the raw Pandoc output. All transforms operate on the full document text string.

---

### 7.1 `strip_artifacts(text)`

Removes Word conversion noise that Pandoc cannot suppress.

| Pattern | What it removes |
|---|---|
| `<!--.*?-->` (DOTALL) | HTML comments from Word track-changes, hidden XML fields |
| `\*\*\s*\*\*` | Empty bold markers `****` |
| `\*\s*\*` | Empty italic markers `**` |
| `^>\s*$` (MULTILINE) | Stray empty blockquote lines left by TOC blockquote stripping |

---

### 7.2 `strip_back_links(text)`

Removes any back-to-TOC links from a previous pipeline run. This makes the pipeline idempotent — running the script twice on the same file produces the same output.

**Rule:** Every back-to-TOC line begins with `<!-- back-to-toc -->`. Stripping is a simple line filter.

```python
BACK_MARKER = "<!-- back-to-toc -->"
lines = [l for l in text.splitlines() if not l.startswith(BACK_MARKER)]
```

---

### 7.3 `link_figure_captions(text)`

Converts the Pandoc output pattern of `image_line + blank_line + caption_paragraph` into a linked image with the caption as alt text and an italic caption paragraph below.

**Input:**
```markdown
![](docname-images/docname-001.png)

Figure 3-1. System Architecture Overview
```

**Output:**
```markdown
![Figure 3-1. System Architecture Overview](docname-images/docname-001.png)

*Figure 3-1. System Architecture Overview*
```

**Pattern:**
```python
CAPTION_PATTERN = re.compile(
    r'(!\[[^\]]*\]\([^)]+\))\n\n'
    r'((?:Figure|Fig\.?|Exhibit|Chart|Diagram|Illustration|Plate|Table)\s+'
    r'[\d\w.\-]+\.?\s+[^\n]+)',
    re.IGNORECASE,
)
```

**Caption prefix keywords:** `Figure`, `Fig.`, `Exhibit`, `Chart`, `Diagram`, `Illustration`, `Plate`, `Table`

**Rule:** A caption is detected only if it immediately follows an image line with exactly one blank line between them, and begins with one of the recognized caption prefixes followed by a reference number/label.

---

### 7.4 `strip_word_toc(text)`

Removes the Word TOC artifact. This is the most complex function in the pipeline because Word TOC fields render in three structurally different forms depending on how the source document was authored.

#### Form 1 — Plain bare link lines

Word TOC fields render as bare hyperlink lines in Pandoc GFM output. Each line is a standalone link with optional page number embedded:

```
[Introduction [4](#introduction)](#_TOC13979763)
[What is CPRS Read-Only ? [4](#cprs)](#cprs)
```

These are preceded by an optional `> Table of Contents` blockquote.

**Detection:** A bare link line matches `^\[.+\]\(#[^)]+\)\s*$`. A block of 3 or more such lines (with blank lines allowed between them) is treated as the TOC field artifact and removed.

**Threshold:** 3+ link lines required. A single `[see also](#anchor)` line in body text should not be stripped.

#### Form 2 — Bullet list under `## Table of Contents`

Some documents embed a bookmarked TOC section in the body styled as a Word list:

```markdown
## Table of Contents
- [Introduction](#introduction)
  - [Section One](#section-one)
```

**Detection:** A heading matching `^#{1,3}\s+Table of Contents\s*$` (case-insensitive). Everything from the heading up to (but not including) the next heading of equal or higher level is removed.

#### Form 3 — Heading-level TOC entries

Some VA documents use `Heading 1` style for each TOC entry. Pandoc converts these to `#` headings whose entire text is a markdown link:

```markdown
# Table Of Contents
# [Preface [ii](#preface)](#preface)
# [Introduction [2](#_Toc119128687)](#_Toc119128687)
```

**Detection:** A heading where the entire text after `# ` matches `\[.+\]\(#[^)]+\)`. The `# Table Of Contents` title heading is detected first; if followed by heading-link entries, the entire block is removed.

**Stray entries:** Any isolated heading-link line not under a TOC title is also removed individually.

---

### 7.5 `normalize_whitespace(text)`

```python
text = re.sub(r'\n{3,}', '\n\n', text)
return text.strip() + "\n"
```

**Rules:**
- Three or more consecutive blank lines collapsed to two
- Leading/trailing whitespace stripped from the entire document
- Exactly one trailing newline

---

## 8. Layer 4 — TOC and Navigation

---

### 8.1 `insert_toc(text)` — via `build_toc()` and `gfm_anchor()`

Generates a fresh linkable Table of Contents from the document's heading structure and inserts it after the first H1.

#### GFM anchor generation — `gfm_anchor(text, seen)`

Implements the GitHub Flavored Markdown anchor algorithm exactly, with deduplication:

```
1. Decode HTML entities:        &amp; → &,  &gt; → >
2. Strip inline links:          [text](url) → text
3. Strip emphasis markers:      ` * _ ~  → (removed)
4. Lowercase
5. Remove non-word characters:  keep [a-z0-9_\s-]
6. Replace whitespace with -
7. Collapse multiple hyphens
8. Strip leading/trailing hyphens
9. Deduplicate: 1st occurrence → base, 2nd → base-1, 3rd → base-2, ...
```

Deduplication tracks a `seen: dict[str, int]` counter per document. The `gfm_anchor` function is called with the same `seen` dict for every heading in the document so duplicates are handled correctly across the full heading set.

#### TOC structure

```markdown
## Table of Contents

- [Chapter One](#chapter-one)
  - [Section 1.1](#section-11)
    - [Subsection 1.1.1](#subsection-111)
- [Chapter Two](#chapter-two)
```

- Heading levels H1–H3 are included (`max_depth=3`)
- H4–H6 are omitted (produces unreadably deep TOCs in dense technical documents)
- Indentation: 2 spaces per level (`"  " * (level - 1)`)

#### Insertion point

The TOC is inserted after the first H1 heading (the document title). Any blank lines between the H1 and the next content are consumed before insertion. If no H1 exists, the TOC is inserted after the YAML frontmatter block.

YAML frontmatter detection: document begins with `---`, ends at the next `---` line.

---

### 8.2 `insert_back_links(text)`

Inserts a back-to-TOC navigation link immediately after every H1, H2, and H3 heading in the document body.

**Back link format:**
```markdown
## Chapter Title

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

```

**Rules:**
- Applied to `#{1,3}` headings only (H1, H2, H3) — H4–H6 are too granular
- The `## Table of Contents` heading itself is excluded
- Empty headings (heading marker with no text) are excluded
- Blank lines immediately following the heading are absorbed before inserting the link — keeps heading + link visually adjacent in the source
- The `<!-- back-to-toc -->` prefix marker enables idempotent removal by `strip_back_links()`
- One blank line is appended after the link for visual separation from the following paragraph

---

### 8.3 `compact_lists(text)`

Removes blank lines between list items to produce tight (single-spaced) lists.

#### List item detection — `_LIST_ITEM_RE`

```python
_LIST_ITEM_RE = re.compile(
    r'^\s*(?:'
    r'[-*+]'                                              # bullet: - * +
    r'|\d+[.)]'                                          # numbered: 1. 2) etc.
    r'|[A-Za-z][.)](?!\S)'                               # lettered: a. B) — negative lookahead prevents matching abbreviations
    r'|(?:i{1,3}|iv|vi{0,3}|viii|ix|x{1,3}|xl|l)[.)]'  # roman numerals
    r')\s'
)
```

**Lettered list disambiguation:** The pattern `[A-Za-z][.)](?!\S)` uses a negative lookahead `(?!\S)` to avoid matching single-letter abbreviations like `e.g.` or `i.e.` that appear at the start of a sentence. The character after the period/paren must be whitespace or end-of-string.

**Roman numeral coverage:** `i`, `ii`, `iii`, `iv`, `v`, `vi`, `vii`, `viii`, `ix`, `x`, `xi`–`xiii`, `xl`, `l`.

#### Continuation line detection — `_is_list_continuation(line)`

An indented non-blank line (`^\s{2,}\S`) is treated as the continuation of a list item. This handles the rare case of a multi-paragraph list item in Pandoc output.

#### Compaction rule

A blank line between two lines is suppressed when:
- The previous non-blank line is a list item OR a list continuation
- The next non-blank line is a list item (item start, not just continuation)

Both conditions must be true. A blank line between a paragraph and the first list item is preserved (correct GFM: blank line before a list after a paragraph). A blank line between the last list item and a following paragraph is preserved.

**Fenced code block protection:** The compactor tracks `in_fence` state using ` ``` ` and `~~~` fence markers. Content inside code fences is never modified.

---

### 8.4 `compact_reference_sections(text)`

Compacts blank lines between plain content lines within named reference sections (Index, Glossary, List of Tables, etc.).

#### Trigger pattern — `COMPACT_SECTION_RE`

```python
COMPACT_SECTION_RE = re.compile(
    r'^(#{1,6})\s+('
    r'index|table of contents|contents|glossary|'
    r'list of (?:tables|figures|illustrations|abbreviations|exhibits|plates)|'
    r'abbreviations|acronyms|bibliography|references|'
    r'list of (?:effective pages?|changes?)'
    r')\s*$',
    re.IGNORECASE,
)
```

**Matched section names:** Index, Table of Contents, Contents, Glossary, List of Tables, List of Figures, List of Illustrations, List of Abbreviations, List of Exhibits, List of Plates, Abbreviations, Acronyms, Bibliography, References, List of Effective Pages, List of Changes.

#### Section boundary

Compaction applies from the matched heading until the next heading of equal or higher level. Nested sub-headings are preserved.

#### Lines exempt from compaction

Inside a matched section, blank lines are suppressed between plain content lines. The following line types are treated as "special" and retain their surrounding blank lines:
- `<!-- back-to-toc -->` markers
- Any `#` heading line
- Lines inside fenced code blocks

#### Trailing blank line

Each compacted section ends with exactly one blank line before the next section heading.

---

## 9. Python Library Reference

All modules are from the Python 3.12 standard library. No `pip install` or virtual environment is required.

### `re` — Regular expressions

Used throughout. Key calls:

| Call | Where used |
|---|---|
| `re.compile(pattern, flags)` | All compiled patterns (called once, reused) |
| `re.sub(pattern, repl, text)` | `strip_artifacts`, `normalize_whitespace`, anchor generation |
| `re.match(pattern, string)` | Line-by-line heading/list detection |
| `re.finditer(pattern, string)` | Image reference collection in document order |
| `re.IGNORECASE` | TOC heading detection, caption prefix matching |
| `re.DOTALL` | HTML comment stripping, HTML img tag matching across lines |
| `re.MULTILINE` | Empty blockquote stripping (matches `^` at each line start) |

### `html` — HTML entity decoding

```python
import html
html.unescape("&amp;lt;")   # → "&lt;"
```

Used in `gfm_anchor()` to decode HTML entities in heading text before anchor generation. Required because Pandoc occasionally encodes special characters in heading text as HTML entities.

### `subprocess` — External process invocation

```python
result = subprocess.run(cmd, capture_output=True, text=True)
result = subprocess.run(cmd, capture_output=True, check=True, timeout=30)
```

Used for Pandoc (`run_pandoc`) and LibreOffice (`_convert_emf_to_png`). `capture_output=True` captures both stdout and stderr. `check=True` raises `CalledProcessError` on non-zero exit. `timeout=30` prevents hung LibreOffice processes from blocking the pipeline.

### `shutil` — File and directory operations

```python
shutil.copy2(src, dst)          # Copy file preserving metadata
shutil.move(src, dst)           # Move file (used after LibreOffice conversion)
shutil.rmtree(path, ignore_errors=True)  # Remove scratch directory
```

### `pathlib.Path` — Filesystem paths

All paths are `Path` objects, never raw strings in internal logic. Converted to `str` only when passed to `subprocess.run()` (required by Pandoc/LibreOffice CLIs).

```python
Path(docx_path).stem     # filename without extension
path.exists()            # existence check
path.read_text()         # read file contents
path.write_text()        # write file contents
path.suffix.lower()      # file extension, normalized
path.mkdir(parents=True) # create directory tree
```

### `argparse` — CLI interface

```python
parser.add_argument("inputs", nargs="+", type=Path, metavar="DOCX")
parser.add_argument("--out-dir", type=Path, default=None)
```

Accepts one or more DOCX paths and an optional output directory. Non-DOCX files and missing files are filtered with a warning before processing begins.

---

## 10. Regex and Pattern Reference

Complete catalogue of all compiled patterns in the script, in order of appearance.

### GFM anchor generation

| Pattern | Purpose |
|---|---|
| `r'\[([^\]]+)\]\([^)]+\)'` | Strip markdown links: keep display text, remove URL |
| `r'[`*_~]'` | Strip emphasis markers |
| `r'[^\w\s-]'` | Remove non-word characters (keep word chars, spaces, hyphens) |
| `r'\s+'` | Replace whitespace runs with single hyphen |
| `r'-+'` | Collapse multiple hyphens to one |

### Image detection

| Pattern | Form | Notes |
|---|---|---|
| `r'(!\[[^\]]*\])\(([^)]+)\)'` | Markdown `![alt](src)` | Group 1: alt part. Group 2: src path |
| `r'<img\s[^>]*\bsrc="([^"]+)"[^>]*(?:alt="([^"]*)")?[^>]*/?>` | HTML `<img>` | Group 1: src. Group 2: alt (optional) |

### Figure caption detection

```
r'(!\[[^\]]*\]\([^)]+\))\n\n'
r'((?:Figure|Fig\.?|Exhibit|Chart|Diagram|Illustration|Plate|Table)\s+[\d\w.\-]+\.?\s+[^\n]+)'
```

Group 1: image tag. Group 2: caption text beginning with recognized prefix + reference label.

### Word TOC detection

| Pattern | Form | What it detects |
|---|---|---|
| `r'^\[.+\]\(#[^)]+\)\s*$'` | Form 1 | Bare hyperlink line (TOC field entry) |
| `r'^>\s*table of contents\s*$'` (IGNORECASE) | Form 1 | Blockquote TOC header |
| `r'^(#{1,6})\s+\[.+\]\(#[^)]+\)\s*$'` | Form 3 | Heading whose text is entirely a link |
| `r'^#{1,6}\s+table\s+of\s+contents\s*$'` (IGNORECASE) | Form 3 | TOC title heading |
| `r'^#{1,3}\s+Table of Contents\s*$'` (IGNORECASE) | Form 2 | Body TOC section heading |

### List item detection

```
r'^\s*(?:[-*+]|\d+[.)]|[A-Za-z][.)](?!\S)|(?:i{1,3}|iv|vi{0,3}|viii|ix|x{1,3}|xl|l)[.])\s'
```

| Sub-pattern | Matches |
|---|---|
| `[-*+]` | Bullet markers |
| `\d+[.)]` | Numbered items: `1.` `2)` etc. |
| `[A-Za-z][.)](?!\S)` | Lettered items: `a.` `B)` — negative lookahead prevents matching `e.g.` |
| `i{1,3}\|iv\|vi{0,3}\|viii\|ix\|x{1,3}\|xl\|l` | Roman numerals i through l |

### Compact reference sections

```
r'^(#{1,6})\s+(index|table of contents|contents|glossary|
list of (?:tables|figures|illustrations|abbreviations|exhibits|plates)|
abbreviations|acronyms|bibliography|references|
list of (?:effective pages?|changes?))\s*$'
```

Case-insensitive. Group 1: heading level. Group 2: section name.

### Back-to-TOC heading detection

| Pattern | Purpose |
|---|---|
| `r'^(#{1,3}) (.+)'` | Match H1–H3 with text |
| `r'^Table of Contents\s*$'` (IGNORECASE) | Exclude the TOC heading from back-link insertion |

---

## 11. Rules and Axioms

These are the invariants the pipeline is designed around. Violations of these rules explain most conversion failures.

### R1 — Source document quality determines output quality

Heading hierarchy is only preserved when source documents use Word's built-in paragraph styles (`Heading 1` through `Heading 6`). Text formatted manually as bold + large font is indistinguishable from body text. No converter can recover structure that was never encoded.

### R2 — Auto-numbering is not stored in OOXML

Word's auto-generated section numbers (1., 1.1, 1.1.1) are computed at render time from `<w:abstractNum>` list definitions. The numbers are not present in the XML. Pandoc reconstructs numbered lists correctly but cannot add section numbers that were never encoded as text.

### R3 — The Word TOC must be discarded and regenerated

The Word TOC field renders as a snapshot of broken links. It is always stripped and replaced with a freshly generated TOC built from the actual heading structure of the converted document. There is no scenario where preserving the Word TOC produces correct output.

### R4 — Image sequence order is stable

Pandoc extracts images in document order. `image1`, `image2`, `image3` in the extracted directory correspond to the first, second, and third image in the document. Sequential renaming to `docname-NNN.png` is reliable because it follows document order, not alphabetical or filesystem order.

### R5 — `--wrap=none` is required

Hard line wraps at 80 characters break all downstream pattern matching. Every heading, list item, and caption assumes a single line. This flag must never be removed.

### R6 — All layers must be idempotent

Running the script twice on the same input must produce identical output. This requires:
- Strip passes before insert passes (TOC, back-links)
- Scratch directories cleaned on success and failure
- Replace operations using `str.replace(old, new, 1)` (first occurrence only)

### R7 — Code fences are inviolable

Content inside fenced code blocks (` ``` ` or `~~~`) must never be modified by any post-processing step. All compaction and replacement functions track `in_fence` state and skip fence-enclosed content.

### R8 — Lists: both neighbors must be list items

A blank line is suppressed only when the preceding AND following non-blank lines are list-related. Suppressing when only one neighbor is a list item would incorrectly merge paragraphs that precede or follow a list.

### R9 — Blank lines around special lines are preserved in reference sections

Back-to-TOC links and sub-headings inside reference sections retain their surrounding blank lines even after compaction. Only plain content lines (index entries, glossary terms) are compacted.

### R10 — EMF/WMF must be converted at extraction time

Windows vector formats are not portable. They must be converted to PNG immediately. Deferring this to a later step risks leaving unconverted files in the output directory if subsequent steps fail.

---

## 12. Test Files and Results

### Test corpus

| File | Source | Size | Images | Notes |
|---|---|---|---|---|
| `cprsguium_ro.docx` | `docx-to-md/` (in-place) | 872 KB | 32 | CPRS Read-Only User Guide; cover image, tables, Index, Glossary |
| `ackq3_0_p12tm.docx` | `raw/ACKQ/` | — | 5 | Technical Manual; Form 3 TOC (headings as links); HTML `<img>` tags |
| `ackq3_0p13_tm.docx` | `raw/ACKQ/` | — | 2 | Technical Manual patch release notes |
| `ackq3_0p13_rn.docx` | `raw/ACKQ/` | — | — | Release notes; minimal images |
| `ackq3_0um.docx` | `raw/ACKQ/` | — | 41 | User Manual; complex bulleted lists, HTML tables, appendices |

### Issues discovered during testing and their fixes

#### Issue 1 — Word TOC not stripped (Form 1)

**Symptom:** The converted markdown contained lines like `[Introduction [4](#introduction)](#_TOC13979763)` after the cover page.

**Root cause:** Form 1 detection regex `r'^\s*-\s+\['` expected bullet list items. The CPRS document's TOC field rendered as plain link lines, not bullet items.

**Fix:** New regex `r'^\[.+\]\(#[^)]+\)\s*$'` matches bare link lines at any indent level. Block of 3+ such lines is treated as the TOC field artifact.

#### Issue 2 — Form 3 TOC (heading-level links) not stripped

**Symptom:** `ackq3_0_p12tm-pandoc.md` TOC contained entries like `- [Preface [ii](#preface)](#preface-iipreface)` mixed with clean entries.

**Root cause:** The ACKQ technical manual uses `Heading 1` style for each TOC entry. Pandoc converts these to `# [Title [page]](#anchor)` headings. The existing stripping logic did not handle this form.

**Fix:** Added Form 3 detection: a heading whose entire text is a markdown link matches `r'^(#{1,6})\s+\[.+\]\(#[^)]+\)\s*$'`. A `# Table Of Contents` heading followed by heading-link lines triggers removal of the entire block.

#### Issue 3 — HTML `<img>` tags not renamed

**Symptom:** After image normalization, some images remained as `<img src="docname-raw-images/media/image1.png" ...>` in the markdown. The raw-images scratch directory was not cleaned up.

**Root cause:** The image collection regex only matched markdown `![alt](src)` syntax. Images with explicit Word dimensions are emitted by Pandoc as HTML `<img>` tags.

**Fix:** Added `html_img_re` pattern to collect HTML img tags alongside markdown img refs. Both forms are sorted by document position and processed in the same renaming loop.

#### Issue 4 — Stray `>   ` blockquote after TOC strip

**Symptom:** An empty `>   ` blockquote line remained in the CPRS output after stripping the `> Table of Contents` blockquote header.

**Root cause:** `strip_word_toc` removed the blockquote content line but left behind an empty blockquote marker.

**Fix:** Added `re.sub(r'^>\s*$', '', text, flags=re.MULTILINE)` to `strip_artifacts()`.

---

## 13. Deviations from Specification

The specification document (`docx-to-markdown-guide.md`) described the intended design. The following changes were made during implementation based on what Pandoc actually produces.

| Specification says | What was implemented | Reason |
|---|---|---|
| Strip TOC as bullet list block | Strip three distinct TOC forms (plain links, heading-links, bullet list) | Discovered during testing that VA documents use all three forms |
| Single `html_img_re` not mentioned | Added HTML `<img>` tag handling | Pandoc uses HTML img for images with explicit Word dimensions |
| `strip_word_toc()` described as simple | Multi-pass algorithm with three distinct forms | Required by actual corpus |
| Compact sections: Index, Glossary only | Extended to 13 section name patterns | Anticipates List of Tables, List of Figures, Abbreviations found in VA corpus |
| Back links on H2 and H3 only | Implemented on H1, H2, H3 | H1 chapter headings in body (not the title) also benefit from navigation |

---

## 14. Known Limitations

### Merged table cells

GFM pipe tables do not support cell spanning. Word tables with horizontally or vertically merged cells lose the merge information silently. Affected tables appear with extra empty cells or collapsed content. Pandoc outputs these as HTML `<table>` elements when the table is too complex for GFM — which preserves the structure but reduces readability.

### Manual-formatted headings

Text styled as bold + large font without a Word `Heading N` paragraph style is converted as bold body text. These paragraphs do not appear in the TOC and do not receive back-to-TOC links. This is a source document authoring issue and cannot be corrected automatically.

**Diagnosis:** Run `python-docx` to audit heading styles before conversion:
```python
from docx import Document
doc = Document("input.docx")
styles = {p.style.name for p in doc.paragraphs}
print([s for s in sorted(styles) if 'Heading' in s])
```

### Auto-generated section numbers lost

Section numbers like `1.`, `1.1`, `1.1.1` that Word generates from outline numbering definitions are not present in the OOXML and cannot be recovered. If section numbers are important for cross-referencing, the source document must have them typed as literal text, not auto-generated.

### Caption detection requires standard prefixes

Figure captions must begin with `Figure`, `Fig.`, `Exhibit`, `Chart`, `Diagram`, `Illustration`, `Plate`, or `Table` followed by a reference number. Captions using other conventions (`Photo`, `Schematic`, `Screenshot`, or no label at all) are not detected and remain as plain paragraphs.

### Roman numeral list detection is limited to i–l

The roman numeral regex covers `i` through `l` (50). Section numbering beyond `l` (uncommon in practice) would require extending the pattern.

### LibreOffice EMF conversion quality

LibreOffice's EMF renderer produces correct output for most Windows metafiles but may misrender complex gradients or proprietary GDI extensions. Quality depends on the complexity of the original vector graphic.

---

*End of implementation guide.*
