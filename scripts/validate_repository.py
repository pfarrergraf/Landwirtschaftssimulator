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
    "game/godot/project.godot",
    "game/godot/scenes/main.tscn",
    "game/godot/export_presets.cfg",
    "website/index.html",
    "website/styles.css",
    "website/app.js",
    "wrangler.toml",
    ".github/workflows/build-android.yml",
    ".github/workflows/build-website.yml",
)


def _read_text(root: Path, relative_path: str) -> str:
    path = root / relative_path
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    for relative_path in REQUIRED_FILES:
        path = root / relative_path
        if not path.is_file():
            errors.append(f"Missing required file: {relative_path}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"Required file is empty: {relative_path}")

    agents_text = _read_text(root, "AGENTS.md")
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

    android_workflow = _read_text(root, ".github/workflows/build-android.yml")
    if android_workflow:
        if "game/godot/" not in android_workflow:
            errors.append("Android workflow does not use canonical game/godot/ path")
        if "apps/game/" in android_workflow:
            errors.append("Android workflow still references legacy apps/game/ path")
        for required_fragment in (
            "landwirtschaftssimulator-debug.apk",
            "actions/upload-artifact",
            "gh release create",
        ):
            if required_fragment not in android_workflow:
                errors.append(
                    f"Android workflow is missing deployment fragment: {required_fragment}"
                )

    website_workflow = _read_text(root, ".github/workflows/build-website.yml")
    if website_workflow:
        if '"website/**"' not in website_workflow:
            errors.append("Website workflow does not watch canonical website/ path")
        if "apps/website/public" in website_workflow:
            errors.append(
                "Website workflow still references legacy apps/website/public path"
            )
        for required_fragment in (
            "wrangler deploy --dry-run",
            "actions/upload-artifact",
        ):
            if required_fragment not in website_workflow:
                errors.append(
                    f"Website workflow is missing deployment fragment: {required_fragment}"
                )

    wrangler_text = _read_text(root, "wrangler.toml")
    if wrangler_text and 'directory = "./website"' not in wrangler_text:
        errors.append("wrangler.toml does not publish the canonical website directory")

    readme_text = _read_text(root, "README.md")
    for canonical_path in ("game/godot/", "website/", "build/android/"):
        if canonical_path not in readme_text:
            errors.append(f"README.md does not document canonical path {canonical_path}")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository governance and deployment validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
