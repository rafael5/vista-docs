"""
Pure document type classification for VA VDL documents.

classify(filename, title) → DocType

-------------------------------------------------------------------------------
AXIOMS — the invariants this classifier is built on
-------------------------------------------------------------------------------

1.  FILENAME BEFORE TITLE.
    VDL filenames follow VA naming conventions (e.g. "cprsguitm.docx" = TM,
    "tiuig.docx" = IG). These conventions are more reliable than free-text
    titles, so filename patterns are checked first.

2.  TITLE AS FALLBACK.
    When the filename is generic (e.g. "document.docx", a patch-named file
    like "or_3_0_350_rn.docx", or a UUID), the document title is the best
    available signal.

3.  SPECIFICITY WINS.
    Within each rule list, more specific patterns appear before broader ones.
    Example: "user's guide" is checked before the broader "guide" fragments.

4.  THE VDL DOC-TYPE TAXONOMY.
    The VA VistA Documentation Library uses these primary doc codes, in rough
    frequency order in the real corpus:
      RN    Release Notes          — patch-level change log
      DIBR  Deploy/Install/Back-out/Rollback — modern combined install doc
      IG    Installation Guide     — standalone install/setup instruction
      UM    User Manual            — end-user task reference
      UG    User Guide             — same intent as UM; title variant
      TM    Technical Manual       — design, architecture, data dictionary
      VDD   Version Description    — high-level version overview
      POM   Production Operations  — ops-team reference (not end-user)
      TRG   Training Guide         — instructor/student curriculum
      SMG   Systems Management     — admin/coordinator ops reference
      QRG   Quick Reference Guide  — condensed cheat-sheet
      SUP   Supplement             — adjunct material; glossaries, appendices

5.  MAPPING STRATEGY.
    The DocType enum has coarser buckets than the full VDL taxonomy. The
    mapping collapses related subtypes:
      User Guide / ADPAC Guide / Manager's Manual /
      Admin Guide / Systems Management Guide        → USER_MANUAL
      (All are user-facing operational references.)

      Getting Started / Tutorial / Quick Start /
      Shortcut / FAQ / Brochure / Checklist          → QUICK_REF
      (All are condensed, task-oriented reference material.)

      Glossary / Troubleshooting / Training /
      Workflow / POM / Checklist / Flowchart          → SUPPLEMENT
      (Adjunct material: not a standalone manual or guide.)

      Deployment Guide / Rollback / Conversion /
      Installation Manual                             → INSTALLATION_GUIDE
      (Any document whose primary purpose is getting the software installed
      or un-installed.)

      ReadMe / Patch Readme                           → RELEASE_NOTE
      (Patch-specific notes delivered as a readme file; same intent as RN.)

      Programmer Manual / API Manual / Developer Guide → BASE_DEV

6.  PRIORITY OF EXISTING PATTERNS.
    The original filename rules (tm., ig., um., rn., etc.) are preserved
    unchanged at the top of the filename list. New title rules are appended
    in order of decreasing specificity. This ensures backward compatibility
    with the ~2,600 already-classified documents.

7.  WHAT THIS CLASSIFIER CANNOT DO.
    It cannot detect non-VistA documents (VA benefit forms, web-app docs,
    etc.) — that exclusion must happen upstream (e.g. in the fetch/ingest
    pipeline) before a document reaches this function.
"""

from __future__ import annotations

import re

from vista_docs.models.manifest import DocType

# ---------------------------------------------------------------------------
# Filename pattern rules (checked first, in priority order)
#
# Convention: VA filenames encode the doc type as a suffix before the
# extension, e.g. "cprsguitm.docx" (TM), "tiuig.docx" (IG), "pssum.docx".
# DIBR is spelled out in the filename rather than using a suffix.
# ---------------------------------------------------------------------------

_FILENAME_RULES: list[tuple[re.Pattern[str], DocType]] = [
    # Technical manual: "tm." suffix or "technical-manual" / "techmanual" slug
    (re.compile(r"(tm\.|technical.?manual)", re.I), DocType.TECHNICAL_MANUAL),
    # User manual: "um." suffix or "user-manual" slug
    (re.compile(r"(um\.|user.?manual)", re.I), DocType.USER_MANUAL),
    # Installation / DIBR: "ig." suffix, "install" keyword, or "dibr" acronym
    (re.compile(r"(ig\.|install|dibr)", re.I), DocType.INSTALLATION_GUIDE),
    # Release notes: "rn." suffix or "release" keyword or "patch.*rn" pattern
    (re.compile(r"(rn\.|release.?note|patch.*rn)", re.I), DocType.RELEASE_NOTE),
    # Quick reference: "qr." / "qrg." suffix or "quick-ref" slug
    (re.compile(r"(qr\.|qrg\.|quick.?ref)", re.I), DocType.QUICK_REF),
    # Change page: "cp." suffix
    (re.compile(r"cp\.", re.I), DocType.CHANGE_PAGE),
    # Supplement: "sp." suffix
    (re.compile(r"sp\.", re.I), DocType.SUPPLEMENT),
]

