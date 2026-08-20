---
name: write-artifacts-content
description: Redacta el contenido completo de los 4 artefactos OpenSpec (proposal, design, tasks, delta) para una feature específica, basándose en plantillas, plan-exercise.md, project.md, y artefactos de features dependientes.
version: 2.0.0
author: [Tuchito]
dependencies:
  - openspec (para estructura de artefactos)
  - git (para control de versiones)
---

# Skill: write-artifacts-content

## Propósito

Redactar el contenido completo de los 4 artefactos OpenSpec para una feature específica, utilizando las plantillas definidas en `assets/` y el contexto del proyecto (`plan-exercise.md`, `project.md`, `AGENTS.md`, y artefactos de features dependientes).

Este skill:
1. Lee el contexto del proyecto (`AGENTS.md`, `project.md`, `plan-exercise.md`)
2. Lee las plantillas de artefactos desde `assets/`
3. Lee artefactos de features dependientes (si existen)
4. Redacta `proposal.md`, `design.md`, `tasks.md`, `specs/delta.md`
5. Pregunta antes de sobrescribir artefactos existentes
6. Reporta el resultado de la operación

---

## Cuándo Usar Este Skill

- Después de ejecutar `create-feature-artifacts` (cuando ya existe el scaffolding vacío)
- Para redactar artefactos de una feature específica
- Como paso previo a `git-feature-branch` e implementación

---

## Flujo de Trabajo del Agente

### Paso 1: Validar Entrada

1. El usuario proporciona el nombre de una feature mediante el comando:
/write-artifacts-content feature-<nombre>-<numero>

**Ejemplo:** `/write-artifacts-content feature-sweep-events-1`

2. Validar que el nombre sigue el formato `feature-<nombre>-<numero>`.

3. Validar que la feature existe en `plan-exercise.md`:
- Leer `plan-exercise.md` (raíz del proyecto)
- Buscar la feature en la sección "## Features propuestas"
- Si no existe → **detener** con mensaje:

  Error: feature-<nombre>-<numero> no encontrada en plan-exercise.md.
  Las features disponibles son: [lista de features]


4. Validar que la carpeta de la feature existe en `openspec/changes/`:
- Si no existe → **detener** con mensaje:
  Error: No se encontró la carpeta openspec/changes/feature-<nombre>-<numero>/.
  Ejecuta primero /create-feature-artifacts para crear el scaffolding.


### Paso 2: Leer Contexto del Proyecto

**2.1. Leer AGENTS.md**
- Ubicación: `AGENTS.md` (raíz del proyecto)
- Propósito: Conocer el rol del agente, tono y estilo esperado
- Si no existe → continuar sin él (usar tono neutral)

**2.2. Leer project.md**
- Ubicación: `project.md` (raíz del proyecto)
- Propósito: Entender el enunciado del problema
- Extraer:
- Descripción general
- Restricciones clave
- Ejemplos (entrada/salida)
- Si no existe → **detener** con mensaje:
Error: No se encontró project.md. Asegúrate de tener el enunciado del problema.


**2.3. Leer plan-exercise.md**
- Ubicación: `plan-exercise.md` (raíz del proyecto)
- Extraer:
- Justificación del corte para la feature seleccionada
- Dependencias (qué features necesita esta feature)
- Posición de la feature en el grafo de dependencias

**2.4. Leer artefactos de features dependientes** (si existen)
- Si la feature tiene dependencias listadas en `plan-exercise.md`:
- Leer `openspec/changes/feature-dependiente-<numero>/proposal.md`
- Leer `openspec/changes/feature-dependiente-<numero>/design.md`
- Extraer:
  - Decisiones de diseño que afectan a la feature actual
  - Interfaz pública que debe consumir esta feature
  - Términos y convenciones usadas
- Esto asegura **consistencia** entre artefactos de features relacionadas

### Paso 3: Leer las Plantillas de Artefactos

**3.1. Ubicación de las plantillas:**
.opencode/skills/write-artifacts-content/assets/
├── plantilla-proposal.md
├── plantilla-design.md
├── plantilla-tasks.md
└── plantilla-delta.md


**3.2. Para cada artefacto, el agente debe:**
1. Leer la plantilla correspondiente
2. Identificar las secciones requeridas y su estructura
3. Usar la plantilla como guía para redactar el contenido

