# CLAUDE.md

Claude Code arbeitet in diesem Repository nach `AGENTS.md` und `docs/agents/WORK_PROTOCOL.md`.

Vor größeren Änderungen sind mindestens `TASKS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, `TESTING.md`, `ROADMAP.md`, `MODELS.md`, `SECURITY.md` und `SKILLS.md` zu lesen. Bei Asset- oder Renderingaufgaben zusätzlich `docs/GRAPHICS_PLAN.md`.

## Verbindlicher Ablauf

1. Agenten-ID und Task-ID festlegen.
2. Den in `DECISIONS.md` dokumentierten Arbeitsmodus prüfen.
3. Eigene Statusdatei unter `docs/agents/status/<agent-id>.md` anlegen oder aktualisieren.
4. In Einzelagent-Modus darf der Coordinator direkt auf `main` arbeiten.
5. In Mehragenten-Modus einen Branch `agent/<task-id>/<agent-id>` verwenden.
6. Nur die im Task exklusiv zugewiesenen Pfade bearbeiten.
7. Kleine Commits mit Agent-, Task- und Testangabe erstellen.
8. Tests, visuelle Nachweise und Übergabe dokumentieren.
9. Zentrale Governance-, Registry- oder Lockdateien nur als Coordinator oder mit Integrationsauftrag verändern.

Vor jedem direkten Update auf `main` muss die Zieldatei erneut gelesen werden, um neuere Änderungen nicht zu überschreiben.

Keine geheimen Zugangsdaten, kostenpflichtigen Dienste, Store-Veröffentlichungen oder endgültigen Markenlizenzentscheidungen ohne ausdrückliche Freigabe. Für Maschinen bis dahin ausschließlich generische, markenfreie Designs verwenden.
