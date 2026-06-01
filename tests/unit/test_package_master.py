"""
Unit tests for enrich/package_master.py

The package master is the authoritative table that resolves an
``app_name_abbrev`` (as it appears in the VDL inventory CSV) to the canonical
``app_name_full``, ``pkg_ns``, and post-consolidation ``canonical_pkg``.

Drives remediation §2 (assessment issues 3.3, 3.4, 3.6).
"""

from __future__ import annotations

import textwrap

import pytest

from vista_docs.enrich.package_master import (
    PackageEntry,
    PackageMaster,
    parse_master,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


SIMPLE_YAML = textwrap.dedent(
    """\
    packages:
      PXRM:
        canonical_name: "Clinical Reminders"
        pkg_ns: "PXRM"
        canonical_pkg: "PXRM"
        aliases: []
      KMPR:
        canonical_name: "Resource Usage Monitor"
        pkg_ns: "KMPR"
        canonical_pkg: "KMPR"
        aliases: ["RUM"]
        notes: "KMP* consolidation absorbed legacy RUM abbrev"
      OR:
        canonical_name: "Order Entry / CPRS"
        pkg_ns: "OR"
        canonical_pkg: "OR"
    """
)


# ---------------------------------------------------------------------------
# parse_master
# ---------------------------------------------------------------------------


def test_parse_master_returns_package_master_instance() -> None:
    master = parse_master(SIMPLE_YAML)
    assert isinstance(master, PackageMaster)


def test_parse_master_indexes_each_abbrev() -> None:
    master = parse_master(SIMPLE_YAML)
    assert set(master.by_abbrev) == {"PXRM", "KMPR", "RUM", "OR"}


def test_parse_master_populates_entry_fields() -> None:
    master = parse_master(SIMPLE_YAML)
    pxrm = master.by_abbrev["PXRM"]
    assert pxrm == PackageEntry(
        abbrev="PXRM",
        canonical_name="Clinical Reminders",
        pkg_ns="PXRM",
        canonical_pkg="PXRM",
        aliases=(),
        notes="",
    )


def test_parse_master_alias_resolves_to_canonical_entry() -> None:
    master = parse_master(SIMPLE_YAML)
    rum = master.by_abbrev["RUM"]
    assert rum.canonical_name == "Resource Usage Monitor"
    assert rum.canonical_pkg == "KMPR"
    # The alias entry preserves the original abbrev so callers can tell
    # which abbrev was looked up.
    assert rum.abbrev == "RUM"


def test_parse_master_optional_notes_default_empty() -> None:
    master = parse_master(SIMPLE_YAML)
    assert master.by_abbrev["OR"].notes == ""


def test_parse_master_optional_aliases_default_empty_tuple() -> None:
    master = parse_master(SIMPLE_YAML)
    assert master.by_abbrev["OR"].aliases == ()


def test_parse_master_empty_yaml_returns_empty_master() -> None:
    master = parse_master("packages: {}\n")
    assert master.by_abbrev == {}


def test_parse_master_rejects_alias_collision_with_canonical_key() -> None:
    bad = textwrap.dedent(
        """\
        packages:
          KMPR:
            canonical_name: "Resource Usage Monitor"
            pkg_ns: "KMPR"
            canonical_pkg: "KMPR"
            aliases: ["RUM"]
          RUM:
            canonical_name: "Something else"
            pkg_ns: "RUM"
            canonical_pkg: "RUM"
        """
    )
    with pytest.raises(ValueError, match="RUM"):
        parse_master(bad)


def test_parse_master_rejects_duplicate_alias_across_packages() -> None:
    bad = textwrap.dedent(
        """\
        packages:
          A:
            canonical_name: "Aye"
            pkg_ns: "A"
            canonical_pkg: "A"
            aliases: ["X"]
          B:
            canonical_name: "Bee"
            pkg_ns: "B"
            canonical_pkg: "B"
            aliases: ["X"]
        """
    )
    with pytest.raises(ValueError, match="X"):
        parse_master(bad)


def test_parse_master_requires_canonical_name() -> None:
    bad = textwrap.dedent(
        """\
        packages:
          PXRM:
            pkg_ns: "PXRM"
            canonical_pkg: "PXRM"
        """
    )
    with pytest.raises(ValueError, match="canonical_name"):
        parse_master(bad)


# ---------------------------------------------------------------------------
# PackageMaster.lookup
# ---------------------------------------------------------------------------


def test_lookup_returns_entry_for_known_abbrev() -> None:
    master = parse_master(SIMPLE_YAML)
    entry = master.lookup("PXRM")
    assert entry is not None
    assert entry.canonical_name == "Clinical Reminders"


def test_lookup_returns_alias_entry() -> None:
    master = parse_master(SIMPLE_YAML)
    entry = master.lookup("RUM")
    assert entry is not None
    assert entry.canonical_pkg == "KMPR"


def test_lookup_returns_none_for_unknown_abbrev() -> None:
    master = parse_master(SIMPLE_YAML)
    assert master.lookup("ZZZ_UNKNOWN") is None


def test_lookup_is_case_sensitive() -> None:
    """VDL abbrevs are upper-case; lower-case input should not silently match."""
    master = parse_master(SIMPLE_YAML)
    assert master.lookup("pxrm") is None
