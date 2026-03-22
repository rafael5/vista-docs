"""
vista-docs CLI — single entry point with subcommands.

  vista-docs crawl   — crawl VDL catalog → inventory/
  vista-docs fetch   — download DOCX/PDF → raw/
  vista-docs ingest  — convert to markdown → markdown/
  vista-docs survey  — analyse corpus structure → survey/
  vista-docs verify  — sanity-check all artifacts
  vista-docs pipeline — run crawl → fetch → ingest → survey
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
    click.echo("Ingesting documents" + (" [SCAFFOLD]" if scaffold else ""))
    click.echo("(not yet implemented)")


# ---------------------------------------------------------------------------
# survey
# ---------------------------------------------------------------------------


@cli.command()
@click.option("--pkg", default="", help="Limit to one package namespace.")
@click.option("--output", type=click.Path(), default="", help="Output directory path.")
def survey(pkg: str, output: str) -> None:
    """Analyse corpus structure and write survey reports."""
    from vista_docs.config import SURVEY_DIR

    out = output or str(SURVEY_DIR)
    click.echo(f"Surveying corpus → {out}")
    click.echo("(not yet implemented)")


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
