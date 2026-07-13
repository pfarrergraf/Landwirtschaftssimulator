# Landwirtschaftssimulator

KI-first entwickelter Landwirtschaftssimulator mit realistischen Feldern, Pflanzenwachstum, Maschinen und einer für Android geeigneten 3D-Pipeline.

## Arbeitsweise

Das Repository ist für parallele Arbeit mehrerer KI-Agenten vorbereitet. Jeder Agent arbeitet auf einem eigenen Branch, beansprucht klar definierte Pfade und dokumentiert seinen Status in einer eigenen Datei unter `docs/agents/status/`.

Vor größeren Änderungen lesen:

- `AGENTS.md`
- `TASKS.md`
- `ARCHITECTURE.md`
- `DECISIONS.md`
- `TESTING.md`
- `ROADMAP.md`
- `SECURITY.md`
- `SKILLS.md`
- `docs/agents/WORK_PROTOCOL.md`

Für Grafik- und Assetarbeit zusätzlich:

- `docs/GRAPHICS_PLAN.md`
- `docs/assets/ASSET_CONTRACT.md`

## Erster spielbarer Ausschnitt

Geplant sind zunächst:

- ein realistisches Testfeld,
- ein vollständiger Weizen-Wachstumszyklus,
- ein generischer Traktor mit Basisanimationen,
- Bodenbearbeitung, Aussaat und Ernte,
- Tageszeit und einfaches Wetter,
- messbare Qualitätsprofile für mobile Geräte.

Die endgültige Engineentscheidung wird separat dokumentiert. Assets bleiben bis dahin über Blender-Quelldateien und glTF/GLB engine-neutral.

## Lokale Qualitätsprüfung

```bash
uv sync --dev
uv run python scripts/validate_repo.py
uv run pytest
```

Es werden keine geheimen Zugangsdaten, proprietären Markenmodelle oder ungeklärten Fremdassets eingecheckt.
