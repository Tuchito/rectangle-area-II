# Design — feature-tests-5

## 1. Arquitectura general

El módulo de pruebas se estructura en función de los casos de prueba del enunciado y casos borde adicionales. Cada prueba:
1. Prepara la entrada (lista de rectángulos).
2. Llama a `calculate_total_area`.
3. Compara con la salida esperada.

Se usa pytest como framework de pruebas (según convenciones del proyecto).

## 2. Decisiones clave

- **Pytest como framework:** Se usa pytest por ser el estándar del proyecto y soportar assertions claras.
- **Pruebas basadas en ejemplos del enunciado:** Prioriza los casos oficiales del problema.
- **Casos borde adicionales:** Incluye casos simples para validar comportamientos extremos.

## 3. Interfaz pública

```python
# tests/test_area_rectangle_ii.py
import pytest
from src.area_calculation import calculate_total_area

def test_example_1():
    rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    assert calculate_total_area(rectangles) == 6

def test_example_2():
    rectangles = [[0,0,1000000000,1000000000]]
    assert calculate_total_area(rectangles) == 49

def test_single_rectangle():
    rectangles = [[0,0,5,5]]
    assert calculate_total_area(rectangles) == 25

def test_no_overlap():
    rectangles = [[0,0,2,2],[3,3,5,5]]
    assert calculate_total_area(rectangles) == 8
```

## 4. Dependencias

- `feature-area-calculation-4`: Proporciona la función `calculate_total_area`.
- Framework: pytest (instalado en entorno virtual).

## 5. Alternativas descartadas

- **Unittest:** Descartado porque pytest es más conciso y el proyecto ya lo usa.
- **Pruebas de integración separadas:** Se decidió mantener todo en un módulo por simplicidad.