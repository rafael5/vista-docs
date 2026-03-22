"""
Integration tests for manifest/store.py — SQLite round-trip.

Uses a real (temporary) SQLite database. No network.
Marked @pytest.mark.integration so they can be run separately:
  pytest -m integration
"""

import pytest

from vista_docs.manifest.store import load_all, open_db, upsert
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


@pytest.fixture
def db(tmp_path):
    conn = open_db(tmp_path / "test_pipeline.db")
    yield conn
    conn.close()


@pytest.mark.integration
class TestStoreRoundTrip:
    def test_upsert_and_load(self, db):
        entry = make_entry()
        upsert(db, entry)
        loaded = load_all(db)
        assert len(loaded) == 1
        assert loaded[0].doc_title == "CPRS Technical Manual"

    def test_upsert_sets_db_id(self, db):
        entry = make_entry()
        saved = upsert(db, entry)
        assert saved.db_id > 0

    def test_upsert_updates_existing(self, db):
        entry = make_entry()
        upsert(db, entry)
        updated = make_entry(fetch_status=FetchStatus.OK, local_path="/raw/OR/file.docx")
        upsert(db, updated)
        loaded = load_all(db)
        assert len(loaded) == 1
        assert loaded[0].fetch_status == FetchStatus.OK
        assert loaded[0].local_path == "/raw/OR/file.docx"

    def test_multiple_entries(self, db):
        upsert(db, make_entry(doc_title="Doc1"))
        upsert(db, make_entry(doc_title="Doc2"))
        loaded = load_all(db)
        assert len(loaded) == 2

    def test_load_empty_db(self, db):
        assert load_all(db) == []

    def test_fetch_status_round_trip(self, db):
        entry = make_entry(fetch_status=FetchStatus.ERROR, fetch_error="404")
        upsert(db, entry)
        loaded = load_all(db)[0]
        assert loaded.fetch_status == FetchStatus.ERROR
        assert loaded.fetch_error == "404"

    def test_doc_type_round_trip(self, db):
        entry = make_entry(doc_type=DocType.RELEASE_NOTE)
        upsert(db, entry)
        assert load_all(db)[0].doc_type == DocType.RELEASE_NOTE
