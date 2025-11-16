
# N ist 1000 (Elemnte in der Liste):

# LS:
# O(N) = 1000 schritte

# BS:
# O(log N) = 10 Schritte

# LS

# def linear_search(data,target):
    
#     # Durchlaufe jedes element in der liste
#     for index, element in enumerate(data):
#         if element == target:
#             return index
#     # Das Element ist nicht in der Liste
#     return -1

# unsorted_data = [x*2 for x in range(100)]
# target_value = 18


# index = linear_search(unsorted_data,target_value)

# if index != -1:
#     print(f"Zielwert {target_value} gefunden an Index: {index}")
# else:
#     print(f"Zielwert {target_value} nicht gefunden")


# liste=[4,5,6,3,54,5]

# for index, element in enumerate(liste):
#     print(index,element)


def binary_search(data,target):
    low = 0
    high = len(data)-1
    
    while low <= high:

        # finde den mittleren Index
        mid = (low+high) // 2
        guess = data[mid]

        if guess == target:
            return mid
        elif guess < target:
            # Das gesuchte Element liegt in der oberen Hälfte
            low = mid + 1
        else:
            high = mid -1
    
    return -1


# elemnte bei Binary search müssen sotiert sein
number=[2,5,8,12,16,23,38,56,72,91]
target_value=23

index = binary_search(number,target_value)

if index != -1:
    print(f"Zielwert {target_value} gefunden an Index: {index}")
else:
    print(f"Zielwert {target_value} nicht gefunden")