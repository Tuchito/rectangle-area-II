# Plantilla para tasks.md

> **Ubicación:** `openspec/changes/feature-<nombre>-<numero>/tasks.md`
> **Propósito:** Desglosar la feature en tareas atómicas, con criterios de "hecho" y dependencias.

---

## Tasks — [nombre de la feature]

- [ ] **Tarea 1: [Nombre de la tarea]**
  [Descripción breve de lo que hay que hacer]
  Criterio de "hecho": [condición clara y verificable]
  Depende de: [tareas anteriores, o "nada"]

- [ ] **Tarea 2: [Nombre de la tarea]**
  [Descripción breve de lo que hay que hacer]
  Criterio de "hecho": [condición clara y verificable]
  Depende de: [tareas anteriores, o "nada"]

- [ ] **Tarea N: [Nombre de la tarea]**
  [Descripción breve de lo que hay que hacer]
  Criterio de "hecho": [condición clara y verificable]
  Depende de: [tareas anteriores, o "nada"]

---

## Criterios de redacción

- **Cantidad:** 3-7 tareas por feature
- **Atomicidad:** Cada tarea debe completarse en una sesión de trabajo
- **Criterio de "hecho":** Sin ambigüedad, verificable (ej: "pasa todas las pruebas", "interfaz definida")
- **Dependencias:** Explicitar qué tareas deben completarse primero

---

## Ejemplo (para feature-sweep-events-1)

```markdown
# Tasks — feature-sweep-events

- [ ] **Tarea 1: Definir la estructura del evento**
  Crear una tupla o dataclass para representar eventos: (x, y1, y2, tipo)
  Criterio de "hecho": La estructura está definida con type hints.
  Depende de: nada.

- [ ] **Tarea 2: Implementar extracción de eventos**
  Recorrer la lista de rectángulos y generar eventos de inicio (+1) y fin (-1).
  Criterio de "hecho": La función devuelve una lista de eventos con los datos correctos.
  Depende de: Tarea 1.

- [ ] **Tarea 3: Implementar ordenamiento de eventos**
  Ordenar eventos por coordenada X. En caso de empate, los inicios van antes que los fines (opcional).
  Criterio de "hecho": La función devuelve eventos ordenados según el criterio.
  Depende de: Tarea 2.