# TASKS.md

## Arbeitsweise

- Vor Beginn Aufgabe in `AGENT_BOARD.md` reservieren.
- Jede Aufgabe erhaelt Akzeptanzkriterien und Validierung.
- Prioritaeten: `P0` grundlegend, `P1` MVP, `P2` Ausbau, `P3` optional.
- Status: `TODO`, `IN_PROGRESS`, `BLOCKED`, `REVIEW`, `DONE`.

# Epic A: Technische Projektbasis

## A-001 Engine-Prototyp festlegen

- Prioritaet: `P0`
- Status: `TODO`
- Ziel: Einen kleinen Android-faehigen 3D-Prototyp mit reproduzierbarem Container-Build erstellen.
- Vorlaeufige Richtung: Godot-first, aber erst nach Prototypvergleich verbindlich entscheiden.
- Akzeptanzkriterien:
  - einfache 3D-Testszene startet lokal,
  - Android-Build ist dokumentiert,
  - Build-Schritte sind reproduzierbar,
  - Entscheidung und Alternativen stehen in `DECISIONS.md`.

## A-002 Grundlegende Modulstruktur anlegen

- Prioritaet: `P0`
- Status: `TODO`
- Module:
  - `core`
  - `world`
  - `farming`
  - `vehicles`
  - `characters`
  - `ui`
  - `savegame`
  - `platform`
- Akzeptanzkriterien:
  - Module haben klare Verantwortlichkeiten,
  - Charakterlogik ist nicht im Welt- oder Fahrzeugcode versteckt,
  - Tests koennen ohne komplette Spielszene laufen.

# Epic B: Spielbarer Avatar / Spielfigur

## B-001 Avatar-Produktdefinition

- Prioritaet: `P0`
- Status: `TODO`
- Ziel: Festlegen, was die Spielfigur im MVP koennen muss.
- MVP-Faehigkeiten:
  - gehen und laufen,
  - Kamera drehen und zoomen,
  - mit Objekten interagieren,
  - Fahrzeuge betreten und verlassen,
  - Werkzeuge aufnehmen und benutzen,
  - einfache Animationen fuer Idle, Gehen, Laufen, Benutzen und Fahren,
  - Name und Aussehen speichern.
- Nicht Teil des ersten MVP:
  - komplexe Gesichtsanimation,
  - Stoffsimulation,
  - fotorealistischer Charaktereditor,
  - Online-Multiplayer-Synchronisation.
- Akzeptanzkriterien:
  - Feature-Scope ist als Checkliste dokumentiert,
  - Android-Performanceziel ist festgelegt,
  - klare Abgrenzung zu spaeteren NPC-Systemen.

## B-002 Avatar-Datenmodell

- Prioritaet: `P0`
- Status: `TODO`
- Vorgeschlagene Daten:
  - stabile `character_id`,
  - Anzeigename,
  - Body-Preset,
  - Hautton-Palette,
  - Haar-Preset und Haarfarbe,
  - Gesicht-Preset,
  - Oberteil, Hose, Schuhe, Kopfbedeckung,
  - freigeschaltete Kosmetik,
  - Position, Rotation und aktueller Zustand,
  - Schema-Version fuer Savegame-Migrationen.
- Akzeptanzkriterien:
  - rein datengetrieben und serialisierbar,
  - keine direkten Szenen- oder Asset-Objekte im Savegame,
  - unbekannte oder entfernte Kosmetik faellt auf sichere Defaults zurueck,
  - Migrationstest fuer mindestens zwei Schema-Versionen.

## B-003 Modulares Charakter-Asset-System

- Prioritaet: `P1`
- Status: `TODO`
- Ziel: Ein gemeinsames Skelett mit austauschbaren visuellen Komponenten.
- Bausteine:
  - ein Basisskelett,
  - wenige optimierte Body-Presets,
  - austauschbare Haare und Kleidung,
  - gemeinsame Material-Paletten statt vieler Einzeltexturen,
  - LOD-Stufen fuer Spielfigur und NPCs.
- Akzeptanzkriterien:
  - alle MVP-Kleidungsstuecke funktionieren auf allen Body-Presets,
  - keine sichtbaren grossen Mesh-Luecken in Standardanimationen,
  - dokumentiertes Polygon-, Material- und Texturbudget,
  - Lizenz und Herkunft jedes Assets dokumentiert.

## B-004 Third-Person-Controller

- Prioritaet: `P1`
- Status: `TODO`
- Ziel: Praezise, mobile-freundliche Spielfigursteuerung.
- Anforderungen:
  - Tastatur/Gamepad fuer Desktop-Tests,
  - virtuelle Sticks und Touch-Buttons fuer Android,
  - konfigurierbare Laufgeschwindigkeit,
  - Schwerkraft, Haehenwechsel und Kollision,
  - Kamera-Kollisionsschutz,
  - Interaktionsfokus vor der Figur.
- Akzeptanzkriterien:
  - identische Gameplay-Schnittstelle fuer Desktop und Touch,
  - keine Eingabelogik direkt in Landwirtschaftsobjekten,
  - Testszene fuer Bewegung, Rampen, enge Raeume und Kamera,
  - stabile Bildrate auf definierter Android-Testklasse.

## B-005 Animations-Zustandsmaschine

