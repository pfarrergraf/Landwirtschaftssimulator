from __future__ import annotations

from pathlib import Path


REQUIRED_FILES = (
    "AGENTS.md",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    "TASKS.md",
    "ARCHITECTURE.md",
    "DECISIONS.md",
    "TESTING.md",
    "ROADMAP.md",
    "CHANGELOG.md",
    "PROMPTS.md",
    "EVALS.md",
    "MODELS.md",
    "SECURITY.md",
    "SKILLS.md",
    "docs/GRAPHICS_PLAN.md",
    "docs/agents/WORK_PROTOCOL.md",
    "docs/agents/status/README.md",
)


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    for relative_path in REQUIRED_FILES:
        path = root / relative_path
        if not path.is_file():
            errors.append(f"Missing required file: {relative_path}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"Required file is empty: {relative_path}")

    agents_text = (root / "AGENTS.md").read_text(encoding="utf-8")
    for required_reference in (
        "TASKS.md",
        "ARCHITECTURE.md",
        "DECISIONS.md",
        "TESTING.md",
        "MODELS.md",
        "SECURITY.md",
        "SKILLS.md",
    ):
        if required_reference not in agents_text:
            errors.append(f"AGENTS.md does not reference {required_reference}")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository governance validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
