#!/usr/bin/python3
# def check_passwd(password):
#     special_char = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special = False
    
#     if len(password) < 8:
#         return False 

#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in special_char:
#             has_special = True
            
#     if has_upper and has_lower and has_digit and has_special:
#         return True
#     else:
#         return False 

# strong_pass = input("PassWd > ")
# if check_passwd(strong_pass):
#     print(f"Password is Strong > {strong_pass}")
# else:
#     print(f"Password is Weak > {strong_pass}")

#! -------- rep exp
import re

def check_password_strength(passwd):
    special_chars_list = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    special_chars_regex = re.escape(special_chars_list)

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[" + special_chars_regex + r"])[A-Za-z\d" + special_chars_regex + r"]{8,}$"
    
    if re.match(pattern, passwd):
        return "Strong PassW0rd"
    else:
        return "Weak or invalid"

strong_pass = input("PassWd > ")
print("-"*40)
print(f"Password '{strong_pass}' Is : {check_password_strength(strong_pass)}")

