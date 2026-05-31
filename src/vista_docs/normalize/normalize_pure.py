"""Pure normalize orchestrator — composes F1-F10 in canonical order (spec §12).

Takes a consolidated document body (plus its current ``description``) and returns
the cleaned body, a frontmatter-update dict, the structured revision records, and
the anchor-alias map. Zero I/O and date-free (the runner stamps ``normalized_at``
and writes sidecars), so the transform is deterministic and idempotent.

Order: F1 denoise -> F2 boilerplate -> F3 heading-infer -> F4 anchors ->
F5 revision -> F6 toc -> F9 figures -> F10 tables -> F8 link-rewrite.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from vista_docs.normalize import NORMALIZE_VERSION
from vista_docs.normalize.anchors_pure import build_anchor_aliases, extract_headings
from vista_docs.normalize.boilerplate_pure import strip_boilerplate
from vista_docs.normalize.classify_pure import DocFeatures, classify
from vista_docs.normalize.delink_pure import unwrap_toc_links
from vista_docs.normalize.denoise_pure import denoise
from vista_docs.normalize.figures_pure import recover_figures
from vista_docs.normalize.heading_infer_pure import infer_headings
from vista_docs.normalize.linkfix_pure import rewrite_legacy_links
from vista_docs.normalize.revision_pure import (
    RevisionRecord,
    depollute_description,
    find_revision_table,
    parse_revision_table,
    remove_revision_table,
    summarize_revisions,
)
from vista_docs.normalize.tables_pure import convert_tables
from vista_docs.normalize.toc_pure import build_toc

_HEADING_LINE_RE = re.compile(r"^#{1,6}\s")
_TOC_ITEM_RE = re.compile(r"^\s*- \[")
_BLANK_LINES_RE = re.compile(r"\n{3,}")
_TRAILING_WS_RE = re.compile(r"[ \t]+$", re.MULTILINE)


@dataclass
class NormalizeResult:
    body: str
    frontmatter: dict
    revisions: list[RevisionRecord] = field(default_factory=list)
    aliases: dict[str, str] = field(default_factory=dict)
    stats: dict = field(default_factory=dict)


def _strip_existing_toc(body: str) -> str:
    """Remove a previously generated ``## Contents`` block (idempotency)."""
    lines = body.split("\n")
    out: list[str] = []
    i, n = 0, len(lines)
    while i < n:
        if lines[i].strip() == "## Contents":
            i += 1
            while i < n and not lines[i].strip():
                i += 1
            while i < n and _TOC_ITEM_RE.match(lines[i]):
                i += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def _place_toc(body: str, toc_md: str) -> str:
    """Insert the TOC after the title block (after a leading H1, else before H2)."""
    if not toc_md:
        return _strip_existing_toc(body)
    body = _strip_existing_toc(body)
    lines = body.split("\n")
    h0 = next((i for i, line in enumerate(lines) if _HEADING_LINE_RE.match(line)), None)
    if h0 is None:
        return body
    block = toc_md.strip("\n").split("\n")
    if lines[h0].startswith("# "):
        new = lines[: h0 + 1] + [""] + block + [""] + lines[h0 + 1 :]
    else:
        new = lines[:h0] + block + [""] + lines[h0:]
    return "\n".join(new)


def _finalize(body: str) -> str:
    body = _TRAILING_WS_RE.sub("", body)
    body = _BLANK_LINES_RE.sub("\n\n", body)
    return body.strip("\n") + "\n"


def normalize_body(
    body: str,
    *,
    description: str | None = None,
    has_pdf: bool = False,
) -> NormalizeResult:
    """Normalize a document body and return body + frontmatter updates."""
    # F1 denoise, then F3a unwrap dead TOC/nav-link wrapping (recovers prose +
    # kills dead anchors so F3 inference and F8 sweep can work), then F2.
    body = denoise(body)
    body, delinked = unwrap_toc_links(body)
    body, removed_boiler = strip_boilerplate(body)

    # F3 — record native headings first, then infer flattened ones.
    native_headings = bool(extract_headings(body))
    body, promoted = infer_headings(body)

    # F4 — anchors + aliases (computed before F5 removes the revision table,
    # which still references the targets we are slugging here).
    aliases = build_anchor_aliases(body)

    # F5 — revision extraction + description de-pollution.
    revisions: list[RevisionRecord] = []
    found = find_revision_table(body)
    if found:
        revisions = parse_revision_table(found[2])
        body, _ = remove_revision_table(body)

    # F6 — TOC from the (post-removal) heading tree. Drop any prior generated
    # TOC first so its ``## Contents`` heading is not re-listed on re-runs.
    body = _strip_existing_toc(body)
    headings = extract_headings(body)
    toc_md = build_toc(headings)
    body = _place_toc(body, toc_md)

    # F9 / F10
    body = recover_figures(body)
    body = convert_tables(body)

    # F8 — link rewrite (last; needs every anchor finalized).
    body = rewrite_legacy_links(body, aliases)

    body = _finalize(body)

    cls = classify(
        DocFeatures(
            has_headings=native_headings,
            has_word_anchors=bool(aliases),
            has_inferred_headings=promoted > 0,
            is_paginated=removed_boiler > 0,
            has_pdf=has_pdf,
        )
    )

    fm: dict = {
        "has_toc": bool(toc_md),
        "toc": "generated" if toc_md else "none",
        "anchors_source": cls.anchors_source,
        "normalize_version": NORMALIZE_VERSION,
    }
    if aliases:
        fm["anchor_aliases"] = dict(sorted(aliases.items()))
    fm.update(summarize_revisions(revisions))
    if description is not None:
        fm["description"] = depollute_description(description)

    return NormalizeResult(
        body=body,
        frontmatter=fm,
        revisions=revisions,
        aliases=aliases,
        stats={
            "boilerplate_removed": removed_boiler,
            "nav_links_unwrapped": delinked,
            "headings_promoted": promoted,
            "doc_class": cls.doc_class,
        },
    )
