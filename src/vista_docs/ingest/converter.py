"""I/O thin layer: DOCX/PDF → raw markdown string via Docling."""
from __future__ import annotations

import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def convert_to_markdown(source_path: Path) -> str:
    """
    Convert a DOCX or PDF file to a raw markdown string using Docling.

    Raises ImportError if docling is not installed.
    Raises ValueError if the file cannot be converted.
    """
    try:
        from docling.document_converter import DocumentConverter
    except ImportError as exc:
        raise ImportError(
            "docling is not installed. Install it with: pip install docling\n"
            "Or use --scaffold mode to generate frontmatter stubs without conversion."
        ) from exc

    converter = DocumentConverter()
    result = converter.convert(str(source_path))
    md = result.document.export_to_markdown()
    logger.info("Converted %s (%d chars)", source_path.name, len(md))
    return md
