
# t~ >>>>                                            Assignments  01[IP Addresses & Subnetting]                                     <<<<<
# ? --------------------------------- 1  ------------------------- 01_ipv4_ipv6.py
#!/usr/bin/python3
# import ipaddress

# def ipv4_ipv6(check_ip) -> str:
#     try :
#         return ipaddress.ip_address(check_ip)
    
#     except ValueError :
#         return f"'{check_ip}' Is Bad IP Try Again.."
    
# check_ip = input("Write IP For Check > ")
# result = ipv4_ipv6(check_ip)
# print("-"*40)
# print(result)

# ? --------------------------------- 2  ------------------------- 02_ipv4_binary.py
#!/usr/bin/python3
# import ipaddress
# def ipv4_binary(my_ip):
#     ip = ipaddress.IPv4Address(my_ip)
#     binary_ip = ".".join(f"{int(octet):08b}" for octet in ip.packed)
#     return f"After Convert > {binary_ip}"

# input_ip = input("Write IP > ")
# result = ipv4_binary(input_ip)
# print("-"*40)
# print(result)
# ? --------------------------------- 3  ------------------------- 03_ip_from_text.py
#!/usr/bin/python3
# import os
# import re

# def extract_ips(file_path)  -> str :

#     ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    
#     try:
#         with open(file_path,"r") as file:
#             content = file.read()

#             found_ips = re.findall(ip_pattern, content)
            
#             valid_ips = [ip for ip in found_ips if all(int(part) <= 255 for part in ip.split('.'))]

#             print("This ips Found : ")

#             for my_ip in  valid_ips:
#                 print(my_ip)

#     except FileNotFoundError:
#         print("File Not Found !\nTry Again ..")
        
# my_path = os.path.dirname(os.path.abspath(__file__))

# file_name = input("Write File Name Like ( my_ips.txt ) : ")

# print("-"*30)

# linux_backslash = input("If Use Script in liunx Type ' / ' : ")

# print("-"*30)

# ips = extract_ips(fr"{my_path}{linux_backslash}{file_name}")

# ips
# ? --------------------------------- 4  ------------------------- 04_private.py
#!/usr/bin/python3

# import ipaddress

# my_ip = input("Write Private IP Like (10.1.1.1) > ")

# try:
#     ip = ipaddress.ip_address(my_ip)
        
#     status = "( Private )" if ip.is_private else "( Public )"

#     print(f"IP : {my_ip} > {status}")
        
# except ValueError:
#     print(f"' {my_ip} ' Not Valid!")
# ? --------------------------------- 5  ------------------------- 05_ip_network_broad.py
#!/usr/bin/python3

# import ipaddress

# def calculate_network_broadcast(ip_with_mask):
#     try:
#         interface = ipaddress.IPv4Interface(ip_with_mask)
        
#         network = interface.network
        
#         network_address = network.network_address

#         broadcast_address = network.broadcast_address
        
#         return network_address, broadcast_address
    
#     except ValueError as e:
#         return f"Err {e}", None

# ip_input = input("Write IP And Mask Like > 192.168.1.60/24\nOR 192.168.1.60/255.255.255.0\n> ")
# print("-"*40)
# net_addr, broad_addr = calculate_network_broadcast(ip_input)

# print(f"IP/Mask: {ip_input}")
# print("-"*40)
# print(f"Network Address: {net_addr}")
# print("-"*40)
# print(f"Broadcast Address: {broad_addr}")
# ? --------------------------------- 6  ------------------------- 06_list_ip.py
#!/usr/bin/python3
# import ipaddress

# def gener_list_ip(ip_mask):
#     my_list = []
    
#     for addr in ipaddress.ip_network(ip_mask):
#         my_list.append(str(addr))

#     print("-"*40)

#     print(f"All IP > {len(my_list)}")
    
#     print("-"*40)

#     print(my_list)

# gener_list_ip('192.0.1.0/27')

# ! ----------- Other

# network = ipaddress.ip_network('192.168.1.0/27')

# all_ips = [str(ip) for ip in network]

# print("-"*40)

# print(f"All IP > {len(all_ips)}")

# print("-"*40)

# print(all_ips)
# ? --------------------------------- 7  ------------------------- 07_ping_ip.py
#!/usr/bin/python3
# from pythonping import ping

