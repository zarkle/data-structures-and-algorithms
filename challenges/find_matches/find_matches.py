from .queue import Queue


def find_matches(tree, value=None):
    """
    Find all matching values in a tree.

    Input: k-ary tree with non-unique values and a target value
    Output: collection of all the nodes from within the tree that match the provided value
    """
    if tree is None or tree.root is None:
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
