from .distinct_bt import distinct_values_bt as DV
from data_structures.binary_search_tree.bst import BST


def test_distinct_bt():
    tree = BST([10, 7, 3, 10, 12, 8, 20])
    assert DV(tree) == [3, 7, 8, 12, 20]
