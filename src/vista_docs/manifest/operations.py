"""
Pure manifest operations — filter, merge, update, deduplicate.

All functions take list[ManifestEntry] and return list[ManifestEntry].
No I/O, no SQLite. Database access lives in manifest/store.py.
"""
from __future__ import annotations

from vista_docs.models.manifest import FetchStatus, ManifestEntry


def filter_by_status(
    entries: list[ManifestEntry], status: FetchStatus
) -> list[ManifestEntry]:
    """Return entries matching the given fetch_status."""
    return [e for e in entries if e.fetch_status == status]


def filter_by_package(
    entries: list[ManifestEntry], app_code: str
) -> list[ManifestEntry]:
    """Return entries for a given package namespace code (e.g. 'OR')."""
    return [e for e in entries if e.app_code == app_code]


def update_fetch_status(
    entries: list[ManifestEntry],
    doc_title: str,
    status: FetchStatus,
    *,
    local_path: str = "",
    fetched_ext: str = "",
    fetch_size: int = 0,
    fetch_error: str = "",
) -> list[ManifestEntry]:
    """
    Return a new list where the entry matching doc_title has updated fetch fields.
    Non-matching entries are returned unchanged. Does not mutate inputs.
    """
    result = []
    for e in entries:
        if e.doc_title == doc_title:
            from dataclasses import replace
            e = replace(
                e,
                fetch_status=status,
                local_path=local_path or e.local_path,
                fetched_ext=fetched_ext or e.fetched_ext,
                fetch_size=fetch_size or e.fetch_size,
                fetch_error=fetch_error or e.fetch_error,
            )
        result.append(e)
    return result


def deduplicate(entries: list[ManifestEntry]) -> list[ManifestEntry]:
    """
    Remove duplicate entries. Uniqueness key: (package_id, doc_title).
    First occurrence wins.
    """
    seen: set[tuple[str, str]] = set()
    result = []
    for e in entries:
        key = (e.package_id, e.doc_title)
        if key not in seen:
            seen.add(key)
            result.append(e)
    return result


def merge_entries(
    existing: list[ManifestEntry],
    incoming: list[ManifestEntry],
) -> list[ManifestEntry]:
    """
    Merge incoming entries into existing, preserving ok/fetched entries.

    Rules:
    - If an existing entry has fetch_status=OK, it is kept as-is.
    - If an incoming entry has no match in existing, it is appended.
    - Matched non-OK existing entries are replaced by incoming.
    """
    existing_map: dict[tuple[str, str], ManifestEntry] = {
        (e.package_id, e.doc_title): e for e in existing
    }
    result: list[ManifestEntry] = []
    seen_keys: set[tuple[str, str]] = set()

    for inc in incoming:
        key = (inc.package_id, inc.doc_title)
        seen_keys.add(key)
        ex = existing_map.get(key)
        if ex is not None and ex.fetch_status == FetchStatus.OK:
            result.append(ex)
        else:
            result.append(inc)

    for ex in existing:
        key = (ex.package_id, ex.doc_title)
        if key not in seen_keys:
            result.append(ex)

    return result
