import pytest
from .queue import Queue


@pytest.fixture
def empty_queue():
    """create an empty queue"""
    return Queue()


@pytest.fixture
def short_queue():
    """create a short queue"""
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    return q


@pytest.fixture
def long_queue():
    """Create a long queue"""
    q = Queue()
    for num in range(1, 11):
        q.enqueue(num)
    return q
