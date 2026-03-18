
#!/usr/bin/python3

# import socket

# common_ports = {
#     20: "FTP (Data Transfer)",
#     21: "FTP (Control)",
#     22: "SSH (Secure Shell)",
#     23: "Telnet",
#     25: "SMTP (Simple Mail Transfer Protocol)",
#     53: "DNS (Domain Name System)",
#     80: "HTTP (Hypertext Transfer Protocol)",
#     110: "POP3 (Post Office Protocol v3)",
#     143: "IMAP (Internet Message Access Protocol)",
#     443: "HTTPS (Hypertext Transfer Protocol Secure)",
# }

# print("--- Common Ports and Services (Fetched via Socket) ---")

# for key,value in common_ports.items():
#     print(f"{key} > {socket.getservbyport(key)}")

#  -------------- Other 

import socket

def my_port():

    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389,1.0,-1]

    common_ports.sort()

    print("--- Common Ports and Services (Fetched via Socket) ---")

    for port in common_ports:
        try:
            service_name = socket.getservbyport(port)

            print(f"{port} -> {service_name.upper()}")

        except (socket.error, TypeError,OverflowError) as e:
            print(f"{port} -> Unknown Service; {e}")

my_port()