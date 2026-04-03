# import random

# random_ports = random.sample(range(1024, 65536), 5)

# print(f"Randomlyy PORTS Find : {random_ports}")
# ! --------------Other
# import socket
# import secrets

# def random_ports(count=5, start=1024, end=65535):
#     open_ports = []
    
#     while len(open_ports) < count:
#         port = secrets.SystemRandom().randint(start, end)
        
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#             try:
#                 s.bind(('', port))
#                 if port not in open_ports:
#                     open_ports.append(port)
#             except socket.error:
#                 continue
                
#     return sorted(open_ports)

# ports = random_ports(5)
# print(f"Randomlyy PORTS Find : {ports}")

# ! --------------Other ( Prof )

# import asyncio
# import random

# async def check_port(ip, port):
#     try:
#         conn = asyncio.open_connection(ip, port)
#         reader, writer = await asyncio.wait_for(conn, timeout=0.1)
#         writer.close()
#         await writer.wait_closed()
#         return port
#     except:
#         return None

# async def find_open_ports_pro(limit=5):
#     target = '192.168.1.10'
#     open_ports = []
    
#     print(f"Scaning...")
    
#     while len(open_ports) < limit:
#         tasks = []
#         potential_ports = [random.randint(1024, 65535) for _ in range(100)]
        
#         for port in potential_ports:
#             tasks.append(check_port(target, port))
        
#         results = await asyncio.gather(*tasks)
        
#         for p in results:
#             if p and p not in open_ports:
#                 open_ports.append(p)
#                 if len(open_ports) >= limit:
#                     break
                    
#     return open_ports[:limit]

# if __name__ == "__main__":
#     found = asyncio.run(find_open_ports_pro(5))
#     print(f"Find Ports Open : {found}")

# ! --------------Other ( Prof )
# import psutil
# import random

# def get_elite_open_ports(limit=5):
#     print(f"Scaning...\n")
    
#     connections = psutil.net_connections(kind='inet4')
    
#     open_ports_info = []
#     for conn in connections:
#         if conn.status == psutil.CONN_LISTEN and 1024 <= conn.laddr.port <= 65535:
#             try:
#                 process = psutil.Process(conn.pid)
#                 proc_name = process.name()
#             except (psutil.NoSuchProcess, psutil.AccessDenied):
#                 proc_name = "Unknown (Protected)"

#             info = {
#                 "port": conn.laddr.port,
#                 "protocol": "TCP" if conn.type == 1 else "UDP",
#                 "process": proc_name,
#                 "pid": conn.pid
#             }
            
#             if info not in open_ports_info:
#                 open_ports_info.append(info)

#     if len(open_ports_info) < limit:
#         print("Find 5 Port Or less..")

#     selected = random.sample(open_ports_info, min(len(open_ports_info), limit))
    
#     print(f"{'PORT':<10} | {'PROTO':<8} | {'PID':<8} | {'SERVICE/PROCESS'}")
#     print("=" * 50)
#     for p in selected:
#         print(f"{p['port']:<10} | {p['protocol']:<8} | {p['pid']:<8} | {p['process']}")

# if __name__ == "__main__":
#     get_elite_open_ports(5)

# ! --------------Other

# import socket
# import random
# from concurrent.futures import ThreadPoolExecutor
# import threading

# TARGET_IP = input("Enter Target IP (e.g., 192.168.1.1): ")
# PORT_RANGE = (1024,65535)
# REQUIRED_PORTS = 5

# found_ports = []
# lock = threading.Lock()

# def scan_port(ip, port):
#     try:
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#             s.settimeout(0.5)
#             result = s.connect_ex((ip, port))
#             if result == 0:
#                 with lock:
#                     if len(found_ports) < REQUIRED_PORTS:
#                         try:
#                             service = socket.getservbyport(port).upper()
#                         except:
#                             service = "Unknown Service"
                        
#                         found_ports.append({"port": port, "service": service})
#                         print(f"[+] Found Open Port: {port} ( {service} )")
#     except Exception:
#         pass

# def run_elite_scanner():
#     print(f"\nStarting Scan on Target: {TARGET_IP}")
#     print(f"Searching for {REQUIRED_PORTS} random open ports in range {PORT_RANGE}...\n")

#     all_ports = list(range(PORT_RANGE[0], PORT_RANGE[1] + 1))
#     random.shuffle(all_ports)

#     with ThreadPoolExecutor(max_workers=100) as executor:
#         for port in all_ports:
#             if len(found_ports) >= REQUIRED_PORTS:
#                 break
#             executor.submit(scan_port, TARGET_IP, port)

#     print("\n" + "="*40)
#     print(f"{'PORT':<10} | {'STATUS':<10} | {'SERVICE'}")
#     print("-" * 40)
#     for p in found_ports:
#         print(f"{p['port']:<10} | {'OPEN':<10} | {p['service']}")
#     print("="*40)

# if __name__ == "__main__":
#     if TARGET_IP:
#         run_elite_scanner()
#     else:
#         print("Error: Target IP is required.")

