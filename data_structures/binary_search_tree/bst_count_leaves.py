def bst_count_leaves(tree):
    """Count the leaf nodes (nodes without children) in a binary tree."""
    leaves = 0

    def _walk(node=None):
        nonlocal leaves
        if node is None:
            return

        if node.left is not None:
            _walk(node.left)

        if node.left is None and node.right is None:
            leaves += 1

        if node.right is not None:
            _walk(node.right)

    _walk(tree.root)
    return leaves

