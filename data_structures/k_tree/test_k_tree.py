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


def test_pre_order(small_tree):
    order = []
    small_tree.pre_order_traversal(lambda n: order.append(n.val))
    assert order == [1, 2, 3]
