.PHONY: install test test-lf watch lint format mypy cov check push pull hooks \
        crawl fetch ingest survey verify pipeline

install:
	uv sync --extra dev
	$(MAKE) hooks

hooks:
	pre-commit install --hook-type pre-commit --hook-type pre-push

test:
	pytest tests/unit/

test-lf:
	pytest --lf

watch:
	ptw -- --tb=short tests/unit/

lint:
	ruff check src/ tests/

format:
	ruff format src/ tests/

mypy:
	mypy src/

cov:
	pytest tests/unit/ --cov --cov-report=term-missing

check: lint mypy cov

pull:
	git pull origin main

push: check
	git push origin main

# ---------------------------------------------------------------------------
# Pipeline targets — run the vista-docs CLI stages
# ---------------------------------------------------------------------------

crawl:
	vista-docs crawl

fetch:
	vista-docs fetch

ingest:
	vista-docs ingest

survey:
	vista-docs survey

verify:
	vista-docs verify

pipeline:
	vista-docs pipeline
