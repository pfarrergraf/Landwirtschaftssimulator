# Integrationsaudit vom 13. Juli 2026

## Prüfperspektiven

Die von mehreren Agenten erzeugten Änderungen wurden in getrennten Tracks geprüft:

1. Repository-Architektur und kanonische Pfade,
2. Website und Cloudflare-Deployment,
3. Godot-/Android-Build und APK-Veröffentlichung,
4. Tests und Schutz vor erneuten Pfadabweichungen.

## Kanonische Projektstruktur

Während der parallelen Arbeit entstanden jeweils zwei Projektlinien. Für alle neuen Änderungen und Deployments gelten verbindlich:

| Bereich | Kanonischer Pfad | Historischer Pfad |
|---|---|---|
| Godot-Spiel | `game/godot/` | `apps/game/` |
| Öffentliche Website | `website/` | `apps/website/public/` |

Die historischen Pfade bleiben zunächst zur Nachvollziehbarkeit erhalten. Kein produktiver Workflow darf sie mehr als Quelle verwenden.

## Websiteprüfung

Der Website-Track wurde unabhängig auf einem eigenen Branch geprüft.

Bestätigt wurden:

- `wrangler.toml` veröffentlicht `website/`,
- HTML, CSS und JavaScript sind vorhanden,
- `npm run check` läuft,
- `wrangler deploy --dry-run` läuft,
- die geprüfte Website wird als Actions-Artefakt bereitgestellt,
- ein direkter Cloudflare-Deploy ist mit `CLOUDFLARE_API_TOKEN` und `CLOUDFLARE_ACCOUNT_ID` möglich,
- die bestehende Cloudflare-Git-Integration kann weiterhin `main` automatisch veröffentlichen.

Der zugehörige Pull Request #13 wurde erst nach erfolgreichem Workflow gemergt.

## Android- und APK-Prüfung

Der erste Audit zeigte, dass der frühere Android-Workflow lediglich Dateien in `apps/game/` prüfte und keine APK erzeugte.

Der neue Workflow verwendet ausschließlich `game/godot/` und führt aus:

1. Java-17-Setup,
2. Android-SDK-Setup und Installation der benötigten Pakete,
3. Download der offiziellen Godot-4.3-Binärdatei und Export-Templates,
4. lokale Debug-Keystore-Erzeugung ohne eingecheckte Geheimnisse,
5. Godot-Import des Projekts,
6. Debug-APK-Export,
7. Prüfung auf eine nichtleere APK,
8. Upload der APK als GitHub-Actions-Artefakt.

Mehrere absichtlich nicht gemergte Prüfläufe deckten nacheinander auf:

- einen ungeeigneten Container-Exportweg,
- fehlende explizite Android-SDK-/Keystore-Konfiguration,
- einen Shell-Fehler bei der Lizenzbestätigung,
- fehlende ETC2/ASTC-Texturimporte für Android.

Nach Behebung aller Punkte lief der vollständige APK-Build erfolgreich. Pull Request #12 wurde anschließend gemergt.

Bei einem Versions-Tag wie `v0.1.0` erstellt der Workflow zusätzlich ein GitHub Release und hängt die erzeugte Debug-APK an.

## Qualitätssicherung

Parallel zum Website- und APK-Build liefen erfolgreich:

- `Validate and test`,
- `Repository validation`,
- die bestehenden Daten-, Simulations- und Strukturtests.

Der Repository-Validator wird erweitert, damit folgende Regressionen künftig automatisch scheitern:

- Android-Workflow verweist wieder auf `apps/game/`,
- Website-Workflow verweist wieder auf `apps/website/public/`,
- Wrangler veröffentlicht nicht mehr `website/`,
- kanonisches Godot-Projekt, Exportpreset oder Website-Einstieg fehlen.

## Verbindliche Deploymentwege

### Website

```text
website/ -> GitHub-Prüfung -> Wrangler-Dry-Run -> Cloudflare Git-Deployment
```

Optional kann GitHub Actions mit den beiden Cloudflare-Secrets selbst produktiv deployen.

### APK

```text
game/godot/ -> GitHub Actions -> Debug-APK-Artefakt
Versions-Tag v* -> GitHub Release mit APK
```

## Verbleibende Grenzen

- Die erzeugte APK ist ein Debug-Build, kein Play-Store-Release.
- Ein erfolgreicher CI-Build ersetzt keinen Test auf einem realen Android-Gerät.
- Website und GitHub Release sind noch nicht über eine automatisch aktualisierte Downloadschaltfläche verbunden.
- Die historischen Verzeichnisse sollten später archiviert oder entfernt werden, sobald keine Dokumentation mehr darauf angewiesen ist.

## Gesamtergebnis

Website- und APK-Deployment sind technisch vorhanden, reproduzierbar geprüft und auf die aktuellen Projektpfade ausgerichtet. Die von mehreren Agenten erzeugten Kernänderungen passen nach den beschriebenen Korrekturen zusammen. Für eine öffentliche APK-Empfehlung fehlt nur noch der reale Gerätetest; für eine dauerhafte Downloadschaltfläche auf der Website fehlt noch die Release-Verknüpfung.