# ! --------------Other ( Prof )

# import socket
# import psutil
# import random
# import logging
# from typing import List, Optional
# from dataclasses import dataclass

# logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# @dataclass
# class PortMetadata:
#     port: int
#     status: str
#     protocol: str
#     service_name: str
#     port_name: str
#     pid: Optional[int] = None

# class ProPortManager:
    
#     def __init__(self, target_ip: str = '192.168.1.10', range_start: int = 1024, range_end: int = 65535):
#         self.target_ip = target_ip
#         self.range_start = range_start
#         self.range_end = range_end

#     def _get_common_name(self, port: int, proto: str) -> str:
#         try:
#             return socket.getservbyport(port, proto.lower())
#         except (OSError, socket.error):
#             return "UNKNOWN"

#     def get_active_system_ports(self, limit: int = 5) -> List[PortMetadata]:
#         unique_ports_map = {}
#         connections = psutil.net_connections(kind='inet4')
        
#         for conn in connections:
#             port = conn.laddr.port
#             if (conn.status == psutil.CONN_LISTEN and 
#                 self.range_start <= port <= self.range_end and 
#                 port not in unique_ports_map):
                
#                 try:
#                     proc = psutil.Process(conn.pid)
#                     proc_name = proc.name()
#                 except (psutil.NoSuchProcess, psutil.AccessDenied):
#                     proc_name = "System/Protected"

#                 protocol = "tcp" if conn.type == socket.SOCK_STREAM else "udp"
                
#                 unique_ports_map[port] = PortMetadata(
#                     port=port,
#                     status="OPEN",
#                     protocol=protocol.upper(),
#                     service_name=proc_name,
#                     port_name=self._get_common_name(port, protocol).upper(),
#                     pid=conn.pid
#                 )

#         unique_list = list(unique_ports_map.values())
#         if len(unique_list) >= limit:
#             return random.sample(unique_list, limit)
#         return unique_list

#     def display_report(self, ports: List[PortMetadata]):
#         header = f"{'PORT':<8} | {'PORTNAME':<15} | {'PROTOCOL':<10} | {'PID':<8} | {'PROCESS'}"
#         print("\n" + "="*80)
#         print(f"TARGET: {self.target_ip} | UNIQUE OPEN PORTS REPORT")
#         print("="*80)
#         print(header)
#         print("-" * 80)
#         for p in ports:
#             print(f"{p.port:<8} | {p.port_name:<15} | {p.protocol:<10} | {p.pid:<8} | {p.service_name}")
#         print("="*80 + "\n")
#         print(f"Total Unique Ports Found: {len(ports)}\n")

# if __name__ == "__main__":
#     target = "192.168.1.10" 
#     manager = ProPortManager(target_ip=target)
#     active_ports = manager.get_active_system_ports(limit=5)
    
#     if active_ports:
#         manager.display_report(active_ports)
#     else:
#         print(f"[-] No unique listening ports found.")

# ! --------------------- Other ( Prof Wirh Ping First )

# import socket
# import psutil
# import random
# import logging
# import subprocess
# import platform
# from typing import List, Optional
# from dataclasses import dataclass

# logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# @dataclass
# class PortMetadata:
#     port: int
#     status: str
#     protocol: str
#     service_name: str
#     port_name: str
#     pid: Optional[int] = None

# class ProPortManager:
    
#     def __init__(self, target_ip: str = '127.0.0.1', range_start: int = 1024, range_end: int = 65535):
#         self.target_ip = target_ip
#         self.range_start = range_start
#         self.range_end = range_end

#     def is_host_up(self) -> bool:

#         logging.info(f"Checking reachability for {self.target_ip}...")
        
#         param = '-n' if platform.system().lower() == 'windows' else '-c'
#         command = ['ping', param, '1', self.target_ip]
        
#         try:
#             exit_code = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
#             return exit_code == 0
#         except Exception as e:
#             logging.error(f"Error checking host: {e}")
#             return False

#     def _get_common_name(self, port: int, proto: str) -> str:
#         try:
#             return socket.getservbyport(port, proto.lower())
#         except (OSError, socket.error):
#             return "UNKNOWN"

#     def get_active_system_ports(self, limit: int = 5) -> List[PortMetadata]:

#         unique_ports_map = {}
#         try:
#             connections = psutil.net_connections(kind='inet4')
#         except psutil.AccessDenied:
#             logging.error("Access Denied! Run as Administrator/Root to see all processes.")
#             return []
        
#         for conn in connections:
#             if conn.status == psutil.CONN_LISTEN:
#                 port = conn.laddr.port
#                 if self.range_start <= port <= self.range_end and port not in unique_ports_map:
                    
#                     try:
#                         proc = psutil.Process(conn.pid)
#                         proc_name = proc.name()
#                     except (psutil.NoSuchProcess, psutil.AccessDenied):
#                         proc_name = "System/Protected"

#                     protocol = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"
                    
