#!/usr/bin/python3
my_list = [9,6,7,9,6,7,1,1,2,2,3,3,4,4]
print(f"Befor Remove Duplicate : {my_list}")
print("-"*70)
def remove_duplicates(arr):
    unique = []
    for item in arr:
        if item not in unique:
            unique.append(item)
    return sorted(unique)
print(f"After Remove Duplicate : {remove_duplicates(my_list)}")
