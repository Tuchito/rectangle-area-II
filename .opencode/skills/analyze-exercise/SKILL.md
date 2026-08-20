---
name: analyze-exercise
description: Analiza un enunciado (project.md) y genera un plan de features (plan-exercise.md) con features atómicas, justificación y dependencias, siguiendo el flujo SDD.
version: 1.0.0
author: [Tuchito]
dependencies:
  - openspec (para lectura de AGENTS.md y project.md)
  - git (para control de versiones)
---

# Skill: analyze-exercise

## Propósito

Analizar un enunciado de problema (`project.md`) y generar un plan de features atómico (`plan-exercise.md`) que servirá como base para el desarrollo con SDD.

Este skill:
1. Lee el contexto del proyecto (`AGENTS.md`, `project.md`, imágenes/gráficos)
2. Sigue la plantilla definida en `assets/plantilla.md`
3. Propone features, justificación y dependencias
4. Solicita aprobación del usuario antes de finalizar

---

## Cuándo Usar Este Skill

- Al iniciar un nuevo proyecto a partir de un enunciado (`project.md`)
- Antes de ejecutar `create-feature-artifacts` (para tener un plan validado)
- Cuando necesites estandarizar el análisis inicial del problema

---

## Flujo de Trabajo del Agente

### Paso 1: Leer el Contexto del Proyecto

**1.1. Leer AGENTS.md**
- Ubicación: `AGENTS.md` (raíz del proyecto)
- Propósito: Conocer el rol del agente, tono y estilo esperado
- Si no existe → continuar sin él (usar tono neutral)

**1.2. Leer project.md**
- Ubicación: `project.md` (raíz del proyecto)
- Propósito: Entender el enunciado del problema
- Extraer:
  - Descripción general
  - Restricciones clave
  - Ejemplos (entrada/salida)
  - Estructura esperada (si la menciona)
- Si no existe → **detener** con mensaje:  
    Error: No se encontró project.md. Asegúrate de tener el enunciado del problema.


**1.3. Buscar imágenes/gráficos (opcional)**
- Buscar archivos de imagen en la raíz: `*.png`, `*.jpg`, `*.jpeg`, `*.gif`
- Si existe alguna imagen:
- Preguntar al usuario: "He encontrado una imagen (rectangulos.png). ¿Quieres describirla para incluirla en el plan?"
- Si el usuario la describe, incluirla en el plan
- Si no, continuar sin ella

### Paso 2: Leer la Plantilla del Plan

**2.1. Leer assets/plantilla.md**
- Ubicación: `.opencode/skills/analyze-exercise/assets/plantilla.md`
- Propósito: Conocer el formato exacto que debe tener `plan-exercise.md`
- Si no existe → **detener** con mensaje:
    Error: No se encontró la plantilla en .opencode/skills/analyze-exercise/assets/plantilla.md


**2.2. Analizar la estructura de la plantilla**
- Identificar secciones requeridas:
- Resumen del problema
- Restricciones clave
- Enfoque sugerido
- Features propuestas (3-5)
- Justificación del corte
- Dependencias entre features
- Checklist de aprobación

### Paso 3: Generar plan-exercise.md

**3.1. Analizar el problema**
- Identificar el dominio del problema (ej: geometría, grafos, strings, etc.)
- Identificar la estructura de datos clave (ej: Segment Tree, Sweep Line, etc.)
- Identificar el algoritmo principal (ej: barrido, DFS, DP, etc.)
- Estimar complejidad temporal y espacial

**3.2. Proponer features atómicas (3-5)**
- Aplicar criterio de atomicidad (Sesión 2):
- ¿Se puede completar en una sola sesión de trabajo?
- ¿Tiene un criterio de "hecho" sin ambigüedad?
- ¿No depende de decisiones de diseño aún no tomadas?

- **Ejemplo para "Área de Rectángulos II":**

    *1. feature-sweep-events: Extraer y ordenar eventos x del barrido*

    *2. feature-segment-tree-coords: Segment Tree con lazy para altura activa*

    *3. feature-area-calculation: Cálculo de área por franjas*

    *4. feature-tests: Pruebas unitarias con ejemplos y casos borde*


**3.3. Justificar el corte**
- Por cada feature, explicar por qué se separó de las demás
- Mencionar qué criterio de atomicidad aplica
- No usar frases genéricas ("porque sí", "porque parecía razonable")

**3.4. Identificar dependencias**
- Grafo de dependencias entre features (ej: `A → B → C`)
- Feature raíz (sin dependencias)
- Feature hoja (depende de todas)

**3.5. Generar el archivo plan-exercise.md**
- Usar la plantilla como guía
- Ubicación: `plan-exercise.md` (raíz del proyecto)
- **No crear carpetas ni artefactos** (eso lo hace `create-feature-artifacts`)

### Paso 4: Solicitar Aprobación del Usuario

**4.1. Mostrar resumen del plan**

Plan generado para [nombre del problema]

   1- Features propuestas:

   2- feature-sweep-events: Extraer y ordenar eventos x

   3- feature-segment-tree-coords: Segment Tree con lazy

   4- feature-area-calculation: Cálculo de área por franjas

   5- feature-tests: Pruebas unitarias

### Dependencias:
    feature-sweep-events → feature-segment-tree-coords → feature-area-calculation -> feature-tests

*Plan completo en: plan-exercise.md*

**4.2. Preguntar al usuario**
¿Apruebas este plan para continuar con el desarrollo? (s/n)

**4.3. Manejo de respuestas**
- `s` o `S` → finalizar el skill, el usuario puede continuar con `create-feature-artifacts`
- `n` o `N` → preguntar:
¿Qué ajustes quieres hacer? (ej: agregar/quitar feature, cambiar nombre, etc.)

- Aplicar los ajustes y regenerar `plan-exercise.md`
- Volver a preguntar (paso 4.2)
- Otro → repetir la pregunta

---

## Comportamiento ante Estado Previo

| Caso | Comportamiento |
|------|----------------|
| `plan-exercise.md` ya existe | Preguntar: "Ya existe un plan. ¿Deseas sobrescribirlo? (s/n)" |
| `project.md` ausente | Detenerse con error |
| `plantilla.md` ausente | Detenerse con error |
| `AGENTS.md` ausente | Continuar sin él (tono neutral) |
| No hay imágenes en la raíz | Continuar sin preguntar por imágenes |

---

## Ejemplo de Uso


# Usuario ejecuta
/analyze-exercise

# El agente:
# 1. Lee AGENTS.md → "Eres un experto desarrollador de software..."
# 2. Lee project.md → "Área de Rectángulos II..."
# 3. Busca imágenes → Encuentra rectangulos.png, pregunta si describirla
# 4. Lee assets/plantilla.md → obtiene formato
# 5. Genera plan-exercise.md en la raíz
# 6. Muestra resumen y pregunta: "¿Apruebas este plan? (s/n)"


**Notas para el Agente**
   a. No crear carpetas ni archivos de código en este skill — solo genera plan-exercise.md

   b. No redactar artefactos — eso es responsabilidad de write-artifacts-content

   c. Ser conservador — ante cualquier duda, preguntar al usuario

   d. Usar el tono de AGENTS.md si existe

   e. La aprobación del usuario es obligatoria antes de finalizar

