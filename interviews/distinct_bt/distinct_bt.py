def distinct_values_bt(bin_tree):
    """Find distinct values in a binary tree."""
    distinct = {}
    result = []

    def _walk(node=None):
        if node is None:
            return

        if node.left is not None:
            _walk(node.left)

        if distinct.get(node.val):
            distinct[node.val] = distinct[node.val] + 1
        else:
            distinct[node.val] = 1

        if node.right is not None:
            _walk(node.right)

    _walk(bin_tree.root)

    for key in distinct:
        # if distinct[key] != 1:
        #     del distinct[key]
        if distinct[key] == 1:
            result.append(key)

    # return list(distinct.keys())
    return result
