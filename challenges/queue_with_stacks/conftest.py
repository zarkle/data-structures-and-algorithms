import pytest
from .queue_with_stacks import Queue


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def short_queue():
    return Queue([1, 2, 3, 4])


@pytest.fixture
def long_queue():
    return Queue([10, 20, 30, 40, 50, 60, 70, 80])
