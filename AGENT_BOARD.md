# AGENT_BOARD.md

Diese Datei ist die gemeinsame, verbindliche Arbeitsanzeige aller KI-Agenten. Vor Beginn und nach Abschluss jeder Aufgabe aktualisieren.

Letzte Aktualisierung: 2026-07-13

## Aktive Arbeiten

| Agent-ID | Ziel | Dateien/Subysteme | Branch | Start UTC | Status | Abhaengigkeiten/Konflikte |
|---|---|---|---|---|---|---|
| `chatgpt-repo-bootstrap-01` | AI-Governance und Avatar-Planungsbasis anlegen | Governance-Dokumente, Architektur, Roadmap, Avatarplanung | `planning/ai-collaboration-avatars` | 2026-07-13T15:55Z | `IN_PROGRESS` | Keine; initialer Repository-Aufbau |

## Reservierte Folgearbeiten

| Arbeitspaket | Empfohlener Branch | Voraussetzungen | Noch nicht beginnen, wenn ... |
|---|---|---|---|
| Avatar-Datenmodell und Save-Schema | `feature/avatar-data-model` | ADR fuer Engine und Persistenz bestaetigt | parallel bereits am Save-System gearbeitet wird |
| Avatar-Prototyp in 3D | `prototype/avatar-controller` | Engine-Prototyp lauffaehig | Player-Controller-Schnittstelle unklar ist |
| Charakter-Customizer UI | `feature/avatar-customizer-ui` | Datenmodell und Basismesh stehen | UI-Navigation noch nicht festgelegt ist |
| NPC-Grundsystem | `feature/npc-foundation` | Avatar-Komponenten wiederverwendbar | Welt- und Zeit-System fehlen |

## Abgeschlossene Arbeiten

| Datum UTC | Agent-ID | Ergebnis | Geaenderte Dateien | Tests/Validierung | Commit/PR | Offene Punkte |
|---|---|---|---|---|---|---|
| 2026-07-13 | `chatgpt-repo-bootstrap-01` | Repository-Initialisierung auf `main` vorgefunden und separaten Planungsbranch angelegt | Branch `planning/ai-collaboration-avatars` | Repository-Metadaten und Startcommit geprueft | Branch erstellt | Governance und Avatarplan werden in diesem Branch ergaenzt |

## Blockaden und Entscheidungsbedarf

| ID | Thema | Auswirkung | Benoetigte Entscheidung | Verantwortlich |
|---|---|---|---|---|
| `DEC-001` | Finale Game-Engine | Beeinflusst Build, Szenen, Skriptsprache und Asset-Pipeline | Prototypvergleich; Godot-first ist nur vorlaeufig | Projektleitung nach Prototyp |
| `DEC-002` | Endgueltige Marken- und Lizenzstrategie | Beeinflusst Name, Store-Auftritt und Fremdassets | Darf nicht autonom final entschieden werden | Benjamin Graf |

## Vorlage fuer neue aktive Arbeit

```markdown
| `agent-id` | Kurzes Ziel | `pfad/a`, `pfad/b` | `feature/branch` | YYYY-MM-DDTHH:MMZ | `CLAIMED` | Keine oder konkrete Konflikte |
```

## Vorlage fuer Abschluss

```markdown
| YYYY-MM-DD | `agent-id` | Konkretes Ergebnis | Geaenderte Dateien | Ausgefuehrte Tests mit Resultat | Commit/PR | Risiken oder Folgeaufgaben |
```
