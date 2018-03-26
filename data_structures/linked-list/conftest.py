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
