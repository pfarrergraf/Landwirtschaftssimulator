from pathlib import Path

from scripts.validate_repository import validate_repository


def test_repository_governance_is_complete() -> None:
    root = Path(__file__).resolve().parents[1]
    assert validate_repository(root) == []
