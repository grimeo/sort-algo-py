dummyArray = [84, 78, 52, 46, 12, 72, 60, 88, 2, 80]

def toSelectionSort(array):
    for i in range(0, len(array) - 1):                          # start array at 0. stop at last index which is arr -1
        min = i                                                 # initialize smallest value in the first index
        for j in range(i + 1, len(array)):                      # compare 
            if array[j] < array[min]:                           # if the second  selected index is smaller
                min = j                                    # smallest is the present index
        array[i], array[min] = array[min], array[i]             # swap the values for sorting
                                                  
toSelectionSort(dummyArray)
print(dummyArray)
