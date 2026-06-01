"""
Package-master loader.

Loads ``data/package_master.yaml`` — the authoritative table that maps each
VDL ``app_name_abbrev`` to its canonical ``app_name_full``, M namespace
(``pkg_ns``), and post-consolidation identity (``canonical_pkg``).

The module is pure: ``parse_master`` takes a YAML string and returns a
``PackageMaster`` instance. ``load_master`` is the thin I/O wrapper that
reads from disk.

Drives remediation §2 (assessment issues 3.3, 3.4, 3.6).
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from pathlib import Path

import yaml


@dataclass(frozen=True)
class PackageEntry:
    """A single resolved package-master row.

    ``abbrev`` reflects the abbrev that was looked up — for an alias entry
    this is the alias itself, while ``canonical_pkg`` points to the surviving
    abbrev for the package.
    """

    abbrev: str
    canonical_name: str
    pkg_ns: str
    canonical_pkg: str
    aliases: tuple[str, ...] = ()
    notes: str = ""


@dataclass(frozen=True)
class PackageMaster:
    """A loaded package-master table."""

    by_abbrev: dict[str, PackageEntry] = field(default_factory=dict)

    def lookup(self, abbrev: str) -> PackageEntry | None:
        return self.by_abbrev.get(abbrev)


def parse_master(yaml_text: str) -> PackageMaster:
    """Parse a package-master YAML document into a PackageMaster.

    Validates:
      - every package has a non-empty ``canonical_name``
      - aliases do not collide with canonical keys
      - aliases do not collide across packages
    """
    raw = yaml.safe_load(yaml_text) or {}
    packages = raw.get("packages") or {}

    by_abbrev: dict[str, PackageEntry] = {}
    seen_aliases: dict[str, str] = {}

    for abbrev, fields in packages.items():
        if not fields or "canonical_name" not in fields:
            raise ValueError(f"package_master: '{abbrev}' missing required field 'canonical_name'")

        aliases = tuple(fields.get("aliases") or ())
        canonical = PackageEntry(
            abbrev=abbrev,
            canonical_name=fields["canonical_name"],
            pkg_ns=fields.get("pkg_ns", ""),
            canonical_pkg=fields.get("canonical_pkg", abbrev),
            aliases=aliases,
            notes=fields.get("notes", ""),
        )
        by_abbrev[abbrev] = canonical

        for alias in aliases:
            if alias in packages:
                raise ValueError(
                    f"package_master: alias '{alias}' (under '{abbrev}') "
                    f"collides with a canonical package key"
                )
            if alias in seen_aliases:
                raise ValueError(
                    f"package_master: alias '{alias}' is claimed by both "
                    f"'{seen_aliases[alias]}' and '{abbrev}'"
                )
            seen_aliases[alias] = abbrev
            by_abbrev[alias] = replace(canonical, abbrev=alias)

    return PackageMaster(by_abbrev=by_abbrev)


def load_master(path: Path) -> PackageMaster:
    """Read a package-master YAML file and return the parsed PackageMaster."""
    return parse_master(path.read_text(encoding="utf-8"))
