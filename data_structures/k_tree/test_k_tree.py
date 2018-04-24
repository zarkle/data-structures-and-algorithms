from .k_tree import KTree as KT
import pytest


def test_insert_root_K_tree():
    tree = KT()
    tree.insert(1, None)
    assert tree.root.val == 1


def test_insert_children_K_tree():
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    child_vals = [node.val for node in tree.root.children]
    assert tree.root.val == 1
    assert tree.root.children[0].val == 2
    assert child_vals == [2, 3]


def test_insert_many_children_K_tree():
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    tree.insert(4, 3)
    tree.insert(5, 3)
    assert tree.root.val == 1
    assert tree.root.children[1].children[0].val == 4
    assert tree.root.children[1].children[1].val == 5


def test_insert_raise_error():
    tree = KT()
    tree.insert(1, None)
    with pytest.raises(ValueError) as err:
        tree.insert(2, 2)
        assert err == 'Parent value not found'


def test_pre_order_small(small_tree):
    order = []
    small_tree.pre_order_traversal(lambda n: order.append(n.val))
    assert order == [1, 2, 3]


def test_pre_order_large(large_tree):
    order = []
    large_tree.pre_order_traversal(lambda n: order.append(n.val))
    assert order == [10, 2, 3, 9, 12, 13]


def test_pre_order_single(single_tree):
    order = []
    single_tree.pre_order_traversal(lambda n: order.append(n.val))
    assert order == [1]


def test_post_order_small(small_tree):
    order = []
    small_tree.post_order_traversal(lambda n: order.append(n.val))
    assert order == [2, 3, 1]


def test_post_order_large(large_tree):
    order = []
    large_tree.post_order_traversal(lambda n: order.append(n.val))
    assert order == [3, 2, 12, 13, 9, 10]


def test_post_order_single(single_tree):
    order = []
    single_tree.post_order_traversal(lambda n: order.append(n.val))
    assert order == [1]


def test_breadth_first_traversal_small(small_tree):
    assert small_tree.breadth_first_traversal() == [1, 2, 3]


def test_breadth_first_traversal_large(large_tree):
    assert large_tree.breadth_first_traversal() == [10, 2, 9, 3, 12, 13]


def test_breadth_first_traversal_single(single_tree):
    assert single_tree.breadth_first_traversal() == [1]

