dummyArray = [84, 78, 52, 46, 12, 72, 60, 88, 2, 80]

# [84, 78, 52, 46, 12, 72, 60, 88, 2, 80]
# pick random number or median number
# [2 , 60, 72, 12, 46, 52, 78, 80, 84, 88]
# []80[84, 88]
# [52 ,46, 12, 72, 60, 2, 78,]80[84, 88]
# [2 , 12 ,46, 52, 72, 60,]78, 80, 84, 88
# [lesser] + pivot + [greater]

def toQuickSort(array):
    greaterElems = []                                                   # separation of greater value in form of arr
    lesserElems = []                                                    # separation of lesser value in form of arr
    arrlen = len(array)
    
    if arrlen <= 1:                                                     # detect if the array items is less than or equal 1
        return array
    else:                                                               # select pivot to determine the less and greater vals
        pivot = array.pop()
    
    for element in array:                                               # loop to distinguish the more or less values
        if element > pivot:                                             # separate the greater
            greaterElems.append(element)                                # put to greater arr
        else:                                                           # separate the lesser value
            lesserElems.append(element)                                 # add to lesser array
    return toQuickSort(lesserElems) + [pivot] + toQuickSort(greaterElems)

print(toQuickSort(dummyArray))