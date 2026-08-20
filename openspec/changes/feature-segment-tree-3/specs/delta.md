# Delta — feature-segment-tree-3

## Estado anterior

Depende de feature-coordinate-compression-2. Solo existían módulos de eventos y compresión.

## Cambios introducidos por esta feature

- **Nuevo:** Módulo `segment_tree.py` con clase `SegmentTree`.
- **Nuevo:** Clase `SegmentTree` con lazy propagation para actualizaciones de rango.
- **Nuevo:** Método `range_add(y1, y2, val)` para actualizar cobertura.
- **Nuevo:** Método `total_length()` para consultar longitud cubierta.

## Impacto en consumidores

- **feature-area-calculation-4** usará el Segment Tree para mantener altura activa durante el barrido.
- **feature-tests-5** probará el Segment Tree con casos del enunciado.
- **Breaking changes:** Ninguno (feature adicional).