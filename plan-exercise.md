# Plan de Análisis — Área de Rectángulos II

## 1. Resumen del problema
Calcular el área total cubierta por un conjunto de rectángulos alineados con los ejes, contando las superposiciones solo una vez. El resultado debe devolver módulo 10^9 + 7.

## 2. Restricciones clave
- Hasta 200 rectángulos (n ≤ 200)
- Coordenadas hasta 10^9 (requiere compresión de coordenadas)
- Rectángulos con área no nula
- Respuesta módulo 10^9 + 7

## 3. Enfoque sugerido
- **Estructura de datos**: Segment Tree con lazy propagation para el eje Y
- **Algoritmo**: Barrido (sweep line) en el eje X, procesando eventos de inicio/fin de rectángulos
- **Complejidad**: O(n log n) donde n es el número de rectángulos (después de compresión de coordenadas)

## 4. Features propuestas (5)
1. **feature-sweep-events**: Extraer y ordenar eventos x del barrido (inicios y finales de rectángulos)
2. **feature-coordinate-compression**: Compresión de coordenadas Y para manejar rangos grandes eficientemente
3. **feature-segment-tree**: Segment Tree con lazy propagation para mantener la longitud total cubierta en el eje Y
4. **feature-area-calculation**: Cálculo del área total acumulando áreas entre eventos x
5. **feature-tests**: Pruebas unitarias con ejemplos del enunciado y casos borde

## 5. Justificación del corte
Cada feature es atómica: se puede completar en una sesión de trabajo, tiene un criterio de "hecho" claro (sin ambigüedad), y no depende de decisiones de diseño aún no tomadas. La separación sigue un flujo lógico de implementación:
- Primero se extraen los eventos del barrido (feature-sweep-events)
- Luego se comprimen las coordenadas Y (feature-coordinate-compression)
- Después se implementa la estructura de datos clave (feature-segment-tree)
- Finalmente se integra todo para calcular el área (feature-area-calculation)
- Las pruebas validan la implementación completa (feature-tests)

## 6. Dependencias entre features
```
feature-sweep-events → feature-coordinate-compression → feature-segment-tree → feature-area-calculation → feature-tests
```
- **Feature raíz**: feature-sweep-events (sin dependencias)
- **Feature hoja**: feature-tests (depende de todas las anteriores)