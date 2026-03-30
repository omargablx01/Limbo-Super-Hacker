
# t~ >>>>                                            Assignments  02[Port & Protocols]                                <<<<<
# ? --------------------------------- 1  ------------------------- 01_list_port.py

#!/usr/bin/python3

# import socket

# def my_port():

#     common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389,1.0,-1,99999999]

#     common_ports.sort(reverse=True)

#     print("\n"+" Common Ports and Services ".center(60,"-")+"\n")

#     print(f"Test Ports > {common_ports}\n")

#     for port in common_ports:
#         try:
#             service_name = socket.getservbyport(port)

#             print(f"{port} -> {service_name.upper()}")

#         except (socket.error, TypeError,OverflowError) as e:
#             print(f"{port} -> Unknown Service; {e}")

# my_port()

# ? --------------------------------- 2  ------------------------- 02_check_port_num.py

#!/usr/bin/python3

# import socket

# def valid_port(port_input):

#     try:
#         port = int(port_input)
        
#         socket.htons(port)
        
#         if 0 <= port <= 65535:

#             print(f"PORT ( {port} ) -> ( {socket.getservbyport(port).upper()} ) Success")

#             return True
#         else:
#             raise ValueError
        
#     except (socket.error, TypeError,OverflowError,ValueError) as e:

#         print(f"{port_input} -> Unknown Service; {e}")

# in_port = input("Write Port Num Like ( 80 ) > ")

# valid_port(in_port)

# !--------------- Other ( RUNING )

# import socket

# def valid_port():

#     try:
#         port = input("Write Port Num Like ( 80 ) > ")
        
#         service_name = socket.getservbyport(int(port))

#         print(f"PORT ( {port} ) -> ( {service_name.upper()} ) Success")

#     except (socket.error, TypeError,OverflowError,ValueError) as e:

#         print(f"{port} -> Unknown Service; {e}")

# valid_port()

# ? --------------------------------- 3  ------------------------- 03_scan1000.py
 
# #!/usr/bin/python3

# import socket

# class scaner_ports:

#     def scan_one(self,get_ip:str) :

#         my_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#         my_soc.settimeout(0.5)
            
#         input_port = int(input("Port Like 80 > "))

#         result = my_soc.connect_ex((get_ip,input_port))
#         try : 
#             if result == 0:
#                 print(f"[+] Port '{input_port}' _ '{socket.getservbyport(input_port)}' is OPEN")
#             else:
#                 print(f"Port '{input_port}' _ '{socket.getservbyport(input_port)}' is CLOSED")

#         except (socket.error, TypeError,OverflowError,ValueError) as e:

#             print(f"{input_port} -> Unknown Service; {e}")
                
#         my_soc.close()

#     def multi_scan(self,get_ip:str):
            
#         my_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#         my_soc.settimeout(0.5)

#         input_port = int(input("Port Like 80 > "))

#         result = my_soc.connect_ex((get_ip,input_port))
#         try : 
#             if result == 0:
#                 print(f"[+] Port '{input_port}' _ '{socket.getservbyport(input_port)}' is OPEN")
#             else:
#                 print(f"Port '{input_port}' _ '{socket.getservbyport(input_port)}' is CLOSED")
                
#         except (socket.error, TypeError,OverflowError,ValueError) as e:

#             print(f"{input_port} -> Unknown Service; {e}")
                
#         my_soc.close()

#         loop = True

#         while loop:
#             true = input("m,more => More\nquit,exit => Quit,Exit > ")

#             if true in ['m','more']:

#                 input_port = int(input("Port Like 80 > "))

#                 result = my_soc.connect_ex((get_ip,input_port))

#                 try : 
#                     if result == 0:
#                         print(f"[+] Port '{input_port}' _ '{socket.getservbyport(input_port)}' is OPEN")
#                     else:
#                         print(f"Port '{input_port}' _ '{socket.getservbyport(input_port)}' is CLOSED")
                
#                 except (socket.error, TypeError,OverflowError,ValueError) as e:

#                     print(f"{input_port} -> Unknown Service; {e}")
                
#                 my_soc.close()

#             elif true in ['quit','exit']:

#                 loop = False

#                 my_soc.close()

#                 print("Closed ..")

#             else :
#                 print("Bad Coice Try Again..!")

#     def scan_ports(self,ip:str):

#         start_port = int(input("Start Port > "))

