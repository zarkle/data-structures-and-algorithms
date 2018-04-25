from .queue import Queue


def find_matches(tree, value=None):
    """
    insert node into K-ary tree at all instances of given parent value
    """
    if tree.root is None:
        raise ValueError('Must provide tree')

    if value is None:
        raise ValueError('Must provide value')

    result = []
    queue = Queue()
    queue.enqueue(tree.root)

    while queue:
        current = queue.dequeue()
        if current.val == value:
            result.append(current)
        for child in current.children:
            queue.enqueue(child)

    return result
