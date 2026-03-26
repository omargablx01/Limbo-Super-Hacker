
#!/usr/bin/python3

import socket
import psutil
from colorama import Fore, Style, init

init(autoreset=True)

def get_process_name(pid):
    try:
        return psutil.Process(pid).name()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return "N/A"

w_proto, w_port, w_ip, w_pid, w_name, w_status = 10, 10, 18, 8, 15, 15

data_list = []
connections = psutil.net_connections(kind='inet4')

for conn in connections:
    local_ip = conn.laddr.ip
    if local_ip not in ["0.0.0.0", "127.0.0.1"]:
        protocol = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"
        local_port = conn.laddr.port
        pid = conn.pid if conn.pid else 0
        p_name = get_process_name(pid) if pid else "System"
        status = conn.status if conn.status else "N/A"
        
        data_list.append({
            "proto": protocol,
            "port": local_port,
            "ip": local_ip,
            "pid": pid,
            "name": p_name,
            "status": status
        })
data_list.sort(key=lambda x: (x['proto'], x['port']), reverse=True)

header = (
    f"{'PROTOCOL'.center(w_proto)} | {'PORT'.center(w_port)} | "
    f"{'LOCAL IP'.center(w_ip)} | {'PID'.center(w_pid)} | "
    f"{'PROCESS'.center(w_name)} | {'STATUS'.center(w_status)}"
)
print(Fore.RED  + Style.BRIGHT + header)
print(Fore.WHITE + "=" * len(header))

for item in data_list:
    color = Fore.CYAN if item['proto'] == "UDP" else Fore.GREEN
    
    row = (
        f"{item['proto'].center(w_proto)} | "
        f"{str(item['port']).center(w_port)} | "
        f"{item['ip'].center(w_ip)} | "
        f"{str(item['pid']).center(w_pid)} | "
        f"{item['name'][:14].center(w_name)} | "
        f"{item['status'].center(w_status)}"
    )
    print(color + row)