from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from landwirtschaftssimulator.regression import run_economic_years  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Run deterministic economic-year regression")
    parser.add_argument("--years", type=int, default=100)
    parser.add_argument("--seed", type=int, default=2026)
    args = parser.parse_args()
    summary = run_economic_years(ROOT, years=args.years, seed=args.seed)
    print(f"years={summary.years}")
    print(f"ending_cash_eur={summary.ending_cash_eur}")
    print(f"total_revenue_eur={summary.total_revenue_eur}")
    print(f"total_expenses_eur={summary.total_expenses_eur}")
    print(f"total_harvest_t={summary.total_harvest_t:.3f}")
    print(f"digest={summary.digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
