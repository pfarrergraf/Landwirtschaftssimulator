# chatgpt-DEPLOY-WEB-cloudflare-ci

- Status: active
- Task: DEPLOY-WEB
- Mode: branch
- Branch: agent/DEPLOY-WEB/web-ci
- Started: 2026-07-13T18:15:00+02:00
- Updated: 2026-07-13T18:15:00+02:00

## Arbeitet gerade an

Prüfung und Umsetzung eines konsistenten Website-Checks und Cloudflare-Deployments.

## Beanspruchte Pfade

- `.github/workflows/build-website.yml`
- `package.json`
- `wrangler.toml`
- eigene Statusdatei

## Erledigt

- veralteten Pfad `apps/website/public` identifiziert
- aktiven Pfad `website/` und Wrangler-Konfiguration bestätigt

## Geänderte Dateien

- diese Statusdatei

## Tests und Nachweise

Noch ausstehend.

## Entscheidungen und Annahmen

Cloudflare Git-Integration bleibt primärer Produktionsweg. GitHub Actions validiert und kann mit Secrets zusätzlich direkt deployen.

## Blocker

Direktes GitHub-Actions-Deployment benötigt `CLOUDFLARE_API_TOKEN` und `CLOUDFLARE_ACCOUNT_ID` als Repository-Secrets.

## Übergabe / Nächste Schritte

Workflow korrigieren, Dry-Run ergänzen und optionalen Produktionsdeploy dokumentieren.
