import pytest
from linked_list import LinkedList as LL

@pytest.fixture
def empty_ll():
    return LL()


@pytest.fixture
def small_ll():
    return LL([1, 2, 3, 4])


def test_insert_first_node(empty_ll):
    """test to insert first node"""
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


def test_insert_two_nodes(empty_ll):
    """test to insert two nodes, new node is inserted at head"""
    empty_ll.insert(2)
    empty_ll.insert(1)
    assert empty_ll.head.val == 1


def test_insert_iterable():
    assert LL([1, 2, 3, 4])._size == 4


def test_find_none(empty_ll):
    """test to search an empty list"""
    assert empty_ll.find(1) is False


def test_find(small_ll):
    """test to find in list"""
    assert small_ll.find(1) is True


def test_not_found(small_ll):
    """test to not find in list"""
    assert small_ll.find(5) is False


def test_length_empty(empty_ll):
    """test length of empty list"""
    assert len(empty_ll) == 0


def test_length(small_ll):
    """test length of list"""
    assert len(small_ll) == 4


def test_check_valid_iterable():
    """check if iterable valid"""
    with pytest.raises(TypeError) as err:
        LL(2)

    assert str(err.value) == 'Invalid iterable'
