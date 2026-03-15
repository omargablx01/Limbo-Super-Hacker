#!/usr/bin/python3
my_list = [115,1,458,2,5,89,4,6,7,4,3,748,415,15,9,12,33,489,412,-1]
lens = len(my_list)
print(f"Before Sort => {my_list}")
for i in range(lens):
    for j in range(0, lens - i - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
print("-"*90)
print(f"After Sort => {my_list}")
