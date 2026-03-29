"""
I/O layer for running `zensical build` across all package repos.

Excluded from unit-test coverage (I/O layer).
"""

from __future__ import annotations

import logging
import subprocess
import sys
from pathlib import Path

log = logging.getLogger(__name__)


def _zensical_bin() -> str:
    """Return the zensical binary co-located with the running Python interpreter."""
    candidate = Path(sys.executable).parent / "zensical"
    if candidate.exists():
        return str(candidate)
    return "zensical"  # fall back to PATH


def run_build_all(
    repos_dir: Path,
    packages: list[str] | None = None,
) -> dict[str, bool]:
    """
    Run `zensical build` in each vista-{pkg} directory under repos_dir.

    Args:
        repos_dir: Root directory containing vista-{pkg}/ repos.
        packages:  If provided, only build these packages. None = all.

    Returns:
        Dict of {app_code: success} for every attempted build.
    """
    zensical = _zensical_bin()

    if packages:
        target = {p.upper() for p in packages}
        dirs = sorted(
            d
            for d in repos_dir.iterdir()
            if d.is_dir()
            and d.name.startswith("vista-")
            and d.name.removeprefix("vista-").upper() in target
        )
    else:
        dirs = sorted(d for d in repos_dir.iterdir() if d.is_dir() and d.name.startswith("vista-"))

    results: dict[str, bool] = {}

    for repo_dir in dirs:
        app_code = repo_dir.name.removeprefix("vista-").upper()
        toml = repo_dir / "zensical.toml"
        if not toml.exists():
            log.warning("%-8s no zensical.toml — skipping", app_code)
            results[app_code] = False
            continue

        try:
            subprocess.run(
                [zensical, "build"],
                cwd=repo_dir,
                check=True,
                capture_output=True,
                text=True,
            )
            log.info("%-8s built → %s/site/", app_code, repo_dir.name)
            results[app_code] = True
        except subprocess.CalledProcessError as e:
            log.warning("%-8s build failed: %s", app_code, e.stderr.strip()[:120])
            results[app_code] = False

    return results
