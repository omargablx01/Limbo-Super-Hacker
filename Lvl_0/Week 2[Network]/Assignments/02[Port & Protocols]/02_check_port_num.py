
#!/usr/bin/python3

import socket

def valid_port(port_input):

    try:
        port = int(port_input)
        
        socket.htons(port)
        
        if 0 <= port <= 65535:

            print(f"PORT ( {port} ) -> ( {socket.getservbyport(port).upper()} ) Success")

            return True
        else:
            raise ValueError
        
    except (socket.error, TypeError,OverflowError,ValueError) as e:

        print(f"{port_input} -> Unknown Service; {e}")

in_port = input("Write Port Num Like 80 > ")

valid_port(in_port)