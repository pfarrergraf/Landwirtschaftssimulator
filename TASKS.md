# TASKS.md

## Arbeitsregeln

- Statuswerte: `planned`, `ready`, `active`, `blocked`, `review`, `done`.
- Jeder Task besitzt einen exklusiven Pfadbereich.
- Gemeinsame Dateien werden nur im Integrations-Track `INT-*` verändert.
- Vor Arbeitsbeginn gelten `AGENTS.md` und `docs/agents/WORK_PROTOCOL.md`.
- Der Coordinator darf Planungsdateien direkt auf `main` pflegen.

## Ziel des ersten spielbaren Builds

Der erste Android-MVP ist erreicht, wenn eine Spielfigur auf einem kleinen Hof frei laufen, ein Feld erreichen, mit einem generischen Traktor interagieren, einsteigen, ein Werkzeug benutzen, Weizen säen und einen gespeicherten Spielstand wieder laden kann.

## Phase 0 – Verträge und Entscheidungen

| ID | Status | Aufgabe | Exklusiver Pfadbereich | Abhängigkeit | Ergebnis |
|---|---|---|---|---|---|
| ARC-001 | ready | Engine- und Renderingentscheidung vorbereiten | `docs/architecture/engine-evaluation/`, `docs/adr/` | keine | belastbare Engineentscheidung für Android-3D |
| GFX-001 | ready | Visual Bible und Assetvertrag | `docs/art/` | keine | Maßstab, Stil, PBR-, LOD- und Naming-Regeln |
| SIM-001 | ready | Simulations-Datenmodell für Felder und Pflanzen | `docs/simulation/`, `data/schema/` | keine | stabile Datenverträge |
| CHR-001 | ready | Charakter-, Avatar- und Interaktionsverträge | `docs/characters/`, `data/schema/characters/` | keine | engine-neutrales Charaktermodell |
| SAV-001 | planned | Savegame-Schema und Migrationsregeln | `docs/savegame/`, `data/schema/savegame/` | SIM-001, CHR-001 | versionierter Persistenzvertrag |
| TOOL-001 | planned | Asset-Pipeline-Grundgerüst | `tools/asset_pipeline/` | GFX-001 | lokale Validierung und Konvertierung |

## Phase 1 – Engine-neutrale Fachpakete

### Grafik und Welt

| ID | Status | Aufgabe | Exklusiver Pfadbereich | Abhängigkeit | Ergebnis |
|---|---|---|---|---|---|
| GFX-010 | ready | Felder, Boden und Bearbeitungszustände | `assets/environment/fields/` | GFX-001 | PBR-Materialsets und Testfeld |
| GFX-020 | ready | Pflanzen und Wachstumsstadien | `assets/crops/` | GFX-001, SIM-001 | instanzierbare Pflanzenpakete |
| GFX-030 | ready | Generische Maschinen | `assets/machines/` | GFX-001 | Traktor- und Gerätepakete ohne Markenbindung |
| GFX-040 | ready | Landschaft, Wege, Höfe und Vegetation | `assets/environment/world/` | GFX-001 | modulare Weltbausteine |
| GFX-050 | ready | Wetter-, Licht- und Saison-Lookdev | `assets/environment/weather/`, `docs/art/lighting/` | GFX-001 | reproduzierbare Look-Presets |
| CHR-010 | planned | Mobile Avatar-Basismesh, Rig und LODs | `assets/characters/player/` | GFX-001, CHR-001 | lizenzierter, Android-tauglicher Spielercharakter |
| CHR-020 | planned | Basisanimationspaket | `assets/characters/animations/` | CHR-010 | idle, walk, run, interact, enter/exit vehicle |
| UI-010 | planned | HUD- und Maschinenanzeigen | `assets/ui/`, `docs/ui/` | ARC-001 | Android-taugliches UI-Kit |
| UI-020 | planned | Touch-Steuerung und Interaktionsanzeigen | `assets/ui/touch/`, `docs/ui/touch/` | CHR-001 | Joystick-, Kamera- und Aktionskonzept |

