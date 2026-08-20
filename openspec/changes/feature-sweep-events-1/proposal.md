# Proposal — feature-sweep-events-1

## Why

Para calcular el área de unión de rectángulos alineados a los ejes, es necesario procesar los rectángulos en el orden de sus coordenadas X. El algoritmo de barrido (sweep line) requiere extraer y ordenar los eventos de inicio y fin de cada rectángulo, ya que el área se calcula como la suma de anchos (diferencias en X) multiplicados por la altura total cubierta en cada franja.

Esta feature es el punto de partida del barrido: sin los eventos correctamente extraídos y ordenados, no es posible procesar los rectángulos de manera eficiente. Según `plan-exercise.md`, el barrido es el enfoque principal del problema y esta feature es la raíz del grafo de dependencias.

## What Changes

- Nuevo módulo: `sweep_events.py`
- Función: `extract_events(rectangles: List[List[int]]) -> List[Tuple[int, int, int, int]]`
  - Cada evento: `(x, y1, y2, type)` donde `type = 1` para inicio, `-1` para fin
- Función: `sort_events(events: List[Tuple]) -> List[Tuple]` (ordenar por X ascendente, inicios antes que fines en caso de empate)
- No depende de otras features — es la feature raíz del proyecto.