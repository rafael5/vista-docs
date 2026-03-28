"""
Unit tests for analyze/corpus_manifest.py — filename generation, transformation
determination, SHA-256 hashing, and manifest assembly.

All tests use in-memory strings and DocumentRecord objects; no filesystem I/O.
"""

import hashlib

from vista_docs.analyze.consolidate import DocumentRecord
from vista_docs.analyze.corpus_manifest import (
    CorpusManifest,
    ManifestRecord,
    _safe_patch_id,
    _sha256,
    _title_slug,
    build_manifest,
    original_filename,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _doc(
    title: str = "A Document",
    *,
    path: str = "/fake/doc.md",
    doc_type: str = "technical-manual",
    app_code: str = "PSO",
    word_count: int = 1000,
    pub_date: str = "January 2020",
    doc_layer: str = "plain",
    patch_id: str = "",
    is_stub: bool = False,
    text: str = "some content",
) -> DocumentRecord:
    return DocumentRecord(
        path=path,
        title=title,
        doc_type=doc_type,
        app_code=app_code,
        word_count=word_count,
        pub_date=pub_date,
        doc_layer=doc_layer,
        patch_id=patch_id,
        is_stub=is_stub,
        text=text,
    )


# ---------------------------------------------------------------------------
# TestSafePatchId
# ---------------------------------------------------------------------------


class TestSafePatchId:
    def test_standard_patch_id(self):
        assert _safe_patch_id("PSO*7.0*507") == "PSO_7_0_507"

    def test_integer_version(self):
        assert _safe_patch_id("PSJ*5*423") == "PSJ_5_423"

    def test_empty_string(self):
        assert _safe_patch_id("") == ""

    def test_leading_trailing_underscores_stripped(self):
        result = _safe_patch_id("*PSO*")
        assert not result.startswith("_")
        assert not result.endswith("_")

    def test_alphanumeric_preserved(self):
        assert _safe_patch_id("DG53") == "DG53"


# ---------------------------------------------------------------------------
# TestTitleSlug
# ---------------------------------------------------------------------------


class TestTitleSlug:
    def test_lowercase(self):
        assert _title_slug("PSO Technical Manual") == "pso_technical_manual"

    def test_special_chars_replaced(self):
        slug = _title_slug("Kernel 8.0: Systems Management")
        assert ":" not in slug
        assert "/" not in slug

    def test_truncated_at_40_chars(self):
        long_title = "A" * 60
        assert len(_title_slug(long_title)) <= 40

    def test_empty_string(self):
        assert _title_slug("") == ""

    def test_leading_trailing_underscores_stripped(self):
        result = _title_slug("  Hello World  ")
        assert not result.startswith("_")
        assert not result.endswith("_")


# ---------------------------------------------------------------------------
# TestOriginalFilename
# ---------------------------------------------------------------------------


class TestOriginalFilename:
    def test_with_patch_id(self):
        doc = _doc(
            "Outpatient Pharmacy Installation Guide",
            doc_type="installation-guide",
            app_code="PSO",
            patch_id="PSO*7.0*507",
        )
        name = original_filename(doc)
        assert name.startswith("PSO_PSO_7_0_507_IG_")
        assert name.endswith(".md")

    def test_without_patch_id(self):
        doc = _doc(
            "PSO Technical Manual",
            doc_type="technical-manual",
            app_code="PSO",
            patch_id="",
        )
        name = original_filename(doc)
        assert name.startswith("PSO_TM_")
        assert name.endswith(".md")

    def test_doc_type_abbreviations(self):
        abbrev_cases = [
            ("installation-guide", "IG"),
            ("release-note", "RN"),
            ("user-manual", "UM"),
            ("technical-manual", "TM"),
            ("change-page", "CP"),
            ("supplement", "SUPP"),
            ("base-dev", "DEV"),
            ("base-hl7", "HL7"),
            ("base-security", "SEC"),
            ("base-setup", "SETUP"),
            ("base-impl", "IMPL"),
            ("quick-ref", "QR"),
            ("unknown", "UNK"),
        ]
        for doc_type, expected_abbrev in abbrev_cases:
            doc = _doc("Test Doc", doc_type=doc_type, app_code="OR", patch_id="")
            name = original_filename(doc)
            assert f"_{expected_abbrev}_" in name or name.startswith(f"OR_{expected_abbrev}_"), (
                f"Expected abbrev {expected_abbrev} in filename for {doc_type}, got: {name}"
            )

    def test_no_double_underscores(self):
        doc = _doc("Test Doc", doc_type="technical-manual", app_code="PSO", patch_id="PSO*7*1")
        name = original_filename(doc)
        assert "__" not in name

    def test_ends_with_md(self):
        doc = _doc("A Doc", doc_type="release-note", app_code="OR", patch_id="OR*3.0*636")
        assert original_filename(doc).endswith(".md")

    def test_filesystem_safe(self):
        doc = _doc(
            "Kernel 8.0: Systems Management (Binder)",
            doc_type="user-manual",
            app_code="XU",
            patch_id="",
        )
        name = original_filename(doc)
        for ch in name:
            assert ch.isalnum() or ch in ("_", "-", "."), f"Unsafe char: {ch!r} in {name}"


# ---------------------------------------------------------------------------
# TestSha256
# ---------------------------------------------------------------------------


class TestSha256:
    def test_known_hash(self):
        expected = hashlib.sha256(b"hello").hexdigest()
        assert _sha256("hello") == expected

    def test_returns_64_char_hex(self):
        result = _sha256("some content")
        assert len(result) == 64
        assert all(c in "0123456789abcdef" for c in result)

    def test_empty_string(self):
        result = _sha256("")
        assert len(result) == 64

    def test_different_content_different_hash(self):
        assert _sha256("content a") != _sha256("content b")


# ---------------------------------------------------------------------------
# TestBuildManifest
# ---------------------------------------------------------------------------


class TestBuildManifest:
    def _make_records(self) -> list[DocumentRecord]:
        return [
            _doc(
                "PSO Installation Guide",
                path="/data/PSO/ig.md",
                doc_type="installation-guide",
                app_code="PSO",
                patch_id="PSO*7.0*507",
                doc_layer="patch",
                text="## Introduction\nContent.",
            ),
            _doc(
                "PSO Technical Manual",
                path="/data/PSO/tm.md",
                doc_type="technical-manual",
                app_code="PSO",
                patch_id="",
                doc_layer="anchor",
                text="## Overview\nTM content.",
            ),
            _doc(
                "OR Release Notes",
                path="/data/OR/rn.md",
                doc_type="release-note",
                app_code="OR",
                patch_id="OR*3.0*636",
                doc_layer="patch",
                text="## Changes\nRN content.",
            ),
        ]

    def test_record_count_matches_input(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "2026-03-28T00:00:00Z")
        assert manifest.total_documents == len(records)
        assert len(manifest.documents) == len(records)

    def test_total_packages_counts_unique_app_codes(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "2026-03-28T00:00:00Z")
        assert manifest.total_packages == 2  # PSO and OR

    def test_repo_name_derived_from_app_code(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "")
        pso_rec = next(
            r
            for r in manifest.documents
            if r.package == "PSO" and r.doc_type == "installation-guide"
        )
        assert pso_rec.repo == "vista-pso"

    def test_original_path_has_correct_prefix(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "")
        for rec in manifest.documents:
            assert rec.original_path.startswith(f"originals/{rec.doc_type}/")

    def test_sha256_is_64_char_hex(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "")
        for rec in manifest.documents:
            assert len(rec.original_sha256) == 64

    def test_migration_status_is_pending(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "")
        assert all(r.migration_status == "pending" for r in manifest.documents)

    def test_git_commit_fields_are_none(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "")
        for rec in manifest.documents:
            assert rec.git_commit_originals is None
            assert rec.git_commit_docs is None

    def test_release_note_transformation(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "")
        rn = next(r for r in manifest.documents if r.doc_type == "release-note")
        assert rn.transformation == "release-note"

    def test_standalone_transformation_for_non_grouped_doc(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "")
        tm = next(r for r in manifest.documents if r.doc_type == "technical-manual")
        assert tm.transformation == "standalone"

    def test_consolidated_master_transformation(self):
        records = self._make_records()
        # Mark the IG as a consolidated master
        transformation_map = {
            "/data/PSO/ig.md": (
                "consolidated-master",
                "docs/installation-guide/pso_ig.md",
                "master",
            ),
        }
        manifest = build_manifest(records, transformation_map, set(), "")
        ig = next(r for r in manifest.documents if r.doc_type == "installation-guide")
        assert ig.transformation == "consolidated-master"
        assert ig.consolidated_role == "master"

    def test_consolidated_addendum_transformation(self):
        records = self._make_records()
        transformation_map = {
            "/data/PSO/ig.md": (
                "consolidated-addendum",
                "docs/installation-guide/pso_ig.md",
                "addendum",
            ),
        }
        manifest = build_manifest(records, transformation_map, set(), "")
        ig = next(r for r in manifest.documents if r.doc_type == "installation-guide")
        assert ig.transformation == "consolidated-addendum"
        assert ig.consolidated_role == "addendum"
        assert ig.consolidated_master == "docs/installation-guide/pso_ig.md"

    def test_stub_transformation(self):
        records = self._make_records()
        stub_paths = {"/data/PSO/ig.md"}
        manifest = build_manifest(records, {}, stub_paths, "")
        ig = next(r for r in manifest.documents if r.doc_type == "installation-guide")
        assert ig.transformation == "stub"

    def test_stub_overrides_transformation_map(self):
        """A stub path takes priority over any transformation_map entry."""
        records = self._make_records()
        transformation_map = {
            "/data/PSO/ig.md": ("consolidated-master", "docs/ig.md", "master"),
        }
        stub_paths = {"/data/PSO/ig.md"}
        manifest = build_manifest(records, transformation_map, stub_paths, "")
        ig = next(r for r in manifest.documents if r.doc_type == "installation-guide")
        assert ig.transformation == "stub"

    def test_generated_at_preserved(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "2026-03-28T12:00:00Z")
        assert manifest.generated == "2026-03-28T12:00:00Z"

    def test_source_markdown_path_preserved(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "")
        ig = next(r for r in manifest.documents if r.doc_type == "installation-guide")
        assert ig.source_markdown_path == "/data/PSO/ig.md"

    def test_patch_id_preserved_in_record(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "")
        ig = next(r for r in manifest.documents if r.doc_type == "installation-guide")
        assert ig.patch_id == "PSO*7.0*507"

    def test_is_stub_field_drives_stub_transformation(self):
        doc = _doc(
            "Stub Doc",
            path="/data/PSO/stub.md",
            doc_type="user-manual",
            app_code="PSO",
            is_stub=True,
            text="stub",
        )
        manifest = build_manifest([doc], {}, set(), "")
        assert manifest.documents[0].transformation == "stub"

    def test_empty_records(self):
        manifest = build_manifest([], {}, set(), "2026-01-01T00:00:00Z")
        assert manifest.total_documents == 0
        assert manifest.total_packages == 0
        assert manifest.documents == []

    def test_returns_corpus_manifest_type(self):
        manifest = build_manifest([], {}, set(), "")
        assert isinstance(manifest, CorpusManifest)

    def test_documents_are_manifest_record_type(self):
        records = self._make_records()
        manifest = build_manifest(records, {}, set(), "")
        assert all(isinstance(r, ManifestRecord) for r in manifest.documents)

    def test_change_page_transformation(self):
        doc = _doc(
            "CP Doc",
            path="/data/PSO/cp.md",
            doc_type="change-page",
            app_code="PSO",
            text="change page content",
        )
        manifest = build_manifest([doc], {}, set(), "")
        assert manifest.documents[0].transformation == "change-page"
