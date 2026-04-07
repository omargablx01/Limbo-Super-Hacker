
# import socket

# def scan_hacker_targets():
#     vulnerable_ports = {
#         21: "FTP",
#         22: "SSH",
#         23: "Telnet",
#         25: "SMTP",
#         53: "DNS",
#         80: "HTTP",
#         110: "POP3",
#         139: "NetBIOS",
#         443: "HTTPS",
#         445: "SMB"
#     }

#     target_ip = "127.0.0.1"
#     print(f"{'PORT':<8} | {'SERVICE':<20} | {'STATUS'}")
#     print("-" * 45)

#     for port,service in vulnerable_ports.items():
#         soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         soc.settimeout(0.5)
        
#         result = soc.connect_ex((target_ip, port))
        
#         status = "OPEN" if result == 0 else "CLOSED"
        
#         print(f"{port:<8} | {service:<20} | {status}")
        
#         soc.close()

# scan_hacker_targets()

# ! ---------------- Other ( Speed Scan RUNING )

import socket
import threading

def scan_port(ip, port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.settimeout(1.0)
    try:
        result = soc.connect_ex((ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"[+] Port {port:5} is OPEN   | Service: {service.upper()}")
    except:
        pass
    finally:
        soc.close()

def fast_scanner():
    target = "127.0.0.1"
    print(f"--- Fast Scanning {target} (Ports 1-1023) ---")
    
    threads = []
    for port in range(1, 1024):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()

    print("--- Fast Scan Completed ---")

if __name__ == "__main__":
    fast_scanner()