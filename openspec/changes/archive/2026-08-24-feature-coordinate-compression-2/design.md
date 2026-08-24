# Design — feature-coordinate-compression-2

## 1. Arquitectura general

La feature se compone de un módulo `coordinate_compression.py` con dos funciones principales:
- `compress_coordinates`: Extrae coordenadas Y únicas de los eventos y las ordena.
- `get_compressed_range`: Mapea rangos Y originales a índices comprimidos.

El proceso de compresión:
1. Extraer todas las coordenadas Y (y1, y2) de los eventos.
2. Obtener valores únicos y ordenarlos.
3. Crear diccionario mapeando cada coordenada a su índice.
4. Usar búsqueda binaria para mapear rangos.

## 2. Decisiones clave

- **Diccionario para mapeo:** Se usa dict por simplicidad y O(1) promedio en acceso.
- **Búsqueda binaria para rangos:** Permite mapear cualquier rango Y original a índices comprimidos en O(log N).
- **Coordinadas como enteros:** Se mantienen como int para compatibilidad con el Segment Tree.

## 3. Interfaz pública

```python
from typing import List, Tuple, Dict

def compress_coordinates(events: List[Tuple[int, int, int, int]]) -> Tuple[List[int], Dict[int, int]]:
    """Extrae coordenadas Y únicas de eventos y devuelve lista ordenada y diccionario de mapeo."""
    pass

def get_compressed_range(y1: int, y2: int, coord_map: Dict[int, int]) -> Tuple[int, int]:
    """Convierte rango Y original a índices comprimidos usando búsqueda binaria."""
    pass
```

## 4. Dependencias

- `feature-sweep-events-1`: Proporciona los eventos de los cuales se extraen coordenadas Y.

## 5. Alternativas descartadas

- **Compresión inline en Segment Tree:** Descartada porque acopla dos responsabilidades y dificulta pruebas unitarias.
- **Usar bisect de Python:** Se consideró pero se implementa búsqueda binaria manual para mayor control y claridad.