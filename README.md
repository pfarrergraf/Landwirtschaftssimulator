# Landwirtschaftssimulator

Android-first geplante 3D-Landwirtschaftssimulation mit modularer Architektur, reproduzierbaren Builds und einer fuer mehrere KI-Agenten geeigneten Arbeitsstruktur.

## Aktueller Stand

Das Repository befindet sich in der Planungs- und Prototypingphase. Die erste vollstaendige Planungsbasis wird im Branch `planning/ai-collaboration-avatars` aufgebaut.

## Wichtigste Dokumente

- `AGENTS.md` – verbindliche Regeln fuer alle KI-Agenten
- `AGENT_BOARD.md` – sichtbare aktive und abgeschlossene Arbeiten
- `TASKS.md` – priorisierte Arbeitspakete, einschliesslich Avatar-/Spielfiguren-Epic
- `ARCHITECTURE.md` – modulare Systemarchitektur
- `ROADMAP.md` – Phasen vom Vertical Slice bis zur Produktreife
- `DECISIONS.md` – Architekturentscheidungen und offene Vorschlaege
- `TESTING.md` – Teststrategie und Android-Validierung
- `SECURITY.md` – Secrets, Assets, Rechte und Release-Sicherheit
- `SKILLS.md` – wiederverwendbare Agenten-Workflows

## Naechstes Produktziel

Ein kleiner Vertical Slice mit:

- einfacher 3D-Hofszene,
- spielbarer Third-Person-Figur,
- Touch- und Desktop-Steuerung,
- einer Interaktion,
- Android-Build und realer Performance-Messung.

Danach folgt der Avatar-MVP mit anpassbarem Aussehen, Animationen, Savegame und spaeterem Fahrzeugwechsel.

## Agentenarbeit

Vor jeder Aenderung `AGENTS.md` lesen und die Aufgabe in `AGENT_BOARD.md` reservieren. Keine parallelen, unkoordinierten Aenderungen an denselben Dateien oder Subsystemen.

## Entscheidungsgrenzen

Repository-Aenderungen, Branches, Commits, Issues, Pull Requests, Tests und GitHub Actions sind fuer autonome Agentenarbeit freigegeben. Secrets, kostenpflichtige Dienste, Store-Veroeffentlichungen sowie endgueltige Marken- oder Lizenzentscheidungen brauchen eine ausdrueckliche Freigabe.