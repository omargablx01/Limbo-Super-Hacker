#!/usr/bin/python3
my_string = input("Write Palindrome String : ")

if my_string == my_string[::-1]:
    print(f"( {my_string[::-1]} ) Is Palindrome")
else:
    print(f"( {my_string} ) No't palindrome")


#@@ With Reversed Function OR

#rev = ''.join(reversed(my_string))

#if my_string == rev:
#    print("palindrome")
#else:
#    print("No't palindrome")
