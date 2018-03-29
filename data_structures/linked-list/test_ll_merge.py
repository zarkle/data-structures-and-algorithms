from ll_merge import merge_lists as ml


def test_merge_list(short_ll, long_ll):
    """test merged list with lists of varying lengths"""
    assert ml(short_ll, long_ll) == 8
    assert len(long_ll) == 10


def test_merge_list_values(short_ll, long_ll):
    """test merged list with lists of varying lengths"""
    ml(short_ll, long_ll)
    assert long_ll.head.val == 8
    assert long_ll.head._next.val == 16


def test_merge_list_two(long_ll, short_ll):
    """test merged list with lists of varying lengths"""
    assert ml(long_ll, short_ll) == 16
    assert len(long_ll) == 10


def test_merge_list_two_values(long_ll, short_ll):
    """test merged list with lists of varying lengths"""
    ml(long_ll, short_ll)
    assert long_ll.head.val == 16
    assert long_ll.head._next.val == 8


def test_merge_list_same(short_ll, small_ll):
    """test merged list with lists of same length"""
    assert ml(short_ll, small_ll) == 8
    assert len(small_ll) == 8


def test_merge_list_same_values(short_ll, small_ll):
    """test merged list with lists of same length"""
    ml(short_ll, small_ll)
    assert small_ll.head.val == 8
    assert small_ll.head._next.val == 4
    assert small_ll.head._next._next._next._next._next._next._next.val == 1


def test_merge_list_empty(short_ll, empty_ll):
    """test merged list when one list is empty"""
    assert ml(short_ll, empty_ll) == 8
    assert len(short_ll) == 4


def test_merge_list_empty_values(short_ll, empty_ll):
    """test merged list when one list is empty"""
    ml(short_ll, empty_ll)
    assert short_ll.head.val == 8
    assert short_ll.head._next.val == 7


def test_merge_list_empty_first(empty_ll, short_ll):
    """test merged list when one list is empty"""
    assert ml(empty_ll, short_ll) == 8
    assert len(short_ll) == 4


def test_merge_list_empty_first_values(empty_ll, short_ll):
    """test merged list when one list is empty"""
    ml(empty_ll, short_ll)
    assert short_ll.head.val == 8
    assert short_ll.head._next.val == 7

