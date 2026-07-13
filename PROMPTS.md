# PROMPTS.md

## Task-Start für einen Fachagenten

```text
Du arbeitest im Repository pfarrergraf/Landwirtschaftssimulator.
Lies AGENTS.md, TASKS.md, ARCHITECTURE.md, DECISIONS.md, TESTING.md,
SECURITY.md, SKILLS.md und docs/agents/WORK_PROTOCOL.md. Bei Grafikarbeit
zusätzlich docs/GRAPHICS_PLAN.md.

Bearbeite ausschließlich Task <TASK-ID> im exklusiven Pfad <PFAD>.
Lege zuerst docs/agents/status/<AGENT-ID>.md an und dokumentiere Branch,
Claim, Plan und beanspruchte Pfade. Verändere keine fremden Statusdateien
und keine koordinatorgeschützten Dateien. Arbeite in kleinen Commits,
führe passende Tests aus und vervollständige vor Übergabe die Statusdatei.
```

## Grafikasset-Review

```text
Prüfe das Assetpaket gegen docs/GRAPHICS_PLAN.md: Maßstab, PBR-Kanäle,
Benennung, Pivot, Collision, LODs, Texturgrößen, mobile Eignung,
Lizenz/Herkunft, Markenfreiheit und reproduzierbare Referenzbilder.
Liste blockierende Fehler getrennt von Optimierungsvorschlägen.
```

## Integration Agent

```text
Integriere ausschließlich bereits freigegebene Task-PRs. Ändere gemeinsame
Registries und Engine-Konfigurationen nur in diesem Integrations-PR.
Prüfe Schnittstellen, Daten-IDs, Assetpfade, Tests, visuelle Regressionen
und Android-Performance. Dokumentiere Konfliktentscheidungen in DECISIONS.md.
```
