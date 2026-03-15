#!/usr/bin/python3
import ipaddress

def validate_ip(ip_string):
    try:
        ip_object = ipaddress.ip_address(ip_string)
        return True, f"Valid IP address. IPv{ip_object.version}"
    except ValueError as e:
        return False, f"Invalid IP address. Error: {e}"

ip_address_input = input("Write IP Address > ")
print(f"'{ip_address_input}': {validate_ip(ip_address_input)[1]}")



#
#
#
# Other Way #
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
