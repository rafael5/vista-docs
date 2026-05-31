"""
Pure functions for merging enriched inventory metadata into markdown frontmatter.

build_inventory_index(rows) → dict[(app_name_abbrev, doc_title), row_dict]
fields_for_doc(index, app_code, title) → dict | None

The index prefers DOCX rows over PDF rows when both formats exist for a document.
Noise rows (vba_form, va_ref) are excluded from the index.
"""

from __future__ import annotations


def build_inventory_index(rows: list[dict]) -> dict[tuple[str, str], dict]:
    """
    Build a lookup index from enriched inventory rows.

    Key: (app_name_abbrev, doc_title)
    Value: the best row for that document (DOCX preferred over PDF).
    Noise rows (noise_type != '') are excluded.
    """
    index: dict[tuple[str, str], dict] = {}

    for row in rows:
        if row.get("noise_type", "") != "":
            continue

        key = (row["app_name_abbrev"], row["doc_title"])
        existing = index.get(key)

        if existing is None:
            index[key] = row
        elif row.get("doc_format", "") == "docx":
            # DOCX row takes precedence — replace any previously stored PDF row
            index[key] = row

    return index


def fields_for_doc(index: dict, app_code: str, title: str) -> dict | None:
    """
    Return frontmatter fields to merge from the inventory for a given document.

    Looks up (app_code, title) in the pre-built index.  Returns None if not found.

    doc_type is only included when the inventory doc_code is non-empty — to avoid
    overwriting the classify-derived value with an empty string.
    All other fields are always included (may be empty string).
    """
    row = index.get((app_code, title))
    if row is None:
        return None

    result: dict = {
        "section": row.get("section_code", ""),
        "app_name": row.get("app_name_full", ""),
        "app_status": row.get("app_status", ""),
        "pkg_ns": row.get("pkg_ns", ""),
        "patch_id": row.get("patch_id", ""),
        "patch_ver": row.get("patch_ver", ""),
        "doc_layer": row.get("doc_layer", ""),
        "doc_label": row.get("doc_label", ""),
        "doc_subject": row.get("doc_subject", ""),
        "group_key": row.get("group_key", ""),
        "app_url": row.get("app_url", ""),
    }

    doc_code = row.get("doc_code", "")
    if doc_code:
        result["doc_type"] = doc_code

    return result


def app_fields_for_code(index: dict, app_code: str) -> dict | None:
    """Return *app-level* frontmatter fields for an app_code, ignoring title.

    Used to backfill documents that have no exact (app_code, title) inventory
    match (e.g. placeholder/demo docs) so they still carry a real section and
    app identity instead of landing in an "Uncategorized"/blank-app bucket.

    Only app-level fields are returned — never doc-level fields like doc_label
    or patch_id, which cannot be guessed from an unrelated row of the same app.
    Returns None if no inventory row exists for the app_code.
    """
    for row in index.values():
        if row.get("app_name_abbrev") == app_code:
            return {
                "section": row.get("section_code", ""),
                "app_name": row.get("app_name_full", ""),
                "app_status": row.get("app_status", ""),
                "pkg_ns": row.get("pkg_ns", "") or app_code,
                "app_url": row.get("app_url", ""),
            }
    return None
