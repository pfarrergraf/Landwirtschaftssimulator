# ARC-001 – Enginebewertung für den Android-MVP

## Ziel

Die Engineentscheidung wird anhand des ersten spielbaren Ausschnitts getroffen, nicht anhand allgemeiner Featurelisten. Bewertet werden Godot 4, Unity 6 und Unreal Engine 5.

## Muss-Kriterien

Eine Engine scheidet aus, wenn eines der folgenden Kriterien im technischen Spike nicht erfüllt wird:

1. reproduzierbarer Android-Build ohne kostenpflichtige Pflichtdienste,
2. Third-Person-Controller und Touch-Eingabe,
3. glTF/GLB-Import mit PBR-Materialien und Animationen,
4. instanzierte Vegetation mit LOD- oder Distanzstrategie,
5. generischer Traktor mit beweglichen Teilen,
6. lokales Save/Load,
7. automatisierbarer Headless- oder CLI-Build,
8. stabile Arbeit auf Windows 11 und WSL2-gestütztem Tooling.

## Gewichtete Bewertungsmatrix

| Kriterium | Gewicht | Godot 4 | Unity 6 | Unreal 5 | Nachweis im Spike |
|---|---:|---:|---:|---:|---|
| Android-Export und Toolchain | 18 | offen | offen | offen | APK auf Testgerät installieren |
| Mobile Rendering und Vegetation | 16 | offen | offen | offen | Testfeld mit Pflanzeninstanzen |
| Third-Person und Touch | 12 | offen | offen | offen | Laufen, Kamera, Aktion |
| Terrain/Feldzustände | 10 | offen | offen | offen | drei Bodenmaterialzustände |
| Fahrzeug und Animation | 10 | offen | offen | offen | Traktor, Radlenkung, Einstiegspunkt |
| glTF/GLB-Workflow | 8 | offen | offen | offen | identisches Referenzasset importieren |
| Build-Automation und CI | 8 | offen | offen | offen | dokumentierter CLI-Build |
| Testbarkeit der Kernlogik | 7 | offen | offen | offen | automatisierter Zustandswechseltest |
| Lizenz- und Kostenrisiko | 6 | offen | offen | offen | schriftliche Bewertung |
| Eignung für AI-Agenten | 5 | offen | offen | offen | textbasierte Projektstruktur und kleine Diffs |
| **Summe** | **100** |  |  |  |  |

Bewertungsskala je Kriterium: 0 = ungeeignet, 1 = starke Einschränkung, 2 = ausreichend, 3 = gut, 4 = sehr gut, 5 = erfüllt Zielbild besonders klar.

## Einheitlicher technischer Spike

Jeder Finalkandidat erhält denselben Minimalumfang:

- 100 × 100 Meter Testfläche,
- drei unterscheidbare Bodenmaterialien,
- 5.000 einfache Pflanzeninstanzen,
- Platzhalter-Avatar mit idle/walk/run,
- Third-Person-Kamera,
- Touch-Joystick und Aktionsknopf,
- generischer Traktor-Platzhalter,
- Ein-/Aussteigen als Zustandswechsel,
- lokaler Spielstand mit Avatarposition und Feldzustand,
- Android-Build im Medium-Profil.

## Messprotokoll

Für jeden Spike werden dokumentiert:

- Engine- und Toolchain-Version,
- Buildsystem und notwendige SDKs,
- APK-Größe,
- Startzeit,
- durchschnittliche und niedrigste FPS,
- RAM- und GPU-Speicherverbrauch soweit messbar,
- Dauer und Fehleranfälligkeit des Builds,
- Importprobleme,
- Codeumfang und Zahl engine-spezifischer Dateien,
- Blocker und Workarounds.

## Vorläufige Arbeitshypothese

Godot wird zuerst geprüft, weil das Repository bereits Godot-first geplant ist und ein schlanker, textbasierter Projektaufbau für den MVP vorteilhaft sein kann. Dies ist keine endgültige Engineentscheidung. Unity und Unreal bleiben Vergleichskandidaten, bis der Spike und die Matrix ausgefüllt sind.

## Entscheidungsregel

Die Engine wird angenommen, wenn:

- alle Muss-Kriterien erfüllt sind,
- der gewichtete Wert mindestens 70 von 100 Punkten erreicht,
- kein ungelöster Android-, Lizenz- oder Build-Blocker besteht,
- der MVP ohne proprietäre Fremdassets reproduzierbar gebaut werden kann.

Bei weniger als fünf Punkten Abstand zwischen den beiden besten Kandidaten entscheidet ein zweiter Performance- und Workflow-Spike.