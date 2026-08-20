---
description: Analiza project.md y genera un plan de features (plan-exercise.md) con features atómicas, justificación y dependencias
---

# Comando: analyze-exercise

## Uso
    /analyze-exercise

## Descripción

Este comando invoca al skill `analyze-exercise`, que:

1. Lee `AGENTS.md`, `project.md` y (opcionalmente) imágenes
2. Sigue la plantilla en `assets/plantilla.md`
3. Genera `plan-exercise.md` con features propuestas
4. Solicita aprobación del usuario

## Comportamiento

- **No crea artefactos** (solo plan)
- **No escribe código** (solo análisis)
- **Requiere aprobación** del usuario

## Ejemplo de Uso
```bash
/analyze-exercise
