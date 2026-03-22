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
import sys

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
@click.option("--delay", type=float, default=1.5, show_default=True, help="Seconds between requests.")
@click.option("--snapshot", is_flag=True, help="Save a dated snapshot of the inventory.")
def crawl(delay: float, snapshot: bool) -> None:
    """Crawl VDL catalog and write inventory CSV/JSON to ~/data/vista-docs/inventory/."""
    from vista_docs.config import INVENTORY_DIR
    INVENTORY_DIR.mkdir(parents=True, exist_ok=True)
    click.echo(f"Crawling VDL → {INVENTORY_DIR}")
    click.echo("(not yet implemented)")


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
    from vista_docs.config import DB_PATH
    click.echo(f"Fetching documents (db: {DB_PATH})" + (" [DRY RUN]" if dry_run else ""))
    click.echo("(not yet implemented)")


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
