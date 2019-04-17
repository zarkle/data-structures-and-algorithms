def sum_nodes(tree, start=None):
    """Estimate water usage for a given sprinkler system. (Sum all the nodes in a (sub)tree starting at the given node value or the whole tree if no value is given.)"""

    def _walk(node):
        if node is None:
            return

        if node.left is not None:
            _walk(node.left)

        if node.val == start:
            _walk_sum(node)

        if node.right is not None:
            _walk(node.right)

    def _walk_sum(node):
        nonlocal sum
        if node is None:
            return

        if node.left is not None:
            _walk_sum(node.left)

        sum += node.val

        if node.right is not None:
            _walk_sum(node.right)

    sum = 0
    if start is None:
        start = tree.root
        _walk_sum(start)
    else:
        _walk(tree.root)
    return sum
