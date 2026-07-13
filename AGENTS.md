# AGENTS.md

## Zweck

Dieses Repository wird von mehreren menschlichen und KI-Agenten parallel bearbeitet. Jeder Agent muss jederzeit sichtbar machen:

1. woran er gerade arbeitet,
2. welche Dateien er beansprucht,
3. was er bereits geändert hat,
4. welche Prüfungen durchgeführt wurden,
5. was der nächste Agent wissen muss.

Diese Regeln gelten für Codex, Claude Code, GitHub Copilot, OpenHands, Aider, lokale vLLM-Agenten und weitere Coding-Agenten.

## Vor jeder größeren Änderung lesen

- `TASKS.md`
- `ARCHITECTURE.md`
- `DECISIONS.md`
- `TESTING.md`
- `ROADMAP.md`
- `MODELS.md`
- `SECURITY.md`
- `SKILLS.md`
- `docs/agents/WORK_PROTOCOL.md`
- bei Grafikarbeiten zusätzlich `docs/GRAPHICS_PLAN.md`

## Verbindlicher Agenten-Workflow

### 1. Identität festlegen

Jeder Arbeitslauf verwendet eine stabile Agenten-ID:

```text
<agent>-<task-id>-<kurzname>
```

Beispiel: `codex-GFX-020-wheat-growth`.

### 2. Aufgabe beanspruchen

Vor Code- oder Assetänderungen:

- eine Aufgabe aus `TASKS.md` wählen,
- den zugehörigen GitHub-Issue verwenden, sofern vorhanden,
- eine eigene Statusdatei unter `docs/agents/status/<agent-id>.md` anlegen,
- dort Aufgabe, Branch, beanspruchte Pfade und geplantes Ergebnis eintragen.

Ein Agent darf keine Aufgabe beginnen, deren Pfade bereits in einer aktiven Statusdatei beansprucht werden.

### 3. Eigener Branch

Branchschema:

```text
agent/<task-id>/<agent-id>
```

Keine parallele Arbeit direkt auf `main`. Ein Agent bearbeitet nur seinen Branch und seinen Pfadbereich.

### 4. Pfadbesitz respektieren

Die Arbeitsbereiche in `TASKS.md` und `docs/GRAPHICS_PLAN.md` sind exklusiv. Änderungen außerhalb des eigenen Bereichs sind nur erlaubt, wenn:

- sie für die Aufgabe zwingend notwendig sind,
- die betroffenen Agenten nicht aktiv dieselben Dateien bearbeiten,
- die Abweichung in der Statusdatei dokumentiert wird.

Gemeinsame Dateien wie `TASKS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, zentrale Konfigurationen und Lockfiles werden nur vom Koordinator oder in einem gesonderten Integrations-PR geändert.

### 5. Kleine, nachvollziehbare Commits

Jeder Commit enthält genau einen logischen Schritt. Empfohlenes Format:

```text
<type>(<bereich>): <kurze beschreibung>

Agent: <agent-id>
Task: <task-id>
Tests: <ausgefuehrte pruefungen oder "not run: <grund>">
```

### 6. Status laufend aktualisieren

Die eigene Datei `docs/agents/status/<agent-id>.md` wird aktualisiert:

- vor dem ersten Eingriff,
- nach jedem abgeschlossenen Teilpaket,
- vor Übergabe oder Pull Request.

Pflichtabschnitte:

```markdown
# <agent-id>

- Status: planned | active | blocked | review | done
- Task: <task-id>
- Branch: <branch>
- Started: <ISO-8601>
- Updated: <ISO-8601>

## Arbeitet gerade an

## Beanspruchte Pfade

## Erledigt

## Geänderte Dateien

## Tests und Nachweise

## Entscheidungen und Annahmen

## Blocker

## Übergabe / Nächste Schritte
```

Jeder Agent verändert ausschließlich seine eigene Statusdatei. Der Koordinator darf abgeschlossene Statusdateien archivieren.

### 7. Pull Request

Ein PR muss enthalten:

- Task-ID und Agenten-ID,
- Ziel und abgegrenzten Umfang,
- Liste der geänderten Pfade,
- Tests oder visuelle Nachweise,
- bekannte Einschränkungen,
- Übergabehinweise.

Grafik-PRs benötigen zusätzlich Vorschaubilder oder reproduzierbare Render-Screenshots, LOD-/Polygonangaben, Texturgrößen, Lizenz-/Herkunftsnachweis und eine Aussage zur Android-Performance.

## Verbotene Konfliktmuster

- keine gemeinsame globale Fortschrittsdatei als Schreibziel aller Agenten,
- keine Änderungen in einem fremden aktiven Pfadbereich,
- keine stillen Architekturentscheidungen,
- keine Markenlogos oder realen Maschinenmarken ohne ausdrücklich bestätigte Lizenzentscheidung,
- keine Geheimnisse, Tokens, Zugangsdaten oder proprietären Rohassets im Repository,
- keine kostenpflichtigen Dienste ohne Freigabe,
- keine Veröffentlichung in Stores ohne Freigabe.

## Integrationsreihenfolge

1. Asset- und Datenverträge
2. unabhängige Fachpakete
3. Import-/Renderingintegration
4. automatisierte Validierung
5. visuelle und Performance-Abnahme
6. Merge durch Koordinator

Bei Konflikten gewinnt die dokumentierte Entscheidung in `DECISIONS.md`; fehlt sie, wird ein ADR ergänzt, bevor weiterimplementiert wird.
