#!/usr/bin/python3
from string import *
import random

def random_12char_passwd(lens=12):
    all_data = ascii_letters + digits + punctuation
    my_len = len(all_data)
    my_str = []

    for _ in range(lens):
        my_str.append(all_data[random.randint(0, my_len - 1)])

    return f"Random 12 Char Passwd : {"".join(my_str)}"

result = random_12char_passwd(12)

print(result)

# OR
'''def strong_passwd(length=12):
    all_char = ascii_letters + digits + punctuation
    password = ''.join(random.choices(all_char, k=length))
    return password
print(strong_passwd(12))'''