# target_ip = input("Write IP Like ( 192.168.1.1 ) > ")
# print("-"*40)
# count_ping = int(input("Count Ping > "))
# print("-"*40)
# timeout = int(input("Timeout Like ( 4 ) > "))
# print("-"*40)
# ping(target_ip,verbose=True,count=count_ping,timeout=timeout)

# ! ------------- Other

# import platform
# import subprocess

# def ping(target:str,count:int=4) -> bool:
#     if count >= 1:
#         param = '-n' if platform.system().lower()=='windows' else '-c'

#         command = ['ping', param, f'{count}', target]

#         return subprocess.call(command) == 0
#     else :
#         return f"{count} Is Under 1 Type Count >= 1"
    
# target_ip = input("Write IP Like ( 192.168.1.1 ) > ")

# print("-"*40)

# count_ping = int(input("Count Ping > "))

# print("-"*40)

# print(ping(target_ip,count_ping))
# ? --------------------------------- 8  ------------------------- 08_convert_ipv6.py
#!/usr/bin/python3
# import ipaddress

# def convert_ipv6(ip_str):
#     try:
#         ip_obj = ipaddress.IPv6Address(ip_str)
        
#         expanded = ip_obj.exploded
        
#         compressed = ip_obj.compressed
        
#         return compressed, expanded
    
#     except ValueError:
#         return "Err : IPv6", None

# ipv6_input = "2001:0db8:0000:0000:0000:ff00:0042:8329"
# befor, after = convert_ipv6(ipv6_input)

# print(f"Befor (Expanded):  {after}")
# print("-"*40)
# print(f"After (Compressed): {befor}")

# ? --------------------------------- 9  ------------------------- 09_ipv4_A_B_C_D_E.py

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

# ! -------------------- Other  ( RUN THIS )
# import ipaddress

# def ipv4(check_ip: str) -> str:
#     try:
#         ip = ipaddress.IPv4Address(check_ip)
        
#         first_octet = int(str(ip).split('.')[0])

#         if ip.is_loopback:
#             return f"Success: {ip} is a Loopback IP."
#         elif ip.is_multicast:
#             return f"Success: {ip} is a Class D (Multicast)."
#         elif first_octet >= 240:
#             return f"Success: {ip} is a Class E (Experimental)."
#         elif 1 <= first_octet <= 126:
#             return f"Success: {ip} is a Class A ."
#         elif 128 <= first_octet <= 191:
#             return f"Success: {ip} is a Class B ."
#         elif 192 <= first_octet <= 223:
#             return f"Success: {ip} is a Class C ."
            
#         return f"IP {ip} is valid but falls outside standard A/B/C classes."

#     except ValueError:
#         return f"Error: '{check_ip}' is not a valid IPv4 address."
    
# ip = input("Write IP For Check > ")
# result = ipv4(ip)
# print("-"*40)
# print(result)

# ? --------------------------------- 10  ------------------------- 10_ips_subneting.py
# @@ ( RUN THIS )

#!/usr/bin/python3

# import ipaddress

# def two_ipv4_network(ip1, ip2, cidr):
#     try:
#         if ipaddress.IPv4Address(ip1) and ipaddress.IPv4Address(ip2):

#             network = ipaddress.ip_network(f"{ip1}/{cidr}", strict=False)
            
#             target_ip = ipaddress.ip_address(ip2)

#             if target_ip in network :
#                 return f"{True} {ip1} & {ip2} In One Network And Prefix Is /{cidr}"
#             else :
#                 return f"{False} {ip1} & {ip2} Not in One Network And Prefix Is /{cidr}"

#     except ValueError as e:
#         return f"Error ; {e}"

# ip_a = input("Write IP One > ")

# ip_b = input("Write IP Two > ")

# prefix = int(input("Write Perfix Like ( /24 ) > "))

# print(two_ipv4_network(ip_a,ip_b,prefix))

# --------------------------------- Other

# import socket
# import struct

# def two_ipv4_network(ip1, ip2, prefix):

#     ip1_int = struct.unpack("!I", socket.inet_aton(ip1))[0]
#     ip2_int = struct.unpack("!I", socket.inet_aton(ip2))[0]

#     host_bits = 32 - prefix
    
#     network1 = ip1_int >> host_bits
#     network2 = ip2_int >> host_bits

#     return network1 == network2

# print(two_ipv4_network("192.168.1.10", "192.168.1.50", 25))
# print(two_ipv4_network("192.168.1.10", "192.168.1.70", 24))s