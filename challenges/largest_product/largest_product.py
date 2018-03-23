def largest_product(array):
    product = 0
    for i in range(len(array)):
        if array[i][0] * array[i][1] > product:
            product = array[i][0] * array[i][1]
    return product
