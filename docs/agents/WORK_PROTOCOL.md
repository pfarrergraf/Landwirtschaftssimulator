# Agent Work Protocol

## Ziel

Das Repository soll sowohl mit einem einzelnen koordinierenden Agenten als auch mit mehreren parallelen Agenten sicher und nachvollziehbar weiterentwickelt werden.

## Betriebsmodi

### Modus A – Einzelagent

Modus A gilt, wenn die Projektleitung ausdrücklich festlegt, dass aktuell nur ein koordinierender Agent arbeitet.

- Direkte Änderungen auf `main` sind erlaubt.
- Branches und Pull Requests sind optional.
- Eine eigene Statusdatei bleibt Pflicht.
- Der Agent liest die betroffene Datei unmittelbar vor jedem Update erneut, damit neuere Änderungen nicht überschrieben werden.
- Jeder Commit enthält nur einen logisch zusammenhängenden Schritt.
- Der Koordinator darf zentrale Planungs-, Governance-, Registry- und Integrationsdateien pflegen.

### Modus B – Mehrere Agenten

Modus B gilt automatisch, sobald mehr als ein Agent gleichzeitig arbeitet.

- Jeder Agent arbeitet auf einem eigenen Branch.
- Exklusive Pfadbereiche und Claims sind verbindlich.
- Zentrale Dateien bleiben koordinatorgeschützt.
- Integration erfolgt über Pull Requests.

Der aktive Modus wird in `DECISIONS.md` festgehalten.

## Rollen

### Coordinator

- pflegt `TASKS.md`, `ROADMAP.md`, `DECISIONS.md` und die Integrationsreihenfolge,
- zerlegt Arbeit in disjunkte Pfadbereiche,
- prüft Übergaben,
- führt in Modus B Integrations-PRs zusammen,
- darf in Modus A zentrale Dateien direkt auf `main` pflegen,
- entscheidet nicht eigenmächtig über kostenpflichtige Dienste, Store-Veröffentlichungen oder endgültige Markenlizenzen.

### Domain Agent

- bearbeitet genau einen fachlichen Task,
- besitzt ausschließlich die im Task genannten Pfade,
- liefert Datenverträge, Tests und Übergabehinweise.

### Integration Agent

- verbindet bereits freigegebene Pakete,
- verändert gemeinsame Dateien nur mit Integrationsauftrag,
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

## Statusdateien

Jeder Agent führt eine eigene Datei:

```text
docs/agents/status/<agent-id>.md
```

Die Datei ist Arbeitsankündigung, Fortschrittsprotokoll und Übergabedokument. Andere Agenten lesen sie, verändern sie aber nicht.

Abgeschlossene Dateien können nach folgendem Schema archiviert werden:

```text
docs/agents/archive/<yyyy-mm>/<agent-id>.md
```

## Claim-Verfahren in Modus A

1. Task in `TASKS.md` oder GitHub Issues wählen.
2. Prüfen, ob eine aktive Statusdatei denselben Pfad beansprucht.
3. Eigene Statusdatei mit `Mode: main` und `Status: active` anlegen.
4. Betroffene Datei unmittelbar vor dem Schreiben erneut lesen.
5. Änderungen direkt auf `main` in kleinen Commits durchführen.
6. Statusdatei mit Ergebnissen und Tests abschließen.

## Claim-Verfahren in Modus B

1. Offenen Task in `TASKS.md` oder GitHub Issues wählen.
2. Prüfen, ob unter `docs/agents/status/` bereits ein aktiver Claim dieselben Pfade nennt.
3. Eigenen Branch `agent/<task-id>/<agent-id>` anlegen.
4. Eigene Statusdatei mit `Mode: branch` und `Status: active` committen.
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
- Input-/Output-Schnittstellen,
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

In Modus A darf der Coordinator diese Dateien direkt auf `main` ändern. In Modus B schlagen Fachagenten Änderungen im PR-Text oder in ihrer Statusdatei vor; die tatsächliche Änderung erfolgt gesammelt durch den Coordinator oder Integration Agent.

## Definition of Done

Ein Task gilt als erledigt, wenn:

- alle Abnahmekriterien erfüllt sind,
- Tests und/oder visuelle Nachweise vorhanden sind,
- keine Geheimnisse oder ungeklärten Fremdrechte enthalten sind,
- die Statusdatei auf `review` oder `done` steht,
- der Übergabeabschnitt vollständig ist,
- Änderungen klein genug sind, um fachlich geprüft zu werden.
