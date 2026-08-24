"""Módulo Segment Tree con lazy propagation para longitud cubierta en el eje Y.

Este módulo implementa un Segment Tree que mantiene la longitud total cubierta
en el eje Y, soportando actualizaciones de rango (sumar/restar cobertura) y
consultas de longitud cubierta en O(log N).

Ejemplo de uso:
    >>> coords = [0, 1, 2, 3]
    >>> tree = SegmentTree(coords)
    >>> tree.range_add(0, 2, 1)  # Cubrir rango [0, 2)
    >>> print(tree.total_length())
    2
"""

from typing import List


class SegmentTree:
    """Segment Tree con lazy propagation para mantener longitud cubierta en el eje Y."""
    
    def __init__(self, coords: List[int]) -> None:
        """Inicializa el árbol con coordenadas Y comprimidas."""
        self.coords = coords
        self.n = len(coords) - 1  # Número de segmentos
        # Estructura del nodo: cover, length, lazy
        self.cover = [0] * (4 * self.n)
        self.length = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        
        # Construir árbol recursivamente
        self._build(0, 0, self.n - 1)
    
    def _build(self, node: int, start: int, end: int) -> None:
        """Construye el árbol recursivamente."""
        if start == end:
            # Nodo hoja: el rango es [coords[start], coords[start+1])
            self.length[node] = 0  # Inicialmente no cubierto
        else:
            mid = (start + end) // 2
            self._build(2 * node + 1, start, mid)
            self._build(2 * node + 2, mid + 1, end)
            self.length[node] = 0  # Inicialmente no cubierto
    
    def _apply_lazy(self, node: int, start: int, end: int) -> None:
        """Aplica lazy pendiente al nodo."""
        if self.lazy[node] != 0:
            self.cover[node] += self.lazy[node]
            if start == end:
                # Nodo hoja
                self.length[node] = self.coords[start + 1] - self.coords[start] if self.cover[node] > 0 else 0
            else:
                # Nodo interno
                if self.cover[node] > 0:
                    self.length[node] = self.coords[end + 1] - self.coords[start]
                else:
                    self.length[node] = self.length[2 * node + 1] + self.length[2 * node + 2]
            # Resetear lazy
            self.lazy[node] = 0
    
    def _push_lazy(self, node: int, start: int, end: int) -> None:
        """Propaga lazy a hijos si es necesario."""
        if self.lazy[node] != 0 and start != end:
            mid = (start + end) // 2
            self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[2 * node + 2] += self.lazy[node]
            self._apply_lazy(2 * node + 1, start, mid)
            self._apply_lazy(2 * node + 2, mid + 1, end)
            self.lazy[node] = 0
    
    def range_add(self, y1: int, y2: int, val: int) -> None:
        """Actualiza el rango [y1, y2) con +1 o -1."""
        # Encontrar índices comprimidos
        idx1 = self._find_index(y1)
        idx2 = self._find_index(y2) - 1
        self._range_add(0, 0, self.n - 1, idx1, idx2, val)
    
    def _find_index(self, y: int) -> int:
        """Encuentra el índice comprimido para una coordenada Y."""
        # Búsqueda binaria
        left, right = 0, len(self.coords) - 1
        while left < right:
            mid = (left + right) // 2
            if self.coords[mid] < y:
                left = mid + 1
            else:
                right = mid
        return left
    
    def _range_add(self, node: int, start: int, end: int, l: int, r: int, val: int) -> None:
        """Implementación recursiva de range_add."""
        # Aplicar lazy pendiente
        self._apply_lazy(node, start, end)
        
        if r < start or end < l:
            # Fuera del rango
            return
        
        if l <= start and end <= r:
            # Dentro del rango
            self.lazy[node] += val
            self._apply_lazy(node, start, end)
            return
        
        # Parcialmente dentro del rango
        mid = (start + end) // 2
        self._push_lazy(node, start, end)
        self._range_add(2 * node + 1, start, mid, l, r, val)
        self._range_add(2 * node + 2, mid + 1, end, l, r, val)
        
        # Actualizar longitud del nodo actual
        if self.cover[node] > 0:
            self.length[node] = self.coords[end + 1] - self.coords[start]
        else:
            self.length[node] = self.length[2 * node + 1] + self.length[2 * node + 2]
    
    def total_length(self) -> int:
        """Devuelve la longitud total cubierta en el eje Y."""
        self._apply_lazy(0, 0, self.n - 1)
        return self.length[0]


if __name__ == "__main__":
    # Ejemplo de uso
    from coordinate_compression import compress_coordinates
    from sweep_events import get_sorted_events
    
    rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
    events = get_sorted_events(rectangles)
    sorted_y, coord_map = compress_coordinates(events)
    
    tree = SegmentTree(sorted_y)
    
    print("Coordenadas comprimidas:", sorted_y)
    print("Árbol creado con", tree.n, "segmentos")
    
    # Ejemplo de actualización
    tree.range_add(0, 2, 1)  # Cubrir rango [0, 2)
    print("Longitud cubierta después de cubrir [0,2):", tree.total_length())
    
    tree.range_add(1, 3, 1)  # Cubrir rango [1, 3)
    print("Longitud cubierta después de cubrir [1,3):", tree.total_length())
    
    tree.range_add(0, 2, -1)  # Descubrir rango [0, 2)
    print("Longitud cubierta después de descubrir [0,2):", tree.total_length())