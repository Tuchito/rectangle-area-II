# Tasks — feature-sweep-events-1

- [ ] **Tarea 1: Definir la estructura del evento**
  Crear una tupla o type alias para representar eventos: (x, y1, y2, type)
  Criterio de "hecho": La estructura está definida con type hints claros.
  Depende de: nada.

- [ ] **Tarea 2: Implementar extracción de eventos**
  Recorrer la lista de rectángulos y generar eventos de inicio (+1) y fin (-1).
  Criterio de "hecho": La función `extract_events` devuelve una lista de eventos con los datos correctos para el ejemplo 1.
  Depende de: Tarea 1.

- [ ] **Tarea 3: Implementar ordenamiento de eventos**
  Ordenar eventos por coordenada X. En caso de empate, los inicios van antes que los fines.
  Criterio de "hecho": La función `sort_events` devuelve eventos ordenados según el criterio.
  Depende de: Tarea 2.

- [ ] **Tarea 4: Integrar extracción y ordenamiento**
  Combinar las funciones en un flujo completo que reciba rectángulos y devuelva eventos ordenados.
  Criterio de "hecho": La función integrada produce eventos ordenados para el ejemplo 1.
  Depende de: Tarea 3.

- [ ] **Tarea 5: Documentar uso público**
  Agregar docstrings y ejemplo de uso en el módulo.
  Criterio de "hecho": El módulo tiene documentación clara y ejemplo ejecutable.
  Depende de: Tarea 4.