import MODULES.ScanPort

network2scan = "127.0.0.1/32"
print(ScanPort.afficheNmap(ScanPort.Nmap(network2scan)))
