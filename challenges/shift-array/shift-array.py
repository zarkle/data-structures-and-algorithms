def insertShiftArray(array, value):
    array
    temp2 = 0
    middle = len(array) // 2
    temp = array[middle]
    array += [array[-1]]
    for i in range(middle, (len(array) - 1)):
        temp2 = array[i + 1]
        array[i + 1] = temp
        temp = temp2
    array[middle] = value
    return array
