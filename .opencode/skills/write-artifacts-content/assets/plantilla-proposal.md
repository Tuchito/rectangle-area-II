# Plantilla para proposal.md

> **Ubicación:** `openspec/changes/feature-<nombre>-<numero>/proposal.md`
> **Propósito:** Definir el "qué" y el "por qué" de la feature.

---

## Why (Ejemplo)

[Explicar por qué esta feature es necesaria, basado en:]
- El enunciado del problema (`project.md`)
- La justificación del corte (`plan-exercise.md`)
- Contexto de features dependientes (si las hay)

**Criterios de redacción:**
- **Extensión:** 2-4 párrafos por sección (no más de 1 página total)
- **Claridad:** Explicaciones directas, sin ambigüedad
- **Conexión:** Vincular explícitamente con `project.md` y el problema general
- **Dependencias:** Mencionar si la feature depende de otras

**Ejemplo (para feature-sweep-events-1 en "Área de Rectángulos II"):**

```markdown
## Why

Para calcular el área de unión de rectángulos alineados a los ejes, es necesario procesar los rectángulos en el orden de sus coordenadas X. El algoritmo de barrido (sweep line) requiere extraer y ordenar los eventos de inicio y fin de cada rectángulo, ya que el área se calcula como la suma de anchos (diferencias en X) multiplicados por la altura total cubierta en cada franja.

Esta feature es el punto de partida del barrido: sin los eventos correctamente extraídos y ordenados, no es posible procesar los rectángulos de manera eficiente. Depende de `plan-exercise.md`, que establece que el barrido es el enfoque principal del problema.

## What Changes (Ejemplo)

- Nuevo módulo: `sweep_events.py`
- Función: `extract_events(rectangles: List[Tuple[int, int, int, int]]) -> List[Tuple[int, int, int, int, int]]`
  - Cada evento: `(x, y1, y2, type)` donde `type = +1` para inicio, `-1` para fin
- Función: `sort_events(events: List) -> List` (ordenar por X ascendente)
- No depende de otras features — es la feature raíz del proyecto.

### What Changes
[Lista de cambios concretos que introduce esta feature:]

    - Nuevos módulos/clases/funciones

    - Cambios en la interfaz pública

    - Dependencias que se añaden

### Formato sugerido:

    - Usar viñetas (-) para cada cambio

    - Indicar si es un nuevo módulo, clase, función o modificación

    - Mencionar dependencias explícitas