dummyArray = [84, 78, 52, 46, 12, 72, 60, 88, 2, 80]

# [84, 78, 52, 46, 12, 72, 60, 88, 2, 80]
# [84, 78, 52, 46, 12, 72, 60, 88, 2, 80]
# [78, 84, 52, 46, 12, 72, 60, 88, 2, 80]
# [52, 78, 84, 46, 12, 72, 60, 88, 2, 80]
# [46, 52, 78, 84, 12, 72, 60, 88, 2, 80]

# insert => sort 
# insert to left side one by one
# [sorting side <<< | >>> unsorted]

def toInsertionSort(array): 
    index_len = range(1, len(array))                                    
    for i in index_len:                                         # loop to array to insert one by one the element
          elem_to_insert = array[i]                             # insert one to the sorting left side of the array
          print(array)                                              
          while array[i-1] > elem_to_insert and i > 0:          # sort the left side of the array from the inserted element to left
              array[i], array[i-1] = array[i], array[i-1]       # swap 
              i  = i -1                                         # decrement so that the we can go to the left side 
              print(array)
    return array

toInsertionSort(dummyArray)
print('Sorted: ' , dummyArray)