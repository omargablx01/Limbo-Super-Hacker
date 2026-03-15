#!/usr/bin/python3
# def extract_vowels(string):
#     my_vowels = ["A","E","I","O","U","a","e","i","o","u"]
#     extracted = []
#     for my_str in string:
#         if my_str in my_vowels :
#             extracted.append(my_str)
#     return extracted
# test_str = input("Write String > ")
# print("-"*40)
# result = extract_vowels(test_str)
# print(f"Vowels For '{test_str}' > {result}")

# ! ------------ Other
# def extract_vowels2(s):
#     vowels = "aeiouAEIOU"
#     extracted = []
#     for char in s:
#         if char in vowels:
#             extracted.append(char)
#     return ",".join(extracted)
# test_str = input("Write String > ")
# print("-"*40)
# result = extract_vowels2(test_str)
# print(f"Vowels For '{test_str}' > {result}")

# ! ---------------- Other
def extract_vowels3(s):
    vowels = "aeiouAEIOU"
    return ",".join([char for char in s if char in vowels])
test_str = input("Write String > ")
print("-"*40)
result = extract_vowels3(test_str)
print(f"Vowels For '{test_str}' > {result}")
