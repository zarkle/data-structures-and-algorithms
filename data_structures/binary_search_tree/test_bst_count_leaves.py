from .bst_count_leaves import bst_count_leaves
from .bst import BST


def test_bst_count_leaves(balanced_bst):
    assert bst_count_leaves(balanced_bst) == 4


def test_bst_count_leaves_single(left_heavy):
    assert bst_count_leaves(left_heavy) == 1


def test_bst_count_leaves_new():
    assert bst_count_leaves(BST([20, 24, 22, 10, 12, 26])) == 3


def test_bst_count_leaves_one():
    assert bst_count_leaves(BST([1])) == 1