#         end_port = int(input("End Port > "))
        
#         print(f"Start For IP '{ip}' From Port '{start_port}' To '{end_port}'...")
    
#         for port in range(start_port, end_port + 1):

#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#             s.settimeout(0.5)
            
#             result = s.connect_ex((ip, port))
            
#             if result == 0:
#                 print(f"[+] Port {port} Is (OPEN)")
#             else:
#                 print(f"[-] Port {port} Is (CLOSE)")

            
#             s.close()
        
# input_ip = input("IP > ")
# scan_port = scaner_ports()
# scan_port.scan_one(input_ip)
# scan_port.multi_scan(input_ip)
# scan_port.scan_ports(input_ip)

# ! -------------------------- Other
# import socket

# Use threading For Faster Scan ..
# import threading

# def scan_port(ip, port):

#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     s.settimeout(1)
    
#     result = s.connect_ex((ip, port))

#     try : 
#         if result == 0:
#             print(f"[+] Port '{port}' _ '{socket.getservbyport(port)}' is OPEN")

#         else:
#             print(f"[-] Port '{port}' _ '{socket.getservbyport(port)}' is CLOSED")
                
#     except (socket.error, TypeError,OverflowError,ValueError) as e:

#         pass

#     s.close()

# def fast_scan(target_ip, start_port, end_port):

#     print(f"Start For IP '{target_ip}' From Port '{start_port}' To '{end_port}'...")

#     threads = []
    
#     for port in range(start_port, end_port + 1):

        
#         t = threading.Thread(target=scan_port, args=(target_ip, port))

#         threads.append(t)

#         t.start()
        
#         if len(threads) > 100: 
#             for t in threads:
#                 t.join()
#             threads = []

# scan_port("10.10.11.143",443)

# target = "10.10.11.143"
# fast_scan(target, 1, 500)

# ! -------------------------- Other
# import socket

# def standard_scan(target_ip, start_port, end_port):

#     print(f"Starting Scan For IP '{target_ip}' From Port '{start_port}' To '{end_port}'...")

#     print("-" * 45)
    
#     for port in range(start_port, end_port + 1):

#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
#         s.settimeout(1.0)
        
#         result = s.connect_ex((target_ip, port))

#         try : 
#             if result == 0:
#                 print("\"" * 45)
#                 print(f"[+] Port '{port}' _ '{socket.getservbyport(port)}' is (OPEN)")
#                 print("\"" * 45)
#             else:
#                 print(f"[-] Port '{port}' _ '{socket.getservbyport(port)}' is (CLOSED)")
                
#         except (socket.error, TypeError,OverflowError,ValueError):

#             pass

#         s.close()

#     print("-" * 45)
#     print("Scan Completed ...")

# target = input("IP Target > ")
# start_port = int(input("Start Port > "))
# end_port = int(input("End Port > "))

# standard_scan(target, start_port, end_port)

# ! ----------------------- Other Prof With Speed

# import socket
# import threading
# from queue import Queue

# target = input("IP Target > ")
# start_p = int(input("Start P0RT > "))
# end_p = int(input("End P0RT > "))
# thread_c = int(input("Thread Count > "))
# time_out = float(input("Time Out > "))

# queue = Queue()
# open_ports = []

# def port_scan(port):

#     try:
#         soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         soc.settimeout(1.0)
        
#         result = soc.connect_ex((target, port))
#         if result == 0:
#             open_ports.append(port)
#             print(f"[+] Port {port} , '{socket.getservbyport(port).upper()}' is OPEN")
#             print("\""*45)
#         soc.close()
#     except:
#         pass

# def worker():

#     while not queue.empty():
#         port = queue.get()
#         port_scan(port)
#         queue.task_done()

# def run_fast_scan(start_port=1, end_port=1024, thread_count=100,time=1.5):

#     print(f"Starting Fast Scan on {target} From P0RT '{start_port}' T0 '{end_port}' Time Out '{time}' (Threads: {thread_count})...")
#     print("-"*45)
    
#     for port in range(start_port, end_port + 1):
#         queue.put(port)

#     thread_list = []

#     for _ in range(thread_count):
#         t = threading.Thread(target=worker)

#         thread_list.append(t)

#         t.start()

#     for t in thread_list:
#         t.join()

#     print("-" * 45)
#     print(f"Scan Finished. Open Ports Found: {sorted(open_ports)}")

