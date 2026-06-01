"""
Central configuration: data paths, rate limits, constants, user-agent.

All paths are resolved relative to DATA_DIR, which defaults to ~/data/vista-docs/
and can be overridden via the DATA_DIR environment variable.
"""

from __future__ import annotations

import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Data directory
# ---------------------------------------------------------------------------

DATA_DIR = Path(os.environ.get("DATA_DIR", Path.home() / "data" / "vista-docs"))

INVENTORY_DIR = DATA_DIR / "inventory"
STATE_DIR = DATA_DIR / "state"
RAW_DIR = DATA_DIR / "raw"
MD_IMG_DIR = DATA_DIR / "md-img"
SURVEY_DIR = DATA_DIR / "survey"

# Curated lookup tables checked into the repo (not the runtime data store).
# This is project-rooted data: package_master.yaml, doc_labels.yaml, etc.
# src/vista_docs/config.py → src/vista_docs → src → <project root>
CURATED_DATA_DIR = Path(__file__).resolve().parents[2] / "data"

DB_PATH = STATE_DIR / "pipeline.db"

# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

USER_AGENT = "vista-docs/0.1 (hobbyist research; contact: see github.com/rferrisx/vista-docs)"
REQUEST_DELAY = 1.5  # seconds between requests
REQUEST_TIMEOUT = 30  # seconds per request
MAX_RETRIES = 3
BACKOFF_FACTOR = 2.0

# ---------------------------------------------------------------------------
# VDL base URL
# ---------------------------------------------------------------------------

VDL_BASE = "https://www.va.gov/vdl"
VDL_INDEX = f"{VDL_BASE}/"

# ---------------------------------------------------------------------------
# GitHub publish remote
# ---------------------------------------------------------------------------

VDL_REMOTE = "git@github.com:vistadocs/vdl.git"
