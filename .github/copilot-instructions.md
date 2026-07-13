# GitHub Copilot Repository Instructions

Before significant changes, read `AGENTS.md`, `AGENT_BOARD.md`, `TASKS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, `TESTING.md`, `SECURITY.md`, and `SKILLS.md`.

## Mandatory coordination

- Claim work in `AGENT_BOARD.md` before editing.
- Record agent ID, goal, files/subsystems, branch, UTC start time, status, and conflicts.
- Do not overwrite files claimed by another active agent without resolving the conflict.
- After completion, record changed files, tests/results, commit or PR, risks, and follow-up tasks.

## Engineering rules

- Keep game logic modular and testable outside full 3D scenes where possible.
- Separate character, farming, vehicle, world, UI, savegame, and platform responsibilities.
- Use stable IDs and versioned serializable schemas for avatar and save data.
- Prefer data-driven configuration over hard-coded asset names.
- Treat Android performance as part of feature acceptance.
- Add tests or a documented manual validation procedure for every feature.
- Never commit secrets, proprietary copied assets, or unlicensed media.

## Authorization boundaries

Repository files, branches, commits, issues, pull requests, tests, and GitHub Actions may be changed autonomously. Ask before using secrets, paid services, publishing to stores, or making final brand and license decisions.