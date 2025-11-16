def binary_search(data,target):
    low = 0
    high = len(data)-1
    while low <= high:
        # mittleren Index finden
        mitte = (low + high)//2
        if target == data[mitte]:
            return mitte
        elif target< data[mitte]:
            high = mitte-1
        elif target > data[mitte]:
            #Das gesuchte Element liegt in der oberen Hälfte
            low = mitte +1 
    return -1


 
number=[2,5,8,12,16,23,38,56,72,91]
target_value=23
 
index = binary_search(number,target_value)
if index != -1:
    print(f"Zielwert {target_value} gefunden an Index: {index}")
else:
    print(f"Zielwert {target_value} nicht gefunden")