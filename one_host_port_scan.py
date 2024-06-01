import socket

#get input from user to define target

ip_target = input("enter target ip address: ")

#define a function to scan one port

def is_port_open(ip_target, port):

    # creates a new socket
    s = socket.socket()
    try:
        # tries to connect to host using that port
        s.connect((ip_target, port))
        # timeout is 1 second; adjust as needed depending on latency
        s.settimeout(1)
    except:
        # cannot connect, port is closed
        return False
    else:
        # the connection was established, port is open!
        return True

# iterate over ports, from 1 to 1024

for port in range(1, 1025):
    if is_port_open(ip_target, port):
        print(ip_target, ":", port, " is open \n")
    else:
        print(ip_target, ":", port, " is closed \n")

if __name__ == "__main__":
    main()
