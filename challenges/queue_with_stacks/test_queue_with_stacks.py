from .queue_with_stacks import Queue
import pytest


def test_make_queue():
    """Test make a new queue"""
    q = Queue([1, 2, 3, 4])
    assert q.stack_one.top.val == 4
    assert q.stack_one._size == 4
    assert q._size == 4


def test_enqueue_single(empty_queue):
    """Test enqueue into an empty queue"""
    assert empty_queue.enqueue(5).stack_one.top.val == 5
    assert empty_queue._size == 1


def test_enqueue_twice(empty_queue):
    """Test enqueue twice into an empty queue"""
    empty_queue.enqueue(20)
    assert empty_queue.enqueue(21).stack_one.top.val == 21
    assert empty_queue._size == 2


def test_enqueue_not_empty(short_queue):
    """"Test enqueue into a non empty queue"""
    assert short_queue.enqueue(5).stack_one.top.val == 5
    assert short_queue._size == 5


def test_enqueue_not_valid(short_queue):
    """"Test enqueue raises error without value"""
    with pytest.raises(TypeError):
        short_queue.enqueue(None)
    assert short_queue.stack_one.top.val == 4
    assert short_queue._size == 4


def test_enqueue_not_valid_long(long_queue):
    """"Test enqueue raises error without value"""
    with pytest.raises(TypeError):
        long_queue.enqueue(None)
    assert long_queue.stack_one.top.val == 80
    assert len(long_queue.stack_one) == 8
    assert long_queue._size == 8


def test_dequeue_single(empty_queue):
    """Test dequeue single time"""
    empty_queue.enqueue(5)
    assert empty_queue.dequeue() == 5
    assert empty_queue._size == 0


def test_dequeue_invalid(empty_queue):
    """"Test dequeue raises error if empty queue"""
    with pytest.raises(IndexError):
        empty_queue.dequeue()


def test_dequeue(short_queue):
    """Test dequeue single time"""
    assert short_queue.dequeue() == 1
    assert short_queue._size == 3


def test_dequeue_stacks(short_queue):
    """Test dequeue single time--stack values"""
    short_queue.dequeue()
    assert short_queue.stack_one._size == 3
    assert short_queue.stack_two._size == 0


def test_dequeue_twice(short_queue):
    """Test dequeue twice--stack values"""
    short_queue.dequeue()
    assert short_queue.dequeue() == 2
    assert short_queue._size == 2


def test_dequeue_long(long_queue):
    """Test dequeue with long queue"""
    assert long_queue.dequeue() == 10
    assert long_queue._size == 7
    assert long_queue.stack_one.top.val == 80


def test_dequeue_long_stacks(long_queue):
    """Test dequeue with long queue--stack values"""
    long_queue.dequeue() == 10
    assert long_queue.stack_one._size == 7
    assert long_queue.stack_two._size == 0
