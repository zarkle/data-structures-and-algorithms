from .bst import BST
import pytest


def test_bst_created_with_iterable():
    """"""
    bintree = BST([1, 2, 3])
    assert bintree.root.val == 1
    assert bintree.root.right.val == 2
    assert bintree.root.right.right.val == 3


def test_bst_created_with_iterable_four():
    """"""
    bintree = BST([1, 3, 2, 4])
    assert bintree.root.val == 1
    assert bintree.root.right.left.val == 2
    assert bintree.root.right.right.val == 4


def test_bst_invalid_iterable():
    """"""
    with pytest.raises(TypeError):
        BST(1)


def test_make_empty_bst():
    """"""
    empty_bst = BST()
    assert empty_bst.root is None


def test_single_is_root():
    """"""
    empty_bst = BST()
    empty_bst.insert(3)
    assert empty_bst.root.val == 3


def test_in_order_operation():
    """"""
    b = BST([1, 3, 2])
    order = []
    b.in_order(lambda n: order.append(n.val))
    assert order == [1, 2, 3]


def test_bst_insert():
    """"""
    bintree = BST([1, 2, 5])
    bintree.insert(3)
    assert bintree.root.val == 1
    assert bintree.root.right.val == 2
    assert bintree.root.right.right.left.val == 3
    assert bintree.root.right.right.val == 5


def test_fixture_left(left_heavy):
    """test left heavy fixture"""
    assert left_heavy.root.val == 10
    assert left_heavy.root.left.val == 8
    assert left_heavy.root.left.left.val == 6
    assert left_heavy.root.left.left.left.val == 4


def test_fixture_right(right_heavy):
    """test right heavy fixture"""
    assert right_heavy.root.val == 1
    assert right_heavy.root.right.val == 3
    assert right_heavy.root.right.right.val == 5
    assert right_heavy.root.right.right.right.val == 7
    assert right_heavy.root.right.right.right.right.val == 9


def test_fixture_balanced(balanced_bst):
    """test balanced fixture"""
    assert balanced_bst.root.val == 10
    assert balanced_bst.root.left.val == 7
    assert balanced_bst.root.left.left.val == 3
    assert balanced_bst.root.left.right.val == 8
    assert balanced_bst.root.right.val == 16
    assert balanced_bst.root.right.left.val == 12
    assert balanced_bst.root.right.right.val == 20


def test_in_order_operation_balance_in_order(balanced_bst):
    """"""
    order = []
    balanced_bst.in_order(lambda n: order.append(n.val))
    assert order == [3, 7, 8, 10, 12, 16, 20]


def test_in_order_operation_balance_pre_order(balanced_bst):
    """"""
    order = []
    balanced_bst.pre_order(lambda n: order.append(n.val))
    assert order == [10, 7, 3, 8, 16, 12, 20]


def test_in_order_operation_balance_post_order(balanced_bst):
    """"""
    order = []
    balanced_bst.post_order(lambda n: order.append(n.val))
    assert order == [3, 8, 7, 12, 20, 16, 10]


def test_in_order_operation_right_in_order(right_heavy):
    """"""
    order = []
    right_heavy.in_order(lambda n: order.append(n.val))
    assert order == [1, 3, 5, 7, 9]


def test_in_order_operation_right_pre_order(right_heavy):
    """"""
    order = []
    right_heavy.pre_order(lambda n: order.append(n.val))
    assert order == [1, 3, 5, 7, 9]


def test_in_order_operation_right_post_order(right_heavy):
    """"""
    order = []
    right_heavy.post_order(lambda n: order.append(n.val))
    assert order == [9, 7, 5, 3, 1]


def test_in_order_operation_left_in_order(left_heavy):
    """"""
    order = []
    left_heavy.in_order(lambda n: order.append(n.val))
    assert order == [4, 6, 8, 10]


def test_in_order_operation_left_pre_order(left_heavy):
    """"""
    order = []
    left_heavy.pre_order(lambda n: order.append(n.val))
    assert order == [10, 8, 6, 4]


def test_in_order_operation_left_post_order(left_heavy):
    """"""
    order = []
    left_heavy.post_order(lambda n: order.append(n.val))
    assert order == [4, 6, 8, 10]
