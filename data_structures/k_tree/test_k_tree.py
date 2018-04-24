from .k_tree import KTree as KT
import pytest


def test_insert_root_K_tree():
    """test insert into K-tree"""
    tree = KT()
    tree.insert(1, None)
    assert tree.root.val == 1


def test_insert_children_K_tree():
    """test insert into K-tree"""
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    child_vals = [node.val for node in tree.root.children]
    assert tree.root.val == 1
    assert tree.root.children[0].val == 2
    assert child_vals == [2, 3]


def test_insert_many_children_K_tree():
    """test insert into K-tree"""
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    tree.insert(4, 3)
    tree.insert(5, 3)
    assert tree.root.val == 1
    assert tree.root.children[1].children[0].val == 4
    assert tree.root.children[1].children[1].val == 5


def test_insert_raise_error_parent_not_found():
    """test insert into K-tree with invalid parent throws error"""
    tree = KT()
    tree.insert(1, None)
    with pytest.raises(ValueError) as err:
        tree.insert(2, 2)
        assert err == 'Parent value not found'


def test_insert_raise_error_none_parent():
    """test insert into K-tree with no parent value throws error"""
    tree = KT()
    tree.insert(1, None)
    with pytest.raises(ValueError) as err:
        tree.insert(2, None)
        assert err == 'Parent value not found'


def test_pre_order_small(small_tree):
    """test pre-order traversal of K-tree"""
    order = []
    small_tree.pre_order_traversal(lambda n: order.append(n.val))
    assert order == [1, 2, 3]


def test_pre_order_large(large_tree):
    """test pre-order traversal of K-tree"""
    order = []
    large_tree.pre_order_traversal(lambda n: order.append(n.val))
    assert order == [10, 2, 3, 9, 12, 13]


def test_pre_order_single(single_tree):
    """test pre-order traversal of K-tree"""
    order = []
    single_tree.pre_order_traversal(lambda n: order.append(n.val))
    assert order == [1]


def test_pre_order_tree(tree):
    """test pre-order traversal of K-tree"""
    order = []
    tree.pre_order_traversal(lambda n: order.append(n.val))
    assert order == [1, 2, 3, 4, 5]


def test_post_order_small(small_tree):
    """test post-order traversal of K-tree"""
    order = []
    small_tree.post_order_traversal(lambda n: order.append(n.val))
    assert order == [2, 3, 1]


def test_post_order_large(large_tree):
    """test post-order traversal of K-tree"""
    order = []
    large_tree.post_order_traversal(lambda n: order.append(n.val))
    assert order == [3, 2, 12, 13, 9, 10]


def test_post_order_single(single_tree):
    """test post-order traversal of K-tree"""
    order = []
    single_tree.post_order_traversal(lambda n: order.append(n.val))
    assert order == [1]


def test_post_order_tree(tree):
    """test post-order traversal of K-tree"""
    order = []
    tree.post_order_traversal(lambda n: order.append(n.val))
    assert order == [2, 3, 4, 5, 1]


def test_breadth_first_traversal_small(small_tree):
    """test breadth-first traversal of K-tree"""
    assert small_tree.breadth_first_traversal() == [1, 2, 3]


def test_breadth_first_traversal_large(large_tree):
    """test breadth-first traversal of K-tree"""
    assert large_tree.breadth_first_traversal() == [10, 2, 9, 3, 12, 13]


def test_breadth_first_traversal_single(single_tree):
    """test breadth-first traversal of K-tree"""
    assert single_tree.breadth_first_traversal() == [1]


def test_breadth_first_traversal_tree(tree):
    """test breadth-first traversal of K-tree"""
    assert tree.breadth_first_traversal() == [1, 2, 3, 4, 5]
