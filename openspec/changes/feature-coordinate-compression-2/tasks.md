# Tasks — feature-coordinate-compression-2

- [x] **Tarea 1: Extraer coordenadas Y únicas de eventos**
  Implementar función que recorra eventos y extraiga valores Y únicos.
  Criterio de "hecho": Para eventos de ejemplo 1, devuelve [0,1,2,3] ordenados.
  Depende de: feature-sweep-events-1 (necesita eventos).

- [x] **Tarea 2: Crear diccionario de mapeo**
  Implementar función que asigne a cada coordenada Y un índice comprimido.
  Criterio de "hecho": Diccionario mapea {0:0, 1:1, 2:2, 3:3} para ejemplo 1.
  Depende de: Tarea 1.

- [x] **Tarea 3: Implementar mapeo de rangos**
  Implementar función que convierta rango Y original a índices comprimidos.
  Criterio de "hecho": Para rango (1,3) devuelve (1,2) en ejemplo comprimido.
  Depende de: Tarea 2.

- [x] **Tarea 4: Integrar compresión completa**
  Combinar funciones en flujo que reciba eventos y devuelva lista comprimida y diccionario.
  Criterio de "hecho": Función integrada procesa eventos de ejemplo 1 correctamente.
  Depende de: Tarea 3.

- [x] **Tarea 5: Documentar uso público**
  Agregar docstrings y ejemplo de uso en el módulo.
  Criterio de "hecho": Módulo tiene documentación clara y ejemplo ejecutable.
  Depende de: Tarea 4.