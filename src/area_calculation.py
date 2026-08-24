"""Módulo para calcular el área total cubierta por rectángulos.

Este módulo integra los componentes de barrido, compresión de coordenadas
y Segment Tree para calcular el área total de unión de rectángulos
alineados con los ejes.

Ejemplo de uso:
    >>> rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    >>> area = calculate_total_area(rectangles)
    >>> print(area)
    6
"""

from typing import List, Tuple, Dict
from sweep_events import get_sorted_events
from coordinate_compression import compress_coordinates
from segment_tree import SegmentTree


def prepare_data(rectangles: List[List[int]]) -> Tuple[List[Tuple[int, int, int, int]], List[int], Dict[int, int]]:
    """Prepara datos para el algoritmo de barrido: eventos ordenados y coordenadas comprimidas."""
    events = get_sorted_events(rectangles)
    sorted_y, coord_map = compress_coordinates(events)
    return events, sorted_y, coord_map


def area_between_events(events: List[Tuple[int, int, int, int]], tree: SegmentTree, index: int) -> int:
    """Calcula el área entre evento actual y siguiente usando altura del Segment Tree."""
    if index >= len(events) - 1:
        return 0
    x_current = events[index][0]
    x_next = events[index + 1][0]
    width = x_next - x_current
    height = tree.total_length()
    return width * height


def calculate_total_area(rectangles: List[List[int]]) -> int:
    """Calcula el área total cubierta por rectángulos módulo 10^9 + 7."""
    MOD = 10**9 + 7
    
    # Preparar datos
    events, sorted_y, coord_map = prepare_data(rectangles)
    
    # Inicializar Segment Tree
    tree = SegmentTree(sorted_y)
    
    total_area = 0
    
    # Recorrer eventos
    for i, event in enumerate(events):
        x, y1, y2, event_type = event
        
        # Calcular área desde el evento anterior
        if i > 0:
            area = area_between_events(events, tree, i - 1)
            total_area = (total_area + area) % MOD
        
        # Actualizar Segment Tree
        # Convertir y1, y2 a índices comprimidos
        comp_y1 = coord_map[y1]
        comp_y2 = coord_map[y2] - 1
        tree.range_add(comp_y1, comp_y2, event_type)
    
    return total_area % MOD


if __name__ == "__main__":
    # Ejemplo de uso
    rectangles1 = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
    area1 = calculate_total_area(rectangles1)
    print(f"Ejemplo 1 - Área total: {area1}")  # Debería imprimir 6
    
    rectangles2 = [[0, 0, 1000000000, 1000000000]]
    area2 = calculate_total_area(rectangles2)
    print(f"Ejemplo 2 - Área total: {area2}")  # Debería imprimir 49