# SKILLS.md

## Zweck

Diese Datei beschreibt wiederverwendbare Arbeitsfaehigkeiten fuer KI-Agenten in diesem Repository. Sie ersetzt keine Implementierung, sondern legt Eingangsdaten, Ergebnis, Validierung und Grenzen fest.

## Skill: `repo-governance`

### Einsatz

Bei jeder neuen groesseren Aufgabe oder paralleler Agentenarbeit.

### Ablauf

1. Pflichtdokumente lesen.
2. Arbeit in `AGENT_BOARD.md` reservieren.
3. Konflikte pruefen.
4. fokussierten Branch und Commits verwenden.
5. Tests ausfuehren.
6. Board, Aufgaben und Entscheidungen aktualisieren.

### Ergebnis

Nachvollziehbare, konfliktarme Aenderung mit Uebergabeprotokoll.

## Skill: `avatar-feature`

### Einsatz

Bei Spielfigur, Charakter-Customizer, Animation, Kleidung, NPC-Basis oder Fahrzeugwechsel.

### Pflichtquellen

- `TASKS.md`, Epic B und C
- Avatarabschnitt in `ARCHITECTURE.md`
- ADR-004 und ADR-005 in `DECISIONS.md`
- Avatar-Testmatrix in `TESTING.md`

### Ablauf

1. Datenmodell oder Schnittstelle zuerst definieren.
2. Platzhalterassets mit stabilen IDs nutzen.
3. Logik von Input, Szene und konkreten Assets trennen.
4. Savegame und Fallbacks beruecksichtigen.
5. Desktop- und Touch-Bedienung testen.
6. Android-Performance messen.

### Ergebnis

Modulares, speicherbares und mobil validiertes Charakterfeature.

## Skill: `android-vertical-slice`

### Einsatz

Bei neuen Systemen, die erst technisch validiert werden muessen.

### Ablauf

1. kleinstmoegliche isolierte Szene erstellen,
2. Desktop-Smoke-Test,
3. Android-Export,
4. Test auf realem Geraet,
5. Frametimes, Speicher und Eingabe dokumentieren,
6. Erkenntnisse als ADR und Aufgaben festhalten.

### Ergebnis

Messbarer Machbarkeitsnachweis statt reinem Architekturentwurf.

## Skill: `asset-intake`

### Einsatz

Beim Hinzufuegen von 3D-Modellen, Texturen, Animationen, Sounds oder KI-generierten Medien.

### Ablauf

1. Quelle und Rechte pruefen.
2. interne Asset-ID vergeben.
3. Lizenz und Erzeugungsweg dokumentieren.
4. mobile Budgets pruefen.
5. Import- und Fallbackverhalten testen.

### Grenze

Keine endgueltige Marken- oder Lizenzentscheidung autonom treffen.

## Skill: `savegame-change`

### Einsatz

Bei neuen oder geaenderten persistenten Daten.

### Ablauf

1. Schema-Version anheben, falls notwendig.
2. Migration definieren.
3. sichere Defaults und Fallbacks einbauen.
4. Roundtrip-, Altversions- und Korruptionstest erstellen.
5. Backup- und Fehlerverhalten dokumentieren.

## Optionale spaetere Integrationen

Noch nicht aktiviert und nicht Teil des MVP:

- lokale LLM-Unterstuetzung fuer Entwicklung oder Inhalte,
- ComfyUI-basierte Konzeptgrafik- oder Asset-Pipeline,
- lokale TTS/STT-Pipelines,
- automatische Lokalisierungsunterstuetzung.

Solche Integrationen muessen separat geplant, lizenziert, gemessen und gegen Produktanforderungen validiert werden.