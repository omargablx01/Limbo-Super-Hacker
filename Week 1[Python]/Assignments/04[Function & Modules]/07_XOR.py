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
def xor_cipher_pythonic(text, key):

    return "".join(chr(ord(text[i]) ^ ord(key[i % len(key)]))for i in range(len(text)))

key = "MySafeKey"
text = "seeyouleater"

encrypted = xor_cipher_pythonic(text, key)
print(f"Encryption > {encrypted}")

decrypted = xor_cipher_pythonic(encrypted, key)
print(f"Decrypted > {decrypted}")
