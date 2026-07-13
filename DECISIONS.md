# DECISIONS.md

## ADR-0001 – Engineentscheidung wird getrennt vorbereitet

- Status: accepted
- Entscheidung: Die endgültige 3D-Engine wird in `ARC-001` bewertet. Bis dahin bleiben Daten, Assets und Tools engine-neutral.
- Grund: Grafik- und Simulationsarbeit soll parallel beginnen können, ohne spätere Engineentscheidung vorwegzunehmen.

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

## Offene Entscheidungen

- `ARC-001`: Engine und Renderingstack.
- Zielgeräte und harte Performancebudgets nach ersten Messungen.
- endgültiges Lizenzmodell für Markenmaschinen.
- Kartenregion und visuelle Regionalisierung des ersten vertikalen Ausschnitts.
