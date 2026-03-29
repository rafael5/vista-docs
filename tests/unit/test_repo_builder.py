"""
Unit tests for migrate/repo_builder.py — repo layout, zensical.toml generation,
PROVENANCE.md generation, and README generation.

All tests use in-memory ManifestRecord objects; no filesystem I/O.
"""

from vista_docs.analyze.corpus_manifest import ManifestRecord
from vista_docs.migrate.repo_builder import (
    DocTypeNav,
    RepoLayout,
    build_repo_layout,
    generate_provenance_md,
    generate_readme,
    generate_zensical_toml,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _rec(
    *,
    package: str = "PSO",
    repo: str = "vista-pso",
    original_path: str = "originals/technical-manual/PSO_TM_pso_tm.md",
    original_sha256: str = "abc123" * 10 + "abcd",
    source_markdown_path: str = "/data/PSO/tm.md",
    doc_type: str = "technical-manual",
    doc_layer: str = "anchor",
    pub_date: str = "January 2022",
    patch_id: str = "",
    word_count: int = 10000,
    transformation: str = "standalone",
    consolidated_master: str = "",
    consolidated_role: str = "",
    migration_status: str = "pending",
) -> ManifestRecord:
    return ManifestRecord(
        package=package,
        repo=repo,
        original_path=original_path,
        original_sha256=original_sha256,
        source_markdown_path=source_markdown_path,
        doc_type=doc_type,
        doc_layer=doc_layer,
        pub_date=pub_date,
        patch_id=patch_id,
        word_count=word_count,
        transformation=transformation,
        consolidated_master=consolidated_master,
        consolidated_role=consolidated_role,
        migration_status=migration_status,
    )


def _pso_records() -> list[ManifestRecord]:
    """A realistic set of PSO records covering multiple doc types."""
    return [
        _rec(
            doc_type="technical-manual",
            transformation="consolidated-master",
            original_path="originals/technical-manual/PSO_TM_pso_tm.md",
        ),
        _rec(
            doc_type="installation-guide",
            transformation="consolidated-master",
            original_path="originals/installation-guide/PSO_IG_pso_ig.md",
            patch_id="PSO*7.0*507",
        ),
        _rec(
            doc_type="installation-guide",
            transformation="consolidated-addendum",
            original_path="originals/installation-guide/PSO_PSO_7_0_500_IG_older.md",
            patch_id="PSO*7.0*500",
        ),
        _rec(
            doc_type="release-note",
            transformation="release-note",
            original_path="originals/release-note/PSO_RN_rn1.md",
            patch_id="PSO*7.0*507",
        ),
        _rec(
            doc_type="release-note",
            transformation="release-note",
            original_path="originals/release-note/PSO_RN_rn2.md",
            patch_id="PSO*7.0*500",
        ),
        _rec(
            doc_type="user-manual",
            transformation="standalone",
            original_path="originals/user-manual/PSO_UM_pso_um.md",
        ),
        _rec(
            doc_type="change-page",
            transformation="change-page",
            original_path="originals/change-page/PSO_CP_cp1.md",
        ),
        _rec(
            doc_type="supplement",
            transformation="stub",
            original_path="originals/supplement/PSO_SUPP_stub.md",
        ),
    ]


# ---------------------------------------------------------------------------
# TestBuildRepoLayout
# ---------------------------------------------------------------------------


class TestBuildRepoLayout:
    def test_returns_repo_layout(self):
        layout = build_repo_layout("PSO", _pso_records())
        assert isinstance(layout, RepoLayout)

    def test_app_code_preserved(self):
        layout = build_repo_layout("PSO", _pso_records())
        assert layout.app_code == "PSO"

    def test_repo_name_derived(self):
        layout = build_repo_layout("PSO", _pso_records())
        assert layout.repo_name == "vista-pso"

    def test_total_originals_count(self):
        records = _pso_records()
        layout = build_repo_layout("PSO", records)
        assert layout.total_originals == len(records)

    def test_doc_types_detected(self):
        layout = build_repo_layout("PSO", _pso_records())
        types = {n.doc_type for n in layout.nav_entries}
        assert "technical-manual" in types
        assert "installation-guide" in types
        assert "release-note" in types
        assert "user-manual" in types

    def test_stubs_excluded_from_nav(self):
        layout = build_repo_layout("PSO", _pso_records())
        # supplement has only a stub record — should not appear in nav
        stub_nav = [n for n in layout.nav_entries if n.doc_type == "supplement"]
        assert stub_nav == []

    def test_change_pages_in_nav(self):
        layout = build_repo_layout("PSO", _pso_records())
        nav_types = {n.doc_type for n in layout.nav_entries}
        assert "change-page" in nav_types

    def test_originals_dir_paths_populated(self):
        layout = build_repo_layout("PSO", _pso_records())
        assert len(layout.originals_dirs) > 0
        for d in layout.originals_dirs:
            assert d.startswith("originals/")

    def test_single_record_package(self):
        records = [_rec(doc_type="technical-manual", transformation="standalone")]
        layout = build_repo_layout("ACKQ", records)
        assert layout.app_code == "ACKQ"
        assert layout.total_originals == 1


# ---------------------------------------------------------------------------
# TestDocTypeNav
# ---------------------------------------------------------------------------


class TestDocTypeNav:
    def test_dataclass_fields(self):
        nav = DocTypeNav(
            doc_type="technical-manual",
            label="Technical Manual",
            originals_dir="originals/technical-manual/",
            docs_dir="docs/technical-manual/",
            count=3,
        )
        assert nav.doc_type == "technical-manual"
        assert nav.label == "Technical Manual"
        assert nav.count == 3


# ---------------------------------------------------------------------------
# TestGenerateZensicalToml
# ---------------------------------------------------------------------------


class TestGenerateZensicalToml:
    def _layout(self) -> RepoLayout:
        return build_repo_layout("PSO", _pso_records())

    def test_returns_string(self):
        toml = generate_zensical_toml(self._layout())
        assert isinstance(toml, str)

    def test_contains_site_name(self):
        toml = generate_zensical_toml(self._layout())
        assert "PSO" in toml
        assert "site_name" in toml

    def test_contains_project_section(self):
        toml = generate_zensical_toml(self._layout())
        assert "[project]" in toml

    def test_contains_nav(self):
        toml = generate_zensical_toml(self._layout())
        assert "nav" in toml

    def test_contains_docs_dir(self):
        toml = generate_zensical_toml(self._layout())
        assert "docs_dir" in toml

    def test_contains_known_doc_types(self):
        toml = generate_zensical_toml(self._layout())
        # Should reference at least one doc type
        assert "technical-manual" in toml or "Technical Manual" in toml

    def test_ends_with_newline(self):
        toml = generate_zensical_toml(self._layout())
        assert toml.endswith("\n")

    def test_stubs_not_in_nav(self):
        toml = generate_zensical_toml(self._layout())
        assert "supplement" not in toml


# ---------------------------------------------------------------------------
# TestGenerateProvenanceMd
# ---------------------------------------------------------------------------


class TestGenerateProvenanceMd:
    def test_returns_string(self):
        md = generate_provenance_md("PSO", _pso_records())
        assert isinstance(md, str)

    def test_contains_package_name(self):
        md = generate_provenance_md("PSO", _pso_records())
        assert "PSO" in md

    def test_contains_total_count(self):
        records = _pso_records()
        md = generate_provenance_md("PSO", records)
        assert str(len(records)) in md

    def test_contains_original_paths(self):
        md = generate_provenance_md("PSO", _pso_records())
        assert "originals/technical-manual/" in md

    def test_contains_transformation_labels(self):
        md = generate_provenance_md("PSO", _pso_records())
        assert "consolidated-master" in md or "standalone" in md

    def test_contains_coverage_section(self):
        md = generate_provenance_md("PSO", _pso_records())
        assert "Coverage" in md or "coverage" in md

    def test_all_originals_listed(self):
        records = _pso_records()
        md = generate_provenance_md("PSO", records)
        for rec in records:
            filename = rec.original_path.split("/")[-1]
            assert filename in md

    def test_ends_with_newline(self):
        md = generate_provenance_md("PSO", _pso_records())
        assert md.endswith("\n")


# ---------------------------------------------------------------------------
# TestGenerateReadme
# ---------------------------------------------------------------------------


class TestGenerateReadme:
    def test_returns_string(self):
        layout = build_repo_layout("PSO", _pso_records())
        readme = generate_readme(layout)
        assert isinstance(readme, str)

    def test_contains_package_name(self):
        layout = build_repo_layout("PSO", _pso_records())
        readme = generate_readme(layout)
        assert "PSO" in readme

    def test_contains_doc_count(self):
        records = _pso_records()
        layout = build_repo_layout("PSO", records)
        readme = generate_readme(layout)
        assert str(len(records)) in readme

    def test_contains_originals_reference(self):
        layout = build_repo_layout("PSO", _pso_records())
        readme = generate_readme(layout)
        assert "originals" in readme

    def test_ends_with_newline(self):
        layout = build_repo_layout("PSO", _pso_records())
        readme = generate_readme(layout)
        assert readme.endswith("\n")
