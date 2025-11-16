def linear_search(data,target):
    for index, element in enumerate(data):
        if element == target:
            return index
        # Das Element nicht in der Liste
    return -1
 
unsorted_data = [5, 12, 2, 91, 16, 23, 8, 38, 72, 56]
target_value = 8
 
 
index = linear_search(unsorted_data,target_value)
print(index)
if index != -1:
    print(f"Zielwert {target_value} gefunden an Index {index}")
else:
    print(f"Zielwert {target_value} nicht gefunden")