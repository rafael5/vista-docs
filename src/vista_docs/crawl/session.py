"""I/O thin layer: requests.Session with rate limiting and retry."""

from __future__ import annotations

import logging
import time

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from vista_docs.config import (
    BACKOFF_FACTOR,
    MAX_RETRIES,
    REQUEST_DELAY,
    REQUEST_TIMEOUT,
    USER_AGENT,
)

logger = logging.getLogger(__name__)


def make_session() -> requests.Session:
    """Create a configured requests.Session for VDL crawling."""
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    retry = Retry(
        total=MAX_RETRIES,
        backoff_factor=BACKOFF_FACTOR,
        status_forcelist=[500, 502, 503, 504],
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def get_with_delay(session: requests.Session, url: str) -> requests.Response:
    """GET url, then sleep REQUEST_DELAY seconds to be polite."""
    logger.debug("GET %s", url)
    resp = session.get(url, timeout=REQUEST_TIMEOUT)
    time.sleep(REQUEST_DELAY)
    return resp
