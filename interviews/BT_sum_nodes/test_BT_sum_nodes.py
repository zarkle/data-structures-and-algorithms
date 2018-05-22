from data_structures.binary_search_tree.bst import BST
from .BT_sum_nodes import sum_nodes


def test_sum_nodes():
    tree = BST([1, 2, 3, 4, 5])
    assert sum_nodes(tree) == 15


def test_sum_nodes_value():
    tree = BST([1, 2, 3, 4, 5])
    assert sum_nodes(tree, 3) == 12


def test_sum_nodes_value_six():
    tree = BST([8, 3, 1, 6, 4, 7, 10, 14, 13])
    assert sum_nodes(tree, 6) == 17


def test_sum_nodes_value_fourteen():
    tree = BST([8, 3, 1, 6, 4, 7, 10, 14, 13])
    assert sum_nodes(tree, 14) == 27


def test_sum_nodes_value_three():
    tree = BST([8, 3, 1, 6, 4, 7, 10, 14, 13])
    assert sum_nodes(tree, 3) == 21
