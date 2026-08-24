# Tasks — feature-area-calculation-4

- [x] **Tarea 1: Integrar extracción de eventos y compresión**
  Crear función que reciba rectángulos y devuelva eventos ordenados y coordenadas comprimidas.
  Criterio de "hecho": Para rectángulos de ejemplo 1, devuelve eventos y compresión correctos.
  Depende de: feature-sweep-events-1, feature-coordinate-compression-2.

- [x] **Tarea 2: Inicializar Segment Tree con compresión**
  Usar coordenadas comprimidas para crear instancia de SegmentTree.
  Criterio de "hecho": Árbol se inicializa con tamaño correcto (4 nodos para ejemplo 1).
  Depende de: Tarea 1, feature-segment-tree-3.

- [x] **Tarea 3: Implementar cálculo de área entre eventos**
  Implementar función que calcule `(x_next - x_current) * tree.total_length()`.
  Criterio de "hecho": Calcula correctamente el área para el ejemplo 1.
  Depende de: Tarea 2.

- [x] **Tarea 4: Implementar algoritmo completo de barrido**
  Recorrer eventos, acumular áreas, actualizar árbol, y devolver resultado módulo.
  Criterio de "hecho": Devuelve 6 para ejemplo 1 y 49 para ejemplo 2.
  Depende de: Tarea 3.

- [x] **Tarea 5: Documentar uso público**
  Agregar docstrings y ejemplo de uso en el módulo.
  Criterio de "hecho": Módulo tiene documentación clara y ejemplo ejecutable.
  Depende de: Tarea 4.