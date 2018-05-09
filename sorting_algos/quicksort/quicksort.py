def quick_sort(lst):
    """Implement quick sort algorithm."""
    if len(lst) < 2:
        return lst

    lst = list(lst)

    left, right, equal = [], [], []

    pivot = lst[0]
    for i in range(len(lst)):
        if lst[i] < pivot:
            left.append(lst[i])
        elif lst[i] > pivot:
            right.append(lst[i])
        else:
            equal.append(lst[i])

    # list comprehension shortcut:
    # left = [i for i in lst if i <= pivot]
    # right = [i for i in lst if i > pivot]

    return quick_sort(left) + equal + quick_sort(right)
