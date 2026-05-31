"""Document classification for the normalize stage (spec §8).

Branches the transform set per document and records the result in the
``anchors_source`` / ``toc`` / ``page_anchors`` frontmatter fields.

| Class | headings | anchors | TOC strategy        | page bridge        |
|-------|----------|---------|---------------------|--------------------|
| A     | yes      | Word    | generated + aliases | no                 |
| B     | yes      | none    | generated           | no                 |
| C     | infer    | none    | F3 -> generated     | F7 if PDF available |
| D     | infer fails | none | none                | log + skip         |
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DocFeatures:
    """Detected structural features of a consolidated document."""

    has_headings: bool
    has_word_anchors: bool
    has_inferred_headings: bool
    is_paginated: bool
    has_pdf: bool


@dataclass(frozen=True)
class ClassifyResult:
    doc_class: str  # A | B | C | D
    anchors_source: str  # word | inferred | mixed | none
    toc: str  # generated | none
    page_bridge: bool


def classify(f: DocFeatures) -> ClassifyResult:
    """Pick the document class and TOC/anchor strategy from its features."""
    if f.has_word_anchors and (f.has_headings or f.has_inferred_headings):
        source = "mixed" if f.has_inferred_headings else "word"
        return ClassifyResult("A", source, "generated", False)
    if f.has_headings:
        return ClassifyResult("B", "none", "generated", False)
    if f.has_inferred_headings:
        return ClassifyResult("C", "inferred", "generated", f.is_paginated and f.has_pdf)
    return ClassifyResult("D", "none", "none", False)
