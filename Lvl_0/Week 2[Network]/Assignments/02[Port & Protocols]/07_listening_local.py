
import psutil

print(f"{'IP Address':<12} | {'Port':<6} | {'Status'}")
print("×" * 35)

for conn in psutil.net_connections(kind="inet4"):
    if conn.status == "LISTEN" and conn.laddr.ip == "127.0.0.1":
        print(f"{conn.laddr.ip:<12} | {conn.laddr.port:<6} | {conn.status}")