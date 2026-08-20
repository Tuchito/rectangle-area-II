---
name: setup-production-project
description: Inicializa la estructura base de un proyecto de práctica (src/, tests/), inicializa Git con rama main, y genera o actualiza .gitignore con merge inteligente. Uso cuando el usuario quiere arrancar un proyecto nuevo o verificar/completar el setup de uno existente.
allowed-tools: Bash(git:*)
license: MIT
compatibility: Requiere Python 3.10+ y git CLI. No crea entorno virtual, AGENTS.md ni repositorio remoto (permanecen manuales).
metadata:
  author: curso-ai-skill-architect
  version: "1.0"
  generatedBy: "practica-my-calendar-iii"
  status: borrador — pendiente de confirmación al archivar openspec/changes/create-setup-production-project
---

# setup-production-project

## Qué hace

Automatiza el setup mínimo de un proyecto de práctica algorítmica (sin
arquitectura en capas, sin base de datos, sin despliegue):

1. Crea `src/` y `tests/` si no existen. Respeta `openspec/` sin modificarlo.
2. Inicializa Git localmente y crea la rama `main`.
3. Genera `.gitignore`, o hace **merge inteligente** con uno ya existente
   (agrega solo las reglas faltantes, bajo el bloque
   `# Agregado por setup-production-project`, sin duplicar ni pisar reglas
   propias).

## Qué NO hace (permanece manual, por decisión documentada)

- No crea `AGENTS.md`.
- No crea el entorno virtual.
- No crea ni hace push al repositorio remoto.

## Idempotencia

Se puede ejecutar cualquier cantidad de veces sobre el mismo proyecto sin
efectos destructivos. Cada ejecución reporta explícitamente qué hizo y qué
omitió por ya existir.

## Cómo se invoca

Desde OpenCode, vía el comando delegado `/setup-production-project`
(ver `.opencode/commands/setup-production-project.md`), o directamente:

```bash
python .opencode/skills/setup-production-project/implementation.py
```

## Salida esperada

```
Resumen de ejecución:
✔ src/ creada
✔ tests/ creada
– openspec/ ya existía, sin cambios
✔ Git inicializado, rama main creada
✔ .gitignore generado
```

## Especificación de origen

Este skill fue diseñado siguiendo el ciclo SDD completo. Ver:
`openspec/changes/create-setup-production-project/{proposal,design,tasks,delta}.md`

## Tests

`tests/test_implementation.py` — 15 tests, 94% de cobertura sobre
`implementation.py`. Ejecutar con:

```bash
python -m pytest .opencode/skills/setup-production-project/tests/ --cov=implementation
```