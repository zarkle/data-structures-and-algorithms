def mergesort(lst):
    """Perform merge sort algorithm."""

    def divide(lst):
        """Divide."""
        if len(lst) <= 1:
            return lst

        middle = len(lst) // 2
        left = lst[:middle]
        right = lst[middle:]

        left = divide(left)
        right = divide(right)
        return merge(left, right)

    def merge(left, right):
        """Conquer."""
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        while len(left) > 0:
            result.append(left.pop(0))
        while len(right) > 0:
            result.append(right.pop(0))

        return result

    return divide(lst)
