
#!/usr/bin/python3
# import ipaddress
# import re

# def ipv4(check_ip:str) -> str:
#     try :
#         class_a = r"^(12[0-6]|1[0-1][0-9]|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$"
#         loob_back = r"^127(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
#         class_b = r"^(12[8-9]|1[3-8][0-9]|19[0-1])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
#         class_c = r"^(19[2-9]|2[0-1][0-9]|22[0-3])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
#         class_d = r"^(22[4-9]|23[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
#         class_e = r"^(24[0-9]|25[0-5])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"

#         ip = f"{ipaddress.IPv4Address(check_ip)}"

#         if re.match(class_a,ip) :
#             return (f"Success: {ip} is a valid Class A address.")
#         elif re.match(loob_back,ip) :
#             return (f"Success: {ip} is a valid Loob Back IP.")
#         elif re.match(class_b,ip) :
#             return (f"Success: {ip} is a valid Class B address.")
#         elif re.match(class_c,ip) :
#             return (f"Success: {ip} is a valid Class C address.")
#         elif re.match(class_d,ip) :
#             return (f"Success: {ip} is a valid Class D address. (Reserved for Multicast)")
#         elif re.match(class_e,ip) :
#             return (f"Success: {ip} is a valid Class E address. (Reserved for Experimental use)")
#         else:
#             return None
    
#     except ValueError :
#         return f"'{check_ip}' Is Bad IP Try Again.."
    
# check_ip = input("Write IP For Check > ")
# result = ipv4(check_ip)
# print("-"*40)
# print(result)

#! ----------------- Other 
# import ipaddress

# def get_ipv4_class(ip):
#     try:
#         ip_obj = ipaddress.IPv4Address(ip)
        
#         first_octet = int(ip.split('.')[0])

#         if 1 <= first_octet <= 126:
#             return "Class A"
#         elif first_octet == 127:
#             return "Class A (Loopback)"
#         elif 128 <= first_octet <= 191:
#             return "Class B"
#         elif 192 <= first_octet <= 223:
#             return "Class C"
#         elif 224 <= first_octet <= 239:
#             return "Class D (Multicast)"
#         elif 240 <= first_octet <= 255:
#             return "Class E (Experimental)"
#         else:
#             return "Invalid IP range"
            
#     except (ValueError, IndexError):
#         return "Invalid IP Address: Each octet must be between 0 and 255."

# ip = input("Write IP For Check > ")
# print("-"*40)
# print(f"The IP {ip} belongs to: {get_ipv4_class(ip)}")

# ! -------------------- Other 
import ipaddress

def ipv4_pro(check_ip: str) -> str:
    try:
        ip = ipaddress.IPv4Address(check_ip)
        
        first_octet = int(str(ip).split('.')[0])

        if ip.is_loopback:
            return f"Success: {ip} is a Loopback IP."
        if ip.is_multicast:
            return f"Success: {ip} is a Class D (Multicast)."
        if first_octet >= 240:
            return f"Success: {ip} is a Class E (Experimental)."
        if 1 <= first_octet <= 126:
            return f"Success: {ip} is a Class A."
        if 128 <= first_octet <= 191:
            return f"Success: {ip} is a Class B."
        if 192 <= first_octet <= 223:
            return f"Success: {ip} is a Class C."
            
        return f"IP {ip} is valid but falls outside standard A/B/C classes."

    except ValueError:
        return f"Error: '{check_ip}' is not a valid IPv4 address."

print(ipv4_pro(input("Write IP For Check > ")))