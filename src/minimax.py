
"""
Implementación del algoritmo Minimax.

Minimax explora todas las hojas del árbol para determinar
el mejor valor posible frente a un rival racional.
"""

from dataclasses import dataclass
from src.game_tree import GameTree


@dataclass
class SearchResult:
    """Almacena el valor encontrado y las hojas evaluadas."""

    value: int
    nodes_evaluated: int


def is_leaf(node: GameTree) -> bool:
    """Devuelve True si el nodo es una hoja terminal."""
    return isinstance(node, int)


def minimax(
    node: GameTree,
    maximizing_player: bool = True,
) -> SearchResult:
    """
    Ejecuta Minimax sobre un árbol de juego.

    maximizing_player:
        True si el jugador actual busca maximizar.
        False si el jugador actual busca minimizar.
    """

    # Caso base: llegamos a una hoja del árbol.
    if is_leaf(node):
        return SearchResult(
            value=node,
            nodes_evaluated=1,
        )

    # Evaluar todos los hijos alternando MAX y MIN.
    results = [
        minimax(child, not maximizing_player)
        for child in node
    ]

    # Sumar las hojas evaluadas en todos los hijos.
    total_nodes = sum(
        result.nodes_evaluated for result in results
    )

    # Elegir el mejor resultado para el jugador actual.
    if maximizing_player:
        best_value = max(result.value for result in results)
    else:
        best_value = min(result.value for result in results)

    return SearchResult(
        value=best_value,
        nodes_evaluated=total_nodes,
    )
