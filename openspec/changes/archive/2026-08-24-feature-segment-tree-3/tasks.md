# Tasks — feature-segment-tree-3

- [x] **Tarea 1: Definir estructura del nodo del árbol**
  Crear clase o diccionario para nodos con cover, length, y campos para lazy.
  Criterio de "hecho": Estructura definida con type hints claros.
  Depende de: nada.

- [x] **Tarea 2: Implementar construcción del árbol**
  Crear árbol recursivo a partir de lista de coordenadas comprimidas.
  Criterio de "hecho": Árbol construido con nodos hoja que representan segmentos.
  Depende de: Tarea 1.

- [x] **Tarea 3: Implementar actualización de rango con lazy**
  Implementar `range_add` con lazy propagation para actualizar cobertura.
  Criterio de "hecho": Actualiza correctamente cobertura en el ejemplo 1.
  Depende de: Tarea 2.

- [x] **Tarea 4: Implementar consulta de longitud cubierta**
  Implementar `total_length` que devuelva la longitud total cubierta.
  Criterio de "hecho": Devuelve longitud correcta después de actualizaciones.
  Depende de: Tarea 3.

- [x] **Tarea 5: Integrar con compresión de coordenadas**
  Usar funciones de feature-coordinate-compression-2 para inicializar árbol.
  Criterio de "hecho": Árbol se inicializa correctamente con coordenadas comprimidas.
  Depende de: Tarea 4, feature-coordinate-compression-2.

- [x] **Tarea 6: Documentar uso público**
  Agregar docstrings y ejemplo de uso en el módulo.
  Criterio de "hecho": Módulo tiene documentación clara y ejemplo ejecutable.
  Depende de: Tarea 5.