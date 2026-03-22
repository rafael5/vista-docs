.PHONY: install test test-lf watch lint format mypy cov check push pull hooks \
        crawl fetch ingest survey verify pipeline

PYTHON := .venv/bin/python
PYTEST  := .venv/bin/pytest
RUFF    := .venv/bin/ruff
MYPY    := .venv/bin/mypy
PRE_COMMIT := .venv/bin/pre-commit
VISTA   := .venv/bin/vista-docs

install:
	uv sync --extra dev
	$(MAKE) hooks

hooks:
	$(PRE_COMMIT) install --hook-type pre-commit --hook-type pre-push

test:
	$(PYTEST) tests/unit/

test-lf:
	$(PYTEST) --lf

watch:
	.venv/bin/ptw -- --tb=short tests/unit/

lint:
	$(RUFF) check src/ tests/

format:
	$(RUFF) format src/ tests/

mypy:
	$(MYPY) src/

cov:
	$(PYTEST) tests/unit/ --cov --cov-report=term-missing

check: lint mypy cov

pull:
	git pull origin main

push: check
	git push origin main

# ---------------------------------------------------------------------------
# Pipeline targets — run the vista-docs CLI stages
# ---------------------------------------------------------------------------

crawl:
	$(VISTA) crawl

fetch:
	$(VISTA) fetch

ingest:
	$(VISTA) ingest

survey:
	$(VISTA) survey

verify:
	$(VISTA) verify

pipeline:
	$(VISTA) pipeline
