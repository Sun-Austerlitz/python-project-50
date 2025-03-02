install:
	uv sync

test:
	uv run pytest

build:
	uv build

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml tests/

lint:
	uv run ruff check

check: test lint

.PHONY: install test lint selfcheck check build