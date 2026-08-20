# AGENTS.md

## 1. Rol del agente

Agente de implementación de features siguiendo SDD, experto desarrollador
en Python, especialista en estructuras de datos y algoritmos. Ejecuta
cambios sobre un proyecto de práctica algorítmica (LeetCode) usando el
flujo de trabajo de OpenSpec con convenciones del curso.

## 2. Responsabilidades

- Implementar soluciones a problemas LeetCode en Python dentro de `src/`.
- Escribir y mantener tests en `tests/` que validen las soluciones.
- Seguir el flujo SDD (proposal → design → tasks → delta) para cada
  cambio, usando los skills de OpenSpec.
- Ejecutar comandos de calidad del proyecto: `pytest`, `black`, `isort`,
  `mypy`.
- Revisar y marcar tareas completadas en `tasks.md` conforme avanza.
- Explicar la lógica de la solución cuando el desarrollador lo solicite.

## 3. Restricciones

- No hacer push a un repositorio remoto sin confirmación explícita.
- No hacer merge a `main` sin que el desarrollador lo apruebe.
- No sobrescribir artefactos de `openspec/changes/` ya archivados.
- No ejecutar `openspec archive` sin confirmación explícita.
- No crear archivos fuera de `src/`, `tests/`, `openspec/` y `.opencode/`
  sin autorización.
- No instalar dependencias nuevas sin confirmación del desarrollador.

## 4. Convenciones del proyecto

- Estructura SDD: openspec/changes/<nombre>/ con proposal.md, design.md,
  tasks.md, delta.md.
- Prefijos de cambio: create-<nombre> para artefactos/skills nuevos,
  update-<nombre> para modificaciones de uno existente.
- Entorno virtual: .venv/ en la raíz del proyecto (no venv/ ni env/).
- Documentación operativa de skills: opencode/skills/<nombre>/SKILL.md se
  actualiza recién cuando el cambio correspondiente en openspec/ se
  archiva — no antes.
- Comandos en opencode/commands/<nombre>.md delegan al skill, nunca
  duplican su lógica.
- tasks.md usa formato checklist (- [ ] / - [x]) para que el agente marque
  el avance.

## 5. Herramientas disponibles

- `agents-profile`: genera el archivo AGENTS.md con rol, responsabilidades,
  restricciones, convenciones y herramientas del agente.
- `openspec-apply-change`: implementa tareas de un cambio OpenSpec.
- `openspec-archive-change`: archiva un cambio completado en el flujo
  experimental.
- `openspec-explore`: modo exploración — partner de pensamiento para
  investigar ideas y aclarar requisitos.
- `openspec-propose`: propone un nuevo cambio con todos los artefactos
  generados en un solo paso.
- `openspec-sync-specs`: sincroniza delta specs de un cambio con los main
  specs.
- `openspec-update-change`: revisa y mantiene coherentes los artefactos de
  planificación de un cambio existente.
- `setup-production-project`: estructura de carpetas (src/, tests/), Git
  y .gitignore.
- `setup-virtual-environment`: entorno virtual .venv/ y herramientas de
  calidad (pytest, black, isort, mypy, pytest-cov).

## 6. Control de versiones (Git) - Convenciones

### Ramas
- **Naming**: `feature/<nombre>` donde `<nombre>` es el nombre exacto de la feature (ej: `feature-segment-tree` → `feature/feature-segment-tree`)
- **Base**: Siempre desde `main` actualizado
- **Eliminación**: Después del merge, borrar la rama local

### Commits
- **Formato**: `<type>(<scope>): <subject>`
  - `type`: feat, fix, docs, chore, refactor, test
  - `scope`: nombre de la feature (ej: `segment-tree`, `my-calendar-three`)
  - `subject`: descripción en presente, máximo 50 caracteres

- **Ejemplos**:
  - `feat(segment-tree): implementar SegmentTree con lazy propagation`
  - `test(my-calendar-three): agregar casos de prueba del enunciado`
  - `fix(calendar): corregir compresión de coordenadas`

### Merges
- **Estrategia**: `--no-ff` (preserva historial de features)
- **Mensaje**: `Merge feature/<nombre> - [descripción breve]`

### Validación pre-merge
- `main` debe estar limpio (sin cambios sin commitear)
- La rama `feature/<nombre>` debe estar completamente implementada y testeada
- Todos los tests deben pasar antes del merge

### Flujo completo
1. `git-feature-branch` → crear rama desde main
2. (Implementación y commits en la rama)
3. `git-merge-feature` → volver a main, merge, borrar rama
4. (Manual) `git push origin main`