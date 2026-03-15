
#!/usr/bin/python3
import ipaddress

def convert_ipv6(ip_str):
    try:
        ip_obj = ipaddress.IPv6Address(ip_str)
        
        expanded = ip_obj.exploded
        
        compressed = ip_obj.compressed
        
        return compressed, expanded
    
    except ValueError:
        return "Err : IPv6", None

ipv6_input = "2001:0db8:0000:0000:0000:ff00:0042:8329"
befor, after = convert_ipv6(ipv6_input)

print(f"Befor (Expanded):  {after}")
print("-"*40)
print(f"After (Compressed): {befor}")