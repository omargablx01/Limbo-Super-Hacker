
#!/usr/bin/python3
import ipaddress
my_ip = input("Write IP Like ' 192.168.1.0/24 '> ")

def gener_list_ip(ip_mask):
    my_list = []
    
    for addr in ipaddress.ip_network(ip_mask):
        my_list.append(str(addr))

    print("-"*40)

    print(f"All IP > {len(my_list)}")
    
    print("-"*40)

    print(my_list)

gener_list_ip(my_ip)

# ! ----------- Other
my_ip = input("Write IP Like ' 192.168.1.0/24 '> ")

def gener_list_ip(ip_mask):

    network = ipaddress.ip_network(ip_mask)

    all_ips = [str(ip) for ip in network]

    print("-"*40)

    print(f"All IP > {len(all_ips)}")

    print("-"*40)

    print(all_ips)

gener_list_ip(my_ip)