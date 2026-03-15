
#!/usr/bin/python3

import ipaddress

my_ip = input("Write Private IP Like (10.1.1.1) > ")

try:
    ip = ipaddress.ip_address(my_ip)
        
    status = "( Private )" if ip.is_private else "( Public )"

    print(f"IP : {my_ip} > {status}")
        
except ValueError:
    print(f"' {my_ip} ' Not Valid!")
