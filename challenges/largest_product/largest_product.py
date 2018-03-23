def largest_product(array):
    product = 0
        for i in array:
            if array[i][0] * array[i][1] > 0:
                product = array[i][0] * array[i][1]
    return product
