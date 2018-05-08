from random import randint


def quick_sort(lst):
    """Implement quick sort algorithm."""
    def partition(lst):
        if len(lst) < 2:
            return lst

        lst = list(lst)

        left, right = [], []
        pivot_index = randint(0, len(lst) - 1)
        for each in lst:
            if each < lst[pivot_index]:
                left.append(each)
            else:
                right.append(each)

        left = partition(left)
        right = partition(right)

        return left + [lst[pivot_index]] + right

    return partition(lst)
