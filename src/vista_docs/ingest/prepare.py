"""
Pure functions for assembling the final markdown output for an ingested document.

No I/O, no Docling dependency.
"""

from __future__ import annotations

from vista_docs.ingest.postprocess import (
    cap_heading_depth,
    format_callouts,
    strip_boilerplate,
    strip_outline_numbering,
    strip_toc,
)
from vista_docs.models.manifest import ManifestEntry


def make_frontmatter(entry: ManifestEntry) -> str:
    """
    Build a YAML frontmatter block for a ManifestEntry.

    Returns a string starting with '---\\n' and ending with '---'.
    Titles containing colons are double-quoted to produce valid YAML.
    """

    def _quote(value: str) -> str:
        """Quote the value if it contains a colon (YAML unsafe)."""
        if ":" in value:
            escaped = value.replace('"', '\\"')
            return f'"{escaped}"'
        return value

    lines = [
        "---",
        f"title: {_quote(entry.doc_title)}",
        f"doc_type: {entry.doc_type.value}",
        f"app_code: {entry.app_code}",
    ]
    if entry.patch:
        lines.append(f"patch: {entry.patch}")
    if entry.docx_url:
        lines.append(f"docx_url: {entry.docx_url}")
    if entry.pdf_url:
        lines.append(f"pdf_url: {entry.pdf_url}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def build_markdown(entry: ManifestEntry, raw_md: str) -> str:
    """
    Assemble the final markdown file: frontmatter + cleaned body.

    Applies the full postprocess pipeline to raw_md (which may be empty
    for scaffold mode).
    """
    frontmatter = make_frontmatter(entry)

    body = raw_md
    body = strip_toc(body)
    body = strip_outline_numbering(body)
    body = cap_heading_depth(body)
    body = format_callouts(body)
    body = strip_boilerplate(body)

    return frontmatter + "\n" + body
