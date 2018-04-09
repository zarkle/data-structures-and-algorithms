from fizzbuzztree import BST, fizzbuzztree


def test_fizzbuzztree_balanced():
    """test fizz buzz on balanced tree"""
    balanced_bst = BST([10, 7, 3, 16, 15, 8, 20])
    fizzbuzztree(balanced_bst)
    assert balanced_bst.root.val == 'buzz'
    assert balanced_bst.root.right.left.val == 'fizz buzz'
    assert balanced_bst.root.left.left.val == 'fizz'


def test_fizzbuzztree_right():
    """test fizz buzz on right-heavy tree"""
    right_bst = BST([1, 3, 5, 7, 9, 15, 20, 21, 26])
    fizzbuzztree(right_bst)
    assert right_bst.root.right.val == 'fizz'
    assert right_bst.root.right.right.val == 'buzz'
    assert right_bst.root.right.right.right.right.right.val == 'fizz buzz'
    assert right_bst.root.right.right.right.right.right.right.right.val == 'fizz'


def test_fizzbuzztree_left():
    """test fizz buzz on left-heavy tree"""
    left_bst = BST([30, 10, 8, 6, 3])
    fizzbuzztree(left_bst)
    assert left_bst.root.val == 'fizz buzz'
    assert left_bst.root.left.val == 'buzz'
    assert left_bst.root.left.left.left.left.val == 'fizz'
