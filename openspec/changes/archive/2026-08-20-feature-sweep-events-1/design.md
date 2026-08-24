# Design — feature-sweep-events-1

## 1. Arquitectura general

La feature se compone de un módulo `sweep_events.py` con dos funciones principales:
- `extract_events`: Transforma la lista de rectángulos en una lista de eventos de barrido.
- `sort_events`: Ordena los eventos por coordenada X para permitir el procesamiento secuencial.

Cada evento es una tupla `(x, y1, y2, type)` donde:
- `x`: coordenada X del evento
- `y1`, `y2`: rango Y del rectángulo (y1 < y2)
- `type`: +1 para inicio de rectángulo, -1 para fin

## 2. Decisiones clave

- **Tupla en lugar de dataclass:** Se usa tupla por simplicidad y rendimiento, ya que los eventos son estructuras inmutables y solo se necesitan para procesamiento secundario.
- **Ordenamiento estable:** En caso de empate en X, los inicios van antes que los fines para procesar correctamente las superposiciones al borde.
- **Type hints explícitos:** Se usan tipos `int` para coordenadas y `List` para colecciones, siguiendo convenciones del proyecto.

## 3. Interfaz pública

```python
from typing import List, Tuple

def extract_events(rectangles: List[List[int]]) -> List[Tuple[int, int, int, int]]:
    """Extrae eventos de inicio y fin de cada rectángulo."""
    pass

def sort_events(events: List[Tuple[int, int, int, int]]) -> List[Tuple[int, int, int, int]]:
    """Ordena eventos por coordenada X ascendente."""
    pass
```

## 4. Dependencias

Ninguna. Es una feature raíz del proyecto.

## 5. Alternativas descartadas

- **Dataclass para eventos:** Descartada por sobrehead de creación y menor rendimiento en procesamiento masivo.
- **Lista de diccionarios:** Descartada por mayor consumo de memoria y menor claridad en el acceso a campos.