import socket

print("Welcome, this is a simple port scanning tool")
print("<----------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)

def scan_port(ip_addr, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip_addr, port))
    s.close()
    return result == 0

def portScanner(ip_addr, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(ip_addr, port):
            open_ports.append(port)
    return open_ports

start_port = int(input("Please enter the start port of the range you want to scan: "))
end_port = int(input("Please enter the end port of the range you want to scan: "))

open_ports = portScanner(ip_addr, start_port, end_port)

if open_ports:
    print("Open ports:", open_ports)
else:
    print("No open ports found in the specified range")

