# AGENTS.md

## Zweck

Dieses Repository kann von einem einzelnen Koordinator oder von mehreren menschlichen und KI-Agenten bearbeitet werden. Jeder Arbeitslauf muss sichtbar machen:

1. woran er gerade arbeitet,
2. welche Dateien oder Pfade er beansprucht,
3. was bereits geändert wurde,
4. welche Prüfungen durchgeführt wurden,
5. was der nächste Arbeitslauf wissen muss.

Diese Regeln gelten für ChatGPT, Codex, Claude Code, GitHub Copilot, OpenHands, Aider, lokale vLLM-Agenten und weitere Coding-Agenten.

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

## Arbeitsmodi

### Modus A – Einzelagent auf `main`

Dieser Modus gilt, wenn die Projektleitung ausdrücklich festlegt, dass aktuell nur ein koordinierender Agent arbeitet.

- Der Koordinator darf direkt auf `main` arbeiten.
- Pull Requests und separate Branches sind optional.
- Vor Beginn wird trotzdem eine eigene Statusdatei unter `docs/agents/status/<agent-id>.md` angelegt oder aktualisiert.
- Änderungen werden in kleinen, logisch getrennten Commits vorgenommen.
- Vor jedem Schreibvorgang ist zu prüfen, ob `main` seit dem letzten Lesen verändert wurde.
- Gemeinsame Planungs-, Governance- und Registry-Dateien dürfen vom Koordinator direkt gepflegt werden.
- Sobald ein weiterer Agent parallel arbeitet, endet Modus A automatisch und Modus B gilt.

### Modus B – Mehrere parallele Agenten

- Jeder Agent verwendet einen eigenen Branch nach dem Schema `agent/<task-id>/<agent-id>`.
- Pfadclaims und Statusdateien sind verbindlich.
- Gemeinsame Dateien werden nur durch den Koordinator oder einen Integration Agent verändert.
- Integration erfolgt per Pull Request.

Der aktuell gültige Modus wird in `DECISIONS.md` dokumentiert.

## Verbindlicher Agenten-Workflow

### 1. Identität festlegen

Jeder Arbeitslauf verwendet eine stabile Agenten-ID:

```text
<agent>-<task-id>-<kurzname>
```

Beispiel: `chatgpt-ARC-001-engine-evaluation`.

### 2. Aufgabe beanspruchen

Vor Code-, Planungs- oder Assetänderungen:

- eine Aufgabe aus `TASKS.md` wählen,
- den zugehörigen GitHub-Issue verwenden, sofern vorhanden,
- eine eigene Statusdatei unter `docs/agents/status/<agent-id>.md` anlegen,
- dort Aufgabe, Arbeitsmodus, Branch oder `main`, beanspruchte Pfade und geplantes Ergebnis eintragen.

Ein Agent darf keine Aufgabe beginnen, deren Pfade bereits in einer aktiven Statusdatei beansprucht werden.

### 3. Branch oder `main` wählen

- In Modus A arbeitet der Koordinator direkt auf `main`.
- In Modus B gilt das Branchschema `agent/<task-id>/<agent-id>`.
- Ein Fachagent darf niemals eigenmächtig von Modus B auf direkte Arbeit auf `main` wechseln.

### 4. Pfadbesitz respektieren

Die Arbeitsbereiche in `TASKS.md` und `docs/GRAPHICS_PLAN.md` sind exklusiv. Änderungen außerhalb des eigenen Bereichs sind nur erlaubt, wenn:

- sie für die Aufgabe zwingend notwendig sind,
- kein anderer aktiver Agent dieselben Dateien bearbeitet,
- die Abweichung in der Statusdatei dokumentiert wird.

Gemeinsame Dateien wie `TASKS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, zentrale Konfigurationen und Lockfiles werden nur vom Koordinator oder in einem gesonderten Integrationsauftrag geändert.

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
- vor Übergabe, Pull Request oder Abschluss auf `main`.

Pflichtabschnitte:

```markdown
# <agent-id>

- Status: planned | active | blocked | review | done
- Task: <task-id>
- Mode: main | branch
- Branch: <branch oder main>
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

### 7. Pull Request oder Direktabschluss

Ein PR oder ein dokumentierter Direktabschluss auf `main` muss enthalten:

- Task-ID und Agenten-ID,
- Ziel und abgegrenzten Umfang,
- Liste der geänderten Pfade,
- Tests oder visuelle Nachweise,
- bekannte Einschränkungen,
- Übergabehinweise.

Grafikänderungen benötigen zusätzlich Vorschaubilder oder reproduzierbare Render-Screenshots, LOD-/Polygonangaben, Texturgrößen, Lizenz-/Herkunftsnachweis und eine Aussage zur Android-Performance.

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
6. Merge oder Direktabschluss durch den Koordinator

Bei Konflikten gewinnt die dokumentierte Entscheidung in `DECISIONS.md`; fehlt sie, wird ein ADR ergänzt, bevor weiterimplementiert wird.
