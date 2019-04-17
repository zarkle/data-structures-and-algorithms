def BST_nearest_val(data, val):
    """Nearest Value in a Binary Seach Tree."""
    nearest = abs(val - data.root.val)
    hour = data.root.val

    def _walk(node=None):
        nonlocal nearest, hour
        if node is None:
            return

        if node.left is not None:
            _walk(node.left)

        # this conditional is only needed if you wanted to return the larger of 2 equidistant data points
        if abs(val - node.val) == nearest:
            if node.val > hour:
                hour = node.val

        if abs(val - node.val) < nearest:
            nearest = abs(val - node.val)
            hour = node.val

        if node.right is not None:
            _walk(node.right)

    _walk(data.root)

    return hour
