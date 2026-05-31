"""Publish-normalization stage.

Converts faithful pandoc output (``consolidated/``) into clean, GitHub-ready
gold markdown without losing navigational or structural information. Every lossy
decision is recorded in frontmatter or a sidecar so it is auditable and
reversible. See ``docs/publish-normalization-spec.md``.

Layout (per repo architecture rules):
  * ``*_pure*.py`` — pure transforms F1-F10, zero I/O, unit-tested first.
  * ``runner.py`` / ``io.py`` / ``pdf_reader.py`` — thin I/O wrappers
    (``[tool.coverage.run] omit``; integration-tested only).

The canonical processing order (spec §12) is::

    F1 denoise → F2 header/footer → F3 heading-infer → F4 anchors →
    F5 revision → F6 toc → F7 page-bridge → F9 figures → F10 tables →
    F8 link-rewrite (last; needs all anchors finalized)
"""

NORMALIZE_VERSION = "1.0"