# run_fast_scan(start_p,end_p,thread_c,time_out)

# ! ------------------------ Other Prof With Standard

# import socket

# target = input("IP Target > ")
# start_p = int(input("Start PORT > "))
# end_p = int(input("End PORT > "))
# time_out = float(input("Time Out (e.g., 1.0) > "))

# open_ports = []

# def run_standard_scan(start_port, end_port, timeout):
#     print(f"\nStarting Standard Scan on {target}")

#     print(f"Range: {start_port} TO {end_port} | Timeout: {timeout}s")

#     print("-" * 45)
    
#     for port in range(start_port, end_port + 1):
#         try:
#             soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#             soc.settimeout(timeout)
            
#             result = soc.connect_ex((target, port))
            
#             if result == 0:
#                 open_ports.append(port)

#                 try:
#                     service = socket.getservbyport(port).upper()

#                 except:
#                     service = "UNKNOWN SERVICE"
                
#                 print(f"[+] Port '{port}' [{service}] is OPEN")
#                 print('"' * 45)
            
#             soc.close()
            
#         except KeyboardInterrupt:
#             print("\n[!] Scan stopped by user.")
#             break
#         except socket.error:
#             pass

#     print("-" * 45)
#     print(f"Scan Finished. Open Ports Found: {sorted(open_ports)}")

# run_standard_scan(start_p, end_p, time_out)

# ! -------------------------- Other 

# import socket
# import platform
# import subprocess

# def is_alive(ip):

#     param = '-n' if platform.system().lower() == 'windows' else '-c'
#     command = ['ping', param, '1', '-w', '1000', ip]
    
#     print(f"[*] Checking if {ip} is online...")
    
#     response = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
#     return response.returncode == 0

# def run_standard_scan(target, start_port, end_port, timeout):
#     if not is_alive(target):
#         print(f"[!] Target {target} seems to be DOWN or Unreachable.")
#         print("[!] Scan aborted.")
#         return

#     print(f"\n[+] Target {target} is UP! Starting scan...")
#     print("-" * 45)
    
#     open_ports = []
    
#     for port in range(start_port, end_port + 1):
#         try:
#             soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             soc.settimeout(timeout)
            
#             result = soc.connect_ex((target, port))
            
#             if result == 0:
#                 open_ports.append(port)
#                 try:
#                     service = socket.getservbyport(port).upper()
#                 except:
#                     service = "UNKNOWN"
                
#                 print(f"[+] Port {port} [{service}] is OPEN")
            
#             soc.close()
            
#         except KeyboardInterrupt:
#             print("\n[!] Scan stopped by user.")
#             break

#     print("-" * 45)
#     print(f"Scan Finished. Open Ports Found: {sorted(open_ports)}")

# target_ip = input("IP Target > ")
# start_p = int(input("Start PORT > "))
# end_p = int(input("End PORT > "))
# time_out = float(input("Time Out (e.g., 1.0) > "))

# run_standard_scan(target_ip, start_p, end_p, time_out)

# ! -------------- CHeck IP & PING & Network & Scan With OUT MASK ( Prof )

# import socket
# import platform
# import subprocess
# import ipaddress

# def get_local_ip():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     try:
#         s.connect(('8.8.8.8', 1))
#         ip = s.getsockname()[0]
#     except:
#         ip = '127.0.0.1'
#     finally:
#         s.close()
#     return ip

# def is_valid_ip(ip_str):
#     try:
#         ipaddress.ip_address(ip_str)
#         return True
#     except ValueError:
#         return False

# def check_network_relation(target_ip):
#     local_ip = get_local_ip()
#     print(f"[*] Your Local IP: {local_ip}")
    
#     try:
#         local_net = ipaddress.ip_network(f"{local_ip}/24", strict=False)
#         target_addr = ipaddress.ip_address(target_ip)
        
#         if target_addr in local_net:
#             print(f"[✓] Target '{target_ip}' is in your Local Network.")
#         else:
#             print(f"[!] Target '{target_ip}' is OUTSIDE your local network.")
#     except Exception as e:
#         print(f"[!] Network Analysis Error: {e}")

# def is_alive(ip):
#     param = '-n' if platform.system().lower() == 'windows' else '-c'
#     wait_param = '-w' if platform.system().lower() == 'windows' else '-W'
#     command = ['ping', param, '1', wait_param, '1000', ip]
    
