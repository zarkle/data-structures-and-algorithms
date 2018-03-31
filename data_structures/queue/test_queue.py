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


def test_enqueue_single(empty_queue):
    """Test making a new queue with a single Node"""
    empty_queue.enqueue(20)
    assert empty_queue.front.val == 20
    assert len(empty_queue) == 1


def test_enqueue(short_queue):
    """Test"""
    assert short_queue.front.val == 1
    assert short_queue.back.val == 5
    assert short_queue.back._next._previous.val == 5
    assert len(short_queue) == 5


def test_enqueue_long(long_queue):
    """Test"""
    assert long_queue.front.val == 1
    assert long_queue.back.val == 10
    assert len(long_queue) == 10


# def test_dequeue(short_queue):
#     """Test"""
#     assert short_queue.dequeue().val == 1
#     assert len(short_queue) == 4


# def test_dequeue_values(short_queue):
#     """Test"""
#     short_queue.dequeue()
#     assert short_queue.front.val == 2
#     assert short_queue.back.val == 5


# def test_dequeue_long(long_queue):
#     """Test"""
#     assert long_queue.dequeue().val == 1
#     assert len(long_queue) == 9


# def test_dequeue_long_values(long_queue):
#     """Test"""
#     long_queue.dequeue()
#     assert long_queue.front.val == 2
#     assert long_queue.back.val == 10
