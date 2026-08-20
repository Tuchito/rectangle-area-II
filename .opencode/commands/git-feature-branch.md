---
description: Lee plan-exercise.md, lista features disponibles, permite seleccionar una, y crea una rama feature-<nombre> basada en main
---

# Comando: git-feature-branch

## Uso
/git-feature-branch


## Descripción

Este comando invoca al skill `git-feature-branch`, que:
1. Lee `plan-exercise.md` (raíz del proyecto)
2. Lista las features disponibles
3. Permite seleccionar una (por número o nombre)
4. Valida que `main` está limpio
5. Crea la rama `feature-<nombre>` y se posiciona en ella

## Comportamiento

- **Lee** `plan-exercise.md`
- **Lista** features numeradas
- **Crea** rama `feature-<nombre>`
- **No modifica** archivos

## Ejemplo de Uso

```bash
/git-feature-branch
# Seleccionar feature por número: 3
# Seleccionar feature por nombre: segment-tree