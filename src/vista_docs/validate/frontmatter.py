"""Pure frontmatter guardrails: sanitize, safe-serialize, validate.

No I/O. Every function takes plain Python values and returns plain Python
values (or raises). This is the single source of truth for what "valid
published frontmatter" means, used by:

  - the audit stage           (serializer invariant + flags)
  - the consolidation stage   (unified schema + safe serialize)
  - the ``validate`` CLI stage (corpus-wide gate before publish/push)
  - the golden serializer tests

Defect classes guarded against (all "hard" — they block publish):
  invalid_yaml · not_utf8 · no_frontmatter · missing_key:<k> · bad_section ·
  legacy_schema · html_in_scalar:<f> · control_char:<f> · mojibake:<f>
"""

from __future__ import annotations

import re
from dataclasses import dataclass

import yaml

from vista_docs.enrich.text_fixers import fix_mojibake

# ---------------------------------------------------------------------------
# Schema constants
# ---------------------------------------------------------------------------

# Required keys every published doc (single-version AND consolidated) must carry,
# present and non-empty.
REQUIRED_KEYS: tuple[str, ...] = (
    "title",
    "doc_type",
    "doc_label",
    "app_code",
    "app_name",
    "section",
    "pkg_ns",
)

VALID_SECTIONS: frozenset[str] = frozenset({"CLI", "FIN", "GUI", "INF", "MON"})

# Keys that only the legacy consolidation schema emitted. A doc carrying any of
# these but lacking the full required key set is a legacy-schema doc.
LEGACY_ONLY_KEYS: frozenset[str] = frozenset(
    {
        "consolidated_title",
        "master_source",
        "prior_versions",
        "consolidated_from",
        "master_pub_date",
    }
)

# Scalar fields that must be clean plain text (no HTML, control chars, mojibake).
SCALAR_FIELDS: tuple[str, ...] = ("description", "audience", "title", "doc_subject")

# Canonical key order for serialization (single-version + consolidation extras).
CANONICAL_KEY_ORDER: list[str] = [
    # Identity
    "title",
    "doc_type",
    "doc_label",
    "doc_layer",
    "doc_subject",
    # Application
    "app_code",
    "app_name",
    "section",
    "app_status",
    # VistA patch identity
    "pkg_ns",
    "patch_ver",
    "patch_id",
    "group_key",
    # VistA technical signatures
    "file_numbers",
    "security_keys",
    "menu_options",
    # Content
    "description",
    "audience",
    "keywords",
    # Structure & counts
    "page_count",
    "word_count",
    "section_count",
    "table_count",
    "figure_count",
    "appendix_count",
    "has_toc",
    # TOC / anchors (normalize stage)
    "toc",
    "anchors_source",
    "anchor_aliases",
    "page_anchors",
    "is_stub",
    # Revision history
    "pub_date",
    "revision_count",
    "revision_newest",
    "revision_oldest",
    "revision_sidecar",
    # Source URLs
    "docx_url",
    "pdf_url",
    "app_url",
    # Audit / provenance
    "audit_applied",
    # Normalize-stage provenance
    "source_sha256",
    "converter",
    "normalized_at",
    "normalize_version",
    # Consolidation provenance extras
    "master_source",
    "master_pub_date",
    "consolidated_from",
    "prior_versions",
]

# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)
_HTML_TAG_RE = re.compile(r"<[a-zA-Z/!][^>]*>")
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
# C0 control chars except tab/newline/carriage-return.
_C0_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
# Residual cp1252-as-utf8 mojibake signatures, plus the replacement char.
_MOJIBAKE_RE = re.compile("\u00e2\u20ac|\u00c3[\x80-\xbf]|\u00c2[\x80-\xbf\xa0]|\ufffd")
_WS_RE = re.compile(r"\s+")
_HTML_ENTITY_RE = re.compile(r"&[a-zA-Z]+;|&#\d+;")


# ---------------------------------------------------------------------------
# sanitize_scalar
# ---------------------------------------------------------------------------


def sanitize_scalar(text: object) -> str:
    """Reduce a scalar frontmatter value to clean plain text.

    Repairs mojibake, removes HTML comments/tags, flattens markdown
    images/links to their text, drops C0 control characters, decodes common
    HTML entities, and collapses whitespace. Idempotent.

    Non-string input returns the empty string.
    """
    if not isinstance(text, str):
        return ""
    s = fix_mojibake(text)
    s = _HTML_COMMENT_RE.sub(" ", s)
    s = _MD_IMAGE_RE.sub(" ", s)
    s = _MD_LINK_RE.sub(r"\1", s)
    s = _HTML_TAG_RE.sub(" ", s)
    s = s.replace("&amp;", "&").replace("&nbsp;", " ")
    s = _HTML_ENTITY_RE.sub("", s)
    s = _C0_RE.sub(" ", s)
    s = _WS_RE.sub(" ", s).strip()
    return s


