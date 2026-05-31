"""Unit tests for F5 revision-history extraction (normalize stage)."""

from vista_docs.normalize.revision_pure import (
    RevisionRecord,
    depollute_description,
    find_revision_table,
    parse_revision_table,
    remove_revision_table,
    summarize_revisions,
)

TABLE = (
    "<table>\n"
    "<caption>Revision History</caption>\n"
    '<thead>\n<tr class="header">\n'
    "<th>Date</th><th>Version/Patch</th><th>Page</th><th>Change</th>"
    "<th>Project Manager</th><th>Technical Writer</th>\n</tr>\n</thead>\n"
    "<tbody>\n"
    '<tr class="odd">\n'
    "<td>06/2023</td><td>OR*3*499</td><td>233, 239, 250</td>\n"
    "<td><p>Added warning.</p><ul>"
    '<li><p>Ordering <a href="#_Toc112615110">Inpatient</a></p></li></ul></td>\n'
    "<td>Redacted</td><td>Redacted</td>\n</tr>\n"
    '<tr class="even">\n'
    "<td>05/2023</td><td>OR*3.0*593</td>"
    '<td><a href="#Smart_Note_593">170</a></td>\n'
    "<td><p>Added note for SMART alerts</p></td>\n"
    "<td>Redacted</td><td>N/A</td>\n</tr>\n"
    "</tbody>\n</table>"
)

BODY = f"Title\n\nRevision History\n\n{TABLE}\n\n## First Section\n\nbody text\n"


def test_find_revision_table():
    found = find_revision_table(BODY)
    assert found is not None
    start, end, html = found
    assert html.startswith("<table>")
    assert BODY[start:end] == html


def test_find_returns_none_for_non_revision_table():
    other = "<table><thead><tr><th>Name</th><th>RPC</th></tr></thead></table>"
    assert find_revision_table(f"text\n\n{other}\n") is None


def test_parse_rows_drop_pm_tw_columns():
    recs = parse_revision_table(TABLE)
    assert recs == [
        RevisionRecord(
            date="2023-06",
            version="OR*3*499",
            pages=[233, 239, 250],
            change="Added warning.; Ordering Inpatient",
            refs=["#_Toc112615110"],
        ),
        RevisionRecord(
            date="2023-05",
            version="OR*3.0*593",
            pages=[170],
            change="Added note for SMART alerts",
            refs=["#Smart_Note_593"],
        ),
    ]


def test_summarize():
    recs = parse_revision_table(TABLE)
    assert summarize_revisions(recs) == {
        "revision_count": 2,
        "revision_newest": "2023-06",
        "revision_oldest": "2023-05",
    }


def test_remove_revision_table_strips_table_and_caption():
    new, removed = remove_revision_table(BODY)
    assert removed is True
    assert "<table>" not in new
    assert "Revision History" not in new
    assert "## First Section" in new
    assert new.startswith("Title")


def test_remove_is_noop_when_absent():
    body = "Title\n\n## Section\n"
    new, removed = remove_revision_table(body)
    assert removed is False
    assert new == body


def test_depollute_description_clears_revision_caption():
    polluted = (
        "Revision HistoryThis table lists the history for each revision of this "
        "document by row in descending order"
    )
    assert depollute_description(polluted) == ""


def test_depollute_keeps_clean_description():
    assert depollute_description("CPRS GUI user guide.") == "CPRS GUI user guide."


def test_depollute_non_string_returns_empty():
    assert depollute_description(None) == ""


def test_parse_normalizes_legacy_mdy_dates():
    # Old CPRS rows use M/D/YY and M/D/YYYY (seen in the real corpus).
    table = (
        "<table><thead><tr><th>Date</th><th>Version/Patch</th>"
        "<th>Page</th><th>Change</th></tr></thead><tbody>"
        "<tr><td>5/21/02</td><td>OR*3*1</td><td></td><td>Initial</td></tr>"
        "<tr><td>5/8/2002</td><td>OR*3*0</td><td></td><td>Draft</td></tr>"
        "</tbody></table>"
    )
    recs = parse_revision_table(table)
    assert [r.date for r in recs] == ["2002-05", "2002-05"]
    assert recs[0].pages == []


def test_parse_returns_empty_for_no_rows():
    assert parse_revision_table("<table></table>") == []
