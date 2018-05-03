from .tree_intersection import tree_intersection


def test_tree_intersection_one():
    """Test tree intersection."""
    assert tree_intersection(BST(['f', 'r', 'a', 'u', 'd']), BST(['p', 'a', 't'])) == {'a'}


def test_tree_intersection_two():
    """Test tree intersection."""
    assert tree_intersection(BST(['start', 'stop']), BST(['stop', 'copying'])) == {'stop'}

