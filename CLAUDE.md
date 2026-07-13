# CLAUDE.md

Claude Code arbeitet in diesem Repository nach `AGENTS.md` und `docs/agents/WORK_PROTOCOL.md`.

Vor größeren Änderungen sind mindestens `TASKS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, `TESTING.md`, `ROADMAP.md`, `MODELS.md`, `SECURITY.md` und `SKILLS.md` zu lesen. Bei Asset- oder Renderingaufgaben zusätzlich `docs/GRAPHICS_PLAN.md`.

## Verbindlicher Ablauf

1. Agenten-ID und Task-ID festlegen.
2. Eigenen Branch `agent/<task-id>/<agent-id>` verwenden.
3. Eigene Statusdatei unter `docs/agents/status/<agent-id>.md` anlegen.
4. Nur die im Task exklusiv zugewiesenen Pfade bearbeiten.
5. Kleine Commits mit Agent-, Task- und Testangabe erstellen.
6. Tests, visuelle Nachweise und Übergabe dokumentieren.
7. Keine zentralen Governance-, Registry- oder Lockdateien ohne Integrationsauftrag verändern.

Keine geheimen Zugangsdaten, kostenpflichtigen Dienste, Store-Veröffentlichungen oder endgültigen Markenlizenzentscheidungen ohne ausdrückliche Freigabe. Für Maschinen bis dahin ausschließlich generische, markenfreie Designs verwenden.
