
"""
Árboles de juego para el laboratorio de Minimax y Poda Alfa-Beta.

Los nodos internos se representan mediante listas.
Las hojas contienen valores enteros.
"""

from typing import TypeAlias

GameTree: TypeAlias = int | list["GameTree"]


def sample_tree() -> GameTree:
    """Árbol pequeño para la demostración inicial. Resultado esperado: 3."""
    return [
        [3, 5],
        [2, 9],
    ]


def medium_tree() -> GameTree:
    """Árbol mediano para comprobar la poda. Resultado esperado: 6."""
    return [
        [[3, 5], [6, 9]],
        [[1, 2], [0, -1]],
        [[7, 4], [8, 6]],
    ]


def ordered_tree_for_pruning() -> GameTree:
    """Árbol ordenado para demostrar la poda. Resultado esperado: 10."""
    return [
        [[10, 9], [8, 7]],
        [[6, 5], [4, 3]],
        [[2, 1], [0, -1]],
    ]
