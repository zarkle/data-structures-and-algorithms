import pytest
from .queue import Queue


def test_make_invalid_queue():
    """Test that a instantiating a new Queue with a non-iterable will raise an error"""
    with pytest.raises(TypeError) as err:
        Queue(1)
    assert str(err.value) == 'Invalid iterable'


def test_make_valid_empty_queue(empty_queue):
    """Test that a new Queue has a back value of None"""
    assert empty_queue.front is None
    assert empty_queue.back is None
    assert len(empty_queue) == 0

