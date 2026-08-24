# Design — feature-area-calculation-4

## 1. Arquitectura general

El módulo `area_calculation.py` integra los componentes anteriores en el algoritmo de barrido completo:

1. Extraer eventos del barrido (feature-sweep-events-1).
2. Comprimir coordenadas Y (feature-coordinate-compression-2).
3. Inicializar Segment Tree con coordenadas comprimidas (feature-segment-tree-3).
4. Recorrer eventos ordenados por X:
   - Para cada evento, calcular el área desde el evento anterior hasta el actual: `(x_actual - x_anterior) * tree.total_length()`.
   - Actualizar el Segment Tree con el evento actual (range_add).
5. Acumular el área total y devolver módulo 10^9 + 7.

## 2. Decisiones clave

- **Área módulo 10^9 + 7:** Se aplica módulo en cada paso para evitar overflow, ya que el área puede ser 10^18.
- **Procesamiento secuencial de eventos:** Se procesan en orden de X para calcular anchos correctamente.
- **Integración en una función principal:** Se encapsula todo en `calculate_total_area` para simplicidad de uso.

## 3. Interfaz pública

```python
from typing import List

def calculate_total_area(rectangles: List[List[int]]) -> int:
    """Calcula el área total cubierta por rectángulos módulo 10^9 + 7."""
    pass

def area_between_events(events: List, tree: SegmentTree, index: int) -> int:
    """Calcula el área entre evento actual y siguiente usando altura del Segment Tree."""
    pass
```

## 4. Dependencias

- `feature-sweep-events-1`: Para extraer eventos del barrido.
- `feature-coordinate-compression-2`: Para comprimir coordenadas Y.
- `feature-segment-tree-3`: Para mantener la altura activa durante el barrido.

## 5. Alternativas descartadas

- **Cálculo sin Segment Tree:** Descartado porque requeriría recomputar altura en cada paso, O(N^2) en lugar de O(N log N).
- **Función separada por cada paso:** Descartada por complejidad innecesaria; una función integrada es más clara para este caso.