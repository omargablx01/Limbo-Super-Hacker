
#!/usr/bin/python3

import ipaddress

def calculate_network_broadcast(ip_with_mask):
    try:
        interface = ipaddress.IPv4Interface(ip_with_mask)
        
        network = interface.network
        
        network_address = network.network_address

        broadcast_address = network.broadcast_address
        
        return network_address, broadcast_address
    
    except ValueError as e:
        return f"Err {e}", None

ip_input = input("Write IP And Mask Like > 192.168.1.60/24\nOR 192.168.1.60/255.255.255.0\n> ")
print("-"*40)
net_addr, broad_addr = calculate_network_broadcast(ip_input)

print(f"IP/Mask: {ip_input}")
print("-"*40)
print(f"Network Address: {net_addr}")
print("-"*40)
print(f"Broadcast Address: {broad_addr}")