### Simulation und Spiellogik

| ID | Status | Aufgabe | Exklusiver Pfadbereich | Abhängigkeit | Ergebnis |
|---|---|---|---|---|---|
| SIM-010 | planned | Feldzustände und Bodenfeuchte | `src/simulation/fields/`, `data/fields/` | SIM-001 | deterministische Feldsimulation |
| SIM-020 | planned | Pflanzenwachstum und Ertrag | `src/simulation/crops/`, `data/crops/` | SIM-001, GFX-020 | Wachstums- und Ertragsmodell |
| SIM-030 | planned | Maschinenparameter und Arbeitsgeräte | `src/simulation/machines/`, `data/machines/` | SIM-001, GFX-030 | Datenmodell für Fahrzeuge und Geräte |
| CHR-030 | planned | Avatar-Datenmodell und Runtime-State | `src/characters/domain/`, `data/characters/` | CHR-001 | Identität, Aussehen, Position, Zustand |
| CHR-040 | planned | Interaktionsdomäne | `src/characters/interactions/` | CHR-001 | Fokus, Reichweite, Aktionen und Bedingungen |
| VEH-010 | planned | Fahrzeug-Sitz- und Übergabevertrag | `src/vehicles/interaction/` | CHR-001, SIM-030 | Ein-/Aussteigen ohne Input-Konflikte |
| SAV-010 | planned | Save-/Load-Kern und Migration | `src/savegame/`, `tests/savegame/` | SAV-001 | atomisches, versioniertes Speichern |

## Phase 2 – Engine-Integration und spielbarer Prototyp

| ID | Status | Aufgabe | Exklusiver Pfadbereich | Abhängigkeit | Ergebnis |
|---|---|---|---|---|---|
| RND-010 | planned | Terrain- und Feldrendering | `src/rendering/terrain/` | ARC-001, GFX-010 | performantes Feldrendering |
| RND-020 | planned | Pflanzen-Instancing, LOD und Impostors | `src/rendering/crops/` | ARC-001, GFX-020 | dichte Bestände auf Android |
| RND-030 | planned | Maschinenrendering und Animation | `src/rendering/machines/` | ARC-001, GFX-030 | Fahrzeugdarstellung und Animation |
| CHR-100 | planned | Third-Person-Controller | `src/characters/presentation/controller/` | ARC-001, CHR-030 | Desktop- und Touch-Bewegung |
| CHR-110 | planned | Third-Person-Kamera | `src/characters/presentation/camera/` | ARC-001, CHR-100 | Kollision, Zoom, Drehung und Kameralimit |
| CHR-120 | planned | Animation State Machine | `src/characters/presentation/animation/` | CHR-020, CHR-100 | stabile Bewegungs- und Aktionsübergänge |
| CHR-130 | planned | Weltinteraktion | `src/characters/presentation/interactions/` | CHR-040, CHR-100 | kontextbezogene Aktionen auf dem Hof |
| VEH-100 | planned | Ein- und Aussteigen in Testtraktor | `src/vehicles/presentation/occupancy/` | VEH-010, CHR-100, RND-030 | sauberer Wechsel Spieler/Fahrzeug |
| UI-100 | planned | Mobile Eingabe integrieren | `src/ui/mobile_controls/` | UI-020, CHR-100 | spielbare Touch-Steuerung |
| SAV-100 | planned | Engine-Anbindung Speichern/Laden | `src/platform/savegame/` | SAV-010, ARC-001 | persistenter MVP-Spielstand |

## Phase 3 – Vertikaler Ausschnitt

