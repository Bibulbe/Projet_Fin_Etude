import nmap
print('------------------------------------')
print('* Mathis JEANNOT & Paul MASCARILLA *')
print('------------------------------------')
def Nmap(ip):
    ip = str(ip)
    nm = nmap.PortScanner()
    print("NMAP Scan starting")
    nm.scan(ip)
    for host in nm.all_hosts():
        displayInfo = f"Host: {host} {nm[host].hostname()}\n"
        displayInfo += f"State: {nm[host].state()}\n"
        for protocol in nm[host].all_protocols():
            displayInfo += "---------------------\n"
            displayInfo += "PORT\t\tSTATE\t\tPRODUCT\t\tVERSION\n"
            lport = nm[host][protocol].keys()
            for port in lport:
                if len(str(port) + str("/") + str(protocol)) < 8:
                    space = "\t\t"
                else:
                    space = "\t"
                product = nm[host][protocol][port]['product']
                version = nm[host][protocol][port]['version']
                state = nm[host][protocol][port]['state']
                displayInfo += f"{port}/{protocol}{space}{state}\t\t{product}\t\t{version}\n"
    return displayInfo
cible = str(input("Entrez l'adresse IPv4 cible : "))
print(Nmap(cible))