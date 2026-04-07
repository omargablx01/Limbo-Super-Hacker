import socket

def tcp_ports_scan():
    target_ip = input("Write Target IP > ")
    start_port = int(input("Write Start Port > "))
    end_port = int(input("Write End Port > "))
    
    prin = f"--- Starting UDP Scan Range {start_port} -> {end_port} on {target_ip} ---\n"

    print(prin,"×" * len(prin))
    
    for port in range(start_port, end_port + 1):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(1.0)

        try:
            service = socket.getservbyport(port)
        except :
            service = "Unknown"

        try:
            result = soc.connect_ex((target_ip, port))

            if result == 0:
                print(f"[+] Port {port:5} | Service: {service.upper():<12} is (OPEN)")
                print("=" * 50)
            else:
                print(f"[-] Port {port:5} | Service: {service:<12} is (CLOSED)")
                
        except Exception as e:
            print(f"[!] Error on port {port}: {e}")
        finally:
            soc.close()
            
    print("\n--- TCP Scan Completed ---")

tcp_ports_scan()