---
description: Redacta el contenido completo de los 4 artefactos OpenSpec (proposal, design, tasks, delta) para una feature específica, usando plantillas
---

# Comando: write-artifacts-content

## Uso

/write-artifacts-content feature-<nombre>-<numero>

## Descripción

Este comando invoca al skill `write-artifacts-content`, que redacta el contenido completo de los 4 artefactos OpenSpec para una feature específica, basándose en:

- `plan-exercise.md` (contexto de atomización y dependencias)
- `project.md` (enunciado original del problema)
- `AGENTS.md` (perfil y tono del agente)
- **Plantillas en `assets/`** (estructura de cada artefacto)
- Artefactos de features dependientes (para consistencia)

## Comportamiento

El agente:

1. **Valida** que la feature existe en `plan-exercise.md`
2. **Lee** `plan-exercise.md`, `project.md`, `AGENTS.md` y dependencias
3. **Lee** las plantillas desde `.opencode/skills/write-artifacts-content/assets/`
4. **Redacta** `proposal.md`, `design.md`, `tasks.md`, `specs/delta.md`
5. **Pregunta** antes de sobrescribir artefactos existentes con contenido
6. **Reporta** el resultado de la operación

**No ejecuta** `openspec validate` ni genera commits automáticos.

## Ejemplo de Uso

```bash
# Redactar artefactos para feature-sweep-events-1
/write-artifacts-content feature-sweep-events-1

# El agente redactará los 4 artefactos basándose en las plantillas y el contexto disponible