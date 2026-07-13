# ROADMAP.md

## Phase 0: Planungs- und Agentenbasis

Ziel: Mehrere KI-Agenten koennen ohne verdeckte Doppelarbeit am Repository arbeiten.

- [x] `AGENTS.md` mit verbindlichen Regeln
- [x] `AGENT_BOARD.md` als gemeinsame Statusdatei
- [x] erste Architektur- und Aufgabenstruktur
- [ ] Claude- und Copilot-Anweisungen angleichen
- [ ] Sicherheits-, Test- und Skill-Dokumente vervollstaendigen
- [ ] Basis-CI fuer Dokument- und Strukturpruefungen

Ergebnis: Planungsbasis ist reviewbar und kann nach `main` gemergt werden.

## Phase 1: Technischer Vertical Slice

Ziel: Eine kleine 3D-Hofszene laeuft auf Desktop und Android.

- Engine-Prototyp und ADR
- reproduzierbarer Entwicklungs- und Buildablauf
- einfache Welt mit Boden, Hof und einem Feld
- Third-Person-Platzhalterfigur
- Touch- und Desktop-Eingabe
- einfacher Interaktionsgegenstand
- Performance-Baseline auf realem Android-Geraet

Ergebnis: Die Spielfigur kann sich bewegen und ein Objekt bedienen.

## Phase 2: Avatar-MVP

Ziel: Eine erkennbare, speicherbare Spielfigur mit grundlegender Anpassung.

- Avatar-Datenmodell
- Basisskelett und wenige Body-Presets
- Haare, Farben und einfache Kleidung
- Charakter-Customizer
- Idle/Walk/Run/Interact
- Savegame und Migration
- mobile Asset- und Renderbudgets

Ergebnis: Spieler erstellt eine Figur, startet das Spiel und behaelt das Aussehen nach Neustart.

## Phase 3: Landwirtschafts-MVP

Ziel: Ein kompletter kleiner Arbeitszyklus.

- Werkzeug aufnehmen
- Boden vorbereiten
- saeen
- Wachstumszustand simulieren
- ernten
- Inventar und einfacher Verkauf
- Avatar-Animationen fuer Werkzeugnutzung

Ergebnis: Ein Feld kann vom Avatar ohne Fahrzeug bearbeitet werden.

## Phase 4: Fahrzeuge und Avatarwechsel

Ziel: Der Avatar kann Maschinen verwenden.

- erstes Fahrzeug
- Ein- und Ausstieg
- Kamera- und Input-Kontextwechsel
- Sitz- und Animationspunkte
- Anbaugeraet oder einfache Arbeitsfunktion
- Speichern im und ausserhalb des Fahrzeugs

Ergebnis: Ein Arbeitsvorgang kann mit einer Maschine abgeschlossen werden.

## Phase 5: Hofleben und NPCs

Ziel: Der Hof wirkt belebt und bietet wiederholbare Interaktionen.

- wiederverwendbare Charakterbasis fuer NPCs
- Hofhelfer, Haendler oder Mechaniker
- einfache Tagesplaene
- Navigation und Interaktionsdialoge
- reduzierte Simulation ausserhalb der Spielernähe

Ergebnis: Mindestens ein NPC erfuellt eine spielrelevante Rolle.

## Phase 6: Ausbau und Produktreife

- mehrere Hofbereiche und Pflanzen
- Tiere
- Wirtschaftsausbau
- Barrierefreiheit
- Grafik- und Ladezeitoptimierung
- Crash- und Savegame-Haertung
- optionale Lokalisierung
- Store-Vorbereitung erst nach ausdruecklicher Freigabe

## Querschnittsziele

In jeder Phase:

- Agentenboard aktuell halten,
- Entscheidungen als ADR dokumentieren,
- Tests und manuelle Validierung ergaenzen,
- Asset-Lizenzen nachhalten,
- Android-Performance messen,
- keine Secrets oder kostenpflichtigen Dienste ohne Freigabe verwenden.