# ---------------------------------------------------------------------------
# Title pattern rules (fallback when filename does not match)
#
# Ordered from most specific to least specific within each logical group
# (see Axiom 3 above). Groups map to the DocType buckets defined in Axiom 5.
# ---------------------------------------------------------------------------

_TITLE_RULES: list[tuple[re.Pattern[str], DocType]] = [
    # --- Technical / User manuals (exact VA label variants) -----------------
    (re.compile(r"technical.?manual", re.I), DocType.TECHNICAL_MANUAL),
    (re.compile(r"user.?manual", re.I), DocType.USER_MANUAL),
    # --- User-facing guides (all collapse to USER_MANUAL per Axiom 5) -------
    # ADPAC = Application Coordinator; these are role-specific operational guides
    (re.compile(r"adpac.?guide", re.I), DocType.USER_MANUAL),
    # Manager's Manual — same intent and audience as a User Manual
    (re.compile(r"manager.?s?\s+manual", re.I), DocType.USER_MANUAL),
    # Administrator's Guide / Admin Guide — ops-team user reference
    (re.compile(r"administrator.?s?\s+guide|admin\s+guide", re.I), DocType.USER_MANUAL),
    # Systems/System Management Guide / Binder — coordinator ops reference
    # Deliberately omits "guide" so multi-volume titles like "Systems Management: Binder" match
    (re.compile(r"systems?\s+management", re.I), DocType.USER_MANUAL),
    # User Guide / User's Guide — exact VA title variant for UM
    (re.compile(r"user.?s?\s+guide", re.I), DocType.USER_MANUAL),
    # Utility Guide — task-oriented guide for a specific tool or utility
    (re.compile(r"utility\s+guide", re.I), DocType.USER_MANUAL),
    # Vendor Guide — third-party integration or vendor-facing operational reference
    (re.compile(r"vendor\s+guide", re.I), DocType.USER_MANUAL),
    # --- Installation / deployment variants (all → INSTALLATION_GUIDE) ------
    (
        re.compile(r"installation.?guide|deployment.*installation|dibr", re.I),
        DocType.INSTALLATION_GUIDE,
    ),
    # "Install Guide" (without "ation") — alternate short title form
    (re.compile(r"\binstall\s+guide\b", re.I), DocType.INSTALLATION_GUIDE),
    # Deploy/Deployment Guide — both the short ("deploy guide") and full form
    (re.compile(r"deploy\w*\s+guide", re.I), DocType.INSTALLATION_GUIDE),
    # Data Migration Guide — data or schema migration; requires install-level access
    (re.compile(r"data\s+migration", re.I), DocType.INSTALLATION_GUIDE),
    # Rollback instructions — the reverse of install; same pipeline artifact
    (re.compile(r"rollback\s+instruction", re.I), DocType.INSTALLATION_GUIDE),
    # Conversion Guide — data or system migration; requires install-level access
    (re.compile(r"conversion\s+guide", re.I), DocType.INSTALLATION_GUIDE),
    # Installation Manual — alternate title form used by some packages
    (re.compile(r"installation\s+manual", re.I), DocType.INSTALLATION_GUIDE),
    # --- Release notes variants (all → RELEASE_NOTE) ------------------------
    (re.compile(r"release.?note", re.I), DocType.RELEASE_NOTE),
    # ReadMe / Readme File — patch-specific notes; same intent as RN
    # The (file|guide) suffix is fully optional — bare "KDC Readme" must also match
    (re.compile(r"read.?me(\s+(file|guide))?", re.I), DocType.RELEASE_NOTE),
    # --- Quick reference / condensed access material (→ QUICK_REF) ----------
    (re.compile(r"quick.?ref", re.I), DocType.QUICK_REF),
    # Getting Started Guide — introductory condensed reference
    (re.compile(r"getting\s+started", re.I), DocType.QUICK_REF),
    # Tutorial — hands-on exercise; not a full manual
    (re.compile(r"\btutorial\b", re.I), DocType.QUICK_REF),
    # Quick Start — even shorter than Getting Started
    (re.compile(r"quick\s+start", re.I), DocType.QUICK_REF),
    # Shortcut list — keyboard/menu reference card
    (re.compile(r"shortcut\s+(list|guide|card)", re.I), DocType.QUICK_REF),
    # FAQ — Frequently Asked Questions
    (re.compile(r"frequently\s+asked|faq\b", re.I), DocType.QUICK_REF),
    # Brochure — summary promotional/informational document
    (re.compile(r"\bbrochure\b", re.I), DocType.QUICK_REF),
    # --- Change page --------------------------------------------------------
    (re.compile(r"change.?page", re.I), DocType.CHANGE_PAGE),
    # --- Supplement / adjunct material (→ SUPPLEMENT) -----------------------
    (re.compile(r"\bsupplement\b", re.I), DocType.SUPPLEMENT),
    # Glossary — terminology reference; not a standalone guide
    (re.compile(r"\bglossary\b", re.I), DocType.SUPPLEMENT),
    # Troubleshooting Guide — diagnostic reference; adjunct to main manual
    (re.compile(r"troubl.{0,3}shoot", re.I), DocType.SUPPLEMENT),
    # Training Guide / Workflow — instructional curriculum or process map
    (re.compile(r"training\s+guide|workflow\b", re.I), DocType.SUPPLEMENT),
    # Production(s) Operations Manual — ops-team runbook; not an end-user guide
    # "Productions" (with s) appears in some titles due to a typo in the VDL
    (re.compile(r"productions?\s+operations\s+manual|\bpom\b", re.I), DocType.SUPPLEMENT),
    # Checklist — task verification list; adjunct to a guide
    (re.compile(r"\bchecklist\b", re.I), DocType.SUPPLEMENT),
    # Flowchart — process diagram document
    (re.compile(r"\bflowchart\b", re.I), DocType.SUPPLEMENT),
    # Dictionary — terminology or data-element reference; same intent as Glossary
    (re.compile(r"\bdictionary\b", re.I), DocType.SUPPLEMENT),
    # Error message guide — diagnostic reference; adjunct to main manual
    (re.compile(r"error\s+message", re.I), DocType.SUPPLEMENT),
    # --- Infrastructure / base platform docs --------------------------------
    # Security guide: security-focused base doc
    (re.compile(r"security", re.I), DocType.BASE_SECURITY),
    # HL7 interface specification
    (re.compile(r"hl7|interface.?spec", re.I), DocType.BASE_HL7),
    # Setup / configuration guide: installation-adjacent base config
    # "set up" (two words) is the same intent as "setup"
    (re.compile(r"set.?up|configuration", re.I), DocType.BASE_SETUP),
    # Developer / programmer / API docs
    (re.compile(r"developer|programming|programmer|\bapi\s+manual", re.I), DocType.BASE_DEV),
    # Implementation guide
    (re.compile(r"implementation", re.I), DocType.BASE_IMPL),
    # --- Catch-all: anything titled "*Manual" not already classified ----------
    # Must appear LAST so every more-specific rule (Technical Manual, User Manual,
    # Programmer Manual, API Manual, etc.) wins by appearing earlier in the list.
    # Covers role-specific manuals (Site Manual, Point of Use Manual, etc.)
    # that don't match any earlier pattern but are clearly user-facing references.
    (re.compile(r"\bmanual\b", re.I), DocType.USER_MANUAL),
]


def classify(filename: str, title: str) -> DocType:
    """
    Classify a VA VDL document as a DocType based on its filename and title.

    Evaluation order (see module-level AXIOMS for full rationale):
      1. Filename patterns  — VA naming conventions are the strongest signal.
      2. Title patterns     — Fallback when filename is generic or patch-named.
      3. DocType.UNKNOWN    — Returned when no pattern matches.

    Both filename and title matching are case-insensitive.

    Args:
        filename: The raw filename (e.g. "cprsguitm.docx"). The extension is
                  included so suffix patterns like "tm." match correctly.
        title:    The document title as it appears in the VDL or frontmatter
                  (e.g. "CPRS Technical Manual: GUI Version").

    Returns:
        The best-matching DocType, or DocType.UNKNOWN.
    """
    stem = filename.lower()

    for pattern, doc_type in _FILENAME_RULES:
        if pattern.search(stem):
            return doc_type

    title_lower = title.lower()
    for pattern, doc_type in _TITLE_RULES:
        if pattern.search(title_lower):
            return doc_type

    return DocType.UNKNOWN
