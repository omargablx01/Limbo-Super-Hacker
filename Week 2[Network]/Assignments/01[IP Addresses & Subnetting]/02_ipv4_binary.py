#!/usr/bin/pyhon3
import ipaddress
def ipv4_binary(my_ip):
    ip = ipaddress.IPv4Address(my_ip)
    binary_ip = ".".join(f"{int(octet):08b}" for octet in ip.packed)
    return f"After Convert > {binary_ip}"

input_ip = input("Write IP > ")
result = ipv4_binary(input_ip)
print("-"*40)
print(result)