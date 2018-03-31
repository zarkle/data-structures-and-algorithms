from .linked_list import LinkedList as LL
from .ll_is_palindrome import is_palindrome


def test_is_palindrome_false():
    ll = LL([1, 2, 3, 4])
    assert is_palindrome(ll) is False


def test_is_palindrome_true():
    ll_pal = LL([10, 20, 20, 10])
    assert is_palindrome(ll_pal) is True

