# Troubleshooting

## Validator meldet fehlende Datei

Vom Repository-Root starten oder das Skript direkt aufrufen; es ermittelt das Root relativ zu seinem Pfad.

## `uv sync` nutzt falsche Python-Version

Eine kompatible Version explizit waehlen:

```bash
uv python install 3.12
uv sync --python 3.12
```

## Android-Workflow scheitert

Zuerst Godot-Version, Exporttemplates, Android SDK, Exportpreset und Secretnamen pruefen. Ein Headless-Import ersetzt keinen Geraetetest.
