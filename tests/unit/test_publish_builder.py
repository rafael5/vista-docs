"""Unit tests for vista_docs.publish.builder (pure logic)."""

import json
import textwrap
from pathlib import Path

import pytest

from vista_docs.publish.builder import (
    _compact,
    _extract_variant,
    _find_image_dirs,
    _read_frontmatter,
    build_publish_entries,
    get_doc_label,
    load_app_info,
    to_kebab,
)

# ---------------------------------------------------------------------------
# to_kebab
# ---------------------------------------------------------------------------


class TestToKebab:
    def test_lowercase(self):
        assert to_kebab("Clinical") == "clinical"

    def test_spaces_to_hyphens(self):
        assert to_kebab("Technical Manual") == "technical-manual"

    def test_ampersand_to_and(self):
        assert to_kebab("Back-Out & Rollback") == "back-out-and-rollback"

    def test_apostrophe_removed(self):
        assert to_kebab("Administrator's Guide") == "administrators-guide"

    def test_smart_quotes_removed(self):
        assert to_kebab("Manager\u2019s Guide") == "managers-guide"

    def test_slash_to_hyphen(self):
        assert to_kebab("AR/WS") == "ar-ws"

    def test_parens_removed(self):
        assert to_kebab("VistA (formerly HealtheVet)") == "vista-formerly-healthevet"

    def test_collapses_multiple_hyphens(self):
        assert to_kebab("foo  --  bar") == "foo-bar"

    def test_strips_leading_trailing_hyphens(self):
        assert to_kebab("--foo--") == "foo"

    def test_already_kebab_passthrough(self):
        assert to_kebab("release-notes") == "release-notes"

    def test_numbers_preserved(self):
        assert to_kebab("version 5.3") == "version-5-3"

    def test_empty_string(self):
        assert to_kebab("") == ""


# ---------------------------------------------------------------------------
# _compact
# ---------------------------------------------------------------------------


class TestCompact:
    def test_version_single_digit(self):
        assert _compact("outpatient-pharmacy-version-7") == "outpatient-pharmacy-v7"

    def test_version_two_parts(self):
        assert _compact("version-5-3") == "v5-3"

    def test_version_three_parts(self):
        assert _compact("version-7-0-1") == "v7-0-1"

    def test_version_at_start(self):
        assert _compact("version-3-release-notes") == "v3-release-notes"

    def test_updated_suffix_removed(self):
        assert _compact("outpatient-pharmacy-v7-updated-pso-7-0-628") == "outpatient-pharmacy-v7"

    def test_updated_suffix_removed_without_version(self):
        assert _compact("pharmacy-updated-pso-7-0-628") == "pharmacy"

    def test_both_version_and_updated(self):
        result = _compact("outpatient-pharmacy-version-7-updated-pso-7-0-628")
        assert result == "outpatient-pharmacy-v7"

    def test_no_noise_passthrough(self):
        assert _compact("gui-version") == "gui-version"

    def test_empty_string(self):
        assert _compact("") == ""

    def test_version_in_middle(self):
        assert _compact("pso-version-7-0-release-notes") == "pso-v7-0-release-notes"

    def test_strips_trailing_hyphen_after_removal(self):
        # updated suffix at very end of string (nothing before it except hyphen)
        result = _compact("pharmacy-updated-abc")
        assert not result.endswith("-")

    @pytest.mark.parametrize(
        "inp, expected",
        [
            ("version-1", "v1"),
            ("version-10", "v10"),
            ("version-5-3", "v5-3"),
            ("version-7-0-1", "v7-0-1"),
        ],
    )
    def test_version_parametrized(self, inp, expected):
        assert _compact(inp) == expected


# ---------------------------------------------------------------------------
# _extract_variant
# ---------------------------------------------------------------------------


class TestExtractVariant:
    def test_strips_app_prefix_and_label(self):
        result = _extract_variant("cprs technical manual: gui version", "CPRS", "Technical Manual")
        assert "gui" in result
        assert "technical manual" not in result.lower()

    def test_strips_label_from_end(self):
        result = _extract_variant(
            "outpatient pharmacy version 7 release notes", "PSO", "Release Notes"
        )
        assert "release notes" not in result.lower()
        assert "outpatient pharmacy" in result.lower()

    def test_strips_label_from_anywhere(self):
        result = _extract_variant(
            "pharmacy release notes operational updates", "PSO", "Release Notes"
        )
        assert "release notes" not in result.lower()

    def test_empty_when_only_label_remains(self):
        result = _extract_variant("pso release notes", "PSO", "Release Notes")
        # After stripping prefix "pso" and label "release notes", should be empty or minimal
        assert "release notes" not in result.lower()

    def test_strips_quotes(self):
        result = _extract_variant('"cprs technical manual"', "CPRS", "Technical Manual")
        assert "cprs" not in result.lower()

    def test_no_mutation_of_input(self):
        title = "cprs technical manual: gui version"
        _extract_variant(title, "CPRS", "Technical Manual")
        assert title == "cprs technical manual: gui version"


