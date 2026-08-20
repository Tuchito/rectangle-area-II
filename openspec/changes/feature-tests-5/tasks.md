# Tasks — feature-tests-5

- [ ] **Tarea 1: Configurar estructura de pruebas**
  Crear directorio `tests/` y archivo `test_area_rectangle_ii.py` con imports básicos.
  Criterio de "hecho": Archivo creado con import de pytest y función de ejemplo.
  Depende de: nada.

- [ ] **Tarea 2: Implementar prueba del ejemplo 1**
  Escribir test que valide el ejemplo 1 del enunciado (salida 6).
  Criterio de "hecho": Test pasa con la implementación actual.
  Depende de: Tarea 1, feature-area-calculation-4.

- [ ] **Tarea 3: Implementar prueba del ejemplo 2**
  Escribir test que valide el ejemplo 2 del enunciado (salida 49).
  Criterio de "hecho": Test pasa con la implementación actual.
  Depende de: Tarea 2.

- [ ] **Tarea 4: Implementar casos borde**
  Escribir tests para casos simples: un solo rectángulo, sin superposición, idénticos.
  Criterio de "hecho": Tests pasan y cubren casos extremos.
  Depende de: Tarea 3.

- [ ] **Tarea 5: Ejecutar suite completa**
  Ejecutar `pytest tests/` y verificar que todos los tests pasan.
  Criterio de "hecho": Todos los tests pasan sin errores.
  Depende de: Tarea 4.