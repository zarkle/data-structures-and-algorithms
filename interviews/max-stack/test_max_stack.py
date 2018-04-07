from max_stack import Stack
import pytest


@pytest.fixture
def empty_stack():
    """create an empty stack"""
    return Stack()


@pytest.fixture
def short_stack():
    """Create a short stack"""
    return Stack([1, 2, 3, 4, 5])


def test_get_max_none(short_stack):
    assert short_stack.max == 5
    assert short_stack.get_max() == 5


def test_get_max_empty(empty_stack):
    empty_stack.push(5)
    assert empty_stack.max == 5
    assert empty_stack.get_max() == 5


def test_get_max_push_three(empty_stack):
    empty_stack.push(5)
    empty_stack.push(3)
    empty_stack.push(4)
    assert empty_stack.max == 5
    assert empty_stack.get_max() == 5


def test_get_max_push_one(short_stack):
    short_stack.push(8)
    assert short_stack.max == 8
    assert short_stack.get_max() == 8


def test_get_max_new():
    s = Stack([4, 6, 5, 2])
    assert s.max == 6
    s.push(8)
    assert s.max == 8

