import pytest
from .stack import Stack


@pytest.fixture
def empty_stack():
    """create an empty stack"""
    return Stack()


@pytest.fixture
def short_stack():
    """Create a short stack"""
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    return s


@pytest.fixture
def tall_stack():
    """Create a tall stack"""
    s = Stack()
    for num in range(10):
        s.push(num)
    return s
