#!/usr/bin/python3
ports_services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    443: "HTTPS",
    445: "SMB",
}
input_port = int(input("Write Port > "))
print("-"*40)
def get_service_name(port_number):
    service = ports_services.get(port_number, "Service Not Found")
    return service

service_name = get_service_name(input_port)
print(f"Port {input_port} Service Is : {service_name}")
