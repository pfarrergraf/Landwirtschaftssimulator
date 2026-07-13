# ARC-001 – Engineentscheidung

## Entscheidung

Für den ersten spielbaren Android-MVP wird **Godot 4.x mit GDScript und Mobile-Renderer** verwendet.

Die konkrete Patchversion wird nach dem ersten reproduzierbaren Android-Export festgeschrieben. Bis dahin gilt: aktuelle stabile Godot-4-Version, keine Preview- oder Nightly-Builds.

## Gründe

- vollständig quelloffen und MIT-lizenziert,
- keine laufende Umsatz-, Seat- oder Runtime-Lizenzentscheidung für den MVP,
- kleine, textbasierte Projekt- und Szenendateien eignen sich gut für KI-gestützte Entwicklung,
- direkte Android-Exportpipeline,
- glTF/GLB-Import passt zum bestehenden Assetvertrag,
- MultiMesh, LOD, Occlusion Culling und Mobile-Renderer passen zur geplanten Vegetationsdarstellung,
- GDScript erlaubt schnelle, überschaubare Prototypen ohne zusätzliche .NET-Abhängigkeit.

## Verworfene Hauptalternative: Unity

Unity bleibt eine technisch leistungsfähige Alternative, insbesondere für größere Teams, umfangreiche Asset-Store-Nutzung und etablierte kommerzielle Mobile-Pipelines. Für dieses frühe, KI-first entwickelte Projekt überwiegen jedoch Godots geringere Lizenz- und Toolchain-Komplexität sowie die besser diffbaren Projektdateien.

## Technische Leitplanken

- Renderer: `gl_compatibility` für breite Android-Kompatibilität im ersten Spike; Forward+/Mobile erst nach Gerätemessung gezielt bewerten.
- Sprache: GDScript für Runtime- und Gameplaycode.
- 3D-Austausch: GLB/glTF 2.0.
- Maßeinheit: 1 Godot-Einheit = 1 Meter.
- Simulation bleibt von Szenen und Nodes getrennt.
- Rendering großer Pflanzenbestände erfolgt später über MultiMesh/Instancing und LOD-nahe Cluster.
- Keine Engine-Plugins ohne Lizenzprüfung und dokumentierten Nutzen.

## Exit-Kriterien ARC-001

- Projekt startet im Editor und per Kommandozeile ohne Parserfehler.
- Testszene enthält Boden, Licht, Kamera und Referenzkörper.
- Android-Exportvorlage und SDK-Pfade sind dokumentiert.
- Leerer APK-Debugbuild wird auf mindestens einem realen Gerät gestartet.
- Erst danach wird die exakte Godot-Patchversion festgeschrieben.

## Offene technische Messungen

1. `gl_compatibility` gegen Mobile-Renderer auf Zielgeräten vergleichen.
2. MultiMesh-Test mit 10.000, 50.000 und 100.000 Pflanzeninstanzen.
3. Texturkompression und Speicherverbrauch auf Android messen.
4. Schattenreichweite und Vegetations-LOD für Low/Mid/High festlegen.
