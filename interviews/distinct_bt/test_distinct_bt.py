from .distinct_bt import distinct_values_bt as DV
from data_structures.binary_search_tree.bst import BST


def test_distinct_bt():
    tree = BST([10, 7, 3, 10, 12, 8, 20])
    assert DV(tree) == [3, 7, 8, 12, 20]


def test_distinct_bt_repeats():
    assert DV(BST([5, 5, 5])) == []


def test_distinct_bt_two():
    assert DV(BST([10, 20, 5, 20, 13, 9, 8, 13])) == [5, 8, 9, 10]

