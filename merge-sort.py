dummyArray = [84, 78, 52, 46, 12, 72, 60, 88, 2, 80]

# [84, 78, 52, 46, 12, 72, 60, 88, 2, 80]

# [84, 78, 52, 46, 12,][72, 60, 88, 2, 80]
# [84, 78, 52][46, 12]
# [84, 78,][52]

# [78, 84][52]
# [52, 78, 84][46, 12,]
# [12, 46, 52, 78, 84]

def toMergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        
        toMergeSort(left)                                 # repeatedly call the function on both half
        toMergeSort(right)

        i = 0                                             # iterator for the left side 
        j = 0                                             # iterator for the right side
        k = 0                                             # iterator for the original array
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              array[k] = left[i]
              i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k]=right[j]
            j += 1
            k += 1

toMergeSort(dummyArray)
print(dummyArray)