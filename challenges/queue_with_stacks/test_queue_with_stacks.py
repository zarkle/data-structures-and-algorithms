from .queue_with_stacks import Queue

def test_make_queue():
    q = Queue([1, 2, 3, 4])
    assert q.top == 4