#     print(f"[*] Pinging {ip} to check status...")
#     response = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#     return response.returncode == 0

# def professional_scanner():
#     print("="*45)
#     print("    PROFESSIONAL NETWORK & PORT SCANNER    ")
#     print("="*45)
    
#     while True:
#         target = input("IP Target > ").strip()
#         if is_valid_ip(target):
#             break
#         print("[!] Invalid IP Address Format. Please Try Again (e.g., 192.168.1.1)")

#     check_network_relation(target)
#     print("-" * 45)
    
#     if not is_alive(target):
#         print(f"[!] '{target}' is DOWN or blocking Ping. Aborting for safety.")

#         # إذا أردت الاستمرار رغم ذلك، يمكنك إزالة return
#         return

#     try:
#         print(f"[+] '{target}' is UP! Preparing to scan...")
#         start_p = int(input("Start PORT (0-65535) > "))
#         end_p = int(input("End PORT (0-65535) > "))
        
#         if not (0 <= start_p <= 65535 and 0 <= end_p <= 65535):
#             print("[!] Port numbers must be between 0 and 65535.")
#             return
            
#         time_out = float(input("Time Out (e.g. 1.5) > "))
#     except ValueError:
#         print("[!] Please enter valid numbers for ports and timeout.")
#         return
    
#     print(f"\n[*] Scanning '{target}' From {start_p} T0 {end_p} ...")
#     print("-" * 45)
    
#     open_ports = []

#     for port in range(start_p, end_p + 1):
#         try:
#             priv_status = "Privileged" if port < 1024 else "Registered/Dynamic"
            
#             soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             soc.settimeout(time_out)
            
#             result = soc.connect_ex((target, port))
            
#             if result == 0:
#                 open_ports.append(port)
#                 try:
#                     service = socket.getservbyport(port).upper()
#                 except:
#                     service = "UNKNOWN SERVICE"
                
#                 print(f"[+] Port | {port} | [{service}] is OPEN ({priv_status})")
            
#             soc.close()
            
#         except KeyboardInterrupt:
#             print("\n[!] User interrupted the scan.")
#             break
#         except Exception:
#             pass

#     print("-" * 45)
#     print(f"Scan Results: {len(open_ports)} ports open.")
#     if open_ports:
#         print(f"Open Ports List: {sorted(open_ports)}")
#     print("=" * 45)

# if __name__ == "__main__":
#     professional_scanner()

# ! -------------- CHeck IP & PING & Network & Scan With MASK ( Prof RUNING ) 

# import socket
# import platform
# import subprocess
# import ipaddress

# def get_local_ip():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     try:
#         s.connect(('8.8.8.8', 1))
#         ip = s.getsockname()[0]
#     except:
#         ip = '127.0.0.1'
#     finally:
#         s.close()
#     return ip

# def is_valid_network(net_str):
#     try:
#         ipaddress.ip_network(net_str, strict=False)
#         return True
#     except ValueError:
#         return False

# def check_network_relation(target_with_mask):
#     local_ip = get_local_ip()
#     print(f"[*] Your Local IP: {local_ip}")
    
#     try:
#         target_ip = target_with_mask.split('/')[0]
        
#         network = ipaddress.ip_network(target_with_mask, strict=False)
        
#         local_addr = ipaddress.ip_address(local_ip)
#         target_addr = ipaddress.ip_address(target_ip)
        
#         print(f"[*] Target IP To Scan: {target_ip}")
#         print(f"[*] Network Scope: {network}")
        
#         if target_addr in network:
#             print(f"[✓] Target Is INSIDE Your Local Network SC0PE.")
#         else:
#             print(f"[!] Target Is OUTSIDE Your Local Network SC0PE.")
            
#         return target_ip
#     except Exception as e:
#         print(f"[!] Network Analysis Error: {e}")
#         return None

# def is_alive(ip):
#     param = '-n' if platform.system().lower() == 'windows' else '-c'
#     wait_param = '-w' if platform.system().lower() == 'windows' else '-W'
#     command = ['ping', param, '1', wait_param, '1000', ip]
    
#     print(f"[*] Pinging {ip} To Check STATUS...")
#     response = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#     return response.returncode == 0

# def professional_scanner():
#     print("="*60)
#     print("    PROFESSIONAL NETWORK & PORT SCANNER (MASK SUPPORT)    ")
#     print("="*60)
    
