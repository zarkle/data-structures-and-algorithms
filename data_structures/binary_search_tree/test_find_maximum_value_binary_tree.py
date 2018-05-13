from .find_maximum_value_binary_tree import find_maximum_value
from .bst import BST


def test_find_maximum_value_balanced(balanced_bst):
    """Test find max value in balanced tree."""
    assert find_maximum_value(balanced_bst) == 20


def test_find_maximum_value_left(left_heavy):
    """Test find max value in left-heavy tree."""
    assert find_maximum_value(left_heavy) == 10


def test_find_maximum_value_right(right_heavy):
    """Test find max value in right-heavy tree."""
    assert find_maximum_value(right_heavy) == 9
