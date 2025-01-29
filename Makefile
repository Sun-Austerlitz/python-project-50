install:
	uv sync

run:
	uv run hexlet-python-package

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml tests/

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build