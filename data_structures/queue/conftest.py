import pytest
from .queue import Queue


@pytest.fixture
def empty_queue():
    """create an empty queue"""
    return Queue()