#                     unique_ports_map[port] = PortMetadata(
#                         port=port,
#                         status="OPEN",
#                         protocol=protocol,
#                         service_name=proc_name,
#                         port_name=self._get_common_name(port, protocol).upper(),
#                         pid=conn.pid
#                     )

#         unique_list = list(unique_ports_map.values())
#         if len(unique_list) >= limit:
#             return random.sample(unique_list, limit)
#         return unique_list

#     def display_report(self, ports: List[PortMetadata]):
#         header = f"{'PORT':<8} | {'PORTNAME':<15} | {'PROTOCOL':<10} | {'PID':<8} | {'PROCESS'}"
#         print("\n" + "="*85)
#         print(f"TARGET: {self.target_ip} | UNIQUE OPEN PORTS REPORT")
#         print("="*85)
#         print(header)
#         print("-" * 85)
#         for p in ports:
#             print(f"{p.port:<8} | {p.port_name:<15} | {p.protocol:<10} | {p.pid:<8} | {p.service_name}")
#         print("="*85 + "\n")
#         print(f"Summary: Found {len(ports)} unique active ports.\n")

# if __name__ == "__main__":
#     target = "127.0.0.1" 
#     manager = ProPortManager(target_ip=target)
    
#     if manager.is_host_up():
#         print(f"[+] {target} is UP and responding. Proceeding to scan...")
        
#         active_ports = manager.get_active_system_ports(limit=5)
        
#         if active_ports:
#             manager.display_report(active_ports)
#         else:
#             print(f"[-] No active listening ports found in the specified range.")
#     else:
#         print(f"[!] {target} is DOWN or blocking ICMP (Ping). Process terminated.")


# ! --------------------- Other (Prof -- Check if OPEN )

import socket
import psutil
import random
import logging
import subprocess
import platform
from typing import List, Optional
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

@dataclass
class PortMetadata:
    port: int
    status: str
    protocol: str
    service_name: str
    port_name: str
    pid: Optional[int] = None

class ProPortManager:
    
    def __init__(self, target_ip: str = '127.0.0.1', range_start: int = 1024, range_end: int = 65535):
        self.target_ip = target_ip
        self.range_start = range_start
        self.range_end = range_end

    def is_host_up(self) -> bool:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', self.target_ip]
        try:
            return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0
        except Exception: return False

    def check_port_status(self, port: int) -> str:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((self.target_ip, port))
            return "OPEN" if result == 0 else "CLOSED"

    def _get_common_name(self, port: int, proto: str) -> str:
        try: return socket.getservbyport(port, proto.lower())
        except: return "UNKNOWN"

    def get_only_open_ports(self, limit: int = 5) -> List[PortMetadata]:
        open_ports = []
        
        try:
            connections = psutil.net_connections(kind='inet4')
            
            potential_ports = [
                c for c in connections 
                if c.status == psutil.CONN_LISTEN and self.range_start <= c.laddr.port <= self.range_end
            ]

            random.shuffle(potential_ports)

            for conn in potential_ports:
                port = conn.laddr.port
                status = self.check_port_status(port)
                
                if status == "OPEN":
                    try:
                        proc = psutil.Process(conn.pid)
                        proc_name = proc.name()
                    except: proc_name = "System/Protected"

                    open_ports.append(PortMetadata(
                        port=port,
                        status="OPEN",
                        protocol="TCP",
                        service_name=proc_name,
                        port_name=self._get_common_name(port, "tcp").upper(),
                        pid=conn.pid
                    ))
                
                if len(open_ports) >= limit:
                    break
                    
        except Exception as e:
            logging.error(f"Error during scan: {e}")
            
        return open_ports

    def display_report(self, ports: List[PortMetadata]):
        header = f"{'PORT':<8} | {'STATUS':<11} | {'SERVICE':<15} | {'PROTOCOL':<8} | {'PROCESS'}"
        print("\n" + "="*85)
        print(f"TARGET: {self.target_ip} | FILTER: ONLY OPEN PORTS : {len(ports)}")
        print(f"RANGE: {self.range_start} - {self.range_end}")
        print("="*85)
        print(header)
        print("-" * 85)
        for p in ports:
            print(f"{p.port:<8} | {p.status:<8} ✅ | {p.port_name:<15} | {p.protocol:<8} | {p.service_name}")
        print("="*85 + "\n")

if __name__ == "__main__":
    target = input("Write Target IP > ")
    range_s = int(input("Wirte Start Range Port > "))
    range_e = int(input("Wirte End Range Port > "))
    print(f"\n[*] Scanning '{target}' From {range_s} T0 {range_e}...")
    manager = ProPortManager(target_ip=target, range_start=range_s, range_end=range_e)
    
    if manager.is_host_up():
        print(f"[+] Host {target} is UP. Searching for OPEN ports...")
        
        open_found = manager.get_only_open_ports(limit=5)
        
        if open_found:
            manager.display_report(open_found)
        else:
            print(f"[-] No OPEN ports found in range {manager.range_start}-{manager.range_end}.")
    else:
        print(f"[!] Host {target} is DOWN or unreachable. Check your network.")
