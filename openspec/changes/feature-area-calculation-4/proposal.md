# Proposal — feature-area-calculation-4

## Why

Una vez que se tienen los eventos del barrido, las coordenadas comprimidas y el Segment Tree para mantener la altura activa, se necesita integrar todo para calcular el área total. El cálculo consiste en recorrer los eventos ordenados por X, actualizar el Segment Tree con cada evento, y acumular el área entre eventos consecutivos usando la altura cubierta.

Esta feature integra todas las anteriores en el algoritmo completo. Según `plan-exercise.md`, depende de feature-segment-tree-3 porque necesita el Segment Tree para mantener la altura activa.

## What Changes

- Nuevo módulo: `area_calculation.py`
- Función: `calculate_total_area(rectangles: List[List[int]]) -> int`
  - Implementa el algoritmo completo: extrae eventos, comprime coordenadas, usa Segment Tree, calcula área.
- Función: `area_between_events(events: List, tree: SegmentTree, index: int) -> int`
  - Calcula el área entre el evento actual y el siguiente usando la altura del Segment Tree.
- Depende de feature-segment-tree-3, feature-coordinate-compression-2, y feature-sweep-events-1.