
# t~ >>>>                                            Assignments  04_Function&Modules                                     <<<<<
# ? --------------------------------- 1  ------------------------- 01_reversedis.py
#!/usr/bin/python3
# def reversedis(my_string):
#     return my_string[::-1]
# my_str = input("Write String > ")
# print("-"*40)
# rev_str = reversedis(my_str)
# print(f"After Reversed > {rev_str}")

# ? --------------------------------- 2  ------------------------- 02_strong_passwd.py
#!/usr/bin/python3
# import string
# def check_passwd(passwd):
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special = False

#     for char in passwd:
#         if len(passwd) >= 8 :
#             if char in string.ascii_uppercase:
#                 has_upper = True
#             elif char in string.ascii_lowercase:
#                 has_lower = True
#             elif char in string.digits:
#                 has_digit = True
#             elif char in string.punctuation:
#                 has_special = True

#     return has_upper and has_lower and has_digit and has_special

# strong_pass = input("PassWd > ")
# if check_passwd(strong_pass):
#     print(f"Password is Strong > {strong_pass}")
# else:
#     print(f"Password is Weak > {strong_pass}")
#! -------- rep exp
# import re

# def check_password_strength(passwd):
#     special_chars_list = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
#     special_chars_regex = re.escape(special_chars_list)

#     pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[" + special_chars_regex + r"])[A-Za-z\d" + special_chars_regex + r"]{8,}$"
    
#     if re.match(pattern, passwd):
#         return "Strong PassW0rd"
#     else:
#         return "Weak or invalid"

# strong_pass = input("PassWd > ")
# print("-"*40)
# print(f"Password '{strong_pass}' Is : {check_password_strength(strong_pass)}")
# ? --------------------------------- 3  ------------------------- 03_random12.py
#!/usr/bin/python3
# from string import *
# import random

# def random_12char_passwd():
#     lens = 12
#     all_data = ascii_letters + digits + punctuation
#     my_len = len(all_data)
#     my_str = []

#     for _ in range(lens):
#         my_str.append(all_data[random.randint(0, my_len - 1)])

#     return f"Random 12 Char Passwd > {"".join(my_str)}"

# result = random_12char_passwd()

# print(result)
# !--------- Other Way
# def strong_passwd():
#     length=12
#     all_char = ascii_letters + digits + punctuation
#     password = ''.join(random.choices(all_char, k=length))
#     return password

# print(strong_passwd())
# ? --------------------------------- 4  ------------------------- 04_MD5_Hash.py 
#!/usr/bin/python3
# import hashlib
# def md5_hash(strings="ntfsx00"):
#     result = hashlib.md5(strings.encode())
#     return f"MD5-Hash : {result.hexdigest()}"

# md5_string = input("Write String For MD5 Hash : ")
# print("-"*40)
# print(md5_hash(md5_string))

# ? --------------------------------- 5  ------------------------- 05_ip.py
# ! Random IP --------- Test Code Out Assignments ---------------- 
# import random

# def generate_random_ip():
#     """
#     Generates a random IPv4 address string (e.g., 192.168.1.1).
#     """
#     ip_octets = [str(random.randint(0, 255)) for _ in range(4)]
    
#     ip_address = ".".join(ip_octets)
    
#     return f"Random IP Address > {ip_address}"

# result = generate_random_ip()
# print(result)
# ? --------------------------------- 5  ------------------------- 05_ip.py
#!/usr/bin/python3
# import re

# def bad_ip(ip, reason=""):
#     print(f"Invalid IP address ( {ip} ). Reason: {reason}")
#     print(f"Format should be like ( 192.168.1.1 ) with numbers between 0-255 and no leading zeros (e.g., use 1 not 01).")
    
# def validate_ip(ip_address_str):
#     pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    
#     result = re.match(pattern, ip_address_str)
    
#     if result:
#         octets = result.groups()
        
#         for octet_str in octets:
#             if len(octet_str) > 1 and octet_str[0] == '0':
#                 bad_ip(ip_address_str, reason="Contains leading zeros.")
#                 return False
                
#             octet_int = int(octet_str)
#             if not (0 <= octet_int <= 255):
#                 bad_ip(ip_address_str, reason=f"Number {octet_int} is out of range (0-255).")
#                 return False
                
#         print(f"True IP > {ip_address_str}")
#         return True
        
#     else:
#         bad_ip(ip_address_str, reason="Incorrect format or structure.")
#         return False

# ip_address_input = input("Write IP Address > ")
# print("-"*40)
# validate_ip(ip_address_input)
# !--------- Other Way
# import ipaddress

# def validate_ip(ip_string):
#     try:
#         ip_object = ipaddress.ip_address(ip_string)
#         return True, f"Valid IP address. IPv{ip_object.version}"
#     except ValueError as e:
#         return False, f"Invalid IP address. Error: {e}"