#     while True:
#         target_input = input("Target (IP/Mask) > ").strip()
#         if is_valid_network(target_input):
#             break
#         print(f"[!] Invalid Format. Use CIDR Notation (e.g., {get_local_ip()}/24)")

#     target_ip = check_network_relation(target_input)
#     if not target_ip: return
    
#     print("-" * 60)
    
#     if not is_alive(target_ip):
#         print(f"[!] '{target_ip}' Is DOWN 0R Blocking Ping. Aborting For Safety.")
#         return

#     try:
#         print(f"[+] '{target_ip}' Is UP! Preparing To Scan...")
#         start_p = int(input("Start PORT (0-65535) > "))
#         end_p = int(input("End PORT (0-65535) > "))
        
#         if not (0 <= start_p <= 65535 and 0 <= end_p <= 65535):
#             print("[!] Port Numbers Must Be Between 0 And 65535.")
#             return
            
#         time_out = float(input("Time Out (e.g. 1.5) > "))
#     except ValueError:
#         print("[!] Please Enter Valid Numbers For Ports And Timeout.")
#         return
    
#     print(f"\n[*] Scanning '{target_ip}' From {start_p} T0 {end_p}...")
#     print("-" * 60)
    
#     open_ports = []

#     for port in range(start_p, end_p + 1):
#         try:
#             priv_status = "Privileged" if port < 1024 else "Registered"
            
#             soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             soc.settimeout(time_out)
            
#             result = soc.connect_ex((target_ip, port))
            
#             if result == 0:
#                 open_ports.append(port)
#                 try:
#                     service = socket.getservbyport(port).upper()
#                 except:
#                     service = "UNKNOWN"
                
#                 print(f"[+] Port | {port:<5} | {service:<15} | {priv_status}")
            
#             soc.close()
            
#         except KeyboardInterrupt:
#             print("\n[!] User Interrupted The Scan.")
#             break
#         except Exception:
#             pass

#     print("-" * 60)
#     print(f"Scan Results: {len(open_ports)} Ports 0PEN.")
#     if open_ports:
#         print(f"Open Ports List: {sorted(open_ports)}")
#     print("=" * 60)

# if __name__ == "__main__":
#     professional_scanner()
# ? --------------------------------- 4  ------------------------- 04_tcp_udp.py
#!/usr/bin/python3

# import socket
# import psutil
# from colorama import Fore, Style, init

# init(autoreset=True)

# def get_process_name(pid):
#     try:
#         return psutil.Process(pid).name()
#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         return "N/A"

# w_proto, w_port, w_ip, w_pid, w_name, w_status = 10, 10, 18, 8, 15, 15

# data_list = []
# connections = psutil.net_connections(kind='inet4')

# for conn in connections:
#     local_ip = conn.laddr.ip
#     if local_ip not in ["0.0.0.0", "127.0.0.1"]:
#         protocol = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"
#         local_port = conn.laddr.port
#         pid = conn.pid if conn.pid else 0
#         p_name = get_process_name(pid) if pid else "System"
#         status = conn.status if conn.status else "N/A"
        
#         data_list.append({
#             "proto": protocol,
#             "port": local_port,
#             "ip": local_ip,
#             "pid": pid,
#             "name": p_name,
#             "status": status
#         })
# data_list.sort(key=lambda x: (x['proto'], x['port']), reverse=True)

# header = (
#     f"{'PROTOCOL'.center(w_proto)} | {'PORT'.center(w_port)} | "
#     f"{'LOCAL IP'.center(w_ip)} | {'PID'.center(w_pid)} | "
#     f"{'PROCESS'.center(w_name)} | {'STATUS'.center(w_status)}"
# )
# print(Fore.RED  + Style.BRIGHT + header)
# print(Fore.WHITE + "=" * len(header))

# for item in data_list:
#     color = Fore.CYAN if item['proto'] == "UDP" else Fore.GREEN
    
#     row = (
#         f"{item['proto'].center(w_proto)} | "
#         f"{str(item['port']).center(w_port)} | "
#         f"{item['ip'].center(w_ip)} | "
#         f"{str(item['pid']).center(w_pid)} | "
#         f"{item['name'][:14].center(w_name)} | "
#         f"{item['status'].center(w_status)}"
#     )
#     print(color + row)
    