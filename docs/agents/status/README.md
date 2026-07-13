# Agent Status Files

Jeder aktive Agent legt genau eine eigene Datei in diesem Verzeichnis an und verändert keine fremde Statusdatei.

Dateiname:

```text
<agent-id>.md
```

Vorlage:

```markdown
# <agent-id>

- Status: planned | active | blocked | review | done
- Task: <task-id>
- Branch: agent/<task-id>/<agent-id>
- Started: <ISO-8601>
- Updated: <ISO-8601>

## Arbeitet gerade an

<konkreter aktueller Schritt>

## Beanspruchte Pfade

- `<exklusiver/pfad/>`

## Erledigt

- <abgeschlossener Schritt>

## Geänderte Dateien

- `<datei>` – <Änderung>

## Tests und Nachweise

- `<Befehl oder visueller Nachweis>` – <Ergebnis>

## Entscheidungen und Annahmen

- <Annahme oder Verweis auf DECISIONS.md>

## Blocker

- keine

## Übergabe / Nächste Schritte

- <präzise Übergabe>
```

Nach Merge darf der Koordinator die Datei nach `docs/agents/archive/<yyyy-mm>/` verschieben.
