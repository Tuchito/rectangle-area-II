---
name: git-commit-feature
description: Hace commit de los cambios con mensaje convencional para la feature actual
---

## Propósito

Commitear los cambios en la rama actual con un mensaje convencional.

## Flujo

1. Validar que estás en una rama `feature/<nombre>`
2. Validar que hay cambios para commitear
3. Generar mensaje: `feat(<feature-name>): <descripción>`
4. Preguntar al usuario: "¿Cuál es la descripción del commit?"
5. Ejecutar `git add .` y `git commit -m "..."`