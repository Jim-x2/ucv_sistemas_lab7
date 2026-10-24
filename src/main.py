
"""Programa principal para comparar Minimax y Alfa-Beta."""

from src.alpha_beta import alpha_beta
from src.game_tree import (
    medium_tree,
    ordered_tree_for_pruning,
    sample_tree,
)
from src.minimax import minimax


def compare_algorithms(tree_name: str, tree) -> None:
    """Muestra los resultados de ambos algoritmos."""

    minimax_result = minimax(tree)
    alpha_beta_result = alpha_beta(tree)

    print(f"\nÁrbol: {tree_name}")
    print("-" * 40)
    print(f"Valor Minimax: {minimax_result.value}")
    print(f"Hojas evaluadas por Minimax: {minimax_result.nodes_evaluated}")
    print(f"Valor Alfa-Beta: {alpha_beta_result.value}")
    print(f"Hojas evaluadas por Alfa-Beta: {alpha_beta_result.nodes_evaluated}")
    print(f"Ramas podadas: {alpha_beta_result.branches_pruned}")


def main() -> None:
    """Ejecuta los ejemplos del laboratorio."""

    compare_algorithms("Árbol pequeño", sample_tree())
    compare_algorithms("Árbol mediano", medium_tree())
    compare_algorithms("Árbol ordenado", ordered_tree_for_pruning())


if __name__ == "__main__":
    main()
