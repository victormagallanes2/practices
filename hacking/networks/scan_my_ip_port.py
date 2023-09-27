import nmap


# Escanear un rango de puertos de una ip especifica
host = '127.0.0.1'
np = nmap.PortScanner()
np.scan(host, '22-8000')
print(np['127.0.0.1'].all_tcp())