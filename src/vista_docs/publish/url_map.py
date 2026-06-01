"""
Build a {patch_id → publish-relative-path} map from the publish/ tree.

The map is the join key for adding `github_md_url` to the inventory CSV
(remediation P4). Each .md file in publish/ has one of three frontmatter
shapes:

  Anchor (consolidated):  master_source + prior_versions  → many patch_ids
  Plain singleton:        patch_id                        → one patch_id
  Patch under patches/:   patch_id                        → one patch_id

`INDEX.md` and `README.md` at the publish/ root are skipped.

Pure functions:
  parse_patch_id        — extract patch_id from a master_source / prior_versions token
  keys_from_frontmatter — list of patch_ids this entry contributes
  build_url_map         — pure: [(rel_path, frontmatter), ...] -> {patch_id: rel_path}

I/O thin layer:
  walk_publish_tree     — walks publish/, reads frontmatter, returns map
  write_url_map_json    — walks + writes publish/url_map.json with full URLs
"""

from __future__ import annotations

import json
import logging
from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)


# Files at publish/ root that are not link targets.
_SKIP_NAMES = frozenset({"INDEX.md", "README.md"})


def parse_patch_id(token: str) -> str:
    """Extract the patch_id portion of a master_source / prior_versions string.

    >>> parse_patch_id("DG*5.3*952 DIBRG")
    'DG*5.3*952'
    >>> parse_patch_id("DG*5.3*554/TIU*1*184 DIBRG")
    'DG*5.3*554/TIU*1*184'
    >>> parse_patch_id("")
    ''

    For prose entries that don't start with a patch identifier (e.g.
    "Blind Rehab Version 5.1.3 Deployment, …"), this returns the first
    whitespace token; the caller should treat such non-NS*V*P keys as
    no-match downstream.
    """
    return token.strip().split(maxsplit=1)[0] if token.strip() else ""


def keys_from_frontmatter(fm: dict) -> list[str]:
    """Return all join keys this publish/ frontmatter contributes.

    Anchor entries (consolidated multi-version) carry only their constituent
    patch_ids. Non-anchor entries (plain singletons + per-patch files mirrored
    from md-img/) carry their precise va.gov source URLs (pdf_url / docx_url)
    AND their patch_id, because patch_id alone is ambiguous for plain
    singletons that share a "NS*V" anchor identifier (e.g. all PIMS V5.3 docs
    share patch_id "ADT*5.3").
    """
    if "master_source" in fm:
        sources: list[str] = [fm.get("master_source", "")]
        sources.extend(fm.get("prior_versions") or [])
        return [pid for s in sources if (pid := parse_patch_id(str(s)))]

    keys: list[str] = []
    for url_field in ("pdf_url", "docx_url"):
        url = str(fm.get(url_field) or "").strip()
        if url:
            keys.append(url)
    pid = str(fm.get("patch_id") or "").strip()
    if pid:
        keys.append(pid)
    return keys


def build_url_map(entries: Iterable[tuple[str, dict]]) -> dict[str, str]:
    """Build {patch_id: rel_path} from (rel_path, frontmatter) pairs.

    Pure. On a well-formed publish/ tree, each patch_id maps to exactly one
    rel_path. If two entries claim the same patch_id (shouldn't happen),
    last writer wins — call sites should log such collisions.
    """
    url_map: dict[str, str] = {}
    for rel_path, fm in entries:
        for key in keys_from_frontmatter(fm):
            url_map[key] = rel_path
    return url_map


def _read_frontmatter(md_path: Path) -> dict:
    """Read the leading YAML frontmatter block of a markdown file."""
    text = md_path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    block = text[4:end]
    try:
        loaded = yaml.safe_load(block)
        return loaded if isinstance(loaded, dict) else {}
    except yaml.YAMLError:
        logger.warning("Could not parse frontmatter in %s", md_path)
        return {}


def walk_publish_tree(publish_root: Path) -> dict[str, str]:
    """Walk publish/ and return {patch_id: rel_path}."""
    entries: list[tuple[str, dict]] = []
    for md in publish_root.rglob("*.md"):
        if md.parent == publish_root and md.name in _SKIP_NAMES:
            continue
        rel = md.relative_to(publish_root).as_posix()
        fm = _read_frontmatter(md)
        entries.append((rel, fm))
    return build_url_map(entries)


def write_url_map_json(
    publish_root: Path,
    *,
    github_owner: str = "vistadocs",
    github_repo: str = "vdl",
    branch: str = "main",
) -> dict:
    """Walk publish/ and write {publish_root}/url_map.json.

    Returns the dict that was written.
    """
    url_map = walk_publish_tree(publish_root)
    payload = {
        "generated_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "github_owner": github_owner,
        "github_repo": github_repo,
        "branch": branch,
        "entry_count": len(url_map),
        "entries": url_map,
    }
    out_path = publish_root / "url_map.json"
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    logger.info("Wrote %s (%d entries)", out_path, len(url_map))
    return payload
