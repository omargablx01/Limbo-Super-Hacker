#!/usr/bin/python3
# import socket
# def resolve_host_to_ip(hostname) -> str:
#     return socket.gethostbyname(hostname)
# Donmain = input("Write Domain Link Ex 'google.com' > ")
# result = resolve_host_to_ip(Donmain)
# print("-"*40)
# print(f"IP Address For '{Donmain}' > {result}")
# ! -------------- Other Way Prof
import socket

def resolve_hostname_to_ip(hostname) -> str:
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return "Could not resolve hostname"

target_hostname = input("Write Domain Link Ex 'google.com' > ")
resolved_ip = resolve_hostname_to_ip(target_hostname)
print("-"*40)
print(f"The IP Address ' {target_hostname} ' => {resolved_ip}")
