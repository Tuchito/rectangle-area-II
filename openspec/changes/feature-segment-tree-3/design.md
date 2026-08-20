# Design — feature-segment-tree-3

## 1. Arquitectura general

El Segment Tree se implementa sobre el eje Y comprimido. Cada nodo almacena:
- `cover`: número de rectángulos que cubren completamente ese nodo.
- `length`: longitud total cubierta en el rango del nodo.

La actualización de rango (`range_add`) incrementa/decrementa `cover` y recalcula `length`:
- Si `cover > 0` → `length = rango_del_nodo`
- Si `cover == 0` y es hoja → `length = 0`
- Si `cover == 0` y tiene hijos → `length = length_hijo_izq + length_hijo_der`

## 2. Decisiones clave

- **Uso de Segment Tree con lazy (en lugar de árbol de Fenwick):** Se eligió Segment Tree porque permite actualizaciones de rango y consulta de longitud cubierta en O(log N). El árbol de Fenwick no maneja fácilmente la consulta de "longitud cubierta" con actualizaciones de rango sin información adicional.

- **Compresión de coordenadas en lugar de nodos dinámicos:** Se usa compresión porque el número de rectángulos es pequeño (≤ 200), pero las coordenadas pueden llegar a 10^9. Esto reduce la memoria a O(N) y simplifica la implementación.

- **Estructura de nodos con cover + length en lugar de tree + lazy separados:** Se unifican cover y length en cada nodo para simplificar la actualización y consulta.

## 3. Interfaz pública

```python
from typing import List

class SegmentTree:
    def __init__(self, coords: List[int]) -> None:
        """Inicializa el árbol con coordenadas Y comprimidas."""
        pass

    def range_add(self, y1: int, y2: int, val: int) -> None:
        """Actualiza el rango [y1, y2) con +1 o -1."""
        pass

    def total_length(self) -> int:
        """Devuelve la longitud total cubierta en el eje Y."""
        pass
```

## 4. Dependencias

- `feature-coordinate-compression-2`: Proporciona el mapeo de coordenadas Y a índices comprimidos.
- El árbol se construye sobre los índices comprimidos.

## 5. Alternativas descartadas

- **Barrido con árbol de Fenwick:** Descartado porque no maneja eficientemente la consulta de longitud cubierta con actualizaciones de rango.
- **Segment Tree sin compresión:** Descartado porque requeriría un árbol de tamaño 10^9, inviable en memoria.