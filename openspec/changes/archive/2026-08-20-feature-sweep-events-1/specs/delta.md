# Delta — feature-sweep-events-1

## Estado anterior

No existe versión previa. Esta feature es el punto de partida del sistema de barrido.

## Cambios introducidos por esta feature

- **Nuevo:** Módulo `sweep_events.py` con funciones para extraer y ordenar eventos.
- **Nuevo:** Estructura de datos `Event` como tupla `(x, y1, y2, type)`.
- **Nuevo:** Función `extract_events(rectangles)` que genera eventos de inicio y fin.
- **Nuevo:** Función `sort_events(events)` que ordena por coordenada X.

## Impacto en consumidores

- **feature-coordinate-compression-2** necesitará los eventos para obtener coordenadas Y únicas.
- **feature-segment-tree-3** usará los eventos procesados para actualizar el árbol.
- **Breaking changes:** Ninguno (es la primera feature).