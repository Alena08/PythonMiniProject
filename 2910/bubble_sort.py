def bsA (array):
    for i in range(len(array)):
        print("-"*30)
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j]=array[j+1]
                array[j+1]=temp
            print(f"{i}) {j}: ", array)
    return array

arr = [-3,44,0,56,9,-8]

print(bsA(arr))