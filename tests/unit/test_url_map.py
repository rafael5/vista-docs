"""
Unit tests for publish/url_map.py.

Three pure functions + one I/O wrapper:

  parse_patch_id(token)         — "DG*5.3*952 DIBRG" -> "DG*5.3*952"
  keys_from_frontmatter(fm)     — list of patch_id keys this entry contributes
  build_url_map(entries)        — pure: [(rel_path, frontmatter), ...] -> {patch_id: rel_path}
  walk_publish_tree(root)       — I/O: walks publish/, calls build_url_map

Drives remediation §5 (assessment §4 / 3.10).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from vista_docs.publish.url_map import (
    build_url_map,
    keys_from_frontmatter,
    parse_patch_id,
    walk_publish_tree,
)

# ---------------------------------------------------------------------------
# parse_patch_id
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "token,expected",
    [
        ("DG*5.3*952 DIBRG", "DG*5.3*952"),
        ("DG*5.3*1016 DIBRG", "DG*5.3*1016"),
        ("DG*5.3*952", "DG*5.3*952"),  # no doc-type suffix
        ("DG*5.3*554/TIU*1*184 DIBRG", "DG*5.3*554/TIU*1*184"),  # multi-NS
        (
            "Blind Rehab Version 5.1.3 Deployment, Installation, Back-out, Rollback Guide",
            # Falls back to first whitespace token; loader treats as no-match downstream.
            "Blind",
        ),
        ("", ""),
        ("   ", ""),
    ],
)
def test_parse_patch_id(token: str, expected: str) -> None:
    assert parse_patch_id(token) == expected


# ---------------------------------------------------------------------------
# keys_from_frontmatter
# ---------------------------------------------------------------------------


def test_keys_from_frontmatter_anchor_consolidated() -> None:
    """Anchor frontmatter contributes master_source + every prior_versions entry."""
    fm = {
        "consolidated_title": "dibrg",
        "app_code": "ADT",
        "doc_type": "DIBR",
        "master_source": "DG*5.3*952 DIBRG",
        "prior_versions": [
            "DG*5.3*916 DIBRG",
            "DG*5.3*1016 DIBRG",
        ],
    }
    keys = keys_from_frontmatter(fm)
    assert set(keys) == {"DG*5.3*952", "DG*5.3*916", "DG*5.3*1016"}


def test_keys_from_frontmatter_anchor_with_no_prior_versions() -> None:
    fm = {"master_source": "DG*5.3*952 DIBRG", "prior_versions": []}
    assert keys_from_frontmatter(fm) == ["DG*5.3*952"]


def test_keys_from_frontmatter_plain_singleton_with_patch_id() -> None:
    """Plain singleton (mirrored from md-img) contributes its own patch_id."""
    fm = {
        "title": "PIMS Version 5.3 Installation Guide",
        "doc_type": "IG",
        "doc_layer": "anchor",
        "patch_id": "ADT*5.3",
        "app_code": "ADT",
    }
    assert keys_from_frontmatter(fm) == ["ADT*5.3"]


def test_keys_from_frontmatter_patch_layer() -> None:
    """Per-patch file under patches/ contributes its patch_id."""
    fm = {
        "title": "DG*5.3*864 USH PRF Legal Solution Installation Guide",
        "doc_layer": "patch",
        "patch_id": "DG*5.3*864",
    }
    assert keys_from_frontmatter(fm) == ["DG*5.3*864"]


def test_keys_from_frontmatter_anchor_takes_precedence_over_patch_id() -> None:
    """If both master_source and patch_id are present (shouldn't happen, but
    be defensive), prefer the anchor's master_source + prior_versions list."""
    fm = {
        "master_source": "DG*5.3*952 DIBRG",
        "prior_versions": ["DG*5.3*916 DIBRG"],
        "patch_id": "DG*5.3*999",  # noise — should be ignored
    }
    keys = keys_from_frontmatter(fm)
    assert set(keys) == {"DG*5.3*952", "DG*5.3*916"}


def test_keys_from_frontmatter_empty_returns_empty_list() -> None:
    assert keys_from_frontmatter({}) == []


def test_keys_from_frontmatter_blank_patch_id_returns_empty() -> None:
    assert keys_from_frontmatter({"patch_id": ""}) == []


def test_keys_from_frontmatter_plain_includes_source_urls() -> None:
    """Non-anchor entries contribute pdf_url and docx_url as precise keys.

    Without these, the patch_id alone collides for plain singletons that
    share an anchor-style identifier (e.g. all PIMS V5.3 docs share
    patch_id 'ADT*5.3').
    """
    fm = {
        "patch_id": "ADT*5.3",
        "pdf_url": "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/pimsig.pdf",
        "docx_url": "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/pimsig.docx",
    }
    keys = keys_from_frontmatter(fm)
    assert "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/pimsig.pdf" in keys
    assert "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/pimsig.docx" in keys
    assert "ADT*5.3" in keys


def test_keys_from_frontmatter_anchor_skips_url_fields() -> None:
    """Anchor entries do not have pdf_url/docx_url (consolidated from many
    sources). Even if a stray field appears, only patch_ids are emitted."""
    fm = {
        "master_source": "DG*5.3*952 DIBRG",
        "prior_versions": [],
        "pdf_url": "https://example/should-not-be-emitted.pdf",
    }
    keys = keys_from_frontmatter(fm)
    assert keys == ["DG*5.3*952"]


def test_build_url_map_plain_with_url_keys_resolves_each_url() -> None:
    """Two distinct plain docs sharing patch_id resolve via their pdf_urls."""
    pdf_a = "https://www.va.gov/vdl/x/a.pdf"
    pdf_b = "https://www.va.gov/vdl/x/b.pdf"
    entries = [
        ("clinical/x/a.md", {"patch_id": "X*5.3", "pdf_url": pdf_a}),
        ("clinical/x/b.md", {"patch_id": "X*5.3", "pdf_url": pdf_b}),
    ]
    url_map = build_url_map(entries)
    assert url_map[pdf_a] == "clinical/x/a.md"
    assert url_map[pdf_b] == "clinical/x/b.md"
    # patch_id collides — last wins; downstream callers must prefer URL key first
    assert url_map["X*5.3"] in {"clinical/x/a.md", "clinical/x/b.md"}


# ---------------------------------------------------------------------------
# build_url_map (pure)
# ---------------------------------------------------------------------------


def test_build_url_map_anchor_creates_many_to_one() -> None:
    entries = [
        (
            "clinical/adt--admission-discharge-transfer/dibrg.md",
            {
                "master_source": "DG*5.3*952 DIBRG",
                "prior_versions": ["DG*5.3*916 DIBRG", "DG*5.3*1016 DIBRG"],
            },
        ),
    ]
    url_map = build_url_map(entries)
    assert url_map == {
        "DG*5.3*952": "clinical/adt--admission-discharge-transfer/dibrg.md",
        "DG*5.3*916": "clinical/adt--admission-discharge-transfer/dibrg.md",
        "DG*5.3*1016": "clinical/adt--admission-discharge-transfer/dibrg.md",
    }


def test_build_url_map_mixed_entry_types() -> None:
    entries = [
        (
            "clinical/adt--admission-discharge-transfer/dibrg.md",
            {"master_source": "DG*5.3*952 DIBRG", "prior_versions": []},
        ),
        (
            "clinical/adt--admission-discharge-transfer/installation-guide.md",
            {"patch_id": "ADT*5.3"},
        ),
        (
            "clinical/adt--admission-discharge-transfer/patches/dg-5-3-864--installation-guide.md",
            {"patch_id": "DG*5.3*864"},
        ),
    ]
    url_map = build_url_map(entries)
    assert url_map["DG*5.3*952"].endswith("dibrg.md")
    assert url_map["ADT*5.3"].endswith("installation-guide.md")
    assert url_map["DG*5.3*864"].endswith("patches/dg-5-3-864--installation-guide.md")


def test_build_url_map_skips_entries_with_no_keys() -> None:
    entries = [
        ("clinical/foo/bar.md", {"some_other_field": "x"}),
        ("clinical/foo/baz.md", {"patch_id": "DG*5.3*1"}),
    ]
    assert build_url_map(entries) == {"DG*5.3*1": "clinical/foo/baz.md"}


def test_build_url_map_last_writer_wins_on_collision() -> None:
    """If two .md files claim the same patch_id (shouldn't happen on a
    well-formed publish/), the later entry overwrites. Document this."""
    entries = [
        ("a.md", {"patch_id": "X*1*1"}),
        ("b.md", {"patch_id": "X*1*1"}),
    ]
    assert build_url_map(entries)["X*1*1"] == "b.md"


# ---------------------------------------------------------------------------
# walk_publish_tree (I/O thin layer)
# ---------------------------------------------------------------------------


def test_walk_publish_tree_against_fixture(tmp_path: Path) -> None:
    """End-to-end: build a tiny publish/ tree in tmp_path and verify the map."""
    pkg = tmp_path / "clinical" / "adt--admission-discharge-transfer"
    pkg.mkdir(parents=True)
    (pkg / "dibrg.md").write_text(
        "---\n"
        'master_source: "DG*5.3*952 DIBRG"\n'
        "prior_versions:\n"
        '  - "DG*5.3*916 DIBRG"\n'
        "---\n"
        "body\n",
        encoding="utf-8",
    )
    (pkg / "installation-guide.md").write_text(
        "---\npatch_id: ADT*5.3\n---\nbody\n",
        encoding="utf-8",
    )
    patches = pkg / "patches"
    patches.mkdir()
    (patches / "dg-5-3-864--installation-guide.md").write_text(
        "---\npatch_id: DG*5.3*864\n---\nbody\n",
        encoding="utf-8",
    )

    # Top-level boilerplate that should be skipped
    (tmp_path / "INDEX.md").write_text("# index\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("# readme\n", encoding="utf-8")

    url_map = walk_publish_tree(tmp_path)

    assert url_map["DG*5.3*952"] == "clinical/adt--admission-discharge-transfer/dibrg.md"
    assert url_map["DG*5.3*916"] == "clinical/adt--admission-discharge-transfer/dibrg.md"
    assert url_map["ADT*5.3"] == "clinical/adt--admission-discharge-transfer/installation-guide.md"
    assert (
        url_map["DG*5.3*864"]
        == "clinical/adt--admission-discharge-transfer/patches/dg-5-3-864--installation-guide.md"
    )
    # INDEX.md / README.md must not appear as values
    assert all(not v.endswith("INDEX.md") for v in url_map.values())
    assert all(not v.endswith("README.md") for v in url_map.values())
