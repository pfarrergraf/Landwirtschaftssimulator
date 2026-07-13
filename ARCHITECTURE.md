# ARCHITECTURE.md

## Projektziel

Eine containerfähig entwickelte Android-3D-Landwirtschaftssimulation mit realistischen Feldern, Pflanzen, Wachstumsstadien, Maschinen und nachvollziehbarer Simulation.

## Aktueller Architekturstatus

Die endgültige Engine ist noch nicht beschlossen. Bis `ARC-001` abgeschlossen ist, bleiben Domänendaten, Assetquellen und Validierungswerkzeuge engine-neutral.

## Schichten

1. **Domain Data** – Kulturen, Feldzustände, Maschinenparameter und Schemata unter `data/`.
2. **Simulation** – deterministische Spielregeln unter `src/simulation/`.
3. **Rendering** – engine-nahe Darstellung unter `src/rendering/`.
4. **Assets** – Quellen und exportierte Pakete unter `assets/`.
5. **Tooling** – lokale Asset- und Prüfwerkzeuge unter `tools/` und `scripts/`.
6. **Quality** – Unit-, Asset-, Visual- und Performance-Tests unter `tests/`.

## Abhängigkeitsrichtung

```text
Data -> Simulation -> Rendering Adapter -> Engine
Assets -> Asset Pipeline -> Rendering Adapter -> Engine
Tests -> Data / Simulation / Assets / Rendering
```

Simulation darf keine direkten Abhängigkeiten auf konkrete 3D-Assets besitzen. Assets verwenden stabile IDs aus den Datenverträgen. Engine-spezifische Dateien werden erst nach der Engineentscheidung ergänzt.

## Integrationsgrenzen

- Kultur-ID und Growth-Stage-ID sind stabile Schnittstellen zwischen Simulation und Grafik.
- Maschinen verwenden stabile Attachment-, Animation- und Arbeitsbreiten-Metadaten.
- Feldzustände werden als Datenzustände modelliert und vom Rendering auf Material-/Meshvarianten abgebildet.
- Gemeinsame Registries werden nur in Integrations-PRs verändert.

## Zielplattform

- Primär: Android.
- Entwicklung: Windows 11 mit WSL2/Ubuntu und containerfähigen Werkzeugen.
- Python-Werkzeuge: Python 3.11/3.12, ausschließlich `uv`.
- KI- und Bildworkflows: lokal vorbereitbar, ComfyUI optional; keine Pflicht zu externen kostenpflichtigen Diensten.
