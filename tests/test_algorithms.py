
from src.alpha_beta import alpha_beta
from src.game_tree import (
    medium_tree,
    ordered_tree_for_pruning,
    sample_tree,
)
from src.minimax import minimax


def test_minimax_sample_tree():
    result = minimax(sample_tree())
    assert result.value == 3
    assert result.nodes_evaluated == 4


def test_alpha_beta_sample_tree():
    tree = sample_tree()
    assert alpha_beta(tree).value == minimax(tree).value


def test_minimax_medium_tree():
    result = minimax(medium_tree())
    assert result.value == 7


def test_alpha_beta_medium_tree():
    tree = medium_tree()
    minimax_result = minimax(tree)
    alpha_beta_result = alpha_beta(tree)

    assert alpha_beta_result.value == minimax_result.value
    assert alpha_beta_result.nodes_evaluated <= minimax_result.nodes_evaluated


def test_alpha_beta_ordered_tree():
    tree = ordered_tree_for_pruning()
    minimax_result = minimax(tree)
    alpha_beta_result = alpha_beta(tree)

    assert minimax_result.value == 8
    assert alpha_beta_result.value == minimax_result.value
    assert alpha_beta_result.branches_pruned > 0
