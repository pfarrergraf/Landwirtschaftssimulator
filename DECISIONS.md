# DECISIONS.md

Architekturentscheidungen werden als ADRs dokumentiert. Statuswerte: `PROPOSED`, `ACCEPTED`, `SUPERSEDED`, `REJECTED`.

## ADR-001: Gemeinsame Agentenkoordination im Repository

- Status: `ACCEPTED`
- Datum: 2026-07-13

### Kontext

Mehrere KI-Agenten koennen gleichzeitig Dateien, Branches und Pull Requests bearbeiten. Ohne sichtbare Reservierung entstehen Doppelarbeit, widerspruechliche Architektur und ueberschriebene Aenderungen.

### Entscheidung

- `AGENTS.md` definiert den verbindlichen Ablauf.
- `AGENT_BOARD.md` ist die gemeinsame Status- und Uebergabedatei.
- Jeder Agent kennzeichnet vor Beginn Ziel, Dateien, Branch und Status.
- Nach Abschluss werden Ergebnis, Tests, Commit/PR und offene Punkte dokumentiert.

### Folgen

- Zusaetzlicher kleiner Dokumentationsaufwand.
- Deutlich bessere Nachvollziehbarkeit und geringeres Konfliktrisiko.

## ADR-002: Separate Planungsbranch fuer den Repository-Aufbau

- Status: `ACCEPTED`
- Datum: 2026-07-13

### Entscheidung

Die erste vollstaendige Planungsbasis wird auf `planning/ai-collaboration-avatars` aufgebaut und per Pull Request gegen `main` geprueft.

### Folgen

`main` bleibt stabil; die Grundstruktur kann als zusammenhaengendes Paket reviewed werden.

## ADR-003: Godot-first fuer den ersten Prototyp

- Status: `PROPOSED`
- Datum: 2026-07-13

### Kontext

Das Projekt benoetigt Android-Export, 3D-Szenen, Touch-Eingabe, reproduzierbare Builds und eine fuer KI-Agenten gut bearbeitbare textbasierte Projektstruktur.

### Vorschlag

Godot 4.x wird fuer den ersten Vertical Slice bevorzugt. Die Entscheidung wird erst nach einem kleinen Prototyp mit Desktop- und Android-Build akzeptiert.

### Bewertungsfragen

- Funktioniert der Android-Build reproduzierbar?
- Sind Projekt- und Szenendateien fuer mehrere Agenten mergebar?
- Reicht die 3D-Performance fuer die definierte Zielgeraeteklasse?
- Sind Touch, Animation, Navigation und Savegame ausreichend?
- Gibt es Lizenz- oder Tooling-Risiken?

### Grenze

Dies ist keine endgueltige Lizenz- oder Markenentscheidung.

## ADR-004: Modulares Avatar-System mit stabilen IDs

- Status: `ACCEPTED`
- Datum: 2026-07-13

### Entscheidung

- Avatar-Aussehen wird durch serialisierbare Daten und stabile Asset-IDs beschrieben.
- Laufzeitobjekte und Szenenreferenzen werden nicht direkt gespeichert.
- Kleidung, Haare und Body-Presets verwenden ein gemeinsames Skelett.
- Spieleravatar und NPCs duerfen visuelle Komponenten und Animationen teilen, behalten aber getrennte Steuerlogik.

### Folgen

- Savegames bleiben migrierbar.
- Platzhalterassets koennen spaeter ersetzt werden.
- Customizer und NPC-System koennen dieselbe Asset-Bibliothek nutzen.

## ADR-005: Mobile Performance ist Akzeptanzkriterium, kein spaeteres Refactoring

- Status: `ACCEPTED`
- Datum: 2026-07-13

### Entscheidung

Jede groessere Grafik- oder Charaktersystemaenderung benoetigt messbare Budgets fuer Draw Calls, Materialien, Texturen, Animationen, Speicher und Frametimes auf einem realen Android-Geraet.

### Folgen

Desktop-only-Prototypen gelten nicht als ausreichender Abschluss fuer mobile Features.

## ADR-Vorlage

```markdown
## ADR-NNN: Titel

- Status: `PROPOSED`
- Datum: YYYY-MM-DD

### Kontext

### Entscheidung

### Alternativen

### Folgen

### Validierung
```
