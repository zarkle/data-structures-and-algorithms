from .find_maximum_value_binary_tree import find_maximum_value
from .bst import BST


def test_find_maximum_value_balanced():
    """Test find max value in balanced tree."""
    balanced = BST([10, 7, 3, 16, 12, 8, 20])
    assert find_maximum_value(balanced) == 20


def test_find_maximum_value_left():
    """Test find max value in left-heavy tree."""
    left = BST([10, 8, 6, 4])
    assert find_maximum_value(left) == 10


def test_find_maximum_value_right():
    """Test find max value in right-heavy tree."""
    right = BST([1, 3, 5, 7, 9])
    assert find_maximum_value(right) == 9
