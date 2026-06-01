"""Unit tests for original-TOC removal (spec §6 F6 — regenerate, don't keep)."""

from vista_docs.normalize.toc_pure import remove_caption_toc, remove_original_toc


def test_removes_toc_block_pointing_at_headings():
    body = (
        "Title\n\n"
        "- [Overview](#overview)\n"
        "- [Setup](#setup)\n"
        "  - [Install](#install)\n"
        "- [Usage](#usage)\n"
        "- [Notes](#notes)\n"
        "- [Bogus](#does-not-exist)\n\n"
        "# Overview\n\nx\n\n# Setup\n\n## Install\n\n# Usage\n\n# Notes\n"
    )
    out, n = remove_original_toc(body)
    assert n == 6
    assert "- [Overview](#overview)" not in out
    assert "# Overview" in out and "## Install" in out  # headings kept


def test_removes_toc_with_malformed_bracketed_item():
    # The real psn shape: a TOC item whose text holds an image + prose (with a ]).
    body = (
        "- [Overview](#overview)\n"
        "- [Setup](#setup)\n"
        "- [Install](#install)\n"
        "- [Usage](#usage)\n"
        "- [Notes](#notes)\n"
        "- [> ![](dir/007.png)See the patch note.](#dir-007-png-see-the-patch-note)\n\n"
        "# Overview\n\n# Setup\n\n# Install\n\n# Usage\n\n# Notes\n"
    )
    out, n = remove_original_toc(body)
    assert n == 6
    assert "007.png" not in out
    assert "](#dir-007-png-see-the-patch-note)" not in out


def test_keeps_short_link_list():
    body = "See:\n\n- [a](#x)\n- [b](#y)\n\ntext\n"
    assert remove_original_toc(body) == (body, 0)


def test_keeps_link_list_not_pointing_at_headings():
    body = "Links:\n\n" + "\n".join(f"- [L{i}](#ext-{i})" for i in range(8)) + "\n\ntext\n"
    out, n = remove_original_toc(body)
    assert n == 0  # 8 items but none resolve to a heading → not a TOC


def test_strips_preceding_contents_caption():
    body = (
        "Contents\n\n"
        + "\n".join(f"- [S{i}](#s{i})" for i in range(6))
        + "\n\n"
        + "".join(f"# S{i}\n\n" for i in range(6))
    )
    out, n = remove_original_toc(body)
    assert n == 6
    assert "Contents" not in out.split("#", 1)[0]  # caption removed above headings


# --- Docling caption-TOC form: '#######... Table of Contents' + 'Entry<TAB>page'

DOCLING_TOC = (
    "Title page\n\n"
    "########### Table of Contents\n\n"
    "Introduction\t1\n"
    "What is CPRS?\t1\n"
    "Using CPRS Documentation\t1\n"
    "Related Manuals\t1\n"
    "VistA Intranet\t1\n"
    "Online Help\t2\n\n"
    "# Introduction\n\nreal body\n"
)


def test_removes_docling_caption_toc():
    out, n = remove_caption_toc(DOCLING_TOC)
    assert n == 6
    assert "Table of Contents" not in out
    assert "###########" not in out
    assert "Introduction\t1" not in out
    assert "# Introduction" in out and "real body" in out  # body kept


def test_caption_toc_keeps_short_runs():
    # Fewer than min_items tabbed lines under a caption → not a TOC, leave it.
    body = "## Contents\n\nA\t1\nB\t2\n\n# Real\n"
    assert remove_caption_toc(body) == (body, 0)


def test_caption_toc_requires_caption():
    # Tabbed 'text<TAB>num' lines with NO 'Contents' caption are left untouched.
    body = "Data\n\n" + "".join(f"Row {i}\t{i}\n" for i in range(8)) + "\n# Real\n"
    assert remove_caption_toc(body) == (body, 0)
