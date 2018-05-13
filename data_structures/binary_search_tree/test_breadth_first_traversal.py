from .breadth_first_traversal import breadth_first_traversal
from .bst import BST


def test_breadth_first_traversal():
    """Test breadth-first traversal."""
    tree = BST([2, 1, 3])
    assert breadth_first_traversal(tree) == [2, 1, 3]


def test_breadth_first_traversal_balanced(balanced_bst):
    """Test breadth-first traversal in balanced tree."""
    assert breadth_first_traversal(balanced_bst) == [10, 7, 16, 3, 8, 12, 20]


def test_breadth_first_traversal_right(right_heavy):
    """Test breadth-first traversal in right heavy tree."""
    assert breadth_first_traversal(right_heavy) == [1, 3, 5, 7, 9]

