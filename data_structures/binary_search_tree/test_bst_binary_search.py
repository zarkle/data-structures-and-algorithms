from .bst_binary_search import bst_binary_search
from .bst import BST


def test_bst_binary_search(balanced_bst):
    assert bst_binary_search(balanced_bst, 10) is True
    assert bst_binary_search(balanced_bst, 11) is False
    assert bst_binary_search(balanced_bst, 12) is True
    assert bst_binary_search(balanced_bst, 22) is False
    assert bst_binary_search(balanced_bst, 8) is True


def test_bst_binary_search_right(right_heavy):
    assert bst_binary_search(right_heavy, 5) is True
    assert bst_binary_search(right_heavy, 6) is False


def test_bst_binary_search_none():
    assert bst_binary_search(BST(), 6) is False
