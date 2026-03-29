"""
vista-docs CLI — single entry point with subcommands.

  vista-docs crawl    — crawl VDL catalog → inventory/
  vista-docs fetch    — download DOCX/PDF → raw/
  vista-docs ingest   — convert to markdown → markdown/
  vista-docs survey   — analyse corpus structure → survey/
  vista-docs headings     — heading frequency analysis → survey/heading_analysis/
  vista-docs consolidate  — master + addenda consolidation → consolidated/
  vista-docs verify       — sanity-check all artifacts
  vista-docs pipeline     — run crawl → fetch → ingest → survey
"""

from __future__ import annotations

import logging

import click

from vista_docs import __version__

logger = logging.getLogger(__name__)


@click.group()
@click.version_option(__version__)
@click.option("-v", "--verbose", is_flag=True, help="Enable debug logging.")
def cli(verbose: bool) -> None:
    """vista-docs: VA VDL document pipeline."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )


# ---------------------------------------------------------------------------
# crawl
# ---------------------------------------------------------------------------


@cli.command()
@click.option(
    "--delay",
    type=float,
    default=1.5,
    show_default=True,
    help="Seconds between requests.",
)
@click.option("--snapshot", is_flag=True, help="Save a dated snapshot of the inventory.")
@click.option("--max-apps", type=int, default=None, help="Limit apps crawled (for testing).")
def crawl(delay: float, snapshot: bool, max_apps: int | None) -> None:
    """Crawl VDL catalog and write inventory CSV/JSON to ~/data/vista-docs/inventory/."""
    from vista_docs.config import INVENTORY_DIR
    from vista_docs.crawl.crawler import crawl as do_crawl
    from vista_docs.crawl.crawler import to_flat_rows, write_csv, write_json

    INVENTORY_DIR.mkdir(parents=True, exist_ok=True)
    click.echo(f"Crawling VDL → {INVENTORY_DIR}")

    sections = do_crawl(max_apps=max_apps, delay=delay)
    rows = to_flat_rows(sections)
    click.echo(f"  Found {len(sections)} sections, {len(rows)} document entries")

    write_csv(rows, INVENTORY_DIR / "vdl_inventory.csv")
    write_json(sections, INVENTORY_DIR / "vdl_inventory.json")

    if snapshot:
        from datetime import date

        snap_name = f"{date.today()}_vdl_inventory.csv"
        write_csv(rows, INVENTORY_DIR / "snapshots" / snap_name)
        click.echo(f"  Snapshot saved: snapshots/{snap_name}")

    click.echo("Done.")


# ---------------------------------------------------------------------------
# fetch
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--pkg", default="", help="Limit to one package namespace (e.g. OR).")
@click.option("--dry-run", is_flag=True, help="Print what would be fetched without downloading.")
@click.option("--force", is_flag=True, help="Re-fetch even if already ok.")
@click.option("--delay", type=float, default=1.5, show_default=True)
def fetch(pkg: str, dry_run: bool, force: bool, delay: float) -> None:
    """Download DOCX/PDF files from VDL into ~/data/vista-docs/raw/."""
    import csv
    import time

    from vista_docs.config import DB_PATH, INVENTORY_DIR
    from vista_docs.crawl.session import make_session
    from vista_docs.fetch.downloader import download_entry
    from vista_docs.manifest.builder import build_entries_from_rows
    from vista_docs.manifest.operations import filter_by_package
    from vista_docs.manifest.store import load_all, open_db, upsert
    from vista_docs.models.manifest import FetchStatus

    inventory_csv = INVENTORY_DIR / "vdl_inventory.csv"
    if not inventory_csv.exists():
        raise click.ClickException(f"Inventory not found: {inventory_csv}\nRun: vista-docs crawl")

    with open(inventory_csv, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    all_entries = build_entries_from_rows(rows)

    if pkg:
        all_entries = filter_by_package(all_entries, pkg.upper())
        if not all_entries:
            raise click.ClickException(f"No entries found for package: {pkg}")

    db = open_db(DB_PATH)
    existing = load_all(db)
    existing_map = {(e.app_code, e.doc_title): e for e in existing}

    to_fetch = []
    for entry in all_entries:
        key = (entry.app_code, entry.doc_title)
        ex = existing_map.get(key)
        if ex and ex.fetch_status == FetchStatus.OK and not force:
            continue
        to_fetch.append(entry)

    skipped = len(all_entries) - len(to_fetch)
    click.echo(
        f"Fetching {len(to_fetch)} documents"
        + (f" [pkg={pkg.upper()}]" if pkg else "")
        + (" [DRY RUN]" if dry_run else "")
        + (f" ({skipped} already ok, skipped)" if skipped else "")
    )

    if dry_run:
        for e in to_fetch:
            click.echo(f"  {e.app_code:8} {e.doc_title[:60]}")
        return

    session = make_session()
    ok = err = 0
    for i, entry in enumerate(to_fetch, 1):
        click.echo(f"[{i}/{len(to_fetch)}] {entry.app_code} — {entry.doc_title[:55]}", nl=False)
        result = download_entry(entry, session)
        upsert(db, result)
        if result.fetch_status == FetchStatus.OK:
            ok += 1
            click.echo(f"  ok {result.fetched_ext} {result.fetch_size // 1024}KB")
        else:
            err += 1
            click.echo(f"  FAIL {result.fetch_error[:60]}")
        if i < len(to_fetch):
            time.sleep(delay)

    db.close()
    click.echo(f"\nDone: {ok} ok, {err} errors.")


# ---------------------------------------------------------------------------
# ingest
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--pkg", default="", help="Limit to one package namespace.")
@click.option("--scaffold", is_flag=True, help="Generate frontmatter stubs only (no Docling).")
@click.option("--force", is_flag=True, help="Re-ingest even if output exists.")
def ingest(pkg: str, scaffold: bool, force: bool) -> None:
    """Convert fetched DOCX/PDF to markdown in ~/data/vista-docs/markdown/."""
    from vista_docs.config import DB_PATH, MARKDOWN_DIR
    from vista_docs.ingest.runner import ingest_entry
    from vista_docs.manifest.operations import filter_by_package
    from vista_docs.manifest.store import load_all, open_db, upsert
    from vista_docs.models.manifest import FetchStatus

    db = open_db(DB_PATH)
    entries = load_all(db)

    to_ingest = [e for e in entries if e.fetch_status == FetchStatus.OK]
    if pkg:
        to_ingest = filter_by_package(to_ingest, pkg.upper())
        if not to_ingest:
            raise click.ClickException(f"No fetched entries for package: {pkg}")

    if not force:
        to_ingest = [e for e in to_ingest if e.ingest_status != FetchStatus.OK]

    mode = "[SCAFFOLD]" if scaffold else ""
    click.echo(
        f"Ingesting {len(to_ingest)} documents"
        + (f" [pkg={pkg.upper()}]" if pkg else "")
        + (f" {mode}" if mode else "")
    )

    ok = err = skip = 0
    for i, entry in enumerate(to_ingest, 1):
        click.echo(f"[{i}/{len(to_ingest)}] {entry.app_code} — {entry.doc_title[:55]}", nl=False)
        result = ingest_entry(entry, MARKDOWN_DIR, scaffold=scaffold, force=force)
        upsert(db, result)
        if result.ingest_status == FetchStatus.OK:
            ok += 1
            click.echo("  ok")
        elif result.ingest_status == FetchStatus.SKIPPED:
            skip += 1
            click.echo("  skipped")
        else:
            err += 1
            click.echo(f"  FAIL {result.ingest_error[:60]}")

    db.close()
    click.echo(f"\nDone: {ok} ok, {skip} skipped, {err} errors.")


# ---------------------------------------------------------------------------
# enrich
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--pkg", default="", help="Limit to one package namespace.")
@click.option("--force", is_flag=True, help="Re-enrich even if already enriched.")
def enrich(pkg: str, force: bool) -> None:
    """Extract metadata from markdown files and enrich their YAML frontmatter."""
    from vista_docs.config import DB_PATH
    from vista_docs.enrich.runner import enrich_corpus
    from vista_docs.manifest.operations import filter_by_package
    from vista_docs.manifest.store import load_all, open_db
    from vista_docs.models.manifest import FetchStatus

    db = open_db(DB_PATH)
    entries = load_all(db)
    db.close()

    to_enrich = [e for e in entries if e.ingest_status == FetchStatus.OK]
    if pkg:
        to_enrich = filter_by_package(to_enrich, pkg.upper())
        if not to_enrich:
            raise click.ClickException(f"No ingested entries for package: {pkg}")

    label = f" [pkg={pkg.upper()}]" if pkg else ""
    click.echo(f"Enriching {len(to_enrich)} documents{label}")

    from vista_docs.config import MARKDOWN_DIR

    result = enrich_corpus(MARKDOWN_DIR, to_enrich, force=force)
    click.echo(f"Done: {result['ok']} ok, {result['skipped']} skipped, {result['errors']} errors.")


# ---------------------------------------------------------------------------
# sync
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--pkg", default="", help="Limit to one app_code folder (e.g. PSO).")
@click.option("--force", is_flag=True, help="Re-sync even if already synced.")
def sync(pkg: str, force: bool) -> None:
    """Sync enriched inventory metadata into markdown frontmatter."""
    from vista_docs.config import INVENTORY_DIR, MARKDOWN_DIR
    from vista_docs.enrich.sync import sync_inventory_corpus

    enriched_csv = INVENTORY_DIR / "vdl_inventory_enriched.csv"
    if not enriched_csv.exists():
        raise click.ClickException(f"Enriched inventory not found: {enriched_csv}")

    label = f" [pkg={pkg.upper()}]" if pkg else ""
    click.echo(f"Syncing inventory fields into markdown frontmatter{label}")

    result = sync_inventory_corpus(MARKDOWN_DIR, enriched_csv, pkg=pkg, force=force)
    click.echo(
        f"Done: {result['ok']} synced, {result['skipped']} skipped, "
        f"{result['no_match']} no-match, {result['errors']} errors."
    )


# ---------------------------------------------------------------------------
# survey
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--pkg", default="", help="Limit to one package namespace.")
@click.option("--output", type=click.Path(), default="", help="Output directory path.")
def survey(pkg: str, output: str) -> None:
    """Analyse corpus structure and write survey reports."""
    from vista_docs.config import DB_PATH, MARKDOWN_DIR, SURVEY_DIR
    from vista_docs.manifest.operations import filter_by_package
    from vista_docs.manifest.store import load_all, open_db
    from vista_docs.models.manifest import FetchStatus
    from vista_docs.survey.analyzer import run_survey

    db = open_db(DB_PATH)
    entries = load_all(db)
    db.close()

    to_survey = [e for e in entries if e.ingest_status == FetchStatus.OK]
    if pkg:
        to_survey = filter_by_package(to_survey, pkg.upper())
        if not to_survey:
            raise click.ClickException(f"No ingested entries for package: {pkg}")

    out_dir = __import__("pathlib").Path(output) if output else SURVEY_DIR
    label = f" [pkg={pkg.upper()}]" if pkg else ""
    click.echo(f"Surveying {len(to_survey)} documents{label} → {out_dir}")

    result = run_survey(MARKDOWN_DIR, to_survey, out_dir, pkg=pkg)
    click.echo(f"Done: {result['ok']} ok, {result['errors']} errors, {result['stubs']} stubs.")


# ---------------------------------------------------------------------------
# headings
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--output", type=click.Path(), default="", help="Output directory path.")
@click.option(
    "--min-docs",
    type=int,
    default=5,
    show_default=True,
    help="Minimum non-stub docs to include a type in the summary.",
)
@click.option(
    "--boilerplate-threshold",
    type=float,
    default=0.70,
    show_default=True,
    help="Frequency ≥ this → BOILERPLATE.",
)
@click.option(
    "--unique-threshold",
    type=float,
    default=0.15,
    show_default=True,
    help="Frequency ≤ this → UNIQUE.",
)
def headings(
    output: str,
    min_docs: int,
    boilerplate_threshold: float,
    unique_threshold: float,
) -> None:
    """Analyse heading frequencies across all doc types and write JSON + summary.md."""
    from vista_docs.analyze.runner import run_heading_analysis
    from vista_docs.config import MARKDOWN_DIR, SURVEY_DIR

    out_dir = __import__("pathlib").Path(output) if output else SURVEY_DIR / "heading_analysis"
    click.echo(f"Analysing headings in {MARKDOWN_DIR} → {out_dir}")

    profiles = run_heading_analysis(
        MARKDOWN_DIR,
        out_dir,
        min_docs=min_docs,
        boilerplate_threshold=boilerplate_threshold,
        unique_threshold=unique_threshold,
    )
    click.echo(f"Done: {len(profiles)} doc types analysed, results in {out_dir}")


# ---------------------------------------------------------------------------
# consolidate
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--output", type=click.Path(), default="", help="Output directory path.")
@click.option(
    "--min-versions",
    type=int,
    default=2,
    show_default=True,
    help="Minimum versions in a group to trigger consolidation.",
)
@click.option(
    "--doc-type",
    "doc_types",
    multiple=True,
    help="Limit to specific doc type(s). Repeat for multiple. Default: all.",
)
def consolidate(output: str, min_versions: int, doc_types: tuple[str, ...]) -> None:
    """Consolidate multi-version documents into master + addenda files."""
    import pathlib

    from vista_docs.analyze.consolidation_runner import run_consolidation
    from vista_docs.config import DATA_DIR, MARKDOWN_DIR

    out_dir = pathlib.Path(output) if output else DATA_DIR / "consolidated"
    types_filter = list(doc_types) if doc_types else None
    click.echo(f"Consolidating {MARKDOWN_DIR} → {out_dir}")
    if types_filter:
        click.echo(f"  Filtering to doc types: {', '.join(types_filter)}")

    results = run_consolidation(
        MARKDOWN_DIR,
        out_dir,
        min_versions=min_versions,
        doc_types=types_filter,
    )
    click.echo(f"Done: {len(results)} groups consolidated, results in {out_dir}")


# ---------------------------------------------------------------------------
# manifest
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--output", type=click.Path(), default="", help="Output directory path.")
@click.option(
    "--doc-type",
    "doc_types",
    multiple=True,
    help="Limit to specific doc type(s). Repeat for multiple. Default: all.",
)
def manifest(output: str, doc_types: tuple[str, ...]) -> None:
    """Generate corpus-manifest.json — complete provenance index for migration."""
    import pathlib

    from vista_docs.analyze.corpus_manifest_runner import run_manifest
    from vista_docs.config import DATA_DIR, MARKDOWN_DIR

    out_dir = pathlib.Path(output) if output else DATA_DIR / "migration"
    types_filter = list(doc_types) if doc_types else None
    click.echo(f"Building corpus manifest from {MARKDOWN_DIR} → {out_dir}")
    if types_filter:
        click.echo(f"  Filtering to doc types: {', '.join(types_filter)}")

    result = run_manifest(MARKDOWN_DIR, out_dir, doc_types=types_filter)
    click.echo(
        f"Done: {result.total_documents} documents, "
        f"{result.total_packages} packages → {out_dir / 'corpus-manifest.json'}"
    )


# ---------------------------------------------------------------------------
# populate-repos
# ---------------------------------------------------------------------------


@cli.command("populate-repos")
@click.option("--output", type=click.Path(), default="", help="Root directory for repos.")
@click.option("--pkg", multiple=True, help="Limit to specific package(s). Repeat for multiple.")
@click.option("--force", is_flag=True, help="Re-populate repos that already exist.")
def populate_repos(output: str, pkg: tuple[str, ...], force: bool) -> None:
    """Populate local git repos from corpus-manifest.json."""
    import pathlib

    from vista_docs.config import DATA_DIR
    from vista_docs.migrate.repo_populator import populate_repos as do_populate

    manifest_path = DATA_DIR / "migration" / "corpus-manifest.json"
    if not manifest_path.exists():
        raise click.ClickException(f"Manifest not found: {manifest_path}\nRun: vista-docs manifest")

    repos_dir = pathlib.Path(output) if output else DATA_DIR / "github-repos"
    packages = list(pkg) if pkg else None

    click.echo(f"Populating repos → {repos_dir}")
    if packages:
        click.echo(f"  Packages: {', '.join(packages)}")

    results = do_populate(manifest_path, repos_dir, packages=packages, force=force)
    total_files = sum(results.values())
    click.echo(
        f"Done: {len(results)} repos created, {total_files} total files committed → {repos_dir}"
    )


# ---------------------------------------------------------------------------
# changelog
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--pkg", multiple=True, help="Limit to specific package(s). Repeat for multiple.")
def changelog(pkg: tuple[str, ...]) -> None:
    """Generate CHANGELOG.md for each package repo from release notes."""

    from vista_docs.config import DATA_DIR
    from vista_docs.migrate.changelog_runner import run_changelog

    manifest_path = DATA_DIR / "migration" / "corpus-manifest.json"
    if not manifest_path.exists():
        raise click.ClickException(f"Manifest not found: {manifest_path}\nRun: vista-docs manifest")

    repos_dir = DATA_DIR / "github-repos"
    packages = list(pkg) if pkg else None

    label = f" [pkg={', '.join(packages)}]" if packages else ""
    click.echo(f"Generating CHANGELOGs{label} → {repos_dir}")

    results = run_changelog(manifest_path, repos_dir, packages=packages)
    total_rn = sum(results.values())
    click.echo(f"Done: {len(results)} repos updated, {total_rn} total release notes")


# ---------------------------------------------------------------------------
# populate-docs
# ---------------------------------------------------------------------------


@cli.command("populate-docs")
@click.option("--pkg", multiple=True, help="Limit to specific package(s). Repeat for multiple.")
def populate_docs(pkg: tuple[str, ...]) -> None:
    """Populate docs/ in each package repo from consolidated masters and originals."""
    from vista_docs.config import DATA_DIR
    from vista_docs.migrate.docs_runner import run_docs

    manifest_path = DATA_DIR / "migration" / "corpus-manifest.json"
    if not manifest_path.exists():
        raise click.ClickException(f"Manifest not found: {manifest_path}\nRun: vista-docs manifest")

    repos_dir = DATA_DIR / "github-repos"
    consolidated_dir = DATA_DIR / "consolidated"
    packages = list(pkg) if pkg else None

    label = f" [pkg={', '.join(packages)}]" if packages else ""
    click.echo(f"Populating docs/{label} → {repos_dir}")

    results = run_docs(manifest_path, repos_dir, consolidated_dir, packages=packages)
    total_files = sum(results.values())
    click.echo(f"Done: {len(results)} repos updated, {total_files} total files → docs/")


# ---------------------------------------------------------------------------
# verify
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--fix", is_flag=True, help="Attempt to fix minor issues automatically.")
def verify(fix: bool) -> None:
    """Sanity-check all pipeline artifacts for consistency."""
    click.echo("Verifying corpus artifacts")
    click.echo("(not yet implemented)")


# ---------------------------------------------------------------------------
# build-all
# ---------------------------------------------------------------------------


@cli.command("build-all")
@click.option("--pkg", multiple=True, help="Limit to specific package(s). Repeat for multiple.")
@click.option("--serve", is_flag=True, help="Start HTTP server after building.")
@click.option("--port", type=int, default=8000, show_default=True, help="HTTP server port.")
def build_all(pkg: tuple[str, ...], serve: bool, port: int) -> None:
    """Run zensical build in every package repo, then optionally serve locally."""
    import http.server
    import os

    from vista_docs.config import DATA_DIR
    from vista_docs.migrate.site_runner import run_build_all

    repos_dir = DATA_DIR / "github-repos"
    packages = list(pkg) if pkg else None

    label = f" [pkg={', '.join(packages)}]" if packages else ""
    click.echo(f"Building sites{label} in {repos_dir}")

    results = run_build_all(repos_dir, packages=packages)
    ok = sum(1 for v in results.values() if v)
    fail = len(results) - ok
    click.echo(f"Done: {ok} built, {fail} failed.")

    if serve:
        click.echo(f"\nServing at http://localhost:{port}/")
        click.echo("  Browse: http://localhost:{port}/vista-pso/site/")
        click.echo("  Ctrl+C to stop.\n")
        os.chdir(repos_dir)
        handler = http.server.SimpleHTTPRequestHandler
        with http.server.HTTPServer(("", port), handler) as httpd:
            httpd.serve_forever()


# ---------------------------------------------------------------------------
# verify-originals
# ---------------------------------------------------------------------------


@cli.command("verify-originals")
@click.option("--pkg", multiple=True, help="Limit to specific package(s). Repeat for multiple.")
def verify_originals(pkg: tuple[str, ...]) -> None:
    """Verify SHA-256 of committed originals against corpus-manifest.json."""
    import sys

    from vista_docs.config import DATA_DIR
    from vista_docs.migrate.verify_builder import summarize_results
    from vista_docs.migrate.verify_runner import run_verify

    manifest_path = DATA_DIR / "migration" / "corpus-manifest.json"
    if not manifest_path.exists():
        raise click.ClickException(f"Manifest not found: {manifest_path}\nRun: vista-docs manifest")

    repos_dir = DATA_DIR / "github-repos"
    packages = list(pkg) if pkg else None

    label = f" [pkg={', '.join(packages)}]" if packages else ""
    click.echo(f"Verifying originals{label} → {repos_dir}")

    results = run_verify(manifest_path, repos_dir, packages=packages)
    summary = summarize_results(results)

    click.echo(
        f"  total={summary['total']}  ok={summary['ok']}  "
        f"mismatch={summary['mismatch']}  missing={summary['missing']}"
    )

    if summary["packages_with_issues"]:
        click.echo(f"  Issues in: {', '.join(summary['packages_with_issues'])}")

    if summary["passed"]:
        click.echo("PASS — all originals intact.")
    else:
        click.echo("FAIL — see warnings above.", err=True)
        sys.exit(1)


# ---------------------------------------------------------------------------
# pipeline
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--pkg", default="", help="Limit to one package namespace.")
@click.option(
    "--from",
    "from_stage",
    type=click.Choice(["crawl", "fetch", "ingest", "survey"]),
    default="crawl",
    show_default=True,
    help="Start from this pipeline stage.",
)
def pipeline(pkg: str, from_stage: str) -> None:
    """Run the full pipeline: crawl → fetch → ingest → survey."""
    stages = ["crawl", "fetch", "ingest", "survey"]
    start = stages.index(from_stage)
    for stage in stages[start:]:
        click.echo(f"Running stage: {stage}")
    click.echo("(not yet implemented)")


if __name__ == "__main__":
    cli()
