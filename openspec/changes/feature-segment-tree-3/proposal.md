# Proposal — feature-segment-tree-3

## Why

Para calcular la altura total cubierta en el eje Y durante el barrido, se necesita una estructura de datos que soporte actualizaciones de rango (sumar/restar cobertura) y consultas de longitud cubierta. El Segment Tree con lazy propagation permite ambas operaciones en O(log N), donde N es el número de coordenadas Y comprimidas.

Esta feature es el núcleo del algoritmo: sin ella, no es posible mantener la altura activa eficientemente. Según `plan-exercise.md`, depende de feature-coordinate-compression-2 porque necesita las coordenadas Y comprimidas para definir el tamaño del árbol.

## What Changes

- Nuevo módulo: `segment_tree.py`
- Clase: `SegmentTree` con lazy propagation
  - Constructor: `__init__(self, coords: List[int])` inicializa árbol sobre coordenadas comprimidas.
  - Método: `range_add(self, y1: int, y2: int, val: int)` actualiza cobertura en rango.
  - Método: `total_length(self) -> int` devuelve longitud total cubierta.
- Depende de feature-coordinate-compression-2 para rangos comprimidos.