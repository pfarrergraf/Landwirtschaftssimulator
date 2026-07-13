# TASKS.md

## Arbeitsregeln

- Statuswerte: `planned`, `ready`, `active`, `blocked`, `review`, `done`.
- Jeder Task besitzt einen exklusiven Pfadbereich.
- Gemeinsame Dateien werden nur im Integrations-Track `INT-*` verändert.
- Vor Arbeitsbeginn gelten `AGENTS.md` und `docs/agents/WORK_PROTOCOL.md`.

## Phase 0 – Verträge und Entscheidungen

| ID | Status | Aufgabe | Exklusiver Pfadbereich | Abhängigkeit | Ergebnis |
|---|---|---|---|---|---|
| ARC-001 | ready | Engine- und Renderingentscheidung vorbereiten | `docs/adr/`, `docs/engine/` | keine | Entscheidungsgrundlage für Android-3D |
| GFX-001 | ready | Visual Bible und Assetvertrag | `docs/art/` | keine | Maßstab, Stil, PBR-, LOD- und Naming-Regeln |
| SIM-001 | ready | Simulations-Datenmodell für Felder und Pflanzen | `docs/simulation/`, `data/schema/` | keine | stabile Datenverträge |
| TOOL-001 | planned | Asset-Pipeline-Grundgerüst | `tools/asset_pipeline/` | GFX-001 | lokale Validierung und Konvertierung |

## Phase 1 – Parallel ausführbare Grafikpakete

| ID | Status | Aufgabe | Exklusiver Pfadbereich | Abhängigkeit | Ergebnis |
|---|---|---|---|---|---|
| GFX-010 | ready | Felder, Boden und Bearbeitungszustände | `assets/environment/fields/` | GFX-001 | PBR-Materialsets und Testfeld |
| GFX-020 | ready | Pflanzen und Wachstumsstadien | `assets/crops/` | GFX-001, SIM-001 | instanzierbare Pflanzenpakete |
| GFX-030 | ready | Generische Maschinen | `assets/machines/` | GFX-001 | Traktor- und Gerätepakete ohne Markenbindung |
| GFX-040 | ready | Landschaft, Wege, Höfe und Vegetation | `assets/environment/world/` | GFX-001 | modulare Weltbausteine |
| GFX-050 | ready | Wetter-, Licht- und Saison-Lookdev | `assets/environment/weather/`, `docs/art/lighting/` | GFX-001 | reproduzierbare Look-Presets |
| UI-010 | planned | HUD- und Maschinenanzeigen | `assets/ui/`, `docs/ui/` | ARC-001 | Android-taugliches UI-Kit |

## Phase 2 – Simulation und Rendering parallel

| ID | Status | Aufgabe | Exklusiver Pfadbereich | Abhängigkeit | Ergebnis |
|---|---|---|---|---|---|
| SIM-010 | planned | Feldzustände und Bodenfeuchte | `src/simulation/fields/`, `data/fields/` | SIM-001 | deterministische Feldsimulation |
| SIM-020 | planned | Pflanzenwachstum und Ertrag | `src/simulation/crops/`, `data/crops/` | SIM-001, GFX-020 | Wachstums- und Ertragsmodell |
| SIM-030 | planned | Maschinenparameter und Arbeitsgeräte | `src/simulation/machines/`, `data/machines/` | SIM-001, GFX-030 | Datenmodell für Fahrzeuge und Geräte |
| RND-010 | planned | Terrain- und Feldrendering | `src/rendering/terrain/` | ARC-001, GFX-010 | performantes Feldrendering |
| RND-020 | planned | Pflanzen-Instancing, LOD und Impostors | `src/rendering/crops/` | ARC-001, GFX-020 | dichte Bestände auf Android |
| RND-030 | planned | Maschinenrendering und Animation | `src/rendering/machines/` | ARC-001, GFX-030 | Fahrzeugdarstellung und Animation |

## Phase 3 – Qualität und Integration

| ID | Status | Aufgabe | Exklusiver Pfadbereich | Abhängigkeit | Ergebnis |
|---|---|---|---|---|---|
| QA-010 | planned | Assetvalidierung | `tests/assets/`, `docs/qa/assets/` | TOOL-001 | automatisierte Format- und Budgetprüfungen |
| QA-020 | planned | Visuelle Referenztests | `tests/visual/`, `docs/qa/visual/` | RND-010, RND-020, RND-030 | reproduzierbare Vergleichsbilder |
| QA-030 | planned | Android-Performance-Matrix | `tests/performance/`, `docs/qa/performance/` | ARC-001 | Messungen für Low/Mid/High-Geräteklassen |
| INT-010 | planned | Grafikpakete integrieren | gemeinsame Engine- und Registry-Dateien | GFX-010 bis GFX-050 | integrierter Grafikstand |
| INT-020 | planned | Simulation und Darstellung verbinden | gemeinsame Engine- und Registry-Dateien | SIM-010 bis RND-030 | spielbarer vertikaler Ausschnitt |

## Empfohlener erster Parallel-Sprint

Diese Tasks dürfen nach Abschluss von GFX-001 und SIM-001 gleichzeitig laufen:

- Agent A: `GFX-010` Felder und Boden
- Agent B: `GFX-020` Pflanzenwachstum
- Agent C: `GFX-030` Maschinen
- Agent D: `GFX-040` Weltbausteine
- Agent E: `TOOL-001` Asset-Pipeline
- Agent F: `QA-010` Validierungsregeln

Die Agenten bearbeiten disjunkte Verzeichnisse. Integration erfolgt anschließend ausschließlich über `INT-010`.
