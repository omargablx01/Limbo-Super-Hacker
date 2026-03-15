
#!/usr/bin/python3
# from pythonping import ping

# target_ip = input("Write IP Like ( 192.168.1.1 ) > ")
# print("-"*40)
# count_ping = int(input("Count Ping > "))
# print("-"*40)
# timeout = int(input("Timeout Like ( 4 ) > "))
# print("-"*40)
# ping(target_ip,verbose=True,count=count_ping,timeout=timeout)

# ! ------------- Other

import platform
import subprocess

def ping(target:str,count:int=4) -> bool:
    if count >= 1:
        param = '-n' if platform.system().lower()=='windows' else '-c'

        command = ['ping', param, f'{count}', target]

        return subprocess.call(command) == 0
    else :
        return f"{count} Is Under 1 Type Count >= 1"
    
target_ip = input("Write IP Like ( 192.168.1.1 ) > ")

print("-"*40)

count_ping = int(input("Count Ping > "))

print("-"*40)

print(ping(target_ip,count_ping))