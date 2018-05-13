import pytest
from .bst import BST
from .tree_intersection import tree_intersection


def test_tree_intersection_one(left_heavy):
    """Test tree intersection."""
    assert tree_intersection(left_heavy, BST([10, 12, 14, 16])) == {10}


def test_tree_intersection_two():
    """Test tree intersection."""
    assert tree_intersection(BST(['f', 'r', 'a', 'u', 'd']), BST(['p', 'a', 't'])) == {'a'}


def test_tree_intersection_third(balanced_bst):
    """Test tree intersection."""
    assert tree_intersection(balanced_bst, BST([10, 12, 14, 16])) == {10, 12, 16}


def test_tree_intersection_fourth():
    """Test tree intersection."""
    assert tree_intersection(BST(['start', 'stop']), BST(['stop', 'copying'])) == {'stop'}


def test_tree_intersection_error():
    """Test tree intersection error without binary tree."""
    with pytest.raises(AttributeError):
        assert tree_intersection(1, 2)
