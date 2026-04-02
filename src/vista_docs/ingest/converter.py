"""I/O thin layer: DOCX → raw GFM markdown string + images via Pandoc."""

from __future__ import annotations

import logging
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

logger = logging.getLogger(__name__)

EMF_FORMATS = {".emf", ".wmf"}


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
    Convert a DOCX file to raw GFM markdown using Pandoc.

    Images are extracted, converted (EMF/WMF → PNG if needed), and written to
    out_img_dir as 001.png, 002.png, …  Image references in the returned
    markdown use paths relative to a sibling markdown file, e.g. 'stem/001.png'.

    Returns (markdown_text, n_images).
    Raises RuntimeError if pandoc fails.
    """
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        md_path = tmp_path / "doc.md"
        raw_img_dir = tmp_path / "raw-images"

        _run_pandoc(source_path, md_path, raw_img_dir)
        n_images = _normalize_images(md_path, raw_img_dir, out_img_dir)
        text = md_path.read_text(encoding="utf-8")

    logger.info("Converted %s (%d chars, %d images)", source_path.name, len(text), n_images)
    return text, n_images
