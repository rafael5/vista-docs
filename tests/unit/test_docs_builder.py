"""
Unit tests for migrate/docs_builder.py — docs entry classification,
destination path derivation, and filtering of stubs/addenda.

All tests use in-memory ManifestRecord objects; no filesystem I/O.
"""

from vista_docs.analyze.corpus_manifest import ManifestRecord
from vista_docs.migrate.docs_builder import (
    DocsEntry,
    build_docs_entries,
    consolidated_group_title,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _rec(
    *,
    package: str = "PSO",
    doc_type: str = "technical-manual",
    original_path: str = "originals/technical-manual/PSO_TM_tm.md",
    transformation: str = "standalone",
    consolidated_master: str = "",
    consolidated_role: str = "",
    pub_date: str = "January 2022",
    patch_id: str = "",
    word_count: int = 5000,
) -> ManifestRecord:
    return ManifestRecord(
        package=package,
        repo=f"vista-{package.lower()}",
        original_path=original_path,
        original_sha256="a" * 64,
        source_markdown_path=f"/data/{package}/doc.md",
        doc_type=doc_type,
        doc_layer="plain",
        pub_date=pub_date,
        patch_id=patch_id,
        word_count=word_count,
        transformation=transformation,
        consolidated_master=consolidated_master,
        consolidated_role=consolidated_role,
    )


def _pso_records() -> list[ManifestRecord]:
    return [
        # consolidated-master
        _rec(
            doc_type="technical-manual",
            original_path="originals/technical-manual/PSO_TM_tm.md",
            transformation="consolidated-master",
            consolidated_master="docs/technical-manual/pso technical manual.md",
            consolidated_role="master",
        ),
        # consolidated-addendum — should be excluded from docs/
        _rec(
            doc_type="technical-manual",
            original_path="originals/technical-manual/PSO_TM_old_tm.md",
            transformation="consolidated-addendum",
            consolidated_master="docs/technical-manual/pso technical manual.md",
            consolidated_role="addendum",
        ),
        # standalone
        _rec(
            doc_type="user-manual",
            original_path="originals/user-manual/PSO_UM_um.md",
            transformation="standalone",
        ),
        # release-note
        _rec(
            doc_type="release-note",
            original_path="originals/release-note/PSO_RN_507.md",
            transformation="release-note",
            patch_id="PSO*7.0*507",
        ),
        # change-page
        _rec(
            doc_type="change-page",
            original_path="originals/change-page/PSO_CP_cp1.md",
            transformation="change-page",
        ),
        # stub — should be excluded from docs/
        _rec(
            doc_type="supplement",
            original_path="originals/supplement/PSO_SUPP_stub.md",
            transformation="stub",
        ),
    ]


# ---------------------------------------------------------------------------
# TestConsolidatedGroupTitle
# ---------------------------------------------------------------------------


class TestConsolidatedGroupTitle:
    def test_extracts_title_from_path(self):
        path = "docs/technical-manual/pso technical manual.md"
        assert consolidated_group_title(path) == "pso technical manual"

    def test_installation_guide(self):
        path = "docs/installation-guide/inbound eprescribing installation guide.md"
        assert consolidated_group_title(path) == "inbound eprescribing installation guide"

    def test_empty_string(self):
        assert consolidated_group_title("") == ""

    def test_deeply_nested(self):
        path = "docs/user-manual/some title here.md"
        assert consolidated_group_title(path) == "some title here"


# ---------------------------------------------------------------------------
# TestBuildDocsEntries
# ---------------------------------------------------------------------------


class TestBuildDocsEntries:
    def test_returns_list(self):
        entries = build_docs_entries(_pso_records())
        assert isinstance(entries, list)

    def test_stubs_excluded(self):
        entries = build_docs_entries(_pso_records())
        paths = [e.docs_path for e in entries]
        assert not any("supplement" in p for p in paths)

    def test_addenda_excluded(self):
        entries = build_docs_entries(_pso_records())
        # Addendum original_path should not appear
        paths = [e.original_path for e in entries]
        assert "originals/technical-manual/PSO_TM_old_tm.md" not in paths

    def test_consolidated_master_included(self):
        entries = build_docs_entries(_pso_records())
        sources = {e.source for e in entries}
        assert "consolidated" in sources

    def test_standalone_uses_original_source(self):
        entries = build_docs_entries(_pso_records())
        um = next(e for e in entries if e.doc_type == "user-manual")
        assert um.source == "original"

    def test_release_note_uses_original_source(self):
        entries = build_docs_entries(_pso_records())
        rn = next(e for e in entries if e.doc_type == "release-note")
        assert rn.source == "original"

    def test_change_page_uses_original_source(self):
        entries = build_docs_entries(_pso_records())
        cp = next(e for e in entries if e.doc_type == "change-page")
        assert cp.source == "original"

    def test_consolidated_master_docs_path(self):
        entries = build_docs_entries(_pso_records())
        tm = next(e for e in entries if e.transformation == "consolidated-master")
        assert tm.docs_path.startswith("docs/technical-manual/")
        assert tm.docs_path.endswith(".md")

    def test_standalone_docs_path_in_correct_dir(self):
        entries = build_docs_entries(_pso_records())
        um = next(e for e in entries if e.doc_type == "user-manual")
        assert um.docs_path.startswith("docs/user-manual/")

    def test_release_note_in_release_note_dir(self):
        entries = build_docs_entries(_pso_records())
        rn = next(e for e in entries if e.doc_type == "release-note")
        assert rn.docs_path.startswith("docs/release-note/")

    def test_consolidated_group_title_preserved(self):
        entries = build_docs_entries(_pso_records())
        tm = next(e for e in entries if e.transformation == "consolidated-master")
        assert tm.consolidated_title == "pso technical manual"

    def test_all_entries_are_docs_entry(self):
        entries = build_docs_entries(_pso_records())
        assert all(isinstance(e, DocsEntry) for e in entries)

    def test_correct_count(self):
        # 6 records: 1 master, 1 addendum(skip), 1 standalone, 1 rn, 1 cp, 1 stub(skip)
        entries = build_docs_entries(_pso_records())
        assert len(entries) == 4

    def test_app_code_preserved(self):
        entries = build_docs_entries(_pso_records())
        assert all(e.app_code == "PSO" for e in entries)

    def test_docs_path_ends_with_md(self):
        entries = build_docs_entries(_pso_records())
        assert all(e.docs_path.endswith(".md") for e in entries)

    def test_empty_records(self):
        assert build_docs_entries([]) == []

    def test_only_stubs_returns_empty(self):
        records = [_rec(transformation="stub")]
        assert build_docs_entries(records) == []
