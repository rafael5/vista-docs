"""
Pure functions for assembling the final markdown output for an ingested document.

No I/O, no external dependencies.
"""

from __future__ import annotations

from vista_docs.ingest.postprocess import (
    cap_heading_depth,
    compact_lists,
    compact_reference_sections,
    format_callouts,
    insert_back_links,
    insert_toc,
    link_figure_captions,
    normalize_whitespace,
    strip_artifacts,
    strip_back_links,
    strip_boilerplate,
    strip_outline_numbering,
    strip_word_toc,
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

    Pipeline order:
      1. Strip Word artifacts and reset idempotent markers
      2. Link figure captions, strip Word TOC
      3. Heading normalisation (outline numbers, depth cap, callouts, boilerplate)
      4. Whitespace normalisation
      5. Prepend frontmatter, then insert generated TOC + back-links
      6. Compact lists and reference sections
    """
    frontmatter = make_frontmatter(entry)

    body = raw_md
    body = strip_artifacts(body)
    body = strip_back_links(body)
    body = link_figure_captions(body)
    body = strip_word_toc(body)
    body = strip_outline_numbering(body)
    body = cap_heading_depth(body)
    body = format_callouts(body)
    body = strip_boilerplate(body)
    body = normalize_whitespace(body)

    full_text = frontmatter + "\n" + body
    full_text = insert_toc(full_text)
    full_text = insert_back_links(full_text)
    full_text = compact_lists(full_text)
    full_text = compact_reference_sections(full_text)

    return full_text
