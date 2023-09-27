import nmap


# Escanear un segmento de red
np = nmap.PortScanner()
np.scan(hosts='192.168.0.0-255', arguments='-sP')
print(np.all_hosts())


