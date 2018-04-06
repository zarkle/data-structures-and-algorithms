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
    c = []
    b.in_order(lambda n: c.append(n.val))
    assert c == [1, 2, 3]


def test_bst_insert():
    """"""
    bintree = BST([1, 2, 5])
    bintree.insert(3)
    assert bintree.root.val == 1
    assert bintree.root.right.val == 2
    assert bintree.root.right.right.left.val == 3
    assert bintree.root.right.right.val == 5

