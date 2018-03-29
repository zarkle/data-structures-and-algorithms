import pytest
from linked_list import LinkedList as LL
from ll_merge import merge_lists as ml
#small (1, 2, 3, 4])
# short ([5, 6, 7, 8])
# long ([11, 12, 13, 14, 15, 16])


def test_merge_list(short_ll, long_ll):
    assert ml(short_ll, long_ll) == 8
    assert long_ll.head.val == 8
    assert long_ll.head._next.val == 16
    assert len(long_ll) == 10


def test_merge_list_two(long_ll, short_ll):
    assert ml(long_ll, short_ll) == 8
    assert long_ll.head.val == 8
    assert long_ll.head._next.val == 16
    assert len(long_ll) == 10


def test_merge_list_same(short_ll, small_ll):
    assert ml(short_ll, small_ll) == 8
    # assert len(small_ll) == 4
    # assert len(short_ll) == 4
    assert small_ll.head.val == 8
    assert small_ll.head._next.val == 4
    assert small_ll.head._next._next.val == 7
    assert small_ll.head._next._next._next._next.val == 6
    assert small_ll.head._next._next._next._next._next._next.val == 5
    assert small_ll.head._next._next._next._next._next._next._next.val == 1
    assert small_ll.head._next._next._next._next._next._next._next._next is None
    assert len(small_ll) == 8


def test_merge_list_empty(short_ll, empty_ll):
    assert ml(short_ll, empty_ll) == 8
    assert short_ll.head.val == 8
    assert short_ll.head._next.val == 7
    assert len(short_ll) == 4

