from .k_tree import KTree as KT
import pytest


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


@pytest.fixture
def small_tree():
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    return tree


@pytest.fixture
def single_tree():
    tree = KT()
    tree.insert(1, None)
    return tree


@pytest.fixture
def tree():
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    tree.insert(4, 1)
    tree.insert(5, 1)
    return tree
