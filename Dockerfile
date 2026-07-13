FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
WORKDIR /workspace
COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen || uv sync
COPY . .
CMD ["sh", "-lc", "uv run python tools/validator/validate_data.py && uv run python -m unittest discover -s tests -v && uv run python tools/balancer/simulate_year.py"]
