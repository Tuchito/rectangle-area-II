---
description: Hace commit de todos los cambios locales en la rama actual con un mensaje convencional para la feature activa
---

# Comando: git-commit-feature

## Uso

## Descripción

Este comando invoca al skill `git-commit-feature`, que automatiza el commit de todos los cambios locales en la rama actual de la feature, generando un mensaje convencional siguiendo el estándar definido en `AGENTS.md`.

El skill:
1. Valida que estás en una rama `feature/<nombre>`
2. Verifica que hay cambios para commitear
3. Solicita una descripción para el commit
4. Genera el mensaje: `feat(<feature-scope>): <descripción>`
5. Ejecuta `git add .` y `git commit -m "<mensaje>"`

## Comportamiento

El agente:

1. **Valida la rama actual**:
   - Ejecuta `git branch --show-current`
   - Si no estás en una rama `feature/<nombre>` → **detenerse** con mensaje:

Error: No estás en una rama feature. Cambia a una rama feature primero.

2. **Verifica cambios pendientes**:
- Ejecuta `git status --porcelain`
- Si no hay cambios → **detenerse** con mensaje:
    No hay cambios para commitear. Asegúrate de haber implementado código.