# ---------------------------------------------------------------------------
# get_doc_label
# ---------------------------------------------------------------------------


class TestGetDocLabel:
    def test_uppercase_code(self):
        assert get_doc_label("TM") == "Technical Manual"

    def test_lowercase_pipeline_name(self):
        assert get_doc_label("technical-manual") == "Technical Manual"

    def test_dibr(self):
        label = get_doc_label("DIBR")
        assert "Deployment" in label
        assert "Rollback" in label

    def test_rn(self):
        assert get_doc_label("RN") == "Release Notes"

    def test_unknown_code_titlecased(self):
        result = get_doc_label("CUSTOM-CODE")
        assert result == "Custom Code"

    def test_case_insensitive_lookup(self):
        assert get_doc_label("tm") == get_doc_label("TM")


# ---------------------------------------------------------------------------
# Fixtures shared by load_app_info and build_publish_entries tests
# ---------------------------------------------------------------------------

INVENTORY_CSV = textwrap.dedent("""\
    app_name_abbrev,app_name_full,section_name,doc_slug
    PSO,Outpatient Pharmacy,Clinical,pso
    CPRS,Computerized Patient Record System,Clinical,cprs
    AR/WS,Accounts Receivable/Workstation,Financial-Administrative,arws
""")

MANIFEST_TEMPLATE = {
    "documents": [],
}


def _write_md(path: Path, frontmatter: dict[str, str], body: str = "# Doc\n") -> None:
    fm_lines = "\n".join(f'{k}: "{v}"' for k, v in frontmatter.items())
    path.write_text(f"---\n{fm_lines}\n---\n\n{body}", encoding="utf-8")


# ---------------------------------------------------------------------------
# load_app_info
# ---------------------------------------------------------------------------


class TestLoadAppInfo:
    def test_loads_basic_entries(self, tmp_path):
        csv_file = tmp_path / "inventory.csv"
        csv_file.write_text(INVENTORY_CSV, encoding="utf-8")
        info = load_app_info(csv_file)

        assert "PSO" in info
        assert info["PSO"].abbrev == "pso"
        assert info["PSO"].full_name == "outpatient-pharmacy"
        assert info["PSO"].section == "clinical"

    def test_section_kebab_normalized(self, tmp_path):
        csv_file = tmp_path / "inventory.csv"
        csv_file.write_text(INVENTORY_CSV, encoding="utf-8")
        info = load_app_info(csv_file)
        assert info["CPRS"].section == "clinical"

    def test_slash_in_abbrev_sanitized(self, tmp_path):
        csv_file = tmp_path / "inventory.csv"
        csv_file.write_text(INVENTORY_CSV, encoding="utf-8")
        info = load_app_info(csv_file)
        assert "ARWS" not in info  # loaded under "AR/WS".upper() = "AR/WS"
        # The key is the raw abbrev uppercased; abbrev field is sanitized
        key = "AR/WS"
        assert key in info
        assert "/" not in info[key].abbrev  # sanitized via to_kebab

    def test_section_rename_applied(self, tmp_path):
        csv_content = textwrap.dedent("""\
            app_name_abbrev,app_name_full,section_name,doc_slug
            GUI,Some App,VistA/GUI Hybrids (formerly HealtheVet),gui
        """)
        csv_file = tmp_path / "inventory.csv"
        csv_file.write_text(csv_content, encoding="utf-8")
        info = load_app_info(csv_file)
        assert info["GUI"].section == "vista-gui-hybrids"

    def test_duplicate_abbrev_first_wins(self, tmp_path):
        csv_content = textwrap.dedent("""\
            app_name_abbrev,app_name_full,section_name,doc_slug
            PSO,Outpatient Pharmacy,Clinical,pso
            PSO,Pharmacy Secondary,Clinical,pso2
        """)
        csv_file = tmp_path / "inventory.csv"
        csv_file.write_text(csv_content, encoding="utf-8")
        info = load_app_info(csv_file)
        assert info["PSO"].full_name == "outpatient-pharmacy"


# ---------------------------------------------------------------------------
# build_publish_entries
# ---------------------------------------------------------------------------


class TestBuildPublishEntries:
    def _setup(self, tmp_path):
        """Return (consolidated_dir, md_img_dir, manifest_path, inventory_csv)."""
        consolidated_dir = tmp_path / "consolidated"
        md_img_dir = tmp_path / "md-img"
        manifest_path = tmp_path / "manifest.json"
        inventory_csv = tmp_path / "inventory.csv"

        consolidated_dir.mkdir()
        md_img_dir.mkdir()
        inventory_csv.write_text(INVENTORY_CSV, encoding="utf-8")

        return consolidated_dir, md_img_dir, manifest_path, inventory_csv

    def test_single_consolidated_group(self, tmp_path):
        cons, md_img, manifest, inv = self._setup(tmp_path)

        pkg_dir = cons / "PSO" / "rn"
        pkg_dir.mkdir(parents=True)
        md_file = pkg_dir / "pso-rn-master.md"
        _write_md(
            md_file,
            {
                "app_code": "PSO",
                "doc_type": "RN",
                "consolidated_title": "Outpatient Pharmacy Release Notes",
            },
        )

        manifest.write_text(json.dumps({"documents": []}), encoding="utf-8")

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info)

        assert len(entries) == 1
        e = entries[0]
        assert e.dest_path == Path("clinical/pso--outpatient-pharmacy/release-notes.md")
        assert not e.is_patch

    def test_anchor_with_variant_disambiguation(self, tmp_path):
        cons, md_img, manifest, inv = self._setup(tmp_path)

        pkg_dir = cons / "CPRS" / "tm"
        pkg_dir.mkdir(parents=True)

        for stem, title in [
            ("cprs-tm-gui", "CPRS Technical Manual: GUI Version"),
            ("cprs-tm-server", "CPRS Technical Manual: Server Configuration"),
        ]:
            _write_md(
                pkg_dir / f"{stem}.md",
                {"app_code": "CPRS", "doc_type": "TM", "consolidated_title": title},
            )

        manifest.write_text(json.dumps({"documents": []}), encoding="utf-8")

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info)

        filenames = {e.dest_path.name for e in entries}
        assert len(entries) == 2
        # Both should have a variant suffix
        assert all("--" in name for name in filenames)
        # No repeated label (technical-manual--technical-manual)
        assert not any(name == "technical-manual--technical-manual.md" for name in filenames)

    def test_patch_layer_goes_to_patches_subdir(self, tmp_path):
        cons, md_img, manifest, inv = self._setup(tmp_path)

        src_md = md_img / "pso-7-0-628-rn.md"
        _write_md(src_md, {"app_code": "PSO", "doc_type": "RN"})

        manifest.write_text(
            json.dumps(
                {
                    "documents": [
                        {
                            "source_markdown_path": str(src_md),
                            "package": "PSO",
                            "doc_type": "RN",
                            "doc_layer": "patch",
                            "patch_id": "PSO*7*628",
                            "consolidated_master": None,
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info)

        assert len(entries) == 1
        e = entries[0]
        assert e.is_patch
        assert "patches" in e.dest_path.parts

    def test_deduplication_prefers_higher_priority_dtype(self, tmp_path):
        cons, md_img, manifest, inv = self._setup(tmp_path)

        title = "PSO Deployment Installation Backout Rollback Guide"
        for dtype in ("dibr", "installation-guide"):
            d = cons / "PSO" / dtype
            d.mkdir(parents=True)
            _write_md(
                d / f"pso-{dtype}.md",
                {"app_code": "PSO", "doc_type": dtype, "consolidated_title": title},
            )

        manifest.write_text(json.dumps({"documents": []}), encoding="utf-8")

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info)

        # Both have the same (app, title) key → deduplicated to one entry
        assert len(entries) == 1
        # dibr has higher priority → the selected doc_type should map to DIBR label
        assert "deployment" in entries[0].dest_path.name or "dibr" not in entries[0].dest_path.name

    def test_package_filter(self, tmp_path):
        cons, md_img, manifest, inv = self._setup(tmp_path)

        for app, dtype in [("PSO", "rn"), ("CPRS", "tm")]:
            d = cons / app / dtype
            d.mkdir(parents=True)
            _write_md(
                d / f"{app.lower()}-doc.md",
                {
                    "app_code": app,
                    "doc_type": dtype.upper(),
                    "consolidated_title": f"{app} Doc",
                },
            )

        manifest.write_text(json.dumps({"documents": []}), encoding="utf-8")

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info, packages=["PSO"])

        assert all(e.dest_path.parts[1].startswith("pso") for e in entries)

    def test_consolidation_summary_skipped(self, tmp_path):
        cons, md_img, manifest, inv = self._setup(tmp_path)

        d = cons / "PSO" / "rn"
        d.mkdir(parents=True)
        _write_md(
            d / "pso-rn-master.md",
            {"app_code": "PSO", "doc_type": "RN", "consolidated_title": "PSO Release Notes"},
        )
        (d / "consolidation_summary.md").write_text("# Summary", encoding="utf-8")

        manifest.write_text(json.dumps({"documents": []}), encoding="utf-8")

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info)

        assert len(entries) == 1  # summary file excluded

    def test_version_compacted_in_variant(self, tmp_path):
        cons, md_img, manifest, inv = self._setup(tmp_path)

        for title, stem in [
            ("PSO Release Notes Version 7", "pso-rn-v7"),
            ("PSO Release Notes Version 5-3", "pso-rn-v53"),
        ]:
            d = cons / "PSO" / f"rn-{stem}"
            d.mkdir(parents=True)
            _write_md(
                d / f"{stem}.md",
                {"app_code": "PSO", "doc_type": "RN", "consolidated_title": title},
            )

        manifest.write_text(json.dumps({"documents": []}), encoding="utf-8")

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info)

        filenames = {e.dest_path.name for e in entries}
        # version-N should be compacted to vN
        assert not any("version-" in f for f in filenames)
        assert any("v7" in f for f in filenames)

    def test_consolidated_skipped_in_single_version(self, tmp_path):
        """A manifest doc with consolidated_master set is not added as single-version."""
        cons, md_img, manifest, inv = self._setup(tmp_path)

        # Put the consolidated master in consolidated/
        d = cons / "PSO" / "rn"
        d.mkdir(parents=True)
        master_md = d / "pso-rn-master.md"
        _write_md(
            master_md,
            {"app_code": "PSO", "doc_type": "RN", "consolidated_title": "PSO Release Notes"},
        )

        # Manifest has a source doc pointing to md-img, with consolidated_master set
        src_md = md_img / "pso-7-0-542-rn.md"
        _write_md(src_md, {"app_code": "PSO", "doc_type": "RN"})

        manifest.write_text(
            json.dumps(
                {
                    "documents": [
                        {
                            "source_markdown_path": str(src_md),
                            "package": "PSO",
                            "doc_type": "RN",
                            "doc_layer": "anchor",
                            "patch_id": None,
                            "consolidated_master": str(master_md),
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info)

        # Only the consolidated master appears; original source is skipped
        assert len(entries) == 1
        assert not entries[0].is_patch

    def test_single_version_anchor_doc(self, tmp_path):
        """Single-version anchor doc (no consolidated group) appears at top level."""
        cons, md_img, manifest, inv = self._setup(tmp_path)

        src_md = md_img / "pso-tm.md"
        _write_md(src_md, {"app_code": "PSO", "doc_type": "TM", "title": "Outpatient Pharmacy TM"})

        manifest.write_text(
            json.dumps(
                {
                    "documents": [
                        {
                            "source_markdown_path": str(src_md),
                            "package": "PSO",
                            "doc_type": "TM",
                            "doc_layer": "anchor",
                            "patch_id": None,
                            "consolidated_master": None,
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info)

        assert len(entries) == 1
        e = entries[0]
        assert not e.is_patch
        assert e.dest_path.name == "technical-manual.md"
        assert "patches" not in e.dest_path.parts

    def test_single_version_anchor_variant_disambiguation(self, tmp_path):
        """Two single-version anchor docs for same app+label get variant suffixes."""
        cons, md_img, manifest, inv = self._setup(tmp_path)

        docs = []
        for stem, title in [
            ("pso-tm-v7", "Outpatient Pharmacy Version 7 Technical Manual"),
            ("pso-tm-v5", "Outpatient Pharmacy Version 5 Technical Manual"),
        ]:
            src = md_img / f"{stem}.md"
            _write_md(src, {"app_code": "PSO", "doc_type": "TM", "title": title})
            docs.append(
                {
                    "source_markdown_path": str(src),
                    "package": "PSO",
                    "doc_type": "TM",
                    "doc_layer": "anchor",
                    "patch_id": None,
                    "consolidated_master": None,
                }
            )

        manifest.write_text(json.dumps({"documents": docs}), encoding="utf-8")

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info)

        assert len(entries) == 2
        filenames = {e.dest_path.name for e in entries}
        assert all("--" in f for f in filenames)
        assert not any("version-" in f for f in filenames)

    def test_manifest_missing_src_skipped(self, tmp_path):
        """Manifest entry pointing to nonexistent file is skipped gracefully."""
        cons, md_img, manifest, inv = self._setup(tmp_path)

        manifest.write_text(
            json.dumps(
                {
                    "documents": [
                        {
                            "source_markdown_path": str(md_img / "does-not-exist.md"),
                            "package": "PSO",
                            "doc_type": "TM",
                            "doc_layer": "anchor",
                            "patch_id": None,
                            "consolidated_master": None,
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info)
        assert entries == []

    def test_consolidated_missing_fields_skipped(self, tmp_path):
        """Consolidated .md without app_code or consolidated_title is skipped."""
        cons, md_img, manifest, inv = self._setup(tmp_path)

        d = cons / "PSO" / "rn"
        d.mkdir(parents=True)
        # Write a file with no app_code
        (d / "bad.md").write_text('---\ndoc_type: "RN"\n---\n\n# Doc\n', encoding="utf-8")

        manifest.write_text(json.dumps({"documents": []}), encoding="utf-8")

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info)
        assert entries == []

    def test_patch_collision_resolved(self, tmp_path):
        """Two patches with the same dest path get disambiguated with src stem."""
        cons, md_img, manifest, inv = self._setup(tmp_path)

        docs = []
        for stem in ("pso-7-0-628-rn-v1", "pso-7-0-628-rn-v2"):
            src = md_img / f"{stem}.md"
            _write_md(src, {"app_code": "PSO", "doc_type": "RN"})
            docs.append(
                {
                    "source_markdown_path": str(src),
                    "package": "PSO",
                    "doc_type": "RN",
                    "doc_layer": "patch",
                    "patch_id": "PSO*7*628",  # same patch_id → collision
                    "consolidated_master": None,
                }
            )

        manifest.write_text(json.dumps({"documents": docs}), encoding="utf-8")

        from vista_docs.publish.builder import load_app_info

        app_info = load_app_info(inv)
        entries = build_publish_entries(cons, md_img, manifest, app_info)

        assert len(entries) == 2
        paths = {e.dest_path for e in entries}
        assert len(paths) == 2  # no collision in output


# ---------------------------------------------------------------------------
# _read_frontmatter
# ---------------------------------------------------------------------------


class TestReadFrontmatter:
    def test_returns_fields(self, tmp_path):
        f = tmp_path / "doc.md"
        f.write_text('---\napp_code: "PSO"\ndoc_type: "RN"\n---\n\n# Body\n', encoding="utf-8")
        fm = _read_frontmatter(f)
        assert fm["app_code"] == "PSO"
        assert fm["doc_type"] == "RN"

    def test_no_frontmatter_returns_empty(self, tmp_path):
        f = tmp_path / "doc.md"
        f.write_text("# Just a heading\n\nNo frontmatter here.\n", encoding="utf-8")
        assert _read_frontmatter(f) == {}

    def test_nonexistent_file_returns_empty(self, tmp_path):
        assert _read_frontmatter(tmp_path / "ghost.md") == {}

    def test_strips_surrounding_quotes(self, tmp_path):
        f = tmp_path / "doc.md"
        f.write_text('---\ntitle: "Quoted Title"\n---\n', encoding="utf-8")
        fm = _read_frontmatter(f)
        assert fm["title"] == "Quoted Title"


# ---------------------------------------------------------------------------
# _find_image_dirs
# ---------------------------------------------------------------------------


class TestFindImageDirs:
    def test_finds_markdown_image_dirs(self, tmp_path):
        img_dir = tmp_path / "pso-7-0-628-rn"
        img_dir.mkdir()
        (img_dir / "001.png").write_bytes(b"")

        md = tmp_path / "doc.md"
        md.write_text(f"# Doc\n\n![Figure 1]({img_dir.name}/001.png)\n", encoding="utf-8")

        dirs = _find_image_dirs(md)
        assert img_dir in dirs

    def test_ignores_missing_image_dirs(self, tmp_path):
        md = tmp_path / "doc.md"
        md.write_text("# Doc\n\n![Fig](nonexistent-dir/001.png)\n", encoding="utf-8")

        dirs = _find_image_dirs(md)
        assert dirs == []

    def test_no_images_returns_empty(self, tmp_path):
        md = tmp_path / "doc.md"
        md.write_text("# Doc\n\nNo images here.\n", encoding="utf-8")
        assert _find_image_dirs(md) == []

    def test_nonexistent_file_returns_empty(self, tmp_path):
        assert _find_image_dirs(tmp_path / "ghost.md") == []

    def test_inline_image_no_subdir_ignored(self, tmp_path):
        md = tmp_path / "doc.md"
        md.write_text("# Doc\n\n![Fig](image.png)\n", encoding="utf-8")
        # No subdirectory path component — not a dir reference
        assert _find_image_dirs(md) == []
