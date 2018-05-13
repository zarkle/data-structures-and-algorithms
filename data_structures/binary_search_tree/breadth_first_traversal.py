"""Traverse a BST using a Breadth-first approach."""
from ..queue.queue import Queue


def breadth_first_traversal(tree):
    """Return breadth-first-traversal of a binary tree."""
    queue = Queue()
    traverse = []

    queue.enqueue(tree.root)
    while len(queue) > 0:
        current = queue.dequeue()
        traverse.append(current.val)
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)
    return traverse
