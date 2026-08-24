"""Módulo para comprimir coordenadas Y de eventos de barrido.

Este módulo proporciona funciones para extraer coordenadas Y únicas de eventos
de barrido y comprimirlas a índices consecutivos, facilitando el uso de
estructuras de datos como Segment Trees.

Ejemplo de uso:
    >>> from sweep_events import get_sorted_events
    >>> rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    >>> events = get_sorted_events(rectangles)
    >>> sorted_y, coord_map = compress_coordinates(events)
    >>> print(sorted_y)
    [0, 1, 2, 3]
    >>> print(coord_map)
    {0: 0, 1: 1, 2: 2, 3: 3}
"""

from typing import List, Tuple, Dict
import bisect


def compress_coordinates(events: List[Tuple[int, int, int, int]]) -> Tuple[List[int], Dict[int, int]]:
    """Extrae coordenadas Y únicas de eventos y devuelve lista ordenada y diccionario de mapeo."""
    y_coords = set()
    for event in events:
        x, y1, y2, _ = event
        y_coords.add(y1)
        y_coords.add(y2)
    sorted_y = sorted(y_coords)
    coord_map = {y: idx for idx, y in enumerate(sorted_y)}
    return sorted_y, coord_map


def get_compressed_range(y1: int, y2: int, coord_map: Dict[int, int]) -> Tuple[int, int]:
    """Convierte rango Y original a índices comprimidos usando búsqueda binaria."""
    # Usar bisect para encontrar índices comprimidos
    idx1 = coord_map[y1]
    idx2 = coord_map[y2]
    return idx1, idx2


if __name__ == "__main__":
    # Ejemplo de uso
    from sweep_events import get_sorted_events
    
    rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
    events = get_sorted_events(rectangles)
    sorted_y, coord_map = compress_coordinates(events)
    
    print("Coordenadas Y únicas ordenadas:", sorted_y)
    print("Diccionario de mapeo:", coord_map)
    
    # Ejemplo de mapeo de rango
    y1, y2 = 1, 3
    comp_y1, comp_y2 = get_compressed_range(y1, y2, coord_map)
    print(f"Rango original ({y1}, {y2}) -> comprimido ({comp_y1}, {comp_y2})")