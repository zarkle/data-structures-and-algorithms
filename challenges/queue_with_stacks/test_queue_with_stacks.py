from .queue_with_stacks import Queue


def test_make_queue():
    """"""
    q = Queue([1, 2, 3, 4])
    assert q.stack_one.top.val == 4
    assert q._size == 4


def test_enqueue_single(empty_queue):
    """"""
    assert empty_queue.enqueue(5).stack_one.top.val == 5
    assert empty_queue._size == 1
