import pytest
from .bst import BST


@pytest.fixture
def left_heavy():
    return BST([10, 8, 6, 4])


@pytest.fixture
def right_heavy():
    return BST([1, 3, 5, 7, 9])


@pytest.fixture
def balanced_bst():
    return BST([10, 7, 3, 16, 12, 8, 20])
