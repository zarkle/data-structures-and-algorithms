def bst_binary_search(tree, value):
    """Use binary search to find a value in a binary search tree. Return True if value in tree; return False if value not in tree."""
    if not tree.root:
        return False

    current = tree.root

    while current:
        if current.val == value:
            return True
        elif value >= current.val:
            if current.right:
                current = current.right
            else:
                return False
        else:
            if current.left:
                current = current.left
            else:
                return False
