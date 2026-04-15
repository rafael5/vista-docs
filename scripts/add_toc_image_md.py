"""
Add a linkable Table of Contents at the top of each markdown file in
~/data/vista-docs/markdown-image/ackq/, based on the headings in the document.
Also inserts a "back to TOC" link beneath every h2 chapter heading in the body.

TOC depth: headings up to level 3 (###) only — deeper levels are omitted
to keep the TOC readable in documents with 100+ headings.

Anchor generation follows GitHub Flavored Markdown rules:
  1. Decode HTML entities
  2. Strip inline markup
  3. Lowercase
  4. Replace spaces with hyphens
  5. Remove characters other than alphanumeric and hyphens
  6. Deduplicate: second occurrence → -1, third → -2, etc.
"""

import html
import re
from pathlib import Path

MD_DIR = Path("/home/rafael/data/vista-docs/markdown-image/ackq")
TOC_MAX_DEPTH = 3  # include h1, h2, h3 — skip h4+
TOC_PLAIN_OPEN = "<!-- toc-plain -->"  # legacy — stripped for idempotency
TOC_PLAIN_CLOSE = "<!-- /toc-plain -->"
TOC_OPEN = "<!-- toc -->"  # legacy — stripped for idempotency
TOC_CLOSE = "<!-- /toc -->"
TOC_TABLE_OPEN = "<!-- toc-table -->"
TOC_TABLE_CLOSE = "<!-- /toc-table -->"
BACK_LINK = "[↑ Table of Contents](#table-of-contents)"
BACK_MARKER = "<!-- back-to-toc -->"


def gfm_anchor(text: str, seen: dict[str, int]) -> str:
    """Generate a GitHub-Flavored Markdown anchor from heading text."""
    # decode HTML entities: &amp; → &, &gt; → >, etc.
    text = html.unescape(text)
    # strip inline markdown: `code`, **bold**, _italic_, [link](url)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # links
    text = re.sub(r"[`*_~]", "", text)  # emphasis markers
    # lowercase
    text = text.lower()
    # replace spaces and non-alphanumeric (except hyphens) with hyphens
    text = re.sub(r"[^\w\s-]", "", text)  # remove punctuation (keep word chars, spaces, -)
    text = re.sub(r"[\s]+", "-", text)  # spaces → hyphens
    text = re.sub(r"-+", "-", text)  # collapse multiple hyphens
    text = text.strip("-")

    if not text:
        return ""

    # deduplicate: if already seen, append counter
    base = text
    count = seen.get(base, 0)
    seen[base] = count + 1
    if count == 0:
        return base
    # second occurrence gets -1 suffix, matching GFM behaviour
    return f"{base}-{count}"


def build_linked_toc(lines: list[str]) -> str:
    """Build the hyperlinked TOC as a markdown list under a ## heading."""
    entries = []
    seen: dict[str, int] = {}

    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if not m:
            continue
        level = len(m.group(1))
        if level > TOC_MAX_DEPTH:
            continue
        raw_text = m.group(2).strip()
        if not raw_text:
            continue

        anchor = gfm_anchor(raw_text, seen)
        if not anchor:
            continue

        display = html.unescape(raw_text)
        display = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", display)
        display = re.sub(r"[`*_~]", "", display).strip()

        indent = "  " * (level - 1)
        entries.append(f"{indent}- [{display}](#{anchor})")

    if not entries:
        return ""

    return "## Table of Contents\n\n" + "\n".join(entries)


def build_plain_toc(lines: list[str]) -> str:
    """Build a plain-text (non-hyperlinked) TOC in a ```text code block."""
    entries = []

    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if not m:
            continue
        level = len(m.group(1))
        if level > TOC_MAX_DEPTH:
            continue
        raw_text = m.group(2).strip()
        if not raw_text:
            continue

        display = html.unescape(raw_text)
        display = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", display)
        display = re.sub(r"[`*_~]", "", display).strip()

        indent = "  " * (level - 1)
        entries.append(f"{indent}{display}")

    if not entries:
        return ""

    return "```text\n" + "\n".join(entries) + "\n```"


