---
description: Lee plan-exercise.md, lista features, permite seleccionar una, y crea su carpeta con artefactos vacíos en openspec/changes/
---

# Comando: create-feature-artifacts

## Uso
/create-feature-artifacts


## Descripción

Este comando invoca al skill `create-feature-artifacts`, que:
1. Lee `plan-exercise.md` (raíz del proyecto)
2. Lista las features disponibles
3. Permite seleccionar una (por número o nombre)
4. Crea la carpeta `feature-<nombre>-<numero>/` en `openspec/changes/`
5. Genera 4 artefactos vacíos: `proposal.md`, `design.md`, `tasks.md`, `specs/delta.md`

## Comportamiento

- **Lee** `plan-exercise.md`
- **Lista** features numeradas
- **Crea** scaffolding vacío
- **No redacta** contenido (eso lo hace `write-artifacts-content`)

## Ejemplo de Uso

```bash
# Seleccionar feature por número
/create-feature-artifacts
# Usuario: 3

# Seleccionar feature por nombre
/create-feature-artifacts
# Usuario: segment-tree