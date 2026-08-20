# Plantilla para delta.md

> **Ubicación:** `openspec/changes/feature-<nombre>-<numero>/specs/delta.md`
> **Propósito:** Documentar los cambios específicos en las especificaciones del sistema que introduce esta feature.

---

## Estado anterior

[Descripción del estado previo del sistema antes de esta feature.]

**Contexto esperado:**
- Si es la primera feature: "No existe versión previa. Es la base del sistema."
- Si depende de otra feature: "Depende de la feature-<nombre>-<numero>."

---

## Cambios introducidos por esta feature

[Lista de cambios concretos en las especificaciones.]

**Formato sugerido:**
- **Nuevo:** [elemento añadido y su propósito]
- **Modificado:** [elemento existente que cambia y por qué]
- **Eliminado:** [elemento que se remueve, si aplica]

---

## Impacto en consumidores

[Qué otras features o componentes se ven afectados.]

- **Features que dependen de esta:** [listar o decir "Ninguna"]
- **Breaking changes:** [si hay cambios que requieran ajustes en otras features]

---

## Ejemplo (para feature-sweep-events-1)

```markdown
## Estado anterior

No existe versión previa. Esta feature es el punto de partida del sistema de barrido.

## Cambios introducidos por esta feature

- **Nuevo:** Módulo `sweep_events.py` con funciones para extraer y ordenar eventos.
- **Nuevo:** Estructura de datos `Event` como tupla `(x, y1, y2, tipo)`.
- **Nuevo:** Función `extract_events(rectangles)` que genera eventos de inicio y fin.
- **Nuevo:** Función `sort_events(events)` que ordena por coordenada X.

## Impacto en consumidores

- **feature-coordinate-compression-2** necesitará los eventos para obtener coordenadas Y.
- **feature-segment-tree-3** usará los eventos procesados para actualizar el árbol.
- **Breaking changes:** Ninguno (es la primera feature).