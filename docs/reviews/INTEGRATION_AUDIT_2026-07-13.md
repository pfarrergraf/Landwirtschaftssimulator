# Integrationsaudit vom 13. Juli 2026

## Umfang

Vier voneinander getrennte Prüfperspektiven wurden angewendet:

1. **Repository-Architektur:** Pfade, Dokumentation und kanonische Projektstruktur.
2. **Android-Build:** Godot-Projekt, Exportpreset, APK-Artefakt und Releaseweg.
3. **Website-Deployment:** aktive Website, Wrangler-Konfiguration und Cloudflare-Workflow.
4. **Qualitätssicherung:** Tests, Validatoren und Schutz gegen erneute Pfadabweichungen.

## Ergebnis

Der fachliche Prototyp ist zusammenführbar, aber die von mehreren Agenten erzeugten Linien waren noch nicht vollständig integriert. Insbesondere existieren jeweils zwei konkurrierende Projektpfade.

### Kritisch: zwei Godot-Projekte

- `apps/game/` ist eine ältere Planungsshell.
- `game/godot/` enthält den aktuell weiterentwickelten spielbaren Prototyp mit Avatar, Kamera, Savegame und Traktor.
- Die aktuellen Tests referenzieren `game/godot/`.
- Der vorhandene Android-Workflow referenziert dagegen noch `apps/game/` und erzeugt keine APK.

**Kanonische Entscheidung für die Integration:** `game/godot/` ist das aktive Spielprojekt. `apps/game/` gilt als Legacy-Pfad und darf nicht mehr für Build oder Deployment verwendet werden.

### Kritisch: zwei Websitepfade

- `apps/website/public/` enthält eine ältere Einzelseite.
- `website/` enthält die aktuelle responsive Website.
- `wrangler.toml` veröffentlicht korrekt `website/`.
- Der bisherige GitHub-Workflow paketiert jedoch noch `apps/website/public/`.

**Kanonische Entscheidung für die Integration:** `website/` ist die aktive Website. `apps/website/public/` gilt als Legacy-Pfad.

### Android-Deployment vor Audit

Der Workflow `.github/workflows/build-android.yml` war nur ein Planungsgate. Er:

- lief ausschließlich manuell,
- prüfte nur zwei Dateien in `apps/game/`,
- installierte Godot nicht,
- besaß kein aktives `export_presets.cfg`,
- erzeugte und veröffentlichte keine APK.

Damit bestand vor diesem Audit **kein funktionsfähiger APK-Deployment-Workflow**.

### Website-Deployment vor Audit

Cloudflare Workers ist über `wrangler.toml` und den Cloudflare-Git-Build vorbereitet. Der GitHub-Workflow `.github/workflows/build-website.yml` war jedoch veraltet und:

- beobachtete den falschen Pfad,
- validierte die aktuelle Website nicht,
- prüfte Wrangler nicht,
- stellte nur ein Artefakt des Legacy-Pfads bereit.

Damit war das direkte Cloudflare-Deployment grundsätzlich möglich, aber die GitHub-seitige Qualitätssicherung passte nicht zur produktiven Website.

### Doppelte Validierungsworkflows

`validate.yml` und `repository-validation.yml` prüfen teilweise unterschiedliche historische Schichten. Beide können vorerst parallel bestehen, müssen aber mittelfristig konsolidiert werden. Entscheidend ist, dass die Repositoryvalidierung künftig die kanonischen Deploymentpfade und Workflows erzwingt.

## Verbindliche Integrationsmaßnahmen

1. Android-Workflow auf `game/godot/` umstellen.
2. Echtes Android-Exportpreset einchecken, ohne private Signierschlüssel.
3. Debug-APK als GitHub-Actions-Artefakt bereitstellen.
4. Bei Versions-Tags eine öffentliche GitHub-Prerelease mit APK erzeugen.
5. Website-Workflow auf `website/` und `wrangler.toml` umstellen.
6. Website-Dateien, JavaScript und Wrangler-Dry-Run automatisch prüfen.
7. Optionalen manuellen Cloudflare-Deploy über GitHub-Secrets ermöglichen; der bestehende Cloudflare-Git-Build bleibt der primäre Produktionsweg.
8. Kanonische Pfade in Governance, Architektur und README dokumentieren.
9. Validator ergänzen, damit Workflows keine Legacy-Pfade mehr referenzieren.

## Abnahmezustand

Das Repository gilt nach Umsetzung der Maßnahmen als integriert, wenn:

- beide Deployment-Workflows ausschließlich kanonische Pfade verwenden,
- ein Actions-Lauf eine Debug-APK als Artefakt erzeugt,
- ein Website-Lauf `wrangler deploy --dry-run` erfolgreich ausführt,
- Cloudflare den Hauptbranch aus `website/` veröffentlicht,
- Repositorytests und Governancevalidierung erfolgreich sind,
- `apps/game/` und `apps/website/public/` ausdrücklich als Legacy gekennzeichnet sind und von keinem Deployment referenziert werden.