def insert_back_links(lines: list[str]) -> tuple[list[str], int]:
    """Insert a back-to-TOC link after every h2 heading, except the TOC heading itself.
    Returns the modified line list and a count of links inserted."""
    out: list[str] = []
    n_inserted = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)

        if re.match(r"^#{2,3} ", line):
            heading_text = re.sub(r"^#+\s+", "", line).strip()
            # skip the TOC section itself and any empty headings
            if heading_text and heading_text != "Table of Contents":
                # absorb any blank lines that immediately follow the heading
                i += 1
                while i < len(lines) and not lines[i].strip():
                    out.append(lines[i])
                    i += 1
                # insert the back link (with its own blank line after)
                out.append(BACK_MARKER + BACK_LINK)
                out.append("")
                n_inserted += 1
                continue  # don't increment i again

        i += 1
    return out, n_inserted


def strip_back_links(lines: list[str]) -> list[str]:
    """Remove previously inserted back-to-TOC lines (idempotent)."""
    return [line for line in lines if not line.startswith(BACK_MARKER)]


def strip_body_toc_section(lines: list[str]) -> list[str]:
    """Remove any '## Table of Contents' section from the document body.

    Docling extracts the original document's TOC as a heading + list block.
    We replace that with our generated linkable TOC, so the original must be
    removed. Strips from '## Table of Contents' up to (but not including) the
    next ## heading or end of file.
    """
    out: list[str] = []
    i = 0
    while i < len(lines):
        if re.match(r"^## Table of Contents\s*$", lines[i]):
            # skip this heading and everything until the next ## heading
            i += 1
            while i < len(lines) and not re.match(r"^## ", lines[i]):
                i += 1
            # drop any trailing blank lines before the next section
            while out and not out[-1].strip():
                out.pop()
        else:
            out.append(lines[i])
            i += 1
    return out


def process_file(md_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    def strip_marked_block(t: str, open_mark: str, close_mark: str) -> str:
        if open_mark not in t:
            return t
        start = t.index(open_mark)
        if close_mark in t:
            end = t.index(close_mark) + len(close_mark)
        else:
            end = t.find("\n#", start + len(open_mark))
            if end == -1:
                end = len(t)
        return t[:start].rstrip("\n") + "\n\n" + t[end:].lstrip("\n")

    # --- idempotent: strip all TOC block variants (current and legacy) ---
    text = strip_marked_block(text, TOC_TABLE_OPEN, TOC_TABLE_CLOSE)
    text = strip_marked_block(text, TOC_PLAIN_OPEN, TOC_PLAIN_CLOSE)
    text = strip_marked_block(text, TOC_OPEN, TOC_CLOSE)
    lines = text.splitlines()

    # --- idempotent: strip previously inserted back links ---
    lines = strip_back_links(lines)

    # --- strip original Docling-extracted TOC section from body ---
    lines = strip_body_toc_section(lines)

    linked_toc = build_linked_toc(lines)
    plain_toc = build_plain_toc(lines)
    if not linked_toc:
        print(f"  no headings found: {md_path.name}")
        return

    n_toc = sum(1 for line in linked_toc.splitlines() if re.match(r"\s*- \[", line))

    # --- insert back-to-TOC links after every h2 in the body ---
    lines, n_back = insert_back_links(lines)

    # --- build block: linked TOC first, plain text TOC below ---
    toc_block = (
        TOC_OPEN
        + "\n"
        + linked_toc
        + "\n\n"
        + TOC_CLOSE
        + "\n\n"
        + TOC_PLAIN_OPEN
        + "\n"
        + plain_toc
        + "\n"
        + TOC_PLAIN_CLOSE
    )

    # --- insert after the document title (h1) ---
    if lines and re.match(r"^# ", lines[0]):
        insert_at = 1
        while insert_at < len(lines) and re.match(r"^# ", lines[insert_at]):
            insert_at += 1
        while insert_at < len(lines) and not lines[insert_at].strip():
            insert_at += 1
        before = "\n".join(lines[:insert_at])
        after = "\n".join(lines[insert_at:])
        new_text = before + "\n\n" + toc_block + "\n\n" + after
    else:
        new_text = toc_block + "\n\n" + "\n".join(lines)

    md_path.write_text(new_text, encoding="utf-8")
    print(f"  {md_path.name}: {n_toc} TOC entries, {n_back} back links")


def main() -> None:
    md_files = sorted(MD_DIR.glob("*.md"))
    print(f"processing {len(md_files)} markdown files in {MD_DIR}\n")
    for md_path in md_files:
        process_file(md_path)
    print("\ndone.")


if __name__ == "__main__":
    main()
