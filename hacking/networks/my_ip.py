import socket
import nmap


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

# np = nmap.PortScanner()
# np.scan('127.0.0.1')
# print(np['127.0.0.1'].all_protocols())


