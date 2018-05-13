from .find_matches import find_matches as FM
from .k_tree import KTree as KT
import pytest


def test_find_match_no_tree():
    """Test that no tree raises error."""
    with pytest.raises(ValueError) as err:
        FM(None, 5)
    assert str(err.value) == 'Must provide tree'


def test_find_match_no_tree_root():
    """Test that no tree raises error."""
    tree = KT()
    with pytest.raises(ValueError) as err:
        FM(tree, 5)
    assert str(err.value) == 'Must provide tree'


def test_find_match_no_value(small_tree):
    """Test that no value raises error."""
    with pytest.raises(ValueError) as err:
        FM(small_tree, None)
    assert str(err.value) == 'Must provide value'


def test_find_match_single(small_tree):
    """Test find match function."""
    tree = FM(small_tree, 1)
    assert len(tree) == 1
    for node in tree:
        assert node.val == 1


def test_find_match_two(large_tree_match):
    """Test find match function."""
    tree = FM(large_tree_match, 2)
    assert len(tree) == 2
    for node in tree:
        assert node.val == 2


def test_find_match_none(large_tree_match):
    """Test find match function."""
    tree = FM(large_tree_match, 9)
    assert len(tree) == 0
