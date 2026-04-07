# import socket

# def udp_ports_scan():
#     target_ip = input("Write Target IP > ")
#     start_port = int(input("Write Start Port > "))
#     end_port = int(input("Write End Port > "))
    
#     prin = f"Scanning Range {start_port} -> {end_port} on {target_ip}"
#     print(prin)
#     print("×" * len(prin))
    
#     for port in range(start_port, end_port + 1):
#         soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         soc.settimeout(0.5)

#         try:
#             service = socket.getservbyport(port)
#         except:
#             service = "Unknown"

#         try:
#             result = soc.connect_ex((target_ip, port))

#             if result == 0:
#                 print(f"[+] Port {port:5} | Service: {service.upper():<12} is (OPEN)")
#                 print("=" * 50)
#             else:
#                 print(f"[-] Port {port:5} | Service: {service:<12} is (CLOSED)")
                
#         except Exception as e:
#             print(f"[!] Error on port {port}: {e}")
#         finally:
#             soc.close()
            
#     print("\n--- UDP Scan Completed ---")

# udp_ports_scan()

# ! --------------- Other ( RUNING )

import socket

def udp_ports_scan():
    target_ip = input("Write Target IP > ")
    start_port = int(input("Write Start Port > "))
    end_port = int(input("Write End Port > "))
    
    prin = f"--- Starting UDP Scan Range {start_port} -> {end_port} on {target_ip} ---\n"

    print(prin,"×" * len(prin))
    
    for port in range(start_port, end_port + 1):
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soc.settimeout(1.5)
        
        try:
            soc.sendto(b"", (target_ip, port))
            
            data, _ = soc.recvfrom(1024)
            print(f"[+] Port {port:5}: OPEN (Received Response)")
            
        except socket.timeout:
            print(f"[?] Port {port:5}: OPEN | FILTERED (No Response)")
            
        except socket.error as e:
            print(f"[-] Port {port:5}: CLOSED ")
            
        finally:
            soc.close()

    print("--- UDP Scan Completed ---")

udp_ports_scan()