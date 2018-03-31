from linked_list import LinkedList as LL
from reverse_ll import reverse_ll


def test_reverse_ll():
    ll = LL([1, 2, 3, 4])
    assert reverse_ll(ll).val == 1


def test_reverse_ll_two():
    ll = LL([10, 20])
    assert reverse_ll(ll).val == 10

