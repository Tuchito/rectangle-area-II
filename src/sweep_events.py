"""Módulo para extraer y ordenar eventos de barrido de rectángulos.

Este módulo proporciona funciones para convertir una lista de rectángulos
en una lista de eventos de barrido, donde cada evento representa el inicio
o fin de un rectángulo en el eje X.

Ejemplo de uso:
    >>> rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    >>> events = get_sorted_events(rectangles)
    >>> print(events)
    [(0, 0, 2, 1), (1, 0, 3, 1), (1, 0, 1, 1), (2, 0, 2, -1), (2, 0, 3, -1), (3, 0, 1, -1)]
"""

from typing import List, Tuple

# Tipo alias para representar eventos de barrido
# Cada evento es una tupla (x, y1, y2, type)
# donde type = 1 para inicio de rectángulo, -1 para fin
Event = Tuple[int, int, int, int]


def extract_events(rectangles: List[List[int]]) -> List[Event]:
    """Extrae eventos de inicio y fin de cada rectángulo."""
    events: List[Event] = []
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        # Evento de inicio
        events.append((x1, y1, y2, 1))
        # Evento de fin
        events.append((x2, y1, y2, -1))
    return events


def sort_events(events: List[Event]) -> List[Event]:
    """Ordena eventos por coordenada X ascendente."""
    # Ordenar por x ascendente, y en caso de empate, inicios (type=1) antes que fines (type=-1)
    return sorted(events, key=lambda e: (e[0], -e[3]))


def get_sorted_events(rectangles: List[List[int]]) -> List[Event]:
    """Extrae y ordena eventos de barrido desde una lista de rectángulos."""
    events = extract_events(rectangles)
    return sort_events(events)


if __name__ == "__main__":
    # Ejemplo de uso
    rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
    events = get_sorted_events(rectangles)
    print("Eventos ordenados:")
    for event in events:
        print(f"  x={event[0]}, y=[{event[1]}, {event[2]}], type={'inicio' if event[3] == 1 else 'fin'}")