# MODELS.md

## Grundsatz

Das Spiel darf ohne laufenden KI-Dienst gebaut und ausgeführt werden. KI-Modelle dienen optional der lokalen Entwicklung von Konzepten, Texturen, Varianten, Dokumentation und Prüfungen.

## Vorgesehene lokale Workflows

- lokales LLM über vLLM für Planung, Codeassistenz und Datenentwürfe,
- ComfyUI für Moodboards, Materialideen und kontrollierte Texturvarianten,
- klassische 3D-Werkzeuge für Geometrie, Retopologie, UV, LOD und Export.

## Hardware- und Softwareprofil

- Windows 11 mit WSL2/Ubuntu,
- RTX Pro 6000 Blackwell mit 96 GB VRAM,
- Python 3.11/3.12,
- PyTorch cu128 passend zur Projektumgebung,
- `uv` für Python-Umgebungen,
- keine separate Triton-, FlashAttention- oder xFormers-Pflicht.

## VRAM-Regel

Bei gleichzeitig laufenden Modellen muss ein Gesamtbudget dokumentiert werden. Modellgewichte, Aktivierungen, KV-Cache, ComfyUI-Pipeline, CUDA-Overhead und Sicherheitsreserve werden gemeinsam betrachtet. Kein Workflow wird nur deshalb freigegeben, weil ein einzelnes Modell isoliert in 96 GB passt.

## Modell- und Assetrechte

Modellgewichte werden nicht im Repository gespeichert. Vor kommerzieller Nutzung KI-generierter Assets sind Modelllizenz, Eingabequellen, Ausgabeprüfung und Herkunftsmetadaten zu dokumentieren.
