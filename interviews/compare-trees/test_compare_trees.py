from compare_trees import compare_trees, BST


def test_compare_trees_false():
    tree1 = BST([2, 1, 1, 1])
    tree2 = BST([2, 1, 2, 1])
    assert compare_trees(tree1, tree2) is False


def test_compare_trees_true_same():
    tree1 = BST([2, 1, 1, 1])
    tree2 = BST([2, 1, 1, 1])
    assert compare_trees(tree1, tree2) is True


def test_compare_trees_true():
    tree1 = BST([1, 2, 1, 2])
    tree2 = BST([2, 1, 2, 1])
    assert compare_trees(tree1, tree2) is True


def test_compare_trees():
    tree1 = BST([1, 1, 1, 1, 1, 1])
    tree2 = BST([2, 1, 2])
    assert compare_trees(tree1, tree2) is False


def test_compare_trees_none():
    tree1 = BST([])
    tree2 = BST([2, 1, 2])
    assert compare_trees(tree1, tree2) is False


def test_compare_trees_long():
    tree1 = BST([1, 2, 1, 2, 2, 1, 2, 1, 2, 1])
    tree2 = BST([2, 1, 2, 1, 1, 1, 2, 1, 2])
    assert compare_trees(tree1, tree2) is True
