"""I/O thin layer: DOCX → raw GFM markdown string + images.

Pandoc is the default backend and handles ~99 % of the corpus well. A small
allowlist of documents (see ``DOCLING_DOCS``) is routed to a Docling backend
instead: pandoc explodes their lists into thousands of bare, empty markers
because of the ``[[…]](#_Toc…)`` cross-reference fields they carry. The flagship
case is ``cprsguium.docx`` (the CPRS GUI user manual) — pandoc produces 3,058
bare markers (~65 % of every bare marker in the whole corpus), Docling produces
none. Docling is an optional dependency (``pip install vista-docs[docling]``),
imported lazily, so the default install stays pandoc-only.
"""

from __future__ import annotations

import logging
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path
from typing import Callable
from xml.etree import ElementTree as ET

logger = logging.getLogger(__name__)

EMF_FORMATS = {".emf", ".wmf"}

# Source-file stems (lower-cased, no extension) routed to the Docling backend.
# Identified by a corpus-wide pandoc bare-marker sweep: these are the only docs
# carrying the heavy `[[…]]` cross-ref explosion. Keep this list tiny and explicit.
DOCLING_DOCS = frozenset({"cprsguium", "constm"})

# OOXML namespaces used when reading alt-text out of the DOCX XML.
_NS_MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"
_NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
_NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"


def _run_pandoc(docx_path: Path, md_path: Path, raw_img_dir: Path) -> None:
    """Convert DOCX to GFM markdown, extracting images to raw_img_dir."""
    raw_img_dir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [
            "pandoc",
            str(docx_path),
            "-f",
            "docx",
            "-t",
            "gfm",
            "--wrap=none",
            "--standalone",
            f"--extract-media={raw_img_dir}",
            "-o",
            str(md_path),
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"pandoc failed:\n{result.stderr}")
    for line in result.stderr.strip().splitlines():
        logger.debug("pandoc: %s", line)


def _select_backend(source_path: Path) -> str:
    """Return the converter backend ('docling' or 'pandoc') for a source DOCX."""
    return "docling" if source_path.stem.lower() in DOCLING_DOCS else "pandoc"


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _find_descendant(el: ET.Element, name: str) -> ET.Element | None:
    for d in el.iter():
        if _local_name(d.tag) == name:
            return d
    return None


def _collect_pictures(el: ET.Element, rels: dict[str, str], out: list[dict]) -> None:
    """Depth-first, document-order walk emitting one record per placed picture.

    Alt-text lives on the drawing wrapper ``<wp:docPr>``; group members fall back
    to the inner ``<pic:cNvPr>``. ``<mc:AlternateContent>`` is collapsed to its
    ``Choice`` so VML fallbacks don't double-count.
    """
    name = _local_name(el.tag)
    if name == "AlternateContent":
        branch = el.find(f"{{{_NS_MC}}}Choice")
        if branch is None:
            branch = el.find(f"{{{_NS_MC}}}Fallback")
        if branch is not None:
            for child in branch:
                _collect_pictures(child, rels, out)
        return
    if name in ("inline", "anchor"):  # a DrawingML drawing container
        docpr = _find_descendant(el, "docPr")
        draw_alt = (docpr.get("descr") if docpr is not None else "") or ""
        draw_title = (docpr.get("title") if docpr is not None else "") or ""
        for pic in (d for d in el.iter() if _local_name(d.tag) == "pic"):
            cnv = _find_descendant(pic, "cNvPr")
            blip = _find_descendant(pic, "blip")
            embed = blip.get(f"{{{_NS_R}}}embed") if blip is not None else None
            pic_alt = (cnv.get("descr") if cnv is not None else "") or ""
            target = rels.get(embed, "") if embed else ""
            out.append(
                {
                    "alt": (pic_alt or draw_alt or draw_title).strip(),
                    "media": target.split("/")[-1] if target else "",
                }
            )
        return
    if name == "imagedata":  # standalone VML image (no DrawingML choice)
        embed = el.get(f"{{{_NS_R}}}id")
        target = rels.get(embed, "") if embed else ""
        out.append({"alt": "", "media": target.split("/")[-1] if target else ""})
        return
    for child in el:
        _collect_pictures(child, rels, out)


