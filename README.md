# Landwirtschaftssimulator

KI-first entwickelter Landwirtschaftssimulator mit steuerbarer Spielfigur, generischem Traktor, geplanter Feldsimulation und einer öffentlichen Projektwebsite.

## Kanonische Projektpfade

Mehrere Agenten haben zunächst getrennte Prototypen angelegt. Für alle neuen Änderungen und automatischen Builds gelten ausschließlich:

| Bereich | Kanonischer Pfad |
|---|---|
| Godot-Spiel | `game/godot/` |
| Öffentliche Website | `website/` |
| Android-Ausgaben | `build/android/` |

`apps/game/` und `apps/website/public/` sind historische Planungsshells. Sie dürfen nicht mehr als Quelle für Deployment-Workflows verwendet werden.

## Aktueller spielbarer Prototyp

Das Godot-Projekt unter `game/godot/` enthält derzeit:

- Third-Person-Spielfigur und Kamera,
- Speichern und Laden des Spielerzustands,
- generischen, markenfreien Traktor,
- Ein- und Aussteigen mit Übergabe der Eingabehoheit,
- einfache Testwelt für die weitere Integration.

Projektdatei:

```text
game/godot/project.godot
```

## Website und Cloudflare

Die statische Website liegt unter `website/`. `wrangler.toml` veröffentlicht genau dieses Verzeichnis.

Der Workflow `.github/workflows/build-website.yml`:

1. prüft HTML-, CSS- und JavaScript-Dateien,
2. führt einen Wrangler-Dry-Run aus,
3. stellt die Website als GitHub-Actions-Artefakt bereit,
4. kann auf `main` direkt zu Cloudflare deployen, wenn die Repository-Secrets `CLOUDFLARE_API_TOKEN` und `CLOUDFLARE_ACCOUNT_ID` vorhanden sind.

Die bereits eingerichtete Cloudflare-Git-Integration kann weiterhin bei jedem Push auf `main` automatisch veröffentlichen.

## Android-APK

Der Workflow `.github/workflows/build-android.yml` baut aus `game/godot/` eine Debug-APK und lädt sie als Actions-Artefakt hoch.

Ausgabepfad:

```text
build/android/landwirtschaftssimulator-debug.apk
```

Bei einem Versions-Tag wie `v0.1.0` wird die erzeugte APK zusätzlich an ein GitHub Release angehängt. Ein CI-Build ist noch keine Freigabe für den Play Store und ersetzt keinen Test auf einem realen Android-Gerät.

## Arbeitsweise mit mehreren Agenten

Jeder Agent arbeitet auf einem eigenen Branch, beansprucht klar definierte Pfade und dokumentiert seinen Status unter `docs/agents/status/`. Vor größeren Änderungen gelten:

- `AGENTS.md`
- `TASKS.md`
- `ARCHITECTURE.md`
- `DECISIONS.md`
- `TESTING.md`
- `ROADMAP.md`
- `SECURITY.md`
- `SKILLS.md`
- `docs/agents/WORK_PROTOCOL.md`

## Lokale Qualitätsprüfung

```bash
uv sync --dev
uv run python scripts/validate_repository.py
uv run pytest
```

Für die Website zusätzlich:

```bash
npm install --ignore-scripts
npm run check
npx wrangler deploy --dry-run
```

Keine Geheimnisse, privaten Signierschlüssel, proprietären Markenmodelle oder ungeklärten Fremdassets werden eingecheckt.
