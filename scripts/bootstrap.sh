#!/usr/bin/env bash
set -euo pipefail
uv sync
uv run python tools/validator/validate_data.py
uv run python -m unittest discover -s tests -v
