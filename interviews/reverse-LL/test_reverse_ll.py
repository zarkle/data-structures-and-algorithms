from linked_list import LinkedList as LL
from reverse_ll import reverse_ll


def test_reverse_ll():
    ll = LL([1, 2, 3, 4])
    assert ll.head.val == 4
    assert reverse_ll(ll) == 1


def test_reverse_ll_two():
    ll = LL([10, 20])
    assert ll.head.val == 20
    assert reverse_ll(ll) == 10


def test_reverse_ll_ten():
    ll = LL([_ for _ in range(1, 11)])
    assert ll.head.val == 10
    assert reverse_ll(ll) == 1

