from k_tree import KTree as KT
from print_level_order import print_level_order
import pytest


@pytest.fixture
def tree():
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    tree.insert(4, 1)
    tree.insert(5, 1)
    return tree


@pytest.fixture
def small_tree():
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    return tree


@pytest.fixture
def large_tree():
    tree = KT()
    tree.insert(10, None)
    tree.insert(2, 10)
    tree.insert(9, 10)
    tree.insert(3, 2)
    tree.insert(12, 9)
    tree.insert(13, 9)
    return tree


def test_print_level_order(tree):
    """test print_level_order"""
    assert print_level_order(tree) == '1 \n2 3 4 5 '


def test_print_level_order_small(small_tree):
    """test print_level_order with small tree"""
    assert print_level_order(small_tree) == '1 \n2 3 '


def test_print_level_order_large(large_tree):
    """test print_level_order with large tree"""
    assert print_level_order(large_tree) == '10 \n2 9 \n3 12 13 '
