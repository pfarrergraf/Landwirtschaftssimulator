# Android-Entwicklungs- und Exportsetup

## Ziel

Ein reproduzierbarer Debug-APK-Build des Projekts unter `game/godot/` ohne kostenpflichtige Dienste.

## Voraussetzungen

- stabile Godot-4-Version mit passenden Export Templates,
- Android Studio oder separat installiertes Android SDK,
- JDK 17,
- Android SDK Platform Tools,
- ein reales Android-Testgerät mit aktiviertem USB-Debugging.

Die konkrete Godot-Patchversion wird erst nach erfolgreichem Gerätetest in diesem Dokument festgeschrieben.

## Empfohlene Verzeichnisstruktur unter Windows

```text
C:\Dev\Godot\
C:\Dev\Android\Sdk\
C:\Dev\Landwirtschaftssimulator\
```

WSL2 wird für Python-, Asset- und Validierungswerkzeuge verwendet. Godot Editor, Android SDK, ADB und der APK-Export laufen zunächst nativ unter Windows, um USB- und SDK-Pfadprobleme zu minimieren.

## Godot konfigurieren

Im Godot Editor unter Editor Settings > Export > Android setzen:

- Java SDK Path: JDK-17-Verzeichnis,
- Android SDK Path: Android-SDK-Verzeichnis,
- ADB: aus `platform-tools`,
- Debug Keystore: Godot-Standard oder lokaler Entwicklungskeystore.

Keine Keystore-Passwörter oder privaten Signierschlüssel in Git einchecken.

## Projekt öffnen

```text
game/godot/project.godot
```

Die Hauptszene ist `res://scenes/main.tscn`.

## Erster manueller Test

1. Projekt im Editor öffnen.
2. Hauptszene starten.
3. Prüfen: Boden, Himmel, Sonnenlicht, Referenzkörper und Spielfigur sichtbar.
4. Mit W/A/S/D laufen.
5. Parser-, Import- und Renderingfehler dokumentieren.

## Android-Preset

Im Editor ein Android-Exportpreset anlegen:

- Runnable: aktiv,
- Export Format: APK für Debugtests,
- Architectures: zunächst `arm64-v8a`,
- Min SDK: anhand der tatsächlich installierten stabilen Godot-Version wählen,
- Internet-Berechtigung: deaktiviert, solange kein Netzwerkfeature existiert,
- Package ID: vorläufig `com.pfarrergraf.landwirtschaftssimulator.dev`.

`export_presets.cfg` darf eingecheckt werden, sofern es keine Geheimnisse oder lokalen absoluten Pfade enthält.

## Gerätetest

```powershell
adb devices
adb install -r .\build\android\landwirtschaftssimulator-debug.apk
```

Zu dokumentieren:

- Godot-Version,
- Export-Template-Version,
- Android SDK/Build Tools,
- Gerätemodell und Android-Version,
- Renderer,
- Start erfolgreich ja/nein,
- sichtbare Grafikfehler,
- durchschnittliche Bildrate der Testszene,
- Speicherverbrauch, sofern gemessen.

## Exit-Kriterium für ARC-001

`ARC-001` wird erst auf `done` gesetzt, wenn mindestens ein reproduzierbarer Debug-APK-Build auf einem realen Gerät startet. Bis dahin ist die Engineentscheidung angenommen, die technische Aufgabe aber `active`.