# ---------------------------------------------------------------------------
# safe_dump_frontmatter — the serializer invariant
# ---------------------------------------------------------------------------


def safe_dump_frontmatter(fm: dict, key_order: list[str] | None = None) -> str:
    """Serialize a frontmatter dict to YAML in canonical order.

    Uses ``yaml.safe_dump`` (which always produces valid YAML), then guarantees
    correctness by round-tripping the output through a strict ``yaml.safe_load``
    and raising ``ValueError`` if it does not re-parse to an equal mapping. No
    document can ever be written with unparseable frontmatter.

    The returned string is the YAML body only (no surrounding ``---`` fences).
    """
    order = key_order if key_order is not None else CANONICAL_KEY_ORDER
    ordered: dict = {}
    for k in order:
        if k in fm:
            ordered[k] = fm[k]
    for k in fm:
        if k not in ordered:
            ordered[k] = fm[k]

    out = yaml.safe_dump(
        ordered,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=1000,
    )

    # Serializer invariant: the output MUST re-parse to the same mapping.
    try:
        reparsed = yaml.safe_load(out)
    except yaml.YAMLError as e:  # pragma: no cover - safe_dump should never do this
        raise ValueError(f"frontmatter serialization is unparseable: {e}") from e
    if reparsed != ordered:
        raise ValueError(
            "frontmatter failed round-trip: serialized output does not "
            "re-parse to the input mapping"
        )
    return out


# ---------------------------------------------------------------------------
# Violations
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Violation:
    """A single data-quality defect found in a document's frontmatter."""

    code: str
    severity: str  # "hard" | "soft"
    detail: str = ""


# ---------------------------------------------------------------------------
# split_frontmatter
# ---------------------------------------------------------------------------


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return ``(frontmatter_raw, body)``; ``frontmatter_raw`` is None if absent."""
    m = _FM_RE.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end() :]


# ---------------------------------------------------------------------------
# validate_frontmatter
# ---------------------------------------------------------------------------


def _empty(v: object) -> bool:
    return v is None or (isinstance(v, str) and not v.strip())


def validate_frontmatter(fm: dict) -> list[Violation]:
    """Validate an already-parsed frontmatter mapping. Returns hard violations."""
    out: list[Violation] = []
    keys = set(fm)

    for k in REQUIRED_KEYS:
        if _empty(fm.get(k)):
            out.append(Violation(f"missing_key:{k}", "hard"))

    if fm.get("section") not in VALID_SECTIONS:
        out.append(Violation("bad_section", "hard", str(fm.get("section"))))

    # Legacy-only schema: carries consolidation legacy keys but is missing the
    # full canonical required set.
    has_required = all(not _empty(fm.get(k)) for k in REQUIRED_KEYS)
    if (LEGACY_ONLY_KEYS & keys) and not has_required:
        out.append(Violation("legacy_schema", "hard"))

    for f in SCALAR_FIELDS:
        v = fm.get(f)
        if not isinstance(v, str):
            continue
        if _HTML_TAG_RE.search(v) or _HTML_COMMENT_RE.search(v):
            out.append(Violation(f"html_in_scalar:{f}", "hard", v[:80]))
        if _C0_RE.search(v):
            out.append(Violation(f"control_char:{f}", "hard"))
        if _MOJIBAKE_RE.search(v):
            out.append(Violation(f"mojibake:{f}", "hard", v[:80]))

    return out


def validate_frontmatter_text(fm_raw: str) -> list[Violation]:
    """Strict-parse a raw frontmatter block, then validate the mapping."""
    try:
        fm = yaml.safe_load(fm_raw)
    except yaml.YAMLError as e:
        return [Violation("invalid_yaml", "hard", str(e).replace("\n", " ")[:160])]
    if not isinstance(fm, dict):
        return [Violation("invalid_yaml", "hard", "frontmatter is not a mapping")]
    return validate_frontmatter(fm)


def validate_doc_bytes(raw: bytes) -> list[Violation]:
    """Validate a whole markdown document given its raw bytes.

    Checks UTF-8 decodability, frontmatter presence, strict YAML re-parse, and
    all frontmatter-level rules.
    """
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        return [Violation("not_utf8", "hard", str(e)[:120])]
    fm_raw, _ = split_frontmatter(text)
    if fm_raw is None:
        return [Violation("no_frontmatter", "hard")]
    return validate_frontmatter_text(fm_raw)
