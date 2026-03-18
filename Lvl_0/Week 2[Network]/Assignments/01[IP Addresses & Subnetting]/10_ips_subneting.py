
#!/usr/bin/python3

import ipaddress

def two_ipv4_network(ip1, ip2, cidr):
    try:
        if ipaddress.IPv4Address(ip1) and ipaddress.IPv4Address(ip2):

            network = ipaddress.ip_network(f"{ip1}/{cidr}", strict=False)
            
            target_ip = ipaddress.ip_address(ip2)

            if target_ip in network :
                return f"{True} {ip1} & {ip2} In One Network And Prefix Is /{cidr}"
            else :
                return f"{False} {ip1} & {ip2} Not in One Network And Prefix Is /{cidr}"

    except ValueError as e:
        return f"Error ; {e}"

ip_a = input("Write IP One > ")

ip_b = input("Write IP Two > ")

prefix = int(input("Write Perfix Like ( /24 ) > "))

print(two_ipv4_network(ip_a,ip_b,prefix))

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
# print(two_ipv4_network("192.168.1.10", "192.168.1.70", 24))