| ID | Status | Aufgabe | Exklusiver Pfadbereich | Abhängigkeit | Ergebnis |
|---|---|---|---|---|---|
| GAME-010 | planned | Kleine Hofkarte und Testfeld | `game/worlds/mvp_farm/` | GFX-040, RND-010 | begehbare MVP-Welt |
| GAME-020 | planned | Traktor, Sämaschine und Feldaktion verbinden | `game/scenarios/sowing_loop/` | SIM-010, SIM-030, VEH-100 | vom Hof zur Aussaat spielbarer Loop |
| GAME-030 | planned | Weizenwachstum sichtbar verbinden | `game/scenarios/wheat_cycle/` | SIM-020, RND-020 | Simulation und Darstellung synchron |
| GAME-040 | planned | Avatar-Customizer mit Presets | `src/ui/avatar_customizer/`, `data/characters/presets/` | CHR-030, CHR-010 | speicherbare Auswahl ohne komplexen Editor |
| GAME-050 | planned | MVP-Onboarding und Aufgabenführung | `src/ui/onboarding/`, `data/tutorial/` | GAME-010, GAME-020 | verständlicher erster Spielablauf |
| INT-010 | planned | Grafikpakete integrieren | gemeinsame Engine- und Registry-Dateien | GFX-010 bis GFX-050 | integrierter Grafikstand |
| INT-020 | planned | Simulation, Avatar und Darstellung verbinden | gemeinsame Engine- und Registry-Dateien | SIM-010 bis SAV-100 | spielbarer vertikaler Ausschnitt |

## Phase 4 – Qualität und Android-Abnahme

| ID | Status | Aufgabe | Exklusiver Pfadbereich | Abhängigkeit | Ergebnis |
|---|---|---|---|---|---|
| QA-010 | planned | Assetvalidierung | `tests/assets/`, `docs/qa/assets/` | TOOL-001 | automatisierte Format- und Budgetprüfungen |
| QA-020 | planned | Visuelle Referenztests | `tests/visual/`, `docs/qa/visual/` | RND-010, RND-020, RND-030, CHR-120 | reproduzierbare Vergleichsbilder |
| QA-030 | planned | Android-Performance-Matrix | `tests/performance/`, `docs/qa/performance/` | ARC-001 | Messungen für Low/Mid/High-Geräteklassen |
| QA-040 | planned | Avatar- und Interaktionstests | `tests/characters/`, `docs/qa/characters/` | CHR-100 bis VEH-100 | Controller-, Kamera- und Übergangstests |
| QA-050 | planned | Savegame- und Migrationstests | `tests/savegame/` | SAV-100 | keine verlorenen oder unlesbaren Spielstände |
| QA-060 | planned | Reale Android-Gerätetests | `docs/qa/device-tests/` | INT-020 | Touch, Thermik, Speicher und Stabilität geprüft |

## Kritischer Pfad zum ersten APK

1. `ARC-001`, `SIM-001`, `CHR-001`, `GFX-001`
2. `SAV-001`, `SIM-010`, `SIM-030`, `CHR-030`, `CHR-040`, `GFX-010`, `GFX-030`, `CHR-010`
3. `CHR-100`, `CHR-110`, `CHR-120`, `RND-010`, `RND-030`, `VEH-100`, `UI-100`, `SAV-100`
4. `GAME-010`, `GAME-020`, `INT-020`
5. `QA-030`, `QA-040`, `QA-050`, `QA-060`

## Reihenfolge für einen einzelnen ChatGPT-Agenten

Da aktuell nur ein Agent arbeitet, werden die Pakete nacheinander umgesetzt. Empfohlene Reihenfolge:

1. `ARC-001` Engineentscheidung
2. `CHR-001` Charakterverträge
3. `SIM-001` Simulationsverträge
4. `GFX-001` Art Bible abschließen
5. `SAV-001` Savegame-Vertrag
6. minimaler Controller- und Testfeld-Spike
7. Traktor-Interaktion und Aussaat-Loop
8. Android-Build und Messung

Die Multi-Agent-Regeln bleiben bestehen, damit später mehrere Coding-Agenten konfliktarm hinzukommen können.