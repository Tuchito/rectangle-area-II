# Proposal — feature-tests-5

## Why

Una vez que la solución está implementada, se necesita validar que funciona correctamente con los ejemplos del enunciado y casos borde. Las pruebas unitarias aseguran que la implementación cumple con las especificaciones y permite detectar regresiones.

Esta feature es la validación final de toda la implementación. Según `plan-exercise.md`, depende de todas las features anteriores porque necesita la función `calculate_total_area` para probar.

## What Changes

- Nuevo módulo: `tests/test_area_rectangle_ii.py`
- Pruebas para:
  - Ejemplo 1 del enunciado (rectángulos superpuestos, salida 6).
  - Ejemplo 2 del enunciado (un rectángulo grande, salida 49).
  - Casos borde: un solo rectángulo, rectángulos sin superposición, rectángulos idénticos.
- Dependencia de feature-area-calculation-4 para la función principal.