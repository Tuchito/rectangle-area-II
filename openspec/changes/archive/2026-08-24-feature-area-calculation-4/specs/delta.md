# Delta — feature-area-calculation-4

## Estado anterior

Depende de feature-segment-tree-3. Solo existían módulos de eventos, compresión y Segment Tree.

## Cambios introducidos por esta feature

- **Nuevo:** Módulo `area_calculation.py` con función principal `calculate_total_area`.
- **Nuevo:** Función `calculate_total_area(rectangles)` que implementa el algoritmo completo.
- **Nuevo:** Función `area_between_events(events, tree, index)` para cálculo parcial.
- **Nuevo:** Integración de todos los componentes en flujo de barrido.

## Impacto en consumidores

- **feature-tests-5** usará `calculate_total_area` para validar la solución completa.
- **Punto de entrada principal:** Esta función será la interfaz pública del problema.
- **Breaking changes:** Ninguno (feature de integración).