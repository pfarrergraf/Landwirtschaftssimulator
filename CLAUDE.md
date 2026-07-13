# CLAUDE.md

## Verbindlicher Einstieg

Vor groesseren Aenderungen lesen:

1. `AGENTS.md`
2. `AGENT_BOARD.md`
3. `TASKS.md`
4. `ARCHITECTURE.md`
5. `DECISIONS.md`
6. `TESTING.md`
7. `SECURITY.md`
8. `SKILLS.md`

## Claude-Code-Arbeitsweise

- Vor Beginn eine eindeutige Agent-ID in `AGENT_BOARD.md` eintragen.
- Betroffene Dateien und Subsysteme reservieren.
- Bestehende aktive Arbeiten nicht ueberschreiben.
- Kleine, pruefbare Schritte mit fokussierten Commits bevorzugen.
- Nach jedem abgeschlossenen Arbeitspaket Tests ausfuehren und Board aktualisieren.
- Architekturentscheidungen nicht stillschweigend treffen; in `DECISIONS.md` dokumentieren.
- Neue Aufgaben und Folgeprobleme in `TASKS.md` erfassen.

## Projektgrenzen

Ohne weitere Rueckfrage sind Repository-Aenderungen, Branches, Commits, Issues, Pull Requests, Tests und GitHub Actions erlaubt.

Rueckfrage ist erforderlich bei Secrets, kostenpflichtigen Diensten, Store-Veroeffentlichungen sowie endgueltigen Marken- oder Lizenzentscheidungen.

## Technische Leitlinien

- Android-first, Desktop fuer Entwicklung und Tests.
- Modulare Trennung von Core, Welt, Landwirtschaft, Fahrzeugen, Charakteren, UI, Savegame und Plattformcode.
- Avatar- und Savegame-Daten ueber stabile IDs, nicht ueber Laufzeitreferenzen.
- Mobile Performance frueh und auf realen Geraeten validieren.
- Fremde oder generierte Assets nur mit dokumentierter Herkunft und Lizenz verwenden.

## Abschlussformat im `AGENT_BOARD.md`

Dokumentiere Ergebnis, Dateien, Tests mit Resultat, Commit/PR, Risiken und Folgeaufgaben.