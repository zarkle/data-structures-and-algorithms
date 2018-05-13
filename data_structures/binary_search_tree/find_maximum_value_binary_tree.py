"""Return the maximum value stored in a BST of numeric values."""
from ..queue.queue import Queue


def find_maximum_value(tree):
    """Return maximum value of tree."""
    queue = Queue()
    max_val = tree.root.val

    queue.enqueue(tree.root)
    while len(queue) > 0:
        current = queue.dequeue()
        if current.val > max_val:
            max_val = current.val
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)
    return max_val
