"""Selection sort.  The algorithm divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right."""


def selection_sort(lst):
    """Implement selection sorting algorithm."""
    if len(lst) < 2:
        return lst

    def smallest_index(lst):
        smallest = lst[0]
        sm_index = 0
        for i in range(len(lst)):
            if lst[i] < smallest:
                smallest = lst[i]
                sm_index = i
        return sm_index

    result = []
    for i in range(len(lst)):
        smallest = smallest_index(lst)
        result.append(lst.pop(smallest))

    return result

# a simpler solution
# def selection_sort(lst):
#     for i in range(len(lst)):
#         current_smallest_index = i
#         for j in range(i, len(lst)):
#             if lst[j] < lst[current_smallest_index]:
#                 current_smallest_index = j
#         if current_smallest_index != i:
#             lst[current_smallest_index], lst[i] = lst[i], lst[current_smallest_index]
#     return lst
