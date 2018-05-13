"""Level-order printout of a k-ary tree."""
from ..queue.queue import Queue


def print_level_order(tree):
    """
    Print level order of K-ary tree.

    - input: k-ary tree
    - output: return a string that contains a listing of all values in the tree, with new lines in-between each level of the tree
    """
    queue = Queue()
    next_queue = Queue()
    final = ''

    queue.enqueue(tree.root)

    while queue or next_queue:
        if not queue:
            queue, next_queue = next_queue, queue
            final += '\n'

        current = queue.dequeue()
        final += f'{current.val} '
        for child in current.children:
            next_queue.enqueue(child)

    return final
