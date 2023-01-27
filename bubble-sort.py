dummyArray = [84, 78, 52, 46, 12, 72, 60, 88, 2, 80]

# [84, 78, 52, 46, 12, 72, 60, 88, 2, 80]
# [78, 84, 52, 46, 12, 72, 60, 88, 2, 80]
# [78, 52, 84, 46, 12, 72, 60, 88, 2, 80]

def toBubbleSort(array):
    index_len = len(array) - 1                                      # len -1 is because the last has no value on right side
    sorted = False                                                  # bool var for checking if the whole arr is sorted
    while not sorted:                                               # loop until the the arr is already sorted
        print(array)
        sorted = True                                               # set the value to true to stop the array if already sorted
        for i in range(0, index_len):                               # loop to compare the right side
            if array[i] > array[i+1]:                               # if left value is greater than right
                sorted = False                                      # not sorted so start again the loop
                array[i], array[i+1] = array[i+1], array[i]        # so swap the values of the right to left bubble
                print(array)
    return array

toBubbleSort(dummyArray)
print(dummyArray)