
#!/usr/bin/python3
import os
import re

def extract_ips(file_path)  -> str :

    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    
    try:
        with open(file_path,"r") as file:
            content = file.read()

            found_ips = re.findall(ip_pattern, content)
            
            valid_ips = [ip for ip in found_ips if all(int(part) <= 255 for part in ip.split('.'))]

            print("This ips Found : ")

            for my_ip in  valid_ips:
                print(my_ip)

    except FileNotFoundError:
        print("File Not Found !\nTry Again ..")
        
my_path = os.path.dirname(os.path.abspath(__file__))

file_name = input("Write File Name Like ( my_ips.txt ) : ")

print("-"*30)

linux_backslash = input("If Use Script in liunx Type ' / ' : ")

print("-"*30)

ips = extract_ips(fr"{my_path}{linux_backslash}{file_name}")

ips
