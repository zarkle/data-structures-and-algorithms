"""Insertion sort."""


def insertion_sort(lst):
    """Implement insertion sorting algorithm."""
    if len(lst) < 2:
        return lst

    for i in range(1, len(lst)):
        while lst[i] < lst[i-1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            if (i - 1) == 0:
                break
            i -= 1

    return lst
