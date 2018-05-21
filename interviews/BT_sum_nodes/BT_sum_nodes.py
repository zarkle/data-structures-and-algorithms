def sum_nodes(tree, start=None):
    """Estimate water usage for a given sprinkler system."""
    sum = 0
    if start is None:
        start = tree.root

    def _walk(node):
        nonlocal sum
        if node is None:
            return

        if node.left is not None:
            _walk(node.left)

        sum += node.val

        if node.right is not None:
            _walk(node.right)

    _walk(start)

    return sum
