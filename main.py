import MODULES.ScanPort as ScanPort

network2scan = "127.0.0.1/32"
scan = ScanPort.Nmap(network2scan)
