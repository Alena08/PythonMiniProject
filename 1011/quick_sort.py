def quickSort(unsortedList):

    if len(unsortedList) <= 1:
        return unsortedList
    else:
        pivot = unsortedList[-1]
        left_list = []
        right_list = []
        mitte = []
        for i in unsortedList:
            if i < pivot:
                left_list.append(i)
            elif i > pivot:
                right_list.append(i)
            else:
                mitte.append(pivot)
        return quickSort(left_list) +mitte + quickSort(right_list)
    
my_list = [20, 2, 9, 8, 7, 12, 15, 1, 6, 8]    
print(my_list)
print(quickSort(my_list))

