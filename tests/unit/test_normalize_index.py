"""Unit tests for the corpus anchor index (spec §11.5)."""

from vista_docs.normalize.index_pure import anchor_index_entry, build_anchor_index


def test_entry_has_headings_slugs_and_aliases():
    body = "# Ordering <u>Medications</u>\n\ntext\n\n## Simple Dose\n"
    entry = anchor_index_entry("cprs/um/x.md", body, {"_Toc1": "ordering-medications"})
    assert entry["doc"] == "cprs/um/x.md"
    assert entry["slugs"] == ["ordering-medications", "simple-dose"]
    assert entry["headings"][0] == {
        "level": 1,
        "text": "Ordering Medications",  # html stripped for display
        "slug": "ordering-medications",
    }
    assert entry["aliases"] == {"_Toc1": "ordering-medications"}


def test_entry_empty_aliases_default():
    entry = anchor_index_entry("a/b.md", "# Title\n")
    assert entry["aliases"] == {}
    assert entry["slugs"] == ["title"]


def test_build_index_keyed_by_doc():
    e1 = anchor_index_entry("a.md", "# A\n")
    e2 = anchor_index_entry("b.md", "# B\n")
    idx = build_anchor_index([e1, e2])
    assert set(idx) == {"a.md", "b.md"}
    assert idx["a.md"]["slugs"] == ["a"]
    assert "doc" not in idx["a.md"]  # key is the doc; value drops the redundant field
