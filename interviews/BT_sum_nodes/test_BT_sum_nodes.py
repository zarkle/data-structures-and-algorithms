from data_structures.binary_search_tree.bst import BST
from .BT_sum_nodes import sum_nodes


def test_sum_nodes():
    tree = BST([1, 2, 3, 4, 5])
    assert sum_nodes(tree) == 15


def test_sum_nodes_value():
    tree = BST([1, 2, 3, 4, 5])
    assert sum_nodes(tree, 3) == 12
