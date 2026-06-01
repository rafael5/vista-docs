"""Frontmatter JSON Schema + pure validator (spec §5, §11.1).

``FRONTMATTER_SCHEMA`` is the source-of-truth declarative contract for published
frontmatter, including the normalize-stage additions. It is mirrored to the
committed ``frontmatter.schema.json`` artifact (drift-guarded by a unit test).

``validate_against_schema`` is a small, dependency-free validator for the JSON
Schema subset the contract uses (``required`` / ``type`` / ``enum`` /
``additionalProperties``). Severities: a missing required key or a bad ``enum``
is ``hard`` (normalize controls those); a type mismatch or unknown key is
``soft`` (advisory, for the validation report). The enforced publish gate stays
``validate.frontmatter.validate_frontmatter``; this is a layered cross-check.
"""

from __future__ import annotations

from pathlib import Path

from vista_docs.validate.frontmatter import REQUIRED_KEYS, VALID_SECTIONS, Violation

SCHEMA_PATH = Path(__file__).with_name("frontmatter.schema.json")

_STR = {"type": "string"}
_INT = {"type": "integer"}
_BOOL = {"type": "boolean"}
_ARR = {"type": "array"}

FRONTMATTER_SCHEMA: dict = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "VistA Docs published frontmatter",
    "type": "object",
    "required": list(REQUIRED_KEYS),
    "additionalProperties": False,
    "properties": {
        # Identity
        "title": _STR,
        "doc_type": _STR,
        "doc_label": _STR,
        "doc_layer": _STR,
        "doc_subject": _STR,
        # Application
        "app_code": _STR,
        "app_name": _STR,
        "section": {"type": "string", "enum": sorted(VALID_SECTIONS)},
        "app_status": _STR,
        # VistA patch identity
        "pkg_ns": _STR,
        "patch_ver": {"type": ["string", "number"]},
        "patch_id": _STR,
        "group_key": _STR,
        # Technical signatures
        "file_numbers": _ARR,
        "security_keys": _ARR,
        "menu_options": {"type": ["integer", "string"]},
        # Content
        "description": _STR,
        "audience": _STR,
        "keywords": _ARR,
        # Structure & counts
        "page_count": _INT,
        "word_count": _INT,
        "section_count": _INT,
        "table_count": _INT,
        "figure_count": _INT,
        "appendix_count": _INT,
        "has_toc": _BOOL,
        # TOC / anchors (normalize)
        "toc": {"type": "string", "enum": ["generated", "original", "none"]},
        "anchors_source": {"type": "string", "enum": ["word", "inferred", "mixed", "none"]},
        "anchor_aliases": {"type": "object"},
        "page_anchors": _BOOL,
        "is_stub": _BOOL,
        # Revision history
        "pub_date": _STR,
        "revision_count": _INT,
        "revision_newest": {"type": ["string", "null"]},
        "revision_oldest": {"type": ["string", "null"]},
        "revision_sidecar": _STR,
        # Source URLs
        "docx_url": _STR,
        "pdf_url": _STR,
        "app_url": _STR,
        # Audit / provenance
        "audit_applied": _STR,
        "source_sha256": _STR,
        "converter": _STR,
        "normalized_at": _STR,
        "normalize_version": _STR,
        # Consolidation extras
        "master_source": _STR,
        "master_pub_date": _STR,
        "consolidated_from": _STR,
        "prior_versions": _ARR,
        "consolidated_title": _STR,
    },
}


def _empty(v: object) -> bool:
    return v is None or (isinstance(v, str) and not v.strip())


def _matches(value: object, tname: str) -> bool:
    if tname == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if tname == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if tname == "boolean":
        return isinstance(value, bool)
    if tname == "null":
        return value is None
    if tname == "string":
        return isinstance(value, str)
    if tname == "array":
        return isinstance(value, list)
    if tname == "object":
        return isinstance(value, dict)
    return True


def _type_names(spec: dict) -> list[str] | None:
    t = spec.get("type")
    if t is None:
        return None
    return [t] if isinstance(t, str) else list(t)


def validate_against_schema(fm: dict, schema: dict = FRONTMATTER_SCHEMA) -> list[Violation]:
    """Validate a frontmatter mapping against the schema (required/type/enum)."""
    out: list[Violation] = []
    props = schema.get("properties", {})

    for k in schema.get("required", []):
        if _empty(fm.get(k)):
            out.append(Violation(f"schema_required:{k}", "hard"))

    for k, v in fm.items():
        spec = props.get(k)
        if spec is None:
            out.append(Violation(f"schema_unknown_key:{k}", "soft"))
            continue
        if v is None:
            # null = "unset"; presence of required keys is enforced above.
            continue
        tnames = _type_names(spec)
        if tnames is not None and not any(_matches(v, t) for t in tnames):
            out.append(Violation(f"schema_type:{k}", "soft", f"expected {spec['type']}"))
            continue
        enum = spec.get("enum")
        if enum is not None and v not in enum:
            out.append(Violation(f"schema_enum:{k}", "hard", str(v)))

    return out
