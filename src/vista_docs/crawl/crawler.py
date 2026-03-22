"""
I/O orchestrator for VDL crawling.

Combines session.py (HTTP) and parser.py (pure parsing) to produce
a complete Section → Application → Document hierarchy from the live VDL.
"""

from __future__ import annotations

import csv
import json
import logging
from pathlib import Path

from vista_docs.config import VDL_BASE
from vista_docs.crawl.parser import (
    parse_application_page,
    parse_index,
    parse_section_page,
)
from vista_docs.crawl.session import get_with_delay, make_session
from vista_docs.models.catalog import Application, Document, Section

logger = logging.getLogger(__name__)


def crawl(
    max_apps: int | None = None,
    delay: float = 1.5,
) -> list[Section]:
    """
    Crawl the full VDL catalog.

    Returns a list of Sections, each with Applications and Documents populated.
    max_apps limits the total applications crawled (for testing).
    """
    session = make_session()
    session.headers["User-Agent"]  # already set in make_session()

    logger.info("Fetching VDL index: %s", VDL_BASE)
    resp = get_with_delay(session, VDL_BASE)
    resp.raise_for_status()
    sections = parse_index(resp.text)
    logger.info("Found %d sections", len(sections))

    apps_crawled = 0
    for section in sections:
        logger.info("Section: %s", section.name)
        resp = get_with_delay(session, section.url)
        if resp.status_code != 200:
            logger.warning("Skipping section %s — HTTP %d", section.name, resp.status_code)
            continue
        apps = parse_section_page(resp.text)
        for app in apps:
            if max_apps is not None and apps_crawled >= max_apps:
                break
            logger.info("  App: %s (%s)", app.name, app.status)
            resp2 = get_with_delay(session, app.url)
            if resp2.status_code == 200:
                app.documents = parse_application_page(resp2.text, base_url=resp2.url)
                logger.info("    → %d documents", len(app.documents))
            else:
                logger.warning("    Skipping app %s — HTTP %d", app.name, resp2.status_code)
            section.applications.append(app)
            apps_crawled += 1

    return sections


def to_flat_rows(sections: list[Section]) -> list[dict]:
    """Flatten Section → Application → Document hierarchy into CSV rows."""
    rows = []
    for section in sections:
        for app in section.applications:
            for doc in app.documents:
                rows.append(
                    {
                        "section_name": section.name,
                        "app_name": app.name,
                        "app_code": app.app_code,
                        "app_status": app.status,
                        "decommission_date": app.decommission_date,
                        "doc_title": doc.title,
                        "doc_type": doc.doc_type_label,
                        "filename": doc.filename,
                        "file_ext": doc.file_ext,
                        "doc_date": doc.file_date,
                        "doc_url": doc.url,
                        "app_url": app.url,
                    }
                )
    return rows


def write_csv(rows: list[dict], path: Path) -> None:
    if not rows:
        logger.warning("No rows to write to %s", path)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    logger.info("Wrote %d rows → %s", len(rows), path)


def write_json(sections: list[Section], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    def _doc_dict(d: Document) -> dict:
        return {
            "title": d.title,
            "url": d.url,
            "filename": d.filename,
            "file_ext": d.file_ext,
            "doc_type": d.doc_type_label,
            "date": d.file_date,
        }

    def _app_dict(a: Application) -> dict:
        return {
            "name": a.name,
            "app_code": a.app_code,
            "status": a.status,
            "url": a.url,
            "documents": [_doc_dict(d) for d in a.documents],
        }

    data = [
        {
            "name": s.name,
            "url": s.url,
            "applications": [_app_dict(a) for a in s.applications],
        }
        for s in sections
    ]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    logger.info("Wrote JSON → %s", path)