**3.3. Si alguna plantilla no existe:**
- **Detener** con mensaje:
Error: No se encontró plantilla-<tipo>.md en assets/.
Asegúrate de que todas las plantillas existen.


### Paso 4: Redactar proposal.md

**Ubicación:** `openspec/changes/feature-<nombre>-<numero>/proposal.md`

**Basado en:** `plantilla-proposal.md`

**Contenido a generar:**
- Sección `## Why`:
- Explicar por qué esta feature es necesaria
- Vincular con `project.md` y `plan-exercise.md`
- Mencionar dependencias si existen
- Sección `## What Changes`:
- Lista de cambios concretos (módulos, clases, funciones)
- Mencionar dependencias que se añaden
- **Nivel intermedio:** 2-4 párrafos por sección, 1 página total

### Paso 5: Redactar design.md

**Ubicación:** `openspec/changes/feature-<nombre>-<numero>/design.md`

**Basado en:** `plantilla-design.md`

**Contenido a generar:**
- **Arquitectura general:** Descripción de alto nivel
- **Decisiones clave:** 2-4 decisiones con justificación y alternativas descartadas
- **Interfaz pública:** Clases, métodos, type hints
- **Dependencias:** Qué otras features necesita
- **Alternativas descartadas:** 1-2 opciones consideradas y por qué no se eligieron
- **Nivel intermedio:** Suficiente para guiar la implementación

### Paso 6: Redactar tasks.md

**Ubicación:** `openspec/changes/feature-<nombre>-<numero>/tasks.md`

**Basado en:** `plantilla-tasks.md`

**Contenido a generar:**
- Lista de tareas con checkboxes `- [ ]`
- Cada tarea con:
- Nombre descriptivo
- Descripción breve
- Criterio de "hecho" (sin ambigüedad)
- Dependencias entre tareas
- **Cantidad:** 3-7 tareas por feature
- **Atomicidad:** Cada tarea debe completarse en una sesión

### Paso 7: Redactar specs/delta.md

**Ubicación:** `openspec/changes/feature-<nombre>-<numero>/specs/delta.md`

**Basado en:** `plantilla-delta.md`

**Contenido a generar:**
- **Estado anterior:** Descripción del estado previo
- **Cambios introducidos:** Categorizados como Nuevo/Modificado/Eliminado
- **Impacto en consumidores:** Qué otras features se ven afectadas
- **Breve y directo**

### Paso 8: Preguntar Antes de Sobrescribir

**Comportamiento:**

1. Para cada uno de los 4 archivos (`proposal.md`, `design.md`, `tasks.md`, `specs/delta.md`):
 - Verificar si existe en `openspec/changes/feature-<nombre>-<numero>/`
 - Si no existe → crearlo sin preguntar
 - Si existe y está vacío (0 bytes) → sobrescribir sin preguntar
 - Si existe y tiene contenido → **preguntar al usuario**

2. **Formato de la pregunta:**
El archivo openspec/changes/feature-<nombre>-<numero>/proposal.md ya existe y tiene contenido.
¿Deseas sobrescribirlo? (s/n)


3. **Manejo de respuestas:**
- `s` o `S` → sobrescribir
- `n` o `N` → conservar el archivo existente, saltar a la siguiente pregunta
- Otro → repetir la pregunta

4. **Resumen final:**
- Mostrar qué archivos se sobrescribieron y cuáles se conservaron

### Paso 9: Escribir los Archivos

1. Guardar cada artefacto redactado en:
  openspec/changes/feature-<nombre>-<numero>/proposal.md
  openspec/changes/feature-<nombre>-<numero>/design.md
  openspec/changes/feature-<nombre>-<numero>/tasks.md
  openspec/changes/feature-<nombre>-<numero>/specs/delta.md


2. **No ejecutar `openspec validate`** (decisión de diseño: la validación se hará después manualmente).

3. **No hacer commits de Git** (decisión de diseño: los cambios se revisan antes de commitear).

### Paso 10: Reportar Resultado

Al finalizar, mostrar un resumen claro:
✅ Artefactos redactados para feature-<nombre>-<numero>

Archivos generados/sobrescritos:

  - openspec/changes/feature-<nombre>-<numero>/proposal.md ✅

  - openspec/changes/feature-<nombre>-<numero>/design.md ✅

  - openspec/changes/feature-<nombre>-<numero>/tasks.md ✅

  - openspec/changes/feature-<nombre>-<numero>/specs/delta.md ✅

