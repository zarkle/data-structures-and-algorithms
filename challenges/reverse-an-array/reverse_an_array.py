def reverse_array(array):
    reverse = []
    for i in range(len(array)):
        reverse = [array[i]] + reverse
    return reverse
