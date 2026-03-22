"""
Unit tests for manifest/operations.py — pure list[ManifestEntry] operations.
"""

from vista_docs.manifest.operations import (
    deduplicate,
    filter_by_package,
    filter_by_status,
    merge_entries,
    update_fetch_status,
)
from vista_docs.models.manifest import DocType, FetchStatus, ManifestEntry


def make_entry(**kwargs) -> ManifestEntry:
    defaults = dict(
        package_id="OR*3.0",
        app_code="OR",
        doc_title="CPRS Technical Manual",
        doc_type=DocType.TECHNICAL_MANUAL,
        docx_url="https://va.gov/file.docx",
        output_filename="cprs-technical-manual.md",
        fetch_status=FetchStatus.PENDING,
    )
    defaults.update(kwargs)
    return ManifestEntry(**defaults)


class TestFilterByStatus:
    def test_returns_only_matching(self):
        entries = [
            make_entry(fetch_status=FetchStatus.PENDING),
            make_entry(doc_title="Doc2", fetch_status=FetchStatus.OK),
            make_entry(doc_title="Doc3", fetch_status=FetchStatus.PENDING),
        ]
        result = filter_by_status(entries, FetchStatus.PENDING)
        assert len(result) == 2
        assert all(e.fetch_status == FetchStatus.PENDING for e in result)

    def test_empty_list(self):
        assert filter_by_status([], FetchStatus.PENDING) == []

    def test_no_matches_returns_empty(self):
        entries = [make_entry(fetch_status=FetchStatus.OK)]
        assert filter_by_status(entries, FetchStatus.PENDING) == []


class TestFilterByPackage:
    def test_returns_only_matching_package(self):
        entries = [
            make_entry(app_code="OR"),
            make_entry(app_code="TIU", package_id="TIU*1.0", doc_title="TIU Doc"),
        ]
        result = filter_by_package(entries, "OR")
        assert len(result) == 1
        assert result[0].app_code == "OR"

    def test_case_sensitive(self):
        entries = [make_entry(app_code="OR")]
        assert filter_by_package(entries, "or") == []


class TestUpdateFetchStatus:
    def test_updates_matching_entry(self):
        entry = make_entry()
        updated = update_fetch_status(
            [entry], "CPRS Technical Manual", FetchStatus.OK, local_path="/raw/OR/file.docx"
        )
        assert updated[0].fetch_status == FetchStatus.OK
        assert updated[0].local_path == "/raw/OR/file.docx"

    def test_nonmatching_entry_unchanged(self):
        entry = make_entry(doc_title="Other Doc")
        updated = update_fetch_status([entry], "CPRS Technical Manual", FetchStatus.OK)
        assert updated[0].fetch_status == FetchStatus.PENDING

    def test_returns_new_list(self):
        entry = make_entry()
        original = [entry]
        result = update_fetch_status(original, entry.doc_title, FetchStatus.OK)
        assert result is not original


class TestDeduplicate:
    def test_removes_exact_duplicates(self):
        entry = make_entry()
        result = deduplicate([entry, entry])
        assert len(result) == 1

    def test_different_titles_kept(self):
        entries = [
            make_entry(doc_title="Doc1"),
            make_entry(doc_title="Doc2"),
        ]
        assert len(deduplicate(entries)) == 2

    def test_key_is_package_and_title(self):
        e1 = make_entry(package_id="OR*3.0", doc_title="TM")
        e2 = make_entry(package_id="TIU*1.0", doc_title="TM")
        assert len(deduplicate([e1, e2])) == 2


class TestMergeEntries:
    def test_existing_ok_preserved(self):
        existing = [make_entry(fetch_status=FetchStatus.OK, local_path="/raw/file.docx")]
        incoming = [make_entry(fetch_status=FetchStatus.PENDING)]
        result = merge_entries(existing, incoming)
        assert result[0].fetch_status == FetchStatus.OK
        assert result[0].local_path == "/raw/file.docx"

    def test_new_entry_added(self):
        existing = [make_entry(doc_title="Existing")]
        incoming = [make_entry(doc_title="New Doc")]
        result = merge_entries(existing, incoming)
        assert len(result) == 2

    def test_empty_existing(self):
        incoming = [make_entry()]
        result = merge_entries([], incoming)
        assert len(result) == 1
