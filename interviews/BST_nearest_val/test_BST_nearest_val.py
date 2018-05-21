from .BST_nearest_val import BST_nearest_val as BNV
from data_structures.binary_search_tree.bst import BST


def test_BST_nearest_val_example_one():
    # data = BST([1, 3, 6, 4, 7, 8, 10, 14, 13])
    data = BST([8, 3, 1, 6, 4, 7, 10, 14, 13])
    assert BNV(data, 9) == 8


def test_BST_nearest_val_example_two():
    data = BST([8, 3, 1, 6, 4, 7, 10, 14, 13])
    assert BNV(data, 13) == 13


def test_BST_nearest_val_example_three():
    data = BST([8, 3, 1, 6, 4, 7, 10, 14, 13])
    assert BNV(data, 0) == 1


def test_BST_nearest_val_final_one():
    data = BST([15, 20, 7, 9, 3, 32, 17])
    assert BNV(data, 13) == 15


def test_BST_nearest_val_final_two():
    data = BST([15, 20, 7, 9, 3, 32, 17])
    assert BNV(data, 30) == 32


def test_BST_nearest_val_duplicates():
    data = BST([15, 20, 7, 9, 20, 32, 32])
    assert BNV(data, 30) == 32
