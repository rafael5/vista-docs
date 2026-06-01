"""
Unit tests for ingest/converter.py — backend routing + the Docling special-case.

The Docling backend is an optional extra (the 2 GB ML stack is NOT required to run
these tests): the heavy conversion is injected, so we exercise alt-text extraction,
backend selection, and image-ref injection as pure logic.

cprsguium.docx ("CPRS User Manual: GUI Version") is the one corpus document pandoc
explodes badly; it (and GMRC/constm) are routed to Docling. See the docling-spike
findings for the why.
"""

import zipfile
from pathlib import Path

import pytest

from vista_docs.ingest.converter import (
    DOCLING_DOCS,
    _extract_docx_alt_text,
    _inject_image_refs,
    _run_docling,
    _select_backend,
)

# ---------------------------------------------------------------------------
# Minimal DOCX fixture — two images, the second wrapped in mc:AlternateContent
# (a DrawingML Choice + a VML Fallback) so we can prove the fallback is NOT
# double-counted. Alt-text lives on <wp:docPr> as Word writes it.
# ---------------------------------------------------------------------------

_NS = (
    'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
    'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
    'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
    'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture" '
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
    'xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" '
    'xmlns:v="urn:schemas-microsoft-com:vml"'
)


def _drawing(docpr_id: int, descr: str, embed: str) -> str:
    return (
        "<w:drawing><wp:inline>"
        f'<wp:docPr id="{docpr_id}" name="Picture {docpr_id}" descr="{descr}"/>'
        "<a:graphic><a:graphicData><pic:pic>"
        f'<pic:nvPicPr><pic:cNvPr id="{docpr_id}" name="img{docpr_id}"/></pic:nvPicPr>'
        f'<pic:blipFill><a:blip r:embed="{embed}"/></pic:blipFill>'
        "</pic:pic></a:graphicData></a:graphic>"
        "</wp:inline></w:drawing>"
    )


_DOCUMENT_XML = (
    f"<w:document {_NS}><w:body>"
    f"<w:p><w:r>{_drawing(1, 'First image alt', 'rId1')}</w:r></w:p>"
    "<w:p><w:r><mc:AlternateContent>"
    f'<mc:Choice Requires="wps">{_drawing(2, "Second image alt", "rId2")}</mc:Choice>'
    '<mc:Fallback><w:pict><v:shape><v:imagedata r:id="rId2"/></v:shape></w:pict></mc:Fallback>'
    "</mc:AlternateContent></w:r></w:p>"
    "</w:body></w:document>"
)

_RELS_XML = (
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Target="media/image1.png"/>'
    '<Relationship Id="rId2" Target="media/image2.png"/>'
    "</Relationships>"
)


@pytest.fixture
def alt_docx(tmp_path: Path) -> Path:
    """A minimal but well-formed .docx with two alt-tagged images."""
    path = tmp_path / "cprsguium.docx"
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("word/document.xml", _DOCUMENT_XML)
        z.writestr("word/_rels/document.xml.rels", _RELS_XML)
        z.writestr("word/media/image1.png", b"\x89PNG\r\n\x1a\nIMAGE-ONE")
        z.writestr("word/media/image2.png", b"\x89PNG\r\n\x1a\nIMAGE-TWO")
    return path


# ---------------------------------------------------------------------------
# Backend routing
# ---------------------------------------------------------------------------


class TestSelectBackend:
    def test_known_offenders_route_to_docling(self):
        assert _select_backend(Path("/raw/CPRS/cprsguium.docx")) == "docling"
        assert _select_backend(Path("/raw/GMRC/constm.docx")) == "docling"

    def test_routing_is_case_insensitive(self):
        assert _select_backend(Path("/raw/CPRS/CPRSGUIUM.DOCX")) == "docling"

    def test_other_docs_route_to_pandoc(self):
        assert _select_backend(Path("/raw/CPRS/cprslmum.docx")) == "pandoc"
        assert _select_backend(Path("/raw/PSB/psbni.docx")) == "pandoc"

    def test_allowlist_contains_expected_stems(self):
        assert {"cprsguium", "constm"} <= DOCLING_DOCS


# ---------------------------------------------------------------------------
# Alt-text extraction from DOCX XML
# ---------------------------------------------------------------------------


class TestExtractDocxAltText:
    def test_counts_pictures_in_document_order(self, alt_docx: Path):
        pics = _extract_docx_alt_text(alt_docx)
        # Two images — the AlternateContent VML Fallback must NOT double-count.
        assert len(pics) == 2

    def test_alt_text_carried_from_drawing_wrapper(self, alt_docx: Path):
        pics = _extract_docx_alt_text(alt_docx)
        assert pics[0]["alt"] == "First image alt"
        assert pics[1]["alt"] == "Second image alt"

    def test_media_filenames_resolved_via_rels(self, alt_docx: Path):
        pics = _extract_docx_alt_text(alt_docx)
        assert pics[0]["media"] == "image1.png"
        assert pics[1]["media"] == "image2.png"


# ---------------------------------------------------------------------------
# Image-ref injection (pure string work)
# ---------------------------------------------------------------------------


class TestInjectImageRefs:
    def test_replaces_placeholders_in_order(self):
        md = "A\n\n<!-- image -->\n\nB\n\n<!-- image -->\n"
        pics = [
            {"alt": "first", "media": "image1.png"},
            {"alt": "second", "media": "image2.png"},
        ]
        out = _inject_image_refs(md, pics, "doc")
        assert "![first](doc/image1.png)" in out
        assert "![second](doc/image2.png)" in out
        assert "<!-- image -->" not in out

    def test_missing_media_keeps_placeholder(self):
        md = "<!-- image -->"
        out = _inject_image_refs(md, [{"alt": "x", "media": ""}], "doc")
        assert out == "<!-- image -->"

    def test_alt_text_sanitised(self):
        md = "<!-- image -->"
        pics = [{"alt": "has ] bracket\nand newline", "media": "i.png"}]
        out = _inject_image_refs(md, pics, "doc")
        alt_region = out[len("![") : out.index("](")]  # text inside ![ ... ]
        assert "]" not in alt_region  # closing bracket would break the markdown
        assert "\n" not in out
        assert out == "![has ) bracket and newline](doc/i.png)"

    def test_mismatch_raises(self):
        # One placeholder, two pics → loud failure, never silent misalignment.
        with pytest.raises(ValueError):
            _inject_image_refs("<!-- image -->", [{"alt": "", "media": "a"}] * 2, "doc")


# ---------------------------------------------------------------------------
# _run_docling orchestration (heavy conversion injected — no docling needed)
# ---------------------------------------------------------------------------


class TestRunDocling:
    def test_produces_refs_and_extracts_media(self, alt_docx: Path, tmp_path: Path):
        md_path = tmp_path / "doc.md"
        raw_img_dir = tmp_path / "raw-images"

        fake_markdown = "Intro\n\n<!-- image -->\n\nMore\n\n<!-- image -->\n"
        _run_docling(
            alt_docx,
            md_path,
            raw_img_dir,
            convert_fn=lambda _p: fake_markdown,
        )

        out = md_path.read_text(encoding="utf-8")
        assert "![First image alt](raw-images/image1.png)" in out
        assert "![Second image alt](raw-images/image2.png)" in out
        # Referenced media actually extracted to the image dir.
        assert (raw_img_dir / "image1.png").read_bytes().endswith(b"IMAGE-ONE")
        assert (raw_img_dir / "image2.png").read_bytes().endswith(b"IMAGE-TWO")
