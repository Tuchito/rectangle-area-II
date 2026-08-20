# Delta — feature-coordinate-compression-2

## Estado anterior

Depende de feature-sweep-events-1. Solo existía el módulo de eventos.

## Cambios introducidos por esta feature

- **Nuevo:** Módulo `coordinate_compression.py` con funciones de compresión.
- **Nuevo:** Función `compress_coordinates(events)` que extrae coordenadas Y únicas.
- **Nuevo:** Función `get_compressed_range(y1, y2, coord_map)` que mapea rangos.
- **Nuevo:** Diccionario de mapeo de coordenadas a índices.

## Impacto en consumidores

- **feature-segment-tree-3** usará la compresión para definir tamaño del árbol y mapear rangos.
- **feature-area-calculation-4** usará los rangos comprimidos para cálculos.
- **Breaking changes:** Ninguno (feature adicional).