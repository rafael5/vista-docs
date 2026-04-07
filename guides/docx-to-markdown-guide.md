# DOCX to Markdown Ingestion Pipeline — Full Fidelity Guide

**Date:** 2026-03-30
**Environment:** Linux Mint, 32 GB RAM, 1 TB SSD, AMD Ryzen (no GPU required)

---

## Table of Contents

1. [Goals and Scope](#1-goals-and-scope)
2. [What Makes DOCX Conversion Hard](#2-what-makes-docx-conversion-hard)
3. [Technology Survey](#3-technology-survey)
4. [Layer-by-Layer Architecture](#4-layer-by-layer-architecture)
5. [Chosen Stack and Rationale](#5-chosen-stack-and-rationale)
6. [Implementation](#6-implementation)
7. [Image Naming and Extraction](#7-image-naming-and-extraction)
8. [TOC Generation](#8-toc-generation)
9. [Post-Processing](#9-post-processing)
10. [Full Pipeline Script](#10-full-pipeline-script)
11. [Configuration Reference](#11-configuration-reference)
12. [Known Limitations](#12-known-limitations)
13. [Lessons Learned](#13-lessons-learned)

---

## 1. Goals and Scope

### What this pipeline produces

For each input `.docx` file, the pipeline produces:

```
output/
├── my-document.md               # Full markdown with all structure preserved
└── my-document_images/
    ├── my-document-001.png      # Figures extracted in sequence order
    ├── my-document-002.png
    └── ...
```

### Structural elements preserved

| Element | Target behavior |
|---|---|
| Table of Contents | Regenerated as linkable GFM markdown TOC |
| Chapter headings (H1) | `# Heading` |
| Section headings (H2–H6) | `## Heading` through `###### Heading` |
| Numbered lists (1, 2, 3) | `1.` `2.` `3.` ordered markdown list |
| Lettered lists (a, b, c) | `a.` `b.` `c.` preserved as-is |
| Roman numeral lists | `i.` `ii.` `iii.` preserved as-is |
| Bulleted lists (nested) | `- ` with indented nesting |
| Appendices | Preserved as H1/H2 headings with Appendix label |
| Tables | GFM pipe tables |
| Figures / inline images | Extracted as `docname-NNN.png`, linked with `![caption](path)` |
| Figure captions | Preserved as caption text below each image |
| Bold / italic emphasis | `**bold**` `*italic*` |
| Footnotes | Converted to inline markdown footnotes `[^1]` |
| Code blocks | Fenced ` ``` ` blocks |

---

## 2. What Makes DOCX Conversion Hard

Understanding failure modes before selecting tools avoids choosing the wrong tool for the job.

### 2.1 Auto-generated list numbering

Word's numbered lists are defined by `<w:abstractNum>` list definitions in the OOXML XML. The rendered numbers (`1.`, `2.`, `a.`, `i.`) are **computed at display time** and are **not stored as text** in the XML. The paragraph only records which list definition and which indent level it belongs to.

A converter that does not parse `<w:numPr>` and `<w:abstractNum>` will silently lose all numbered list structure — producing flat, unnumbered paragraphs.

### 2.2 Manual formatting masquerading as headings

Some Word documents simulate headings using manual formatting: bold text, a larger font size, or a custom character style — without applying a proper Word paragraph style (`Heading 1`, `Heading 2`, etc.). A converter that relies on paragraph styles to detect headings will miss these entirely.

No automated converter handles this reliably. It is a source document authoring problem.

### 2.3 Images stored as binary blobs

DOCX files are ZIP archives. Embedded images are stored in `word/media/` inside the ZIP as binary files (PNG, JPEG, WMF, EMF). EMF/WMF are Windows vector formats with no standard Linux renderer. Converting them to PNG requires either LibreOffice or a Windows GDI renderer.

### 2.4 The TOC is a field, not content

Word's Table of Contents is an auto-generated field (`<w:fldChar>`) containing rendered snapshot text. The snapshot may be stale (not updated before export). The actual document structure is in the heading paragraphs — not in the TOC field. The correct approach is to discard the Word TOC and regenerate it from the heading structure of the converted markdown.

### 2.5 Tables with merged cells

Word tables support horizontally and vertically merged cells (`<w:hMerge>`, `<w:vMerge>`). GFM pipe tables do not support merged cells. Any merger becomes invisible in the markdown output — a known lossy conversion that no current tool solves at the GFM layer.

---

## 3. Technology Survey

### 3.1 Conversion engines

| Tool | Type | DOCX headings | Auto-numbered lists | Tables | Images | Footnotes | Speed | GPU |
|---|---|---|---|---|---|---|---|---|
| **Pandoc 3.x** | OOXML parser | ✓ perfect | ✓ reconstructed | ✓ GFM | ✓ extracted | ✓ | <1s/doc | no |
| **Docling 2.x** | ML + XML | ✓ good | ✗ lost | ✓ good | ✓ `doc.pictures` | ✗ | 5–30s/doc | optional |
| **python-docx** | XML library | ✓ with code | ✓ with code | ✓ with code | ✓ with code | ✓ with code | <1s/doc | no |
| **Mammoth** | OOXML→HTML | ✓ via style map | partial | ✓ | ✓ | ✗ | <1s/doc | no |
| **Marker** | ML (vision) | ✓ | ✓ | ✓ | ✓ | partial | 10–60s/doc | optional |
| **MarkItDown** | python-docx wrapper | ✓ | partial | ✓ | partial | ✗ | <1s/doc | no |
| **LibreOffice headless** | Full office engine | ✓ | ✓ | ✓ | ✓ | ✓ | 3–10s/doc | no |
| **unstructured** | Multi-format parser | ✓ | partial | ✓ | partial | ✗ | 1–5s/doc | no |

### 3.2 Detailed comparison

#### Pandoc

**Pros:**
- Best-in-class OOXML parser, developed since 2006
- Reads `<w:numPr>` and `<w:abstractNum>` — correctly reconstructs all list numbering including letters, roman numerals, and multi-level outlines
- `--extract-media` extracts all embedded images to a directory with sequential filenames
- Native GFM output with pipe tables
- Handles footnotes, endnotes, tracked changes, comments
- Deterministic, scriptable, zero configuration
- 0 RAM overhead beyond document size
- Lua filter API for custom transformations

**Cons:**
- Cannot handle manual-formatted headings (no style = no heading detection)
- EMF/WMF vector images extracted as-is — need post-conversion to PNG
- Image filenames are generic (`image1.png`) — require renaming
- Merged table cells are silently flattened
- No figure caption linking (caption is a separate paragraph, not an `![alt](src)` unit)

**Verdict:** The correct primary converter for well-authored DOCX files.

---

#### Docling 2.x

**Pros:**
- Excellent PDF pipeline with layout detection (EGRET model family)
- Extracts images via `doc.pictures` API with `pic.get_image(doc)` → PIL Image
- Optional VLM figure description (SmolVLM, Granite)
- Handles scanned PDFs via OCR
- Active development, large model ecosystem

**Cons:**
- DOCX backend does not parse `<w:numPr>` — auto-numbered lists are lost
- Significantly slower than Pandoc for DOCX (5–30s vs <1s per file)
- Overkill for clean DOCX with proper Word styles
- No footnote support
- `do_picture_description` requires model download (~500MB–2GB)

**Verdict:** Use for PDF ingestion. Use only for DOCX when Word styles are poorly applied and ML layout detection is needed as a fallback.

---

#### python-docx

**Pros:**
- Direct access to every OOXML element
- Can parse `<w:numPr>` with custom code to reconstruct list numbering exactly
- Extracts images from `docx.part.related_parts` with original filenames
- Can read document properties, custom properties, tracked changes

**Cons:**
- Requires writing a full markdown renderer from scratch
- Every structural element (table, list, heading, image, footnote) requires custom handling
- Significant maintenance burden
- No existing production-quality markdown renderer built on it

**Verdict:** Valuable as a complement for preprocessing or post-processing. Not a standalone converter.

---

#### Mammoth

**Pros:**
- Clean DOCX→HTML conversion
- Style map API: map custom Word styles to HTML/markdown elements
- Handles embedded images with a callback API
- Good for documents with custom corporate styles

**Cons:**
- Primary output is HTML, not markdown — requires a second-pass HTML→markdown conversion (adding error surface)
- Numbered list reconstruction is partial
- No footnote support
- Less actively maintained than Pandoc

**Verdict:** Useful when Word documents use custom style names that need explicit mapping. Not recommended for general use.

---

#### Marker

**Pros:**
- Vision-model based — handles documents with non-standard formatting
- Good table extraction
- Handles mixed text+image layouts
- Works on both DOCX and PDF

**Cons:**
- 10–60s per document on CPU; requires GPU for reasonable throughput at corpus scale
- Non-deterministic (ML model outputs vary slightly between runs)
- Not well-suited to documents with standard Word styles where Pandoc would be more accurate
- High memory footprint during model load (~4–8GB)

**Verdict:** Use only when Pandoc fails and the document structure cannot be recovered by any other means. Too slow and resource-intensive for a corpus of thousands of documents.

---

#### LibreOffice headless

**Pros:**
- Full Word-compatible rendering engine
- Can convert EMF/WMF to PNG reliably
- Handles all list numbering (same rendering engine as LibreOffice Writer)

**Cons:**
- 3–10s per document startup overhead (JVM-like cold start)
- Markdown output requires intermediate ODT/HTML export + a second tool
- Not scriptable from Python without subprocess
- Output quality depends on LibreOffice's own markdown/HTML exporter which has known issues

**Verdict:** Use exclusively to convert EMF/WMF vector images to PNG as a post-processing step.

---

#### MarkItDown (Microsoft, 2024)

**Pros:**
- Simple API, maintained by Microsoft
- Uses python-docx internally
- Handles basic DOCX structure well

**Cons:**
- python-docx wrapper with limited extension points
- Numbered list reconstruction is incomplete
- No image extraction API

**Verdict:** Too limited for high-fidelity ingestion. Not recommended.

---

### 3.3 Summary recommendation

| Pipeline layer | Chosen tool | Rationale |
|---|---|---|
| DOCX structural conversion | **Pandoc 3.x** | Best OOXML parser; correct list numbering; GFM tables; zero configuration |
| Image extraction | **Pandoc `--extract-media`** + rename script | Extracts all embedded images in sequence; rename to `docname-NNN.png` |
| EMF/WMF → PNG | **LibreOffice headless** (`soffice --headless`) | Only reliable EMF/WMF renderer on Linux |
| Figure caption linking | **python post-processor** | Pandoc outputs caption as a following paragraph — link it to the preceding image |
| TOC generation | **python post-processor** | Discard Word TOC; regenerate from heading structure using GFM anchors |
| PDF ingestion | **Docling 2.x** | OCR + layout detection; not used for DOCX |

---

## 4. Layer-by-Layer Architecture

```
┌─────────────────────────────────────────────────────┐
│  Input: document.docx                               │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  Layer 1: Pandoc conversion                         │
│  pandoc input.docx -f docx -t gfm                  │
│    --wrap=none --standalone                         │
│    --extract-media=./raw_images                     │
│    -o raw_output.md                                 │
│                                                     │
│  Output: raw_output.md (structure correct)          │
│          raw_images/image1.png, image2.emf, ...     │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  Layer 2: Image normalization                       │
│  - Convert EMF/WMF → PNG via LibreOffice            │
│  - Rename image1.png → docname-001.png              │
│  - Move to docname_images/ directory                │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  Layer 3: Markdown post-processing                  │
│  - Update image paths in markdown                   │
│  - Link figure captions to preceding image          │
│  - Strip Word TOC field artifacts                   │
│  - Normalize whitespace and paragraph spacing       │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  Layer 4: TOC generation                            │
│  - Scan heading structure                           │
│  - Generate GFM anchor links                        │
│  - Insert linkable TOC after H1 title               │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  Output: docname.md + docname_images/               │
└─────────────────────────────────────────────────────┘
```

---

## 5. Chosen Stack and Rationale

### Primary converter: Pandoc 3.x

Pandoc is the only open-source tool that correctly reconstructs Word's auto-numbered lists from OOXML list definitions. Every other tool either ignores the numbering (Docling, MarkItDown) or requires manual style mapping (Mammoth).

On a corpus of thousands of DOCX files, Pandoc's sub-second conversion speed is essential. Marker or Docling at 10–30s per file would take hours for the same corpus.

### Image pipeline: Pandoc extract + rename

Pandoc's `--extract-media` writes all embedded images to a directory in document order. The filenames are generic (`image1.png`, `image2.jpeg`) but the sequence is reliable. A rename step maps them to `docname-NNN.png`.

EMF and WMF files (Windows vector format) require LibreOffice for conversion. LibreOffice's `--headless --convert-to png` command produces correct PNG output.

### Post-processing: Python

Three tasks are done in Python after Pandoc:
1. Rename image references in the markdown to match the new `docname-NNN.png` filenames
2. Attach figure captions: Pandoc outputs a caption as a plain paragraph after the image line — this step converts the pair into `![caption](path)` with the caption as the alt text
3. Strip the Word TOC artifact (Pandoc renders the TOC field snapshot as a list of plain links — these are structurally incorrect and should be replaced)

### TOC: Regenerate from headings

The Word TOC is a rendered field snapshot — it may be stale and does not contain GFM anchor links. It is discarded and replaced with a freshly generated linkable TOC built from the heading structure of the converted document, using GitHub Flavored Markdown anchor rules.

---

## 6. Implementation

### 6.1 Dependencies

```bash
# System
sudo apt install pandoc libreoffice-headless

# Python
uv add pillow  # for any PIL-based image handling
```

Verify:
```bash
pandoc --version    # should be 3.x
soffice --version   # LibreOffice version
```

### 6.2 Pandoc invocation

```python
import subprocess
from pathlib import Path

def run_pandoc(docx_path: Path, md_path: Path, raw_img_dir: Path) -> None:
    """Convert DOCX to GFM markdown with embedded images extracted."""
    raw_img_dir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [
            "pandoc", str(docx_path),
            "-f", "docx",
            "-t", "gfm",
            "--wrap=none",           # no hard line wraps
            "--standalone",          # include YAML frontmatter (title, author, date)
            f"--extract-media={raw_img_dir}",
            "-o", str(md_path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    if result.stderr:
        # Pandoc writes warnings to stderr — log but do not fail
        print(f"  pandoc warnings: {result.stderr.strip()}")
```

The `--standalone` flag outputs document metadata as YAML frontmatter:

```yaml
---
title: "CPRS User Manual"
author: "Department of Veterans Affairs"
date: "January 2024"
---
```

---

## 7. Image Naming and Extraction

### 7.1 What Pandoc produces

After `--extract-media=raw_images/`, the directory contains:

```
raw_images/
├── image1.png
├── image2.jpeg
├── image3.emf       ← Windows vector — must convert
├── image4.wmf       ← Windows metafile — must convert
└── ...
```

The markdown references them as:
```markdown
![](raw_images/image1.png)
![](raw_images/image3.emf)
```

### 7.2 Renaming to `docname-NNN.png`

```python
import re
import shutil
import subprocess
from pathlib import Path

EMF_FORMATS = {".emf", ".wmf"}

def normalize_images(
    md_path: Path,
    raw_img_dir: Path,
    out_img_dir: Path,
    doc_slug: str,
) -> None:
    """
    Rename extracted images to docname-NNN.png in sequence order.
    Convert EMF/WMF to PNG via LibreOffice.
    Update image references in the markdown file.
    """
    out_img_dir.mkdir(parents=True, exist_ok=True)

    text = md_path.read_text(encoding="utf-8")

    # Find all image references in document order
    img_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
    matches = list(img_pattern.finditer(text))

    replacements: list[tuple[str, str]] = []  # (old_ref, new_ref)
    seq = 1

    for m in matches:
        alt_text = m.group(1)
        src_rel = m.group(2)
        src_path = md_path.parent / src_rel

        if not src_path.exists():
            continue

        suffix = src_path.suffix.lower()
        new_name = f"{doc_slug}-{seq:03d}.png"
        new_path = out_img_dir / new_name

        if suffix in EMF_FORMATS:
            # Convert via LibreOffice headless
            _convert_emf_to_png(src_path, new_path)
        else:
            shutil.copy2(src_path, new_path)

        new_ref = f"{out_img_dir.name}/{new_name}"
        replacements.append((m.group(0), f"![{alt_text}]({new_ref})"))
        seq += 1

    # Apply replacements
    for old, new in replacements:
        text = text.replace(old, new, 1)

    md_path.write_text(text, encoding="utf-8")

    # Clean up raw image dir
    if raw_img_dir.exists():
        shutil.rmtree(raw_img_dir)


def _convert_emf_to_png(emf_path: Path, out_path: Path) -> None:
    """Convert EMF/WMF to PNG using LibreOffice headless."""
    tmp_dir = out_path.parent / "_lo_tmp"
    tmp_dir.mkdir(exist_ok=True)
    try:
        subprocess.run(
            [
                "soffice", "--headless",
                "--convert-to", "png",
                "--outdir", str(tmp_dir),
                str(emf_path),
            ],
            capture_output=True,
            check=True,
            timeout=30,
        )
        # LibreOffice outputs <stem>.png in the outdir
        converted = tmp_dir / (emf_path.stem + ".png")
        if converted.exists():
            shutil.move(str(converted), str(out_path))
        else:
            # fallback: copy original if conversion failed
            shutil.copy2(emf_path, out_path.with_suffix(emf_path.suffix))
    except subprocess.CalledProcessError:
        # LibreOffice failed — copy original with original extension
        shutil.copy2(emf_path, out_path.with_suffix(emf_path.suffix))
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
```

### 7.3 Figure caption linking

Pandoc outputs a figure as two consecutive elements:

```markdown
![](my-doc_images/my-doc-001.png)

Figure 3-1. System Architecture Overview
```

The caption paragraph immediately following an image line is the figure caption. The post-processor converts this pair into a single image with the caption as alt text:

```markdown
![Figure 3-1. System Architecture Overview](my-doc_images/my-doc-001.png)

*Figure 3-1. System Architecture Overview*
```

The alt text enables screen readers and search indexing; the italic paragraph below preserves the caption visibly in rendered markdown.

```python
CAPTION_PATTERN = re.compile(
    r'(!\[[^\]]*\]\([^)]+\))\n\n(Figure\s+[\d\w.-]+\.?\s+[^\n]+)',
    re.IGNORECASE,
)

def link_figure_captions(text: str) -> str:
    """Attach figure caption text to the preceding image as alt text."""
    def replace(m: re.Match) -> str:
        img_tag = m.group(1)
        caption = m.group(2).strip()
        # Replace empty or generic alt text with caption
        new_img = re.sub(r'!\[[^\]]*\]', f'![{caption}]', img_tag, count=1)
        return f"{new_img}\n\n*{caption}*"
    return CAPTION_PATTERN.sub(replace, text)
```

---

## 8. TOC Generation

### 8.1 Why the Word TOC is discarded

Pandoc renders the Word TOC field snapshot as a list of plain links pointing to anchor IDs that do not exist in the output markdown. These links are broken and structurally misleading. The section is removed.

### 8.2 Detection and removal

The Word TOC renders as a block of lines matching `- [Title](#some-word-id)` at the top of the document, before the first real heading. Detection heuristic: a block of 3+ consecutive list lines appearing before the first `## ` heading.

```python
def strip_word_toc(text: str) -> str:
    """Remove the Word TOC field artifact from the converted markdown."""
    lines = text.splitlines()
    out = []
    i = 0
    # Skip YAML frontmatter
    if lines and lines[0].strip() == '---':
        i = 1
        while i < len(lines) and lines[i].strip() != '---':
            out.append(lines[i])
            i += 1
        if i < len(lines):
            out.insert(0, '---')
            out.append('---')
            i += 1

    # Detect TOC block: 3+ consecutive list lines before first ## heading
    toc_start = None
    toc_end = None
    j = i
    while j < len(lines):
        if re.match(r'^- \[', lines[j]) or re.match(r'^\s+- \[', lines[j]):
            if toc_start is None:
                toc_start = j
            toc_end = j
        elif toc_start is not None and not lines[j].strip():
            pass  # blank line inside TOC block
        elif toc_start is not None:
            break
        j += 1

    if toc_start is not None and (toc_end - toc_start) >= 2:
        lines = lines[:toc_start] + lines[toc_end + 1:]

    return "\n".join(lines)
```

### 8.3 Regenerated linkable TOC

After stripping the Word TOC, a fresh linkable TOC is generated from the heading structure using GFM anchor rules (same algorithm as GitHub renders). See `add_toc_image_md.py` for the full implementation with deduplication.

```python
import html
import re

def gfm_anchor(text: str, seen: dict[str, int]) -> str:
    text = html.unescape(text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'[`*_~]', '', text)
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    if not text:
        return ''
    base = text
    count = seen.get(base, 0)
    seen[base] = count + 1
    return base if count == 0 else f"{base}-{count}"


def build_toc(lines: list[str], max_depth: int = 3) -> str:
    entries = []
    seen: dict[str, int] = {}
    for line in lines:
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if not m:
            continue
        level = len(m.group(1))
        if level > max_depth:
            continue
        raw = m.group(2).strip()
        if not raw:
            continue
        anchor = gfm_anchor(raw, seen)
        display = re.sub(r'[`*_~]', '', html.unescape(raw)).strip()
        display = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', display)
        indent = "  " * (level - 1)
        entries.append(f"{indent}- [{display}](#{anchor})")
    if not entries:
        return ""
    return "## Table of Contents\n\n" + "\n".join(entries)
```

---

## 9. Post-Processing

### 9.1 Normalize whitespace

Pandoc occasionally produces 3+ consecutive blank lines between sections. Normalize to maximum 2 blank lines:

```python
def normalize_blank_lines(text: str) -> str:
    return re.sub(r'\n{3,}', '\n\n', text)
```

### 9.2 Normalize heading spacing

Ensure one blank line before and after every heading:

```python
def normalize_heading_spacing(text: str) -> str:
    # One blank line before headings (not at document start)
    text = re.sub(r'([^\n])\n(#{1,6} )', r'\1\n\n\2', text)
    # One blank line after headings
    text = re.sub(r'(#{1,6} [^\n]+)\n([^\n])', r'\1\n\n\2', text)
    return text
```

### 9.3 Strip Word artifact comments

Pandoc sometimes emits HTML comments from Word track-changes or hidden text fields:

```python
def strip_word_artifacts(text: str) -> str:
    # Strip Word XML comment artifacts
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # Strip empty bold/italic markers
    text = re.sub(r'\*\*\s*\*\*', '', text)
    text = re.sub(r'\*\s*\*', '', text)
    return text
```

---

## 10. Full Pipeline Script

```python
"""
docx_to_md.py — Full-fidelity DOCX to Markdown pipeline.

Usage:
    python docx_to_md.py input.docx --out-dir ./output
    python docx_to_md.py ./raw/ACKQ/*.docx --out-dir ./markdown

Pipeline:
    1. Pandoc: DOCX → raw GFM + extracted images
    2. Image normalize: rename to docname-NNN.png, convert EMF/WMF → PNG
    3. Post-process: captions, whitespace, artifact removal
    4. TOC: strip Word TOC, regenerate linkable TOC from headings
"""
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path


# ── GFM anchor generation ────────────────────────────────────────────────────

def gfm_anchor(text: str, seen: dict[str, int]) -> str:
    text = html.unescape(text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'[`*_~]', '', text)
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    if not text:
        return ''
    base = text
    count = seen.get(base, 0)
    seen[base] = count + 1
    return base if count == 0 else f"{base}-{count}"


def build_toc(lines: list[str], max_depth: int = 3) -> str:
    entries = []
    seen: dict[str, int] = {}
    for line in lines:
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if not m:
            continue
        level = len(m.group(1))
        if level > max_depth:
            continue
        raw = m.group(2).strip()
        if not raw:
            continue
        anchor = gfm_anchor(raw, seen)
        if not anchor:
            continue
        display = re.sub(r'[`*_~]', '', html.unescape(raw)).strip()
        display = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', display)
        indent = "  " * (level - 1)
        entries.append(f"{indent}- [{display}](#{anchor})")
    if not entries:
        return ""
    return "## Table of Contents\n\n" + "\n".join(entries)


# ── Pandoc conversion ─────────────────────────────────────────────────────────

def run_pandoc(docx_path: Path, md_path: Path, raw_img_dir: Path) -> None:
    raw_img_dir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [
            "pandoc", str(docx_path),
            "-f", "docx",
            "-t", "gfm",
            "--wrap=none",
            "--standalone",
            f"--extract-media={raw_img_dir}",
            "-o", str(md_path),
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"pandoc failed: {result.stderr}")
    if result.stderr:
        print(f"    pandoc: {result.stderr.strip()}")


# ── Image normalization ───────────────────────────────────────────────────────

EMF_FORMATS = {".emf", ".wmf"}


def _convert_emf_to_png(emf_path: Path, out_path: Path) -> bool:
    tmp_dir = out_path.parent / "_lo_tmp"
    tmp_dir.mkdir(exist_ok=True)
    try:
        subprocess.run(
            ["soffice", "--headless", "--convert-to", "png",
             "--outdir", str(tmp_dir), str(emf_path)],
            capture_output=True, check=True, timeout=30,
        )
        converted = tmp_dir / (emf_path.stem + ".png")
        if converted.exists():
            shutil.move(str(converted), str(out_path))
            return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        pass
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
    return False


def normalize_images(
    md_path: Path,
    raw_img_dir: Path,
    out_img_dir: Path,
    doc_slug: str,
) -> int:
    """Rename images to doc_slug-NNN.png and update markdown references."""
    out_img_dir.mkdir(parents=True, exist_ok=True)
    text = md_path.read_text(encoding="utf-8")
    img_pattern = re.compile(r'(!\[[^\]]*\])\(([^)]+)\)')
    matches = list(img_pattern.finditer(text))

    n_images = 0
    for seq, m in enumerate(matches, start=1):
        alt_part = m.group(1)
        src_rel = m.group(2)
        # Pandoc uses the raw_img_dir name as prefix in the path
        src_path = md_path.parent / src_rel
        if not src_path.exists():
            continue
        suffix = src_path.suffix.lower()
        new_name = f"{doc_slug}-{seq:03d}.png"
        new_path = out_img_dir / new_name
        if suffix in EMF_FORMATS:
            ok = _convert_emf_to_png(src_path, new_path)
            if not ok:
                # keep original extension on failure
                new_name = f"{doc_slug}-{seq:03d}{suffix}"
                new_path = out_img_dir / new_name
                shutil.copy2(src_path, new_path)
        else:
            shutil.copy2(src_path, new_path)
        new_ref = f"{out_img_dir.name}/{new_name}"
        text = text.replace(m.group(0), f"{alt_part}({new_ref})", 1)
        n_images += 1

    md_path.write_text(text, encoding="utf-8")
    if raw_img_dir.exists():
        shutil.rmtree(raw_img_dir)
    return n_images


# ── Post-processing ───────────────────────────────────────────────────────────

CAPTION_PATTERN = re.compile(
    r'(!\[[^\]]*\]\([^)]+\))\n\n((?:Figure|Fig\.?|Exhibit)\s+[\d\w.\-]+\.?\s+[^\n]+)',
    re.IGNORECASE,
)


def link_figure_captions(text: str) -> str:
    def replace(m: re.Match) -> str:
        img_tag = m.group(1)
        caption = m.group(2).strip()
        new_img = re.sub(r'!\[[^\]]*\]', f'![{caption}]', img_tag, count=1)
        return f"{new_img}\n\n*{caption}*"
    return CAPTION_PATTERN.sub(replace, text)


def strip_word_toc(text: str) -> str:
    """Remove the rendered Word TOC field from the converted markdown."""
    lines = text.splitlines()
    # Find a block of 3+ consecutive list lines and remove it
    i = 0
    toc_start = None
    toc_end = None
    while i < len(lines):
        if re.match(r'^\s*-\s+\[', lines[i]):
            if toc_start is None:
                toc_start = i
            toc_end = i
        elif toc_start is not None and not lines[i].strip():
            pass  # blank line within block
        elif toc_start is not None:
            break
        i += 1
    if toc_start is not None and toc_end is not None and (toc_end - toc_start) >= 2:
        lines = lines[:toc_start] + lines[toc_end + 1:]
    return "\n".join(lines)


def insert_toc(text: str) -> str:
    """Insert a generated linkable TOC after the H1 title."""
    lines = text.splitlines()
    toc_str = build_toc(lines)
    if not toc_str:
        return text
    # Find insert point: after H1 + blank lines
    insert_at = 0
    if lines and re.match(r'^# ', lines[0]):
        insert_at = 1
        while insert_at < len(lines) and not lines[insert_at].strip():
            insert_at += 1
    before = "\n".join(lines[:insert_at])
    after = "\n".join(lines[insert_at:])
    return before + "\n\n" + toc_str + "\n\n" + after


def normalize_whitespace(text: str) -> str:
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + "\n"


def strip_artifacts(text: str) -> str:
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    text = re.sub(r'\*\*\s*\*\*', '', text)
    text = re.sub(r'\*\s*\*', '', text)
    return text


# ── Main pipeline ─────────────────────────────────────────────────────────────

def process_docx(docx_path: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    doc_slug = docx_path.stem.lower().replace(" ", "-")
    md_path = out_dir / f"{doc_slug}.md"
    raw_img_dir = out_dir / f"{doc_slug}_raw_images"
    out_img_dir = out_dir / f"{doc_slug}_images"

    print(f"  converting: {docx_path.name}")

    # Layer 1: Pandoc
    run_pandoc(docx_path, md_path, raw_img_dir)

    # Layer 2: Image normalization
    n_images = normalize_images(md_path, raw_img_dir, out_img_dir, doc_slug)

    # Layer 3: Post-processing
    text = md_path.read_text(encoding="utf-8")
    text = strip_artifacts(text)
    text = link_figure_captions(text)
    text = strip_word_toc(text)
    text = normalize_whitespace(text)

    # Layer 4: TOC
    text = insert_toc(text)

    md_path.write_text(text, encoding="utf-8")
    print(f"    → {md_path.name}  ({n_images} images)")


def main(docx_paths: list[Path], out_dir: Path) -> None:
    print(f"processing {len(docx_paths)} file(s) → {out_dir}\n")
    for docx_path in docx_paths:
        try:
            process_docx(docx_path, out_dir)
        except Exception as e:
            print(f"  ERROR {docx_path.name}: {e}")
    print("\ndone.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="DOCX → Markdown pipeline")
    parser.add_argument("inputs", nargs="+", type=Path, help="DOCX file(s) or glob")
    parser.add_argument("--out-dir", type=Path, default=Path("./output"), help="Output directory")
    args = parser.parse_args()
    main(args.inputs, args.out_dir)
```

---

## 11. Configuration Reference

### Pandoc flags

| Flag | Effect | When to change |
|---|---|---|
| `-t gfm` | GitHub Flavored Markdown | Use `-t markdown` for Pandoc-extended markdown (footnotes rendered differently) |
| `--wrap=none` | No hard line wraps | Remove to get 80-char wrapped output |
| `--standalone` | YAML frontmatter | Remove if frontmatter is unwanted |
| `--extract-media=DIR` | Extract images to DIR | Always use — without it images are base64-embedded in the markdown |
| `--reference-links` | Use `[label][id]` link style instead of inline | Useful for documents with many repeated links |
| `--atx-headers` | Use `#` style headings (default in GFM) | No change needed |

### TOC depth

In `build_toc()`, set `max_depth`:
- `2` — H1 and H2 only (chapter-level TOC)
- `3` — H1–H3 (default — section level)
- `4` — H1–H4 (subsection level; produces large TOCs in dense documents)

### Image naming

The `doc_slug` is derived from `docx_path.stem.lower().replace(" ", "-")`. For a file named `CPRS User Manual v28.docx`, the slug is `cprs-user-manual-v28` and images are named `cprs-user-manual-v28-001.png`, `cprs-user-manual-v28-002.png`, etc.

---

## 12. Known Limitations

### Merged table cells

GFM pipe tables do not support cell spanning. A Word table with merged cells will have the merged content collapsed into a single cell with no indication of the original span. This is a GFM format limitation — no converter can solve it at the markdown layer.

**Workaround:** Use HTML table output for affected documents:
```bash
pandoc input.docx -t html -o output.html
```

### Manual-formatted headings

Text formatted as bold + large font without a Word `Heading N` paragraph style is indistinguishable from body text to any OOXML parser. These paragraphs appear as bold body text in the output.

**Detection:** Run `python-docx` to audit styles before conversion:
```python
from docx import Document
doc = Document("input.docx")
styles_used = {p.style.name for p in doc.paragraphs}
print(styles_used)  # should contain 'Heading 1', 'Heading 2', etc.
```

### EMF/WMF conversion quality

LibreOffice's EMF/WMF renderer produces correct output for most Windows metafiles but may misrender complex gradient fills or proprietary GDI extensions. Quality depends on the original graphic's complexity.

### Appendix heading detection

Appendices styled as `Heading 1` with text like `Appendix A — Glossary` are correctly converted to `# Appendix A — Glossary`. Appendices styled differently (e.g., a custom `Appendix` paragraph style) require a Pandoc Lua filter to map the custom style to a heading level.

### Figure caption detection

The `link_figure_captions()` function matches captions beginning with `Figure`, `Fig.`, or `Exhibit`. Captions using other conventions (`Illustration`, `Plate`, `Chart`, `Diagram`) are not matched and remain as plain paragraphs below the image.

**Fix:** Extend `CAPTION_PATTERN` with additional caption prefixes:
```python
CAPTION_PATTERN = re.compile(
    r'(!\[[^\]]*\]\([^)]+\))\n\n'
    r'((?:Figure|Fig\.?|Exhibit|Chart|Diagram|Illustration|Plate)\s+[\d\w.\-]+\.?\s+[^\n]+)',
    re.IGNORECASE,
)
```

---

## 13. Lessons Learned

### Pandoc is the correct tool for DOCX; ML tools are for PDFs

The temptation is to reach for the newest ML-based converter. For well-authored DOCX files, this is the wrong choice. Pandoc has a mature, complete OOXML parser that handles numbering, footnotes, styles, and metadata correctly. ML models add latency, non-determinism, and resource overhead without improving accuracy for structured XML input.

### The Word TOC must be discarded, not converted

Pandoc converts the Word TOC field snapshot into a list of broken links. Every approach that tries to preserve the Word TOC produces structurally incorrect output. The correct approach: always discard and regenerate from the heading structure.

### Image sequence order is stable in Pandoc

Pandoc extracts images in document order. The sequence `image1.png`, `image2.png` maps directly to the first, second, third figure in the document. This makes sequential renaming reliable. Do not rely on file modification time or alphabetical sort — use the sequence order from the markdown itself.

### EMF is a Windows-only format; convert immediately

EMF and WMF files are Windows vector formats. Any tool that does not convert them leaves non-portable files in the output. Convert to PNG at extraction time — do not defer. LibreOffice's headless mode on Linux is the only reliable non-Windows EMF renderer.

### `--wrap=none` is essential for downstream processing

Without `--wrap=none`, Pandoc introduces hard line breaks at 80 characters inside paragraphs. These breaks break regex-based post-processing (heading detection, caption matching) and make the markdown difficult to read and diff. Always use `--wrap=none`.

### DOCX fidelity is determined at authoring time, not conversion time

The highest-impact intervention is upstream: ensuring source documents use Word's built-in paragraph styles correctly. `Heading 1`–`Heading 6`, `List Bullet`, `List Number`, `Caption` — when applied correctly, every converter handles them well. When authors use manual formatting, no converter can recover the lost structure.

---

*End of guide.*
