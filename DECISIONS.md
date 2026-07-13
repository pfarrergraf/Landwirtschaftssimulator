# DECISIONS.md

## ADR-0001 – Godot 4 für den Android-MVP

- Status: accepted
- Entscheidung: Der erste spielbare Android-MVP wird mit Godot 4.x, GDScript und zunächst dem GL-Compatibility-Renderer entwickelt.
- Grund: offene MIT-Lizenz, direkte Android-Pipeline, gut diffbare Textdateien, glTF/GLB-Unterstützung und geeignete Instancing-Werkzeuge für KI-first-Entwicklung.
- Nachprüfung: Die konkrete Patchversion und der endgültige Renderer werden nach reproduzierbarem APK-Build und Gerätemessungen festgeschrieben.
- Detaildokument: `docs/architecture/engine-evaluation/DECISION.md`.

## ADR-0002 – glTF/GLB als neutraler 3D-Austauschvertrag

- Status: accepted
- Entscheidung: glTF 2.0 / GLB ist das kanonische Austauschformat; Blender-Dateien bleiben Quelldateien.
- Grund: klare PBR-, Transform- und Animationsverträge bei guter Werkzeugunterstützung.

## ADR-0003 – Mobile Realistik statt ungefilterter Fotorealistik

- Status: accepted
- Entscheidung: Physikalisch plausible Materialien und Maße werden mit LOD, Instancing, Impostors und Qualitätsprofilen kombiniert.
- Grund: Android-Performance ist ein Produktkriterium, kein nachträglicher Optimierungsschritt.

## ADR-0004 – Konfliktarme Agentenstatusdateien

- Status: accepted
- Entscheidung: Jeder Agent schreibt nur in `docs/agents/status/<agent-id>.md`; es gibt keine gemeinsame, von allen Agenten fortlaufend bearbeitete Logdatei.
- Grund: parallele Arbeit darf keine vermeidbaren Merge-Konflikte erzeugen.

## ADR-0005 – Markenfreie Maschinen bis zur Lizenzentscheidung

- Status: accepted
- Entscheidung: Maschinen werden zunächst generisch, ohne Logos, Modellnamen oder nahezu identische Markennachbauten gestaltet.
- Grund: endgültige Marken- und Lizenzentscheidungen benötigen gesonderte Freigabe.

## ADR-0006 – Engine-neutrale Domäne trotz Godot-Runtime

- Status: accepted
- Entscheidung: Feld-, Pflanzen-, Maschinen-, Charakter- und Savegame-Daten bleiben außerhalb von Godot-Szenen stabil modelliert. Godot-Nodes sind Adapter, nicht Quelle der Fachlogik.
- Grund: Simulationstests, Datenmigration und spätere technische Änderungen bleiben beherrschbar.

## Offene Entscheidungen

- konkrete stabile Godot-Patchversion nach erstem Android-Build,
- GL Compatibility gegen Mobile-Renderer auf realen Zielgeräten,
- Zielgeräte und harte Performancebudgets nach ersten Messungen,
- endgültiges Lizenzmodell für Markenmaschinen,
- Kartenregion und visuelle Regionalisierung des ersten vertikalen Ausschnitts.