# ip_address_input = input("Write IP Address > ")
# print(f"'{ip_address_input}': {validate_ip(ip_address_input)[1]}")
# ? --------------------------------- 6  ------------------------- 06_rand_mac.py
# ! OLD + HAbd :DD
#!/usr/bin/python3
# from string import *
# import random

# def rand_mac(count=12):
#     all_data = hexdigits
#     lens = len(all_data)
#     my_mac = []
#     if count == 12 :
#         for _ in range(count):
#             my_mac.append(all_data[random.randint(0,lens - 1)])
        
#         my_mac = f"{"".join(my_mac[:2])}-{"".join(my_mac[2:4])}-{"".join(my_mac[4:6])}-{"".join(my_mac[6:8])}-{"".join(my_mac[8:10])}-{"".join(my_mac[10:])}"

#         return f"Random MAC Address > {my_mac} "

# result = rand_mac()
# print(result)
# ! -------------- Other 
# ! Prof + GPT
#!/usr/bin/python3
# import random

# def generate_rand_mac():
    
#     mac = [random.randint(0x00, 0xff) for _ in range(6)]
#     dash = "-".join(f"{f:02x}" for f in mac)
#     colon = ":".join(f"{f:02x}" for f in mac)
#     return f"{dash}  __  {colon}"

# print(f"Random MAC Address > {generate_rand_mac()}")
# ? --------------------------------- 7  ------------------------- 07_XOR.py
#!/usr/bin/python3
# import operator

# def xor_cipher(text,key):
#     result = ''
#     for i in range(len(text)):
#         char_code = ord(text[i])
#         key_code = ord(key[i % len(key)])

#         xor_result = operator.xor(char_code,key_code)

#         result += chr(xor_result)

#     return result

# text = "seeyouleater"
# key = "MySafeKey"

# encrypted = xor_cipher(text,key)
# print(f"Encryption > {encrypted}")

# decrypted = xor_cipher(encrypted,key)

# print(f"Decrypted > {decrypted}")
# !----------- Other Way
# def xor_encrypt_decrypt(text, key):

#     xored_list = []
#     key_length = len(key)
#     for i in range(len(text)):
#         text_char_code = ord(text[i])
#         key_char_code = ord(key[i % key_length])
        
#         xor_result = text_char_code ^ key_char_code
        
#         xored_list.append(chr(xor_result))
        
#     return "".join(xored_list)

# message = "seeyouleater"
# secret_key = "MySafeKey"

# encrypted_message = xor_encrypt_decrypt(message, secret_key)
# print(f"Encrypted > {encrypted_message}")

# decrypted_message = xor_encrypt_decrypt(encrypted_message, secret_key)
# print(f"Decrypted > {decrypted_message}")
# !----------- Other Way
# def xor_cipher_pythonic(text, key):

#     return "".join(chr(ord(text[i]) ^ ord(key[i % len(key)]))for i in range(len(text)))

# key = "MySafeKey"
# text = "seeyouleater"

# encrypted = xor_cipher_pythonic(text, key)
# print(f"Encryption > {encrypted}")

# decrypted = xor_cipher_pythonic(encrypted, key)
# print(f"Decrypted > {decrypted}")
# ? --------------------------------- 8  ------------------------- 08_rand_uuid.py
#!/usr/bin/python3
# import uuid
# def random_uuid():
#     return uuid.uuid4()
# print(f"Random device ID: {random_uuid()}")
# ? --------------------------------- 9  ------------------------- 09_host_to_ip.py
#!/usr/bin/python3
# import socket
# def resolve_host_to_ip(hostname) -> str:
#     return socket.gethostbyname(hostname)
# Donmain = input("Write Domain Link Ex 'google.com' > ")
# result = resolve_host_to_ip(Donmain)
# print("-"*40)
# print(f"IP Address For '{Donmain}' > {result}")
# ! -------------- Other Way Prof
# import socket

# def resolve_hostname_to_ip(hostname) -> str:
#     try:
#         ip_address = socket.gethostbyname(hostname)
#         return ip_address
#     except socket.gaierror:
#         return "Could not resolve hostname"

# target_hostname = input("Write Domain Link Ex 'google.com' > ")
# resolved_ip = resolve_hostname_to_ip(target_hostname)
# print("-"*40)
# print(f"The IP Address ' {target_hostname} ' => {resolved_ip}")
# ? --------------------------------- 10  ------------------------- 09_host_to_ip.py
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
# def extract_vowels3(s):
#     vowels = "aeiouAEIOU"
#     return ",".join([char for char in s if char in vowels])
# test_str = input("Write String > ")
# print("-"*40)
# result = extract_vowels3(test_str)
# print(f"Vowels For '{test_str}' > {result}")
