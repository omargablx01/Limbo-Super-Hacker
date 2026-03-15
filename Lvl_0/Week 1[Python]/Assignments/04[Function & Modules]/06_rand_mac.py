#!/usr/bin/python3
import random

def generate_rand_mac():
    
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    dash = "-".join(f"{f:02x}" for f in mac)
    colon = ":".join(f"{f:02x}" for f in mac)
    return f"{dash}  __  {colon}"

print(f"Random MAC Address > {generate_rand_mac()}")
