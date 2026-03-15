#!/usr/bin/python3
import hashlib
def md5_hash(strings="ntfsx00"):
    result = hashlib.md5(strings.encode())
    return f"MD5-Hash : {result.hexdigest()}"

md5_string = input("Write String For MD5 Hash : ")
print("-"*40)
print(md5_hash(md5_string))
