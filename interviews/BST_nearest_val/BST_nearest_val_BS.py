def nearest_val(lst, n, start=0, end=None):
    """Recursive binary search."""
    if end is None:
        end = len(lst) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    nearest = abs(lst[mid])
    hour = lst[mid]

    if n == lst[mid]:
        return mid
    if n < lst[mid]:
        return binary_search(lst, n, start, mid-1)
    # n > lst[mid]
    return binary_search(lst, n, mid+1, end)


def binary_search(seq, t):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return m


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

        if abs(val - node.val) < nearest:
            nearest = abs(val - node.val)
            hour = node.val

        if node.right is not None:
            _walk(node.right)

    _walk(data.root)

    return hour