def _extract_docx_alt_text(docx_path: Path) -> list[dict]:
    """Per-picture ``{"alt", "media"}`` records in document order.

    Docling never parses Word's alt-text (0 captions/annotations), so we read it
    straight from the DOCX XML. The resulting list aligns 1:1 with Docling's
    ``<!-- image -->`` placeholders.
    """
    with zipfile.ZipFile(docx_path) as z:
        rels: dict[str, str] = {}
        for rel in ET.fromstring(z.read("word/_rels/document.xml.rels")):
            rid, target = rel.get("Id"), rel.get("Target")
            if rid is not None and target is not None:
                rels[rid] = target
        root = ET.fromstring(z.read("word/document.xml"))
    pics: list[dict] = []
    _collect_pictures(root, rels, pics)
    return pics


def _inject_image_refs(markdown: str, pics: list[dict], img_dir_name: str) -> str:
    """Replace each ``<!-- image -->`` placeholder with ``![alt](img_dir_name/media)``.

    Placeholders are consumed in order against ``pics``; a count mismatch raises
    rather than risk silently misaligning every caption. Pictures with no media
    keep the bare placeholder.
    """
    n_placeholders = markdown.count("<!-- image -->")
    if n_placeholders != len(pics):
        raise ValueError(
            f"image placeholder/alt-text mismatch: {n_placeholders} placeholders "
            f"vs {len(pics)} pictures"
        )
    pic_iter = iter(pics)

    def _repl(_m: re.Match) -> str:
        pic = next(pic_iter)
        if not pic["media"]:
            return "<!-- image -->"
        alt = pic["alt"].replace("]", ")").replace("\n", " ")
        return f"![{alt}]({img_dir_name}/{pic['media']})"

    return re.sub(r"<!-- image -->", _repl, markdown)


def _extract_media(docx_path: Path, raw_img_dir: Path, names: set[str]) -> None:
    """Copy the named ``word/media/*`` entries out of the DOCX into raw_img_dir."""
    raw_img_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(docx_path) as z:
        for entry in z.namelist():
            base = entry.rsplit("/", 1)[-1]
            if entry.startswith("word/media/") and base in names:
                (raw_img_dir / base).write_bytes(z.read(entry))


def _default_docling_convert(docx_path: Path) -> str:
    """Convert a DOCX to markdown with Docling's default pipeline (lazy import)."""
    try:
        from docling.document_converter import DocumentConverter
    except ImportError as exc:  # pragma: no cover - exercised only without the extra
        raise RuntimeError(
            f"Docling backend required for {docx_path.name} but 'docling' is not "
            "installed. Install it with: uv pip install -e '.[docling]'"
        ) from exc
    result = DocumentConverter().convert(str(docx_path))
    return result.document.export_to_markdown()


def _run_docling(
    docx_path: Path,
    md_path: Path,
    raw_img_dir: Path,
    *,
    convert_fn: Callable[[Path], str] | None = None,
) -> None:
    """Docling backend: markdown with real image refs + alt-text, into md_path.

    Mirrors :func:`_run_pandoc`'s contract — writes ``md_path`` with refs pointing
    into ``raw_img_dir`` and populates ``raw_img_dir`` with the extracted media —
    so the existing :func:`_normalize_images` pass runs unchanged afterwards.
    ``convert_fn`` is injectable for testing; production uses Docling.
    """
    if convert_fn is None:
        convert_fn = _default_docling_convert
    raw_markdown = convert_fn(docx_path)
    pics = _extract_docx_alt_text(docx_path)
    _extract_media(docx_path, raw_img_dir, {p["media"] for p in pics if p["media"]})
    md_path.write_text(_inject_image_refs(raw_markdown, pics, raw_img_dir.name), encoding="utf-8")


