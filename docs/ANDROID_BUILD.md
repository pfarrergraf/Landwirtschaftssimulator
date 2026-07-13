# Android Build Plan

- Godot-Version im Workflow pinnen.
- OpenJDK und Android SDK in GitHub Actions installieren.
- Debug-APK fuer Pull Requests oder manuelle Runs erzeugen.
- Signiertes AAB nur bei Release-Tags und vorhandenen Secrets.
- Keystore niemals committen.
- Ziel-API vor jedem Store-Release gegen die aktuelle Google-Play-Vorgabe pruefen.
- ARM64 als Pflichtarchitektur; weitere Architekturen nach Zielgeraeten.
- Mobile Renderer und abgestufte Grafikqualitaet.

Der Workflow ist zunaechst als manuell ausloesbare Builddefinition angelegt. Er wird aktiviert, sobald Exportpresets und die erste echte Szene stabil sind.
