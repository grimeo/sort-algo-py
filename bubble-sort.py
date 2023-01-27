dummyArray = [84, 78, 52, 46, 12, 72, 60, 88, 2, 80]

def toBubbleSort(list_a):
    indexing_length = len(list_a) - 1                               #
    sorted = False                                                  # var for checking if the 
    while not sorted:                                               #
        sorted = True                                               #
        for i in range(0, indexing_length):                         # loop 
            if list_a[i] > list_a[i+1]:                             # if left value is greater than right
                sorted = False                                      # not sorted
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]     # so swap the values
    return list_a

toBubbleSort(dummyArray)
print(dummyArray)