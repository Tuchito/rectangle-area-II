---
name: git-feature-branch
description: Lee plan-exercise.md, lista las features disponibles, permite seleccionar una y crea una rama feature/<nombre> basada en main.
version: 2.0.0
author: [Tuchito]
dependencies:
  - git
  - openspec (para leer plan-exercise.md)
---

# Skill: git-feature-branch

## Propósito

Leer el plan de features (`plan-exercise.md`), listar las features disponibles, permitir al usuario seleccionar una, y crear una rama `feature/<nombre>` a partir de `main`.

Este skill:
1. Lee `AGENTS.md` para conocer el rol del agente
2. Lee `plan-exercise.md` y extrae las features
3. Muestra las features numeradas al usuario
4. Permite seleccionar una (por número o nombre)
5. Valida que `main` está limpio
6. Crea la rama `feature/<nombre>` y se posiciona en ella

---

## Cuándo Usar Este Skill

- Antes de comenzar la implementación de una feature
- Después de redactar los artefactos de una feature
- Como parte del flujo SDD: `write-artifacts-content` → `git-feature-branch` → implementación → `git-merge-feature`

---

## Flujo de Trabajo del Agente

### Paso 0: Leer Contexto del Proyecto

- Leer `AGENTS.md` (raíz del proyecto) para conocer el rol del agente
- Si no existe → continuar sin él (tono neutral)

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

**Presentar las features en formato numerado:**
📋 Features disponibles en plan-exercise.md:

    - feature-sweep-events-1 — Extraer y ordenar eventos x del barrido

    - feature-coordinate-compression-2 — Compresión de coordenadas Y

    - feature-segment-tree-3 — Segment Tree con lazy propagation

    - feature-area-calculation-4 — Cálculo del área total

    - feature-tests-5 — Pruebas unitarias

¿Cuál feature quieres implementar? (escribe el número o el nombre):


### Paso 4: Procesar la Selección del Usuario

**4.1. Si el usuario responde con un número (ej: "3"):**
- Validar que el número esté en el rango (1..N)
- Seleccionar la feature correspondiente
- El nombre de la rama será `feature-<nombre>` (sin el número)

**4.2. Si el usuario responde con un nombre (ej: "segment-tree"):**
- Buscar coincidencia parcial en los nombres de features
- Si hay una sola coincidencia → seleccionarla
- Si hay múltiples → pedir que sea más específico
- Si no hay coincidencia → mostrar error y volver a preguntar

**4.3. Si el usuario responde con "cancelar" o "salir":**
- Finalizar sin crear la rama

**4.4. Nombre de la rama:**
- La rama se llamará `feature-<nombre>` (ej: `feature-sweep-events`)
- **No incluye el número** (a diferencia de la carpeta de artefactos)

### Paso 5: Validar el Estado de Git

**5.1. Verificar que estás en la rama `main`:**

    - git branch --show-current

Si no estás en main → detener con mensaje:

Error: No estás en la rama main. Cambia a main primero.

**5.2. Verificar que main está actualizado (opcional):**

    - git fetch origin
    - git status
Si hay diferencias con origin/main → advertir y preguntar:

Advertencia: main no está sincronizado con origin/main.
¿Deseas continuar? (s/n)

**5.3. Verificar que no hay cambios sin commitear en main:**

    - git status --porcelain
Si hay cambios sin commitear → detener con mensaje:

Error: Hay cambios sin commitear en main.
Haz commit o stash de los cambios antes de continuar.

### Paso 6: Validar que la Rama no Existe Ya

**6.1 Verificar si la rama feature-<nombre> ya existe:**


    - git branch --list feature-<nombre>
    - git branch -r --list origin/feature-<nombre>

**6.2 Si existe localmente → detener con mensaje:**

    - Error: La rama feature-<nombre> ya existe localmente.
    - Si deseas trabajar en ella, usa: git checkout feature-<nombre>

**6.3 Si existe en remoto → advertir y preguntar:**

    - Advertencia: La rama feature-<nombre> existe en remoto.
    - ¿Deseas hacer checkout de la rama remota? (s/n)
    - Si responde "s" → git checkout -b feature-<nombre> origin/feature-<nombre>
    - Si responde "n" → detenerse

### Paso 7: Crear la Rama y Posicionarse
**7.1 Crear la rama desde main:**

    - git checkout -b feature-<nombre>

**7.2 Verificar que la rama se creó correctamente:**

    - git branch --show-current
    - Debe mostrar feature-<nombre>

### Paso 8: Reportar Resultado
 *Al finalizar, mostrar un resumen claro:*

    ✅ Rama creada y posicionada

    Rama actual: feature-<nombre>
    Base: main (commit: [hash] - [mensaje])

    📝 Siguiente paso: Implementa el código y haz commits en esta rama.

*Notas para el Agente*
    - Leer siempre plan-exercise.md (no plan-features.md)

    - El nombre de la rama es feature-<nombre> (sin número)

    - No hacer commits en este skill — solo crea la rama

    - No modificar archivos — solo operaciones de Git

    - Ser conservador — ante cualquier duda, detenerse y preguntar

    - Usar el tono de AGENTS.md si existe