- Prioritaet: `P1`
- Status: `TODO`
- Zustaende:
  - Idle,
  - Walk,
  - Run,
  - Interact,
  - Carry,
  - ToolUse,
  - EnterVehicle,
  - Drive,
  - ExitVehicle.
- Akzeptanzkriterien:
  - keine hart verdrahteten Asset-Namen in Spiellogik,
  - Uebergaenge sind datengetrieben,
  - Werkzeug- und Fahrzeugaktionen koennen Ereignisse ausloesen,
  - Fallback-Animation verhindert Blockieren der Spielfigur.

## B-006 Interaktionssystem

- Prioritaet: `P1`
- Status: `TODO`
- Ziel: Einheitliche Schnittstelle fuer Felder, Tiere, Maschinen, Tueren, Lager und Gegenstaende.
- Akzeptanzkriterien:
  - Interaktionsobjekte implementieren einen gemeinsamen Vertrag,
  - UI zeigt kontextabhaengige Aktion,
  - Reichweite und Blickrichtung werden geprueft,
  - Interaktionen koennen abgebrochen werden,
  - automatisierte Tests fuer Auswahlprioritaet und Reichweite.

## B-007 Fahrzeug betreten und verlassen

- Prioritaet: `P1`
- Status: `TODO`
- Ziel: Sauberer Wechsel zwischen Avatar- und Fahrzeugsteuerung.
- Akzeptanzkriterien:
  - definierte Ein- und Ausstiegspunkte,
  - Avatar wird waehrend Fahrt korrekt geparkt oder dargestellt,
  - Kamera und Input-Kontext wechseln deterministisch,
  - kein Aussteigen in Hindernisse,
  - Save/Load funktioniert sowohl zu Fuss als auch im Fahrzeug.

## B-008 Charakter-Customizer UI

- Prioritaet: `P1`
- Status: `TODO`
- MVP-Auswahl:
  - Name,
  - Body-Preset,
  - Hautton,
  - Haare und Haarfarbe,
  - Oberteil,
  - Hose,
  - Schuhe,
  - optional Kopfbedeckung.
- Akzeptanzkriterien:
  - komplett per Touch bedienbar,
  - Vorschau reagiert ohne Szenenneustart,
  - zufaellige Auswahl erzeugt nur gueltige Kombinationen,
  - Einstellungen werden gespeichert und wiederhergestellt,
  - UI bleibt mit Platzhalterassets funktionsfaehig.

## B-009 Avatar-Savegame und Migration

- Prioritaet: `P1`
- Status: `TODO`
- Akzeptanzkriterien:
  - atomisches Speichern,
  - Versionsfeld im Schema,
  - sichere Defaults bei fehlenden Feldern,
  - Backup bei fehlgeschlagener Migration,
  - automatisierte Roundtrip- und Migrationstests.

## B-010 Android-Optimierung fuer Charaktere

- Prioritaet: `P1`
- Status: `TODO`
- Messpunkte:
  - CPU-Zeit fuer Controller und Animation,
  - GPU-Zeit und Draw Calls,
  - Speicherbedarf von Meshes, Texturen und Animationen,
  - Ladezeit des Customizers,
  - thermische Stabilitaet bei laengerem Spiel.
- Akzeptanzkriterien:
  - dokumentierte Budgets,
  - Profiling auf realem Android-Geraet,
  - LOD- und Sichtbarkeitsregeln greifen,
  - keine ungeprueften 4K-Charaktertexturen im MVP.

# Epic C: NPCs und Hofleben

## C-001 Wiederverwendbare Charakterbasis

- Prioritaet: `P2`
- Status: `TODO`
- Ziel: Spieleravatar und NPCs teilen visuelle Komponenten, Animationen und Interaktionsschnittstellen, ohne dieselbe Steuerlogik zu erzwingen.

## C-002 Hof-NPCs

- Prioritaet: `P2`
- Status: `TODO`
- Erste Rollen:
  - Familienmitglied oder Hofhelfer,
  - Haendler,
  - Mechaniker,
  - Tierarzt,
  - Nachbar.
- Akzeptanzkriterien:
  - einfacher Tagesplan,
  - Navigation zwischen Wegpunkten,
  - Dialog- und Interaktionshaken,
  - geringe Simulationsrate ausserhalb der Spielernähe.

## C-003 Avatar-Reaktionen und Emotes

- Prioritaet: `P2`
- Status: `TODO`
- Umfang:
  - winken,
  - zustimmen,
  - ablehnen,
  - freuen,
  - erschoepft.

# Epic D: Spaetere Erweiterungen

## D-001 Mehrere Spielprofile

- Prioritaet: `P2`
- Status: `TODO`

## D-002 Optionale First-Person-Perspektive

- Prioritaet: `P3`
- Status: `TODO`

## D-003 Barrierearme Avatarsteuerung

- Prioritaet: `P2`
- Status: `TODO`
- Optionen:
  - einhaendige Touch-Belegung,
  - anpassbare Button-Groessen,
  - automatische Laufhilfe,
  - reduzierte Kamerabewegung,
  - hohe UI-Kontraste.

## D-004 Multiplayer-Vorbereitung ohne Implementierungszwang

- Prioritaet: `P3`
- Status: `TODO`
- Ziel: IDs und Zustandsdaten so gestalten, dass spaetere Synchronisation moeglich bleibt, ohne den MVP mit Netzwerkcode zu belasten.
