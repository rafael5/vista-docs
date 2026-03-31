"""
vista-docs CLI — single entry point with subcommands.

  vista-docs crawl        — crawl VDL catalog → inventory/
  vista-docs fetch        — download DOCX/PDF → raw/
  vista-docs ingest       — convert to markdown → md-img/
  vista-docs enrich       — populate YAML frontmatter in-place
  vista-docs survey       — analyse corpus structure → state.db
  vista-docs headings     — heading frequency analysis → state.db
  vista-docs consolidate  — master + addenda consolidation → consolidated/
  vista-docs manifest     — build corpus-manifest.json index
  vista-docs publish      — write human-browsable publish/ tree from consolidated/
  vista-docs push         — publish then commit + push markdown to GitHub
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
@click.option("--scaffold", is_flag=True, help="Generate frontmatter stubs only (no conversion).")
@click.option("--force", is_flag=True, help="Re-ingest even if output exists.")
def ingest(pkg: str, scaffold: bool, force: bool) -> None:
    """Convert fetched DOCX to markdown + images in ~/data/vista-docs/md-img/."""
    from vista_docs.config import DB_PATH, MD_IMG_DIR
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
        result = ingest_entry(entry, MD_IMG_DIR, scaffold=scaffold, force=force)
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

    from vista_docs.config import MD_IMG_DIR

    result = enrich_corpus(MD_IMG_DIR, to_enrich, force=force)
    click.echo(f"Done: {result['ok']} ok, {result['skipped']} skipped, {result['errors']} errors.")


# ---------------------------------------------------------------------------
# sync
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--pkg", default="", help="Limit to one app_code folder (e.g. PSO).")
@click.option("--force", is_flag=True, help="Re-sync even if already synced.")
def sync(pkg: str, force: bool) -> None:
    """Sync enriched inventory metadata into markdown frontmatter in ~/data/vista-docs/md-img/."""
    from vista_docs.config import INVENTORY_DIR, MD_IMG_DIR
    from vista_docs.enrich.sync import sync_inventory_corpus

    enriched_csv = INVENTORY_DIR / "vdl_inventory_enriched.csv"
    if not enriched_csv.exists():
        raise click.ClickException(f"Enriched inventory not found: {enriched_csv}")

    label = f" [pkg={pkg.upper()}]" if pkg else ""
    click.echo(f"Syncing inventory fields into markdown frontmatter{label}")

    result = sync_inventory_corpus(MD_IMG_DIR, enriched_csv, pkg=pkg, force=force)
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
    from vista_docs.config import DB_PATH, MD_IMG_DIR, SURVEY_DIR
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

    result = run_survey(MD_IMG_DIR, to_survey, out_dir, pkg=pkg)
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
    from vista_docs.config import MD_IMG_DIR, SURVEY_DIR

    out_dir = __import__("pathlib").Path(output) if output else SURVEY_DIR / "heading_analysis"
    click.echo(f"Analysing headings in {MD_IMG_DIR} → {out_dir}")

    profiles = run_heading_analysis(
        MD_IMG_DIR,
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
    from vista_docs.config import DATA_DIR, MD_IMG_DIR

    out_dir = pathlib.Path(output) if output else DATA_DIR / "consolidated"
    types_filter = list(doc_types) if doc_types else None
    click.echo(f"Consolidating {MD_IMG_DIR} → {out_dir}")
    if types_filter:
        click.echo(f"  Filtering to doc types: {', '.join(types_filter)}")

    results = run_consolidation(
        MD_IMG_DIR,
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
    from vista_docs.config import DATA_DIR, MD_IMG_DIR

    out_dir = pathlib.Path(output) if output else DATA_DIR / "migration"
    types_filter = list(doc_types) if doc_types else None
    click.echo(f"Building corpus manifest from {MD_IMG_DIR} → {out_dir}")
    if types_filter:
        click.echo(f"  Filtering to doc types: {', '.join(types_filter)}")

    result = run_manifest(MD_IMG_DIR, out_dir, doc_types=types_filter)
    click.echo(
        f"Done: {result.total_documents} documents, "
        f"{result.total_packages} packages → {out_dir / 'corpus-manifest.json'}"
    )


# ---------------------------------------------------------------------------
# publish
# ---------------------------------------------------------------------------


@cli.command()
@click.option(
    "--output",
    type=click.Path(),
    default="",
    help="Output directory (default: ~/data/vista-docs/publish/).",
)
@click.option("--pkg", multiple=True, help="Limit to specific package(s). Repeat for multiple.")
@click.option("--force", is_flag=True, help="Overwrite existing publish/ output.")
def publish(output: str, pkg: tuple[str, ...], force: bool) -> None:
    """Write human-browsable publish/ tree from consolidated/ and md-img/."""
    import pathlib

    from vista_docs.config import DATA_DIR
    from vista_docs.publish.runner import run_publish

    manifest_path = DATA_DIR / "migration" / "corpus-manifest.json"
    if not manifest_path.exists():
        raise click.ClickException(f"Manifest not found: {manifest_path}\nRun: vista-docs manifest")

    out_dir = pathlib.Path(output) if output else DATA_DIR / "publish"
    consolidated_dir = DATA_DIR / "consolidated"
    md_img_dir = DATA_DIR / "md-img"
    inventory_csv = DATA_DIR / "inventory" / "vdl_inventory_enriched.csv"
    packages = list(pkg) if pkg else None

    if out_dir.exists() and not force:
        raise click.ClickException(
            f"Output directory already exists: {out_dir}\nUse --force to overwrite."
        )

    label = f" [pkg={', '.join(packages)}]" if packages else ""
    click.echo(f"Publishing{label} → {out_dir}")

    results = run_publish(
        consolidated_dir=consolidated_dir,
        md_img_dir=md_img_dir,
        manifest_path=manifest_path,
        inventory_csv=inventory_csv,
        out_dir=out_dir,
        packages=packages,
        force=force,
    )
    click.echo(
        f"Done: {results['packages']} packages, "
        f"{results['anchor_files']} anchor docs, "
        f"{results['patch_files']} patch docs, "
        f"{results['image_dirs']} image dirs → {out_dir}"
    )


# ---------------------------------------------------------------------------
# push
# ---------------------------------------------------------------------------


@cli.command()
@click.option(
    "--remote",
    default="",
    help="Git remote URL (default: git@github.com:vistadocs/vdl.git).",
)
@click.option("--message", default="", help="Override the auto-generated commit message.")
@click.option(
    "--no-publish",
    "skip_publish",
    is_flag=True,
    help="Skip regenerating publish/ — push the current contents as-is.",
)
def push(remote: str, message: str, skip_publish: bool) -> None:
    """Publish then commit and push markdown docs to GitHub (images excluded)."""

    from vista_docs.config import DATA_DIR, VDL_REMOTE
    from vista_docs.publish.runner import run_publish, run_push

    out_dir = DATA_DIR / "publish"
    remote_url = remote or VDL_REMOTE

    if not skip_publish:
        manifest_path = DATA_DIR / "migration" / "corpus-manifest.json"
        if not manifest_path.exists():
            raise click.ClickException(
                f"Manifest not found: {manifest_path}\nRun: vista-docs manifest"
            )
        click.echo(f"Publishing → {out_dir}")
        results = run_publish(
            consolidated_dir=DATA_DIR / "consolidated",
            md_img_dir=DATA_DIR / "md-img",
            manifest_path=manifest_path,
            inventory_csv=DATA_DIR / "inventory" / "vdl_inventory_enriched.csv",
            out_dir=out_dir,
            force=True,
        )
        click.echo(
            f"  {results['packages']} packages, "
            f"{results['anchor_files']} anchor docs, "
            f"{results['patch_files']} patch docs"
        )
    elif not out_dir.exists():
        raise click.ClickException(
            f"publish/ not found: {out_dir}\nRun without --no-publish to generate it first."
        )

    click.echo(f"Pushing markdown to {remote_url} ...")
    pushed = run_push(
        out_dir=out_dir,
        remote_url=remote_url,
        commit_message=message or None,
    )
    if pushed:
        click.echo("Done — pushed to GitHub.")
    else:
        click.echo("Nothing new to push.")


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
