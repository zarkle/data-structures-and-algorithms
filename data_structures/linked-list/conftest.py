import pytest
from linked_list import LinkedList as LL


@pytest.fixture
def empty_ll():
    """fixture for empty array"""
    return LL()


@pytest.fixture
def small_ll():
    """fixture for short array"""
    return LL([1, 2, 3, 4])


@pytest.fixture
def short_ll():
    """fixture for short array"""
    return LL([5, 6, 7, 8])


@pytest.fixture
def long_ll():
    """fixture for long array"""
    return LL([11, 12, 13, 14, 15, 16])
