# Proposal — feature-coordinate-compression-2

## Why

Las coordenadas Y de los rectángulos pueden llegar hasta 10^9, pero solo hay hasta 200 rectángulos (400 coordenadas únicas). Para implementar un Segment Tree eficiente, es necesario comprimir estas coordenadas a índices consecutivos (0..M-1), reduciendo el rango de trabajo de 10^9 a O(N).

Esta feature es prerequisito para el Segment Tree, ya que permite definir el tamaño del árbol y mapear rangos Y originales a rangos comprimidos. Según `plan-exercise.md`, depende de feature-sweep-events-1 porque necesita los eventos para extraer todas las coordenadas Y únicas.

## What Changes

- Nuevo módulo: `coordinate_compression.py`
- Función: `compress_coordinates(events: List[Tuple[int, int, int, int]]) -> Tuple[List[int], Dict[int, int]]`
  - Recibe eventos del barrido, devuelve lista de coordenadas Y únicas ordenadas y diccionario de mapeo.
- Función: `get_compressed_range(y1: int, y2: int, coord_map: Dict[int, int]) -> Tuple[int, int]`
  - Convierte un rango Y original a índices comprimidos.
- Depende de feature-sweep-events-1 para obtener eventos.