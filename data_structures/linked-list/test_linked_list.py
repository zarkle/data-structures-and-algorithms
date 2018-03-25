import pytest
from linked_list import LinkedList as LL

@pytest.fixture
def empty_ll():
    return LL()



@pytest.fixture
def small_ll():
    return LL([1, 2, 3, 4])


def test_insert_first_node(empty_ll):
    assert empty_ll.head is None
    empty_ll.inesrt(2)
    assert empty_ll.head.val == 2
