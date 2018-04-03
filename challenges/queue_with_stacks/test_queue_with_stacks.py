from .queue_with_stacks import Queue
import pytest


def test_make_queue():
    """"""
    q = Queue([1, 2, 3, 4])
    assert q.stack_one.top.val == 4
    assert q._size == 4


def test_enqueue_single(empty_queue):
    """"""
    assert empty_queue.enqueue(5).stack_one.top.val == 5
    assert empty_queue._size == 1


def test_enqueue_not_empty(short_queue):
    """"""""
    assert short_queue.enqueue(5).stack_one.top.val == 5
    assert short_queue._size == 5


def test_enqueue_not_valid(short_queue):
    """"""""
    with pytest.raises(TypeError):
        short_queue.enqueue(None)
    assert short_queue.stack_one.top.val == 4
    assert short_queue._size == 4


def test_enqueue_not_valid_long(long_queue):
    """"""""
    with pytest.raises(TypeError):
        long_queue.enqueue(None)
    assert long_queue.stack_one.top.val == 80
    assert len(long_queue.stack_one) == 8
    assert long_queue._size == 8


def test_dequeue_single(empty_queue):
    empty_queue.enqueue(5)
    assert empty_queue.dequeue() == 5
    assert empty_queue._size == 0


def test_dequeue_invalid(empty_queue):
    with pytest.raises(IndexError):
        empty_queue.dequeue()


def test_dequeue(short_queue):
    assert short_queue.dequeue() == 1
    assert short_queue._size == 3


def test_dequeue_twice(short_queue):
    short_queue.dequeue()
    assert short_queue.dequeue() == 2
    assert short_queue._size == 2


def test_dequeue_long(long_queue):
    assert long_queue.dequeue() == 10
    assert long_queue._size == 7
    assert long_queue.stack_one.top.val == 80


def test_dequeue_long_stacks(long_queue):
    long_queue.dequeue() == 10
    assert long_queue.stack_one._size == 7
    assert long_queue.stack_two._size == 0
