def binary_search(array, value):
    result = -1
    for i in range(len(array)):
        if array[i] == value:
            return i
    return result