def _convert_emf_to_png(emf_path: Path, out_path: Path) -> bool:
    """Convert EMF/WMF to PNG via LibreOffice headless. Returns True on success."""
    tmp_dir = out_path.parent / "_lo_tmp"
    tmp_dir.mkdir(exist_ok=True)
    try:
        subprocess.run(
            [
                "soffice",
                "--headless",
                "--convert-to",
                "png",
                "--outdir",
                str(tmp_dir),
                str(emf_path),
            ],
            capture_output=True,
            check=True,
            timeout=30,
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


def _normalize_images(md_path: Path, raw_img_dir: Path, out_img_dir: Path) -> int:
    """
    Rename extracted images to NNN.png in document order, converting EMF/WMF to PNG.
    Updates image references in the markdown file in-place.
    Returns the number of images processed.
    """
    out_img_dir.mkdir(parents=True, exist_ok=True)
    text = md_path.read_text(encoding="utf-8")

    md_img_re = re.compile(r"(!\[[^\]]*\])\(([^)]+)\)")
    html_img_re = re.compile(
        r'<img\s[^>]*\bsrc="([^"]+)"[^>]*(?:alt="([^"]*)")?[^>]*/?>',
        re.IGNORECASE | re.DOTALL,
    )

    # Collect all image references in document order
    refs: list[tuple[int, int, str, str, str]] = []  # (start, end, full_match, src, alt)
    for m in md_img_re.finditer(text):
        alt = m.group(1)[2:-1]  # strip ![ and ]
        refs.append((m.start(), m.end(), m.group(0), m.group(2), alt))
    for m in html_img_re.finditer(text):
        alt = m.group(2) or ""
        refs.append((m.start(), m.end(), m.group(0), m.group(1), alt))
    refs.sort(key=lambda x: x[0])

    if not refs:
        if raw_img_dir.exists():
            shutil.rmtree(raw_img_dir)
        return 0

    replacements: list[tuple[str, str]] = []
    n_images = 0
    seq = 1
    for _, _, full_match, src_rel, alt in refs:
        src_path = md_path.parent / src_rel
        if not src_path.exists():
            src_path = Path(src_rel)
        if not src_path.exists():
            seq += 1
            continue

        suffix = src_path.suffix.lower()
        new_name = f"{seq:03d}.png"
        new_path = out_img_dir / new_name

        if suffix in EMF_FORMATS:
            ok = _convert_emf_to_png(src_path, new_path)
            if not ok:
                new_name = f"{seq:03d}{suffix}"
                new_path = out_img_dir / new_name
                shutil.copy2(src_path, new_path)
        else:
            shutil.copy2(src_path, new_path)

        # Reference is relative to the markdown file; out_img_dir is a sibling folder
        new_ref = f"{out_img_dir.name}/{new_name}"
        replacements.append((full_match, f"![{alt}]({new_ref})"))
        n_images += 1
        seq += 1

    for old, new in replacements:
        text = text.replace(old, new, 1)

    md_path.write_text(text, encoding="utf-8")

    if raw_img_dir.exists():
        shutil.rmtree(raw_img_dir)

    return n_images


def convert_docx(source_path: Path, out_img_dir: Path) -> tuple[str, int]:
    """
    Convert a DOCX file to raw GFM markdown.

    Pandoc is used by default; documents in :data:`DOCLING_DOCS` are routed to the
    Docling backend instead (see module docstring). Either way, images are
    extracted, converted (EMF/WMF → PNG if needed), and written to out_img_dir as
    001.png, 002.png, …  Image references in the returned markdown use paths
    relative to a sibling markdown file, e.g. 'stem/001.png'.

    Returns (markdown_text, n_images).
    Raises RuntimeError if the chosen backend fails.
    """
    backend = _select_backend(source_path)
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        md_path = tmp_path / "doc.md"
        raw_img_dir = tmp_path / "raw-images"

        if backend == "docling":
            logger.info("Using Docling backend for %s", source_path.name)
            _run_docling(source_path, md_path, raw_img_dir)
        else:
            _run_pandoc(source_path, md_path, raw_img_dir)
        n_images = _normalize_images(md_path, raw_img_dir, out_img_dir)
        text = md_path.read_text(encoding="utf-8")

    logger.info(
        "Converted %s via %s (%d chars, %d images)",
        source_path.name,
        backend,
        len(text),
        n_images,
    )
    return text, n_images
