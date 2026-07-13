# Multi-Agent Work Protocol

## Ziel

Mehrere Agenten sollen gleichzeitig Fortschritt erzielen, ohne dieselben Dateien, Assets oder Entscheidungen parallel zu verändern.

## Rollen

### Coordinator

- pflegt `TASKS.md`, `ROADMAP.md`, `DECISIONS.md` und Integrationsreihenfolge,
- zerlegt Arbeit in disjunkte Pfadbereiche,
- prüft Übergaben und führt Integrations-PRs zusammen,
- entscheidet nicht eigenmächtig über kostenpflichtige Dienste, Store-Veröffentlichungen oder endgültige Markenlizenzen.

### Domain Agent

- bearbeitet genau einen fachlichen Task,
- besitzt ausschließlich die im Task genannten Pfade,
- liefert Datenverträge, Tests und Übergabehinweise.

### Integration Agent

- verbindet bereits freigegebene Pakete,
- verändert gemeinsame Dateien nur in einem gesonderten Integrations-PR,
- dokumentiert Abhängigkeiten und Regressionen.

### QA Agent

- verändert Produktivcode nur bei ausdrücklich zugewiesenen Fixes,
- reproduziert Fehler,
- ergänzt Tests, Screenshots, Performance-Messungen und Abnahmeprotokolle.

## Konfliktarme Aufteilung

Jeder Task enthält:

- eindeutige Task-ID,
- exklusiven Pfadbereich,
- Eingabevertrag,
- Ausgabevertrag,
- Abnahmekriterien,
- Abhängigkeiten.

Zwei aktive Tasks dürfen denselben exklusiven Pfad nicht beanspruchen. Gemeinsame Dateien werden nur durch den Coordinator oder einen Integration Agent geändert.

## Statusdateien statt globalem Schreibkonflikt

Jeder Agent führt eine eigene Datei:

```text
docs/agents/status/<agent-id>.md
```

Die Datei ist gleichzeitig Arbeitsankündigung, Fortschrittsprotokoll und Übergabedokument. Andere Agenten lesen sie, verändern sie aber nicht.

Abgeschlossene Dateien können nach Merge nach folgendem Schema verschoben werden:

```text
docs/agents/archive/<yyyy-mm>/<agent-id>.md
```

## Claim-Verfahren

1. Offenen Task in `TASKS.md` oder GitHub Issues wählen.
2. Prüfen, ob unter `docs/agents/status/` bereits ein aktiver Claim dieselben Pfade nennt.
3. Eigenen Branch anlegen.
4. Eigene Statusdatei mit `Status: active` committen.
5. Erst danach Produktivdateien ändern.

Bei gleichzeitigem Claim gewinnt der zuerst auf GitHub sichtbare Commit. Der spätere Agent muss einen anderen Task wählen oder seinen Pfadbereich neu zuschneiden.

## Übergabevertrag

Eine Übergabe ist erst vollständig, wenn dokumentiert sind:

- aktueller Stand,
- geänderte Dateien,
- noch offene Punkte,
- reproduzierbare Befehle,
- Testresultate,
- bekannte Risiken,
- Input/Output-Schnittstellen,
- Assetherkunft und Lizenzstatus bei Grafiken.

## Gemeinsame Integrationspunkte

Folgende Dateien sind standardmäßig koordinatorgeschützt:

- `TASKS.md`
- `ROADMAP.md`
- `ARCHITECTURE.md`
- `DECISIONS.md`
- `CHANGELOG.md`
- Lockfiles
- zentrale Engine-/Build-Konfiguration
- zentrale Asset-Registry

Fachagenten schlagen Änderungen daran im PR-Text oder in ihrer Statusdatei vor. Die tatsächliche Änderung erfolgt gesammelt in einem Integrations-PR.

## Definition of Done

Ein Task gilt als erledigt, wenn:

- alle Abnahmekriterien erfüllt sind,
- Tests und/oder visuelle Nachweise vorhanden sind,
- keine Geheimnisse oder ungeklärten Fremdrechte enthalten sind,
- Statusdatei auf `review` oder `done` steht,
- Übergabeabschnitt vollständig ist,
- PR klein genug ist, um fachlich geprüft zu werden.
