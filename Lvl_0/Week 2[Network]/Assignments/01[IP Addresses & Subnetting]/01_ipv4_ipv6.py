
#!/usr/bin/pyhon3
import ipaddress

def ipv4_ipv6(check_ip) -> str:
    try :
        return ipaddress.ip_address(check_ip)
    
    except ValueError :
        return f"'{check_ip}' Is Bad IP Try Again.."
    
check_ip = input("Write IP For Check > ")
result = ipv4_ipv6(check_ip)
print("-"*40)
print(result)