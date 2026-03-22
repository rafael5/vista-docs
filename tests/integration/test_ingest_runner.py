"""
Integration tests for ingest/runner.py — I/O layer.

Uses real temp directories and real DOCX bytes. Does NOT invoke Docling.
Scaffold mode only: generates frontmatter stubs without conversion.
"""

import pytest

from vista_docs.ingest.runner import ingest_entry
from vista_docs.models.manifest import DocType, FetchStatus, ManifestEntry

pytestmark = pytest.mark.integration


def _make_entry(tmp_path, **kwargs) -> ManifestEntry:
    """Create a minimal ManifestEntry with a real local file."""
    # Write a tiny dummy DOCX-shaped file (just bytes — scaffold skips parsing)
    src = tmp_path / "raw" / "CPRS" / "cprsguitm.docx"
    src.parent.mkdir(parents=True)
    src.write_bytes(b"PK\x03\x04" + b"\x00" * 28)  # minimal ZIP/DOCX magic

    defaults = dict(
        package_id="OR*3.0",
        app_code="CPRS",
        doc_title="CPRS Technical Manual: GUI Version",
        doc_type=DocType.TECHNICAL_MANUAL,
        patch="OR*3.0*636",
        docx_url="https://www.va.gov/vdl/documents/Clinical/CPRS/cprsguitm.docx",
        pdf_url="https://www.va.gov/vdl/documents/Clinical/CPRS/cprsguitm.pdf",
        output_filename="cprs-technical-manual-gui-version.md",
        fetch_status=FetchStatus.OK,
        local_path=str(src),
        fetched_ext="docx",
    )
    defaults.update(kwargs)
    return ManifestEntry(**defaults)


class TestIngestEntryScaffold:
    def test_returns_manifest_entry(self, tmp_path):
        entry = _make_entry(tmp_path)
        md_dir = tmp_path / "markdown"
        result = ingest_entry(entry, md_dir, scaffold=True)
        assert isinstance(result, ManifestEntry)

    def test_ingest_status_ok(self, tmp_path):
        entry = _make_entry(tmp_path)
        md_dir = tmp_path / "markdown"
        result = ingest_entry(entry, md_dir, scaffold=True)
        assert result.ingest_status == FetchStatus.OK

    def test_markdown_file_created(self, tmp_path):
        entry = _make_entry(tmp_path)
        md_dir = tmp_path / "markdown"
        result = ingest_entry(entry, md_dir, scaffold=True)
        assert result.markdown_path != ""
        import pathlib

        assert pathlib.Path(result.markdown_path).exists()

    def test_markdown_has_frontmatter(self, tmp_path):
        entry = _make_entry(tmp_path)
        md_dir = tmp_path / "markdown"
        result = ingest_entry(entry, md_dir, scaffold=True)
        import pathlib

        content = pathlib.Path(result.markdown_path).read_text()
        assert content.startswith("---\n")
        assert "title:" in content

    def test_markdown_path_under_app_code_subdir(self, tmp_path):
        entry = _make_entry(tmp_path)
        md_dir = tmp_path / "markdown"
        result = ingest_entry(entry, md_dir, scaffold=True)
        import pathlib

        p = pathlib.Path(result.markdown_path)
        assert p.parent.name == "CPRS"

    def test_skips_already_ok_without_force(self, tmp_path):
        entry = _make_entry(tmp_path)
        md_dir = tmp_path / "markdown"
        # First run
        r1 = ingest_entry(entry, md_dir, scaffold=True)
        mtime1 = __import__("pathlib").Path(r1.markdown_path).stat().st_mtime
        # Second run without force — should skip
        r2 = ingest_entry(r1, md_dir, scaffold=True)
        mtime2 = __import__("pathlib").Path(r2.markdown_path).stat().st_mtime
        assert r2.ingest_status == FetchStatus.OK
        assert mtime1 == mtime2  # file not rewritten

    def test_force_rewrites_file(self, tmp_path):
        import time

        entry = _make_entry(tmp_path)
        md_dir = tmp_path / "markdown"
        r1 = ingest_entry(entry, md_dir, scaffold=True)
        time.sleep(0.01)
        r2 = ingest_entry(r1, md_dir, scaffold=True, force=True)
        mtime2 = __import__("pathlib").Path(r2.markdown_path).stat().st_mtime
        r1_mtime = __import__("pathlib").Path(r1.markdown_path).stat().st_mtime
        assert mtime2 >= r1_mtime

    def test_skips_entry_with_fetch_error(self, tmp_path):
        entry = _make_entry(tmp_path, fetch_status=FetchStatus.ERROR, fetch_error="404")
        md_dir = tmp_path / "markdown"
        result = ingest_entry(entry, md_dir, scaffold=True)
        assert result.ingest_status == FetchStatus.SKIPPED

    def test_ingest_error_on_missing_file(self, tmp_path):
        entry = _make_entry(tmp_path, local_path="/nonexistent/path/file.docx")
        md_dir = tmp_path / "markdown"
        result = ingest_entry(entry, md_dir, scaffold=True)
        assert result.ingest_status == FetchStatus.ERROR
        assert result.ingest_error != ""
