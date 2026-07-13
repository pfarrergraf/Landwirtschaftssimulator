.PHONY: bootstrap validate test balance all

bootstrap:
	uv sync

validate:
	uv run python tools/validator/validate_data.py

test:
	uv run python -m unittest discover -s tests -v

balance:
	uv run python tools/balancer/simulate_year.py

all: bootstrap validate test balance
