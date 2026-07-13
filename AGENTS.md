# AGENTS.md

## Zweck

Diese Datei ist der verbindliche Arbeitsvertrag fuer alle KI-Agenten und menschlichen Mitwirkenden in diesem Repository. Sie gilt fuer Codex, Claude Code, GitHub Copilot, OpenHands, Aider, lokale vLLM-Agenten und vergleichbare Werkzeuge.

## Vor jeder groesseren Aenderung lesen

1. `AGENTS.md`
2. `AGENT_BOARD.md`
3. `TASKS.md`
4. `ARCHITECTURE.md`
5. `DECISIONS.md`
6. `TESTING.md`
7. `SECURITY.md`
8. `SKILLS.md`

## Verbindlicher Koordinationsablauf

Jeder Agent muss seine Arbeit in `AGENT_BOARD.md` sichtbar machen.

### Vor Arbeitsbeginn

1. Eine eindeutige Agent-ID waehlen, zum Beispiel `codex-avatar-01`.
2. Unter **Aktive Arbeiten** eine Zeile anlegen.
3. Folgende Angaben eintragen:
   - Agent-ID
   - Ziel und betroffene Dateien
   - Branch
   - Startzeit in UTC
   - Status `CLAIMED`
   - Abhaengigkeiten oder moegliche Konflikte
4. Pruefen, ob ein anderer Agent dieselben Dateien oder dasselbe Subsystem bearbeitet.
5. Bei Konflikt nicht parallel ueberschreiben. Aufgabe enger schneiden oder auf einem separaten Branch arbeiten.

### Waehrend der Arbeit

- Status auf `IN_PROGRESS`, `BLOCKED`, `REVIEW` oder `DONE` setzen.
- Neue Annahmen sofort in `DECISIONS.md` als Vorschlag oder ADR festhalten.
- Umfangsaenderungen im Board dokumentieren.
- Keine fremden aktiven Arbeitszeilen entfernen oder umdeuten.
- Keine unzusammenhaengenden Refactorings in denselben Commit mischen.

### Nach Abschluss

1. Tests und Validierung ausfuehren.
2. In `AGENT_BOARD.md` unter **Abgeschlossene Arbeiten** dokumentieren:
   - Ergebnis
   - geaenderte Dateien
   - Tests und deren Resultat
   - offene Risiken oder Folgeaufgaben
   - Commit oder Pull Request
3. Eigene Zeile aus **Aktive Arbeiten** erst danach entfernen.
4. Neue Folgeaufgaben in `TASKS.md` eintragen.

## Statusdefinitionen

- `CLAIMED`: Aufgabe reserviert, Umsetzung noch nicht begonnen.
- `IN_PROGRESS`: Umsetzung laeuft.
- `BLOCKED`: Externe Entscheidung oder fehlende Voraussetzung verhindert Fortschritt.
- `REVIEW`: Umsetzung abgeschlossen, Pruefung ausstehend.
- `DONE`: Validiert und dokumentiert.

## Branch- und Commit-Regeln

- Keine direkte Arbeit auf `main`, ausser bei ausdruecklich angeordneten Kleinstkorrekturen.
- Branch-Namen: `<typ>/<kurzbeschreibung>`, zum Beispiel `feature/avatar-customization`.
- Commit-Nachrichten nach Conventional Commits, zum Beispiel:
  - `feat: add avatar appearance data model`
  - `test: cover avatar save migration`
  - `docs: record character pipeline decision`
- Ein Commit soll genau eine logisch zusammenhaengende Aenderung enthalten.
- Pull Requests muessen Ziel, Tests, Risiken und Folgeaufgaben nennen.

## Technische Leitplanken

- Zielplattform: Android-faehige 3D-Landwirtschaftssimulation mit reproduzierbaren Container-Builds.
- Architektur modular halten: Spielwelt, Landwirtschaft, Fahrzeuge, Avatare, UI, Speichern/Laden und Plattformintegration getrennt.
- Spiellogik darf nicht unnoetig an eine konkrete Grafik- oder Plattform-API gekoppelt werden.
- Datengetriebene Konfiguration bevorzugen.
- Neue Features brauchen mindestens einen automatisierten Test oder eine dokumentierte manuelle Pruefroutine.
- Performance-Budgets fuer Android frueh pruefen; keine ungemessenen hochaufloesenden Assets oder komplexen Shader als Standard.

## Freigabe und Grenzen

Fuer `pfarrergraf/Landwirtschaftssimulator` duerfen Agenten ohne weitere Rueckfrage:

- Dateien erstellen, aendern und loeschen,
- Branches und Commits anlegen,
- Issues und Pull Requests erstellen,
- Tests und GitHub Actions konfigurieren,
- selbststaendig weiterarbeiten und validieren.

Vorherige Rueckfrage ist erforderlich bei:

- geheimen Zugangsdaten oder produktiven Tokens,
- kostenpflichtigen Diensten oder verbindlichen Ausgaben,
- Veroeffentlichungen im Play Store oder anderen Stores,
- endgueltigen Marken-, Namens- oder Lizenzentscheidungen,
- irreversiblen externen Veroeffentlichungen.

## Sicherheitsregeln

- Niemals Secrets committen.
- `.env.example` enthaelt nur Platzhalter.
- Fremde 3D-Modelle, Texturen, Animationen und Sounds nur mit nachvollziehbarer Lizenzquelle aufnehmen.
- Keine proprietaeren Spiele-Assets kopieren oder nachbauen.
- Generierte Assets muessen Herkunft, Modell/Tool und Nutzungsrechte dokumentieren.

## Definition of Done

Eine Aufgabe ist erst abgeschlossen, wenn:

- die Akzeptanzkriterien erfuellt sind,
- relevante Tests erfolgreich sind,
- Dokumentation und Board aktualisiert sind,
- keine bekannten kritischen Fehler verschwiegen werden,
- Risiken und Folgeaufgaben sichtbar erfasst sind.