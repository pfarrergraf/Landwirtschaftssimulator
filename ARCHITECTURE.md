# ARCHITECTURE.md

## Zielbild

Eine Android-faehige, containerisiert baubare 3D-Landwirtschaftssimulation mit klar getrennten Systemen, datengetriebener Konfiguration und testbarer Kernlogik.

## Vorlaeufige technische Richtung

- Engine: Godot-first-Prototyp, finale Entscheidung nach Build- und Performance-Test.
- Zielplattform zuerst: Android; Desktop dient Entwicklung, Tests und Debugging.
- Build: reproduzierbar in einer dokumentierten Container-/CI-Umgebung, soweit Engine- und Android-Tooling dies erlauben.
- Assets: modulare, mobile-optimierte 3D-Modelle mit dokumentierter Herkunft und Lizenz.

## Schichten

### 1. Domain/Core

Engine-arme Spiellogik und Datenmodelle:

- Zeit und Kalender
- Wirtschaft und Inventar
- Felder, Pflanzen, Tiere
- Charakterdaten
- Savegame-Schema und Migration
- Ereignisse und Regeln

Diese Schicht soll nach Moeglichkeit ohne komplette 3D-Szene testbar sein.

### 2. Application/Game Systems

Orchestriert Anwendungsfaelle:

- Pflanzen, pflegen, ernten
- Werkzeug benutzen
- Fahrzeug betreten und verlassen
- Handel
- Charakter anpassen
- Speichern und Laden

### 3. Presentation/Engine Adapter

- 3D-Szenen und Nodes
- Animationen
- Kamera
- UI und Touch-Eingabe
- Audio
- Partikel und visuelle Effekte

### 4. Platform Adapter

- Android-Eingabe und Lebenszyklus
- Dateisystem und Speicherorte
- optionale Store- oder Cloud-Anbindungen
- Telemetrie nur nach ausdruecklicher Freigabe

## Module

### `characters`

Verantwortung:

- Avatar-Konfiguration
- Spielerbewegung
- Animationszustand
- Interaktionsfokus
- Kleidung und visuelle Presets
- NPC-Basisdaten

Nicht verantwortlich fuer:

- konkrete Feldlogik
- Fahrzeugphysik
- globale Save-Dateiverwaltung

Wichtige Schnittstellen:

- `CharacterAppearanceData`
- `CharacterRuntimeState`
- `MovementIntent`
- `InteractionCandidate`
- `VehicleSeatContract`
- `CharacterSavePort`

### `vehicles`

- Fahrzeugphysik
- Sitze und Ein-/Ausstiegspunkte
- Fahrzeugsteuerung
- Anbaugeraete
- Treibstoff und Zustand

### `farming`

- Boden und Felder
- Pflanzenzyklen
- Werkzeuge und Arbeitsvorgaenge
- Ertrag

### `world`

- Weltsegmentierung
- Wetter und Tageszeit
- Navigation
- Streaming und Sichtbarkeit

### `ui`

- HUD
- Touch-Steuerung
- Menues
- Charakter-Customizer
- Barrierearme Einstellungen

### `savegame`

- atomisches Speichern
- Schema-Versionen
- Migrationen
- Backups
- Profilverwaltung

## Avatar-Komponentenmodell

```text
PlayerCharacter
|- CharacterIdentity
|- CharacterAppearance
|- CharacterMotor
|- CharacterAnimator
|- InteractionScanner
|- EquipmentSlots
|- VehicleTransition
|- SavegameBinding
`- InputAdapter
```

Grundsatz: Input erzeugt Absichten; der Motor setzt sie um. Landwirtschaftsobjekte kennen keine Touch- oder Tastaturdetails.

## Datenfluss einer Interaktion

```text
InputAdapter
  -> InteractionIntent
  -> InteractionScanner waehlt Kandidaten
  -> InteractableContract prueft Bedingungen
  -> Application Service fuehrt Aktion aus
  -> Domain State aendert sich
  -> Presentation aktualisiert UI/Animation
```

## Savegame-Regeln

- Nur stabile IDs und serialisierbare Werte speichern.
- Keine direkten Referenzen auf Szenenobjekte oder Laufzeitinstanzen.
- Jedes Schema hat eine Versionsnummer.
- Entfernte Asset-IDs erhalten definierte Fallbacks.
- Migrationen sind vorwaertsgerichtet, getestet und mit Backup abgesichert.

## Android-Performanceprinzipien

- wenige Materialien und Draw Calls pro Charakter,
- gemeinsame Texturatlanten oder Paletten,
- LODs fuer Avatare und NPCs,
- Animationen ausserhalb relevanter Distanz reduzieren,
- keine standardmaessigen 4K-Texturen,
- reale Geraeteprofile statt reiner Desktop-Messungen,
- Touch-UI und Kamera auf stabile Frametimes optimieren.

## Noch offene Architekturentscheidungen

- finale Engine,
- Skriptsprache und native Erweiterungen,
- genaue Savegame-Technik,
- Navigationsloesung fuer NPCs,
- Asset-Format und Charakter-Pipeline,
- Zielgeraeteklassen und konkrete Performancebudgets.

Diese Entscheidungen werden in `DECISIONS.md` als ADRs dokumentiert.