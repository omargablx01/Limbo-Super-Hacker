
import socket

# def privileged(port:int):
#     try :
#         if port in range(0, 1024):
#             print(f"{port} => {socket.getservbyport(port).upper()}")
#     except (socket.error,OSError) as e :
#         print(f"Error ; '{port}' {e}")

# input_port = int(input("Write Port > "))
# privileged(input_port)

# ! ------------------ Other
import socket

def privileged_range(port: int):
    start_range = 0

    end_range = 1023

    if start_range <= port <= end_range:
        try:
            service = socket.getservbyport(port).upper()
            return f"Port '{port}' Is PRIVILEGED. Service: {service}"
        
        except (socket.error,OSError,TypeError) as e:
            return f"Port '{port}' Is PRIVILEGED. (Service Unknown) {str(e).upper()}."
        
    else:
        return f"Port '{port}' Is N0T In The Privileged Range {start_range}-{end_range}."

try :
    input_port = int(input("Write Port > "))
    print(privileged_range(input_port))

except ValueError:
    print("Error: Please Enter A Valid Numeric Port Number.")