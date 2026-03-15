#!/usr/bin/python3
def reversedis(my_string):
    return my_string[::-1]
my_str = input("Write String > ")
print("-"*40)
rev_str = reversedis(my_str)
print(f"After Reversed > {rev_str}")
