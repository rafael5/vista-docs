"""Frontmatter validation guardrails.

Makes broken corpus data impossible to publish:

  - ``sanitize_scalar``       strip HTML / markdown / control junk to plain text
  - ``safe_dump_frontmatter`` canonical-order YAML that re-parses (raises if not)
  - ``validate_frontmatter``  flag every data-quality defect at the source
"""

from vista_docs.validate.frontmatter import (
    CANONICAL_KEY_ORDER,
    LEGACY_ONLY_KEYS,
    REQUIRED_KEYS,
    SCALAR_FIELDS,
    VALID_SECTIONS,
    Violation,
    safe_dump_frontmatter,
    sanitize_scalar,
    split_frontmatter,
    validate_doc_bytes,
    validate_frontmatter,
    validate_frontmatter_text,
)

__all__ = [
    "CANONICAL_KEY_ORDER",
    "LEGACY_ONLY_KEYS",
    "REQUIRED_KEYS",
    "SCALAR_FIELDS",
    "VALID_SECTIONS",
    "Violation",
    "safe_dump_frontmatter",
    "sanitize_scalar",
    "split_frontmatter",
    "validate_doc_bytes",
    "validate_frontmatter",
    "validate_frontmatter_text",
]
