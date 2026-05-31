"""Unit tests for the pure normalize orchestrator (composes F1-F10, spec §12)."""

from vista_docs.normalize.normalize_pure import normalize_body

SAMPLE = (
    "CPRS User Guide\n"
    "\n"
    "Revision History\n"
    "\n"
    "<table>\n"
    "<thead><tr><th>Date</th><th>Version/Patch</th><th>Page</th><th>Change</th>"
    "<th>Project Manager</th><th>Technical Writer</th></tr></thead>\n"
    "<tbody>\n"
    "<tr><td>06/2023</td><td>OR*3*499</td><td>233</td>"
    '<td><p>See <a href="#OrderingSimple">Ordering</a></p></td>'
    "<td>Redacted</td><td>Redacted</td></tr>\n"
    "</tbody></table>\n"
    "\n"
    '<span id="OrderingSimple"></span>\n'
    "\n"
    "# Ordering Medications\n"
    "\n"
    "Some" + " " * 20 + "padded text.\n"
    "\n"
    "Page 5 of 12\n"
    "\n"
    "## Simple Dose\n"
    "\n"
    "See [the order step](#OrderingSimple).\n"
)


def test_revision_table_extracted_and_summarized():
    r = normalize_body(SAMPLE, description="Revision HistoryThis table lists the history")
    assert "<table>" not in r.body
    assert r.frontmatter["revision_count"] == 1
    assert r.frontmatter["revision_newest"] == "2023-06"
    assert len(r.revisions) == 1
    assert r.revisions[0].refs == ["#OrderingSimple"]


def test_description_depolluted():
    r = normalize_body(SAMPLE, description="Revision HistoryThis table lists the history")
    assert r.frontmatter["description"] == ""


def test_toc_generated_and_flagged():
    r = normalize_body(SAMPLE)
    assert r.frontmatter["has_toc"] is True
    assert r.frontmatter["toc"] == "generated"
    assert "## Contents" in r.body
    assert "(#ordering-medications)" in r.body
    assert "(#simple-dose)" in r.body


def test_aliases_built_and_links_rewritten():
    r = normalize_body(SAMPLE)
    assert r.aliases.get("OrderingSimple") == "ordering-medications"
    # F8: the legacy reference is rewritten to the slug
    assert "(#ordering-medications)" in r.body
    assert "#OrderingSimple" not in r.body


def test_denoise_and_boilerplate_applied():
    r = normalize_body(SAMPLE)
    assert " " * 20 not in r.body
    assert "Page 5 of 12" not in r.body


def test_anchors_source_word_when_bookmarks_present():
    r = normalize_body(SAMPLE)
    assert r.frontmatter["anchors_source"] == "word"


def test_normalize_version_stamped():
    r = normalize_body(SAMPLE)
    assert r.frontmatter["normalize_version"] == "1.0"


def test_idempotent_body():
    once = normalize_body(SAMPLE, description="Revision HistoryThis table lists")
    twice = normalize_body(once.body, description=once.frontmatter["description"])
    assert twice.body == once.body
