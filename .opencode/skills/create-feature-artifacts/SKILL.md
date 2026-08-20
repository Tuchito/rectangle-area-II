---
name: create-feature-artifacts
description: Lee plan-exercise.md, lista las features disponibles, permite seleccionar una, y crea su carpeta con artefactos vacíos en openspec/changes/
version: 2.0.0
author: [Tuchito]
dependencies:
  - openspec (para estructura de artefactos)
  - git (para control de versiones)
---

# Skill: create-feature-artifacts

## Propósito

Leer el plan de features (`plan-exercise.md`), listar las features disponibles, permitir al usuario seleccionar una, y crear el scaffolding de artefactos OpenSpec para esa feature en `openspec/changes/`.

Este skill:
1. Lee `plan-exercise.md` (raíz del proyecto)
2. Extrae la lista de features (sección "## Features propuestas")
3. Muestra las features numeradas al usuario
4. Permite seleccionar una (por número o nombre)
5. Crea la carpeta `openspec/changes/feature-<nombre>-<numero>/`
6. Genera los 4 artefactos vacíos: `proposal.md`, `design.md`, `tasks.md`, `specs/delta.md`

---

## Cuándo Usar Este Skill

- Después de ejecutar `analyze-exercise` (cuando ya existe `plan-exercise.md`)
- Para crear el scaffolding de una feature específica
- Como paso previo a `write-artifacts-content`

---

## Flujo de Trabajo del Agente

### Paso 1: Validar Existencia de plan-exercise.md

1. Buscar `plan-exercise.md` en la raíz del proyecto
2. Si no existe → **detener** con mensaje:
    Error: No se encontró plan-exercise.md en la raíz del proyecto.
    Ejecuta primero /analyze-exercise para generar el plan.


### Paso 2: Leer y Extraer Features

1. Leer `plan-exercise.md`
2. Localizar la sección "## Features propuestas" (o "## 4. Features propuestas")
3. Extraer cada feature con su número y descripción.
- **Formato esperado:** `1. **feature-<nombre>**: <descripción>`
- **Ejemplo:** `1. **feature-sweep-events**: Extraer y ordenar eventos x del barrido`
4. Si no se encuentran features → **detener** con mensaje:
    Error: No se encontraron features en plan-exercise.md.
    Asegúrate de que la sección '## Features propuestas' existe y tiene el formato correcto.


### Paso 3: Mostrar Lista al Usuario

Presentar las features en formato numerado:

    - Features disponibles en plan-exercise.md:

    - feature-sweep-events — Extraer y ordenar eventos x del barrido

    - feature-coordinate-compression — Compresión de coordenadas Y

    - feature-segment-tree — Segment Tree con lazy propagation

    - feature-area-calculation — Cálculo del área total

    - feature-tests — Pruebas unitarias

Selecciona el número de la feature que quieres crear (1-5), o escribe el nombre:

### Paso 4: Procesar la Selección del Usuario

**4.1. Si el usuario responde con un número (ej: "3"):**
- Validar que el número esté en el rango (1..N)
- Seleccionar la feature correspondiente

**4.2. Si el usuario responde con un nombre (ej: "segment-tree"):**
- Buscar coincidencia parcial en los nombres de features
- Si hay una sola coincidencia → seleccionarla
- Si hay múltiples → pedir que sea más específico
- Si no hay coincidencia → mostrar error y volver a preguntar

**4.3. Si el usuario responde con "todas" o "all":**
- Preguntar: "¿Deseas crear todas las features? (s/n)"
- Si responde "s" → crear todas (una por una)
- Si responde "n" → volver al paso 3

### Paso 5: Crear la Carpeta y Artefactos

**5.1. Determinar el nombre de la carpeta:**
- Formato: `feature-<nombre>-<numero>`
- **Ejemplo:** `feature-sweep-events-1`
- **Importante:** Usar el número de la feature del plan (no un índice nuevo)

**5.2. Crear la estructura:**
openspec/changes/feature-<nombre>-<numero>/
├── proposal.md
├── design.md
├── tasks.md
└── specs/── delta.md

*Artefactos creados para feature-sweep-events-1*

📁 openspec/changes/feature-sweep-events-1/
├── proposal.md (vacío)
├── design.md (vacío)
├── tasks.md (vacío)
└── specs/delta.md (vacío)


### Paso 6: Preguntar por Siguiente Feature

Después de crear una feature, preguntar:
¿Quieres crear otra feature? (s/n)
- Si "s" → volver al paso 3 (mostrar features restantes)
- Si "n" → finalizar

---

## Casos Límite

| Caso                                      | Comportamiento |
|-------------------------------------------|--------------------------------|
| `plan-exercise.md` no existe                      | Detenerse con error |
| La sección "## Features propuestas" no existe     | Detenerse con error |
| El usuario selecciona un número fuera de rango    | Mostrar error y volver a preguntar |
| El usuario escribe un nombre ambiguo              | Pedir que sea más específico |
| La carpeta de la feature ya existe                | Preguntar si sobrescribir |
| El usuario escribe "cancelar" o "salir"           | Finalizar sin crear nada |
| `openspec/changes/` no existe                     | Detenerse: "Ejecuta openspec init primero" |

---

## Formato de plan-exercise.md (Esperado)

El skill espera que `plan-exercise.md` tenga una sección como:

```markdown
## 4. Features propuestas (5)
1. **feature-sweep-events**: Extraer y ordenar eventos x del barrido
2. **feature-coordinate-compression**: Compresión de coordenadas Y
3. **feature-segment-tree**: Segment Tree con lazy propagation
4. **feature-area-calculation**: Cálculo del área total
5. **feature-tests**: Pruebas unitarias

**Ejemplo de Uso**
# Usuario ejecuta
/create-feature-artifacts

# El agente:
# 1. Lee plan-exercise.md
# 2. Muestra lista de features
# 3. Usuario selecciona, por ej: "3" (feature-segment-tree)
# 4. Crea openspec/changes/feature-segment-tree-3/
# 5. Reporta éxito
# 6. Pregunta: "¿Quieres crear otra feature?"