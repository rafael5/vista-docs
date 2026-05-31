"""Extractors must never emit HTML markup into description/audience scalars."""

from __future__ import annotations

from vista_docs.enrich.extractors import extract_audience, extract_description

_HTML_TABLE_INTRO = """---
title: X
---

## Introduction

<table style="width:100%;"> <colgroup> <col style="width: 13%" /> </colgroup> <tbody> <tr class="odd"> <td>Date</td> </tr> </tbody> </table>

This package automates the entry, display, and use of audiometric exam
information for the Audiology and Speech Pathology Service across the system.
"""

_HTML_IN_PARAGRAPH = """---
title: X
---

## Overview

The <b>CPRS</b> package provides a <i>graphical</i> interface for clinicians to
review and act on patient data, orders, notes, and results in one place here.
"""

_AUDIENCE_WITH_HTML = """---
title: X
---

## Audience

This manual is intended for <strong>system administrators</strong> and IRM staff
who maintain the package. <!-- back-to-toc -->
"""


def test_description_skips_html_table_block():
    out = extract_description(_HTML_TABLE_INTRO)
    assert "<" not in out and ">" not in out
    assert "Audiology" in out


def test_description_strips_inline_html_tags():
    out = extract_description(_HTML_IN_PARAGRAPH)
    assert "<b>" not in out and "<i>" not in out
    assert "CPRS" in out and "graphical" in out


def test_audience_strips_html_tags_and_comments():
    out = extract_audience(_AUDIENCE_WITH_HTML)
    assert "<" not in out and ">" not in out
    assert "<!--" not in out
    assert "system administrators" in out
