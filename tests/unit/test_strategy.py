"""
Unit tests for fetch/strategy.py — pure URL derivation logic.
"""
import pytest

from vista_docs.fetch.strategy import candidate_urls, swap_extension


class TestSwapExtension:
    def test_docx_to_pdf(self):
        assert swap_extension("https://va.gov/vdl/docs/file.docx") == "https://va.gov/vdl/docs/file.pdf"

    def test_pdf_to_docx(self):
        assert swap_extension("https://va.gov/vdl/docs/file.pdf") == "https://va.gov/vdl/docs/file.docx"

    def test_uppercase_extension(self):
        result = swap_extension("https://va.gov/vdl/docs/file.DOCX")
        assert result.endswith(".pdf")

    def test_unknown_extension_unchanged(self):
        url = "https://va.gov/vdl/docs/file.zip"
        assert swap_extension(url) == url


class TestCandidateUrls:
    def test_docx_url_only_returns_docx_first(self):
        urls = candidate_urls(docx_url="https://va.gov/file.docx", pdf_url="")
        assert urls[0].endswith(".docx")
        assert urls[1].endswith(".pdf")

    def test_pdf_url_only_returns_pdf_first(self):
        urls = candidate_urls(docx_url="", pdf_url="https://va.gov/file.pdf")
        # DOCX preferred — if only PDF given, we derive DOCX first
        assert urls[0].endswith(".docx")
        assert urls[1].endswith(".pdf")

    def test_both_urls_docx_first(self):
        urls = candidate_urls(
            docx_url="https://va.gov/file.docx",
            pdf_url="https://va.gov/file.pdf",
        )
        assert urls[0].endswith(".docx")
        assert urls[1].endswith(".pdf")

    def test_no_urls_returns_empty_list(self):
        assert candidate_urls(docx_url="", pdf_url="") == []

    def test_no_duplicate_urls(self):
        urls = candidate_urls(
            docx_url="https://va.gov/file.docx",
            pdf_url="https://va.gov/file.pdf",
        )
        assert len(urls) == len(set(urls))

    def test_returns_at_most_two_urls(self):
        urls = candidate_urls(
            docx_url="https://va.gov/file.docx",
            pdf_url="https://va.gov/file.pdf",
        )
        assert len(urls) <= 2
