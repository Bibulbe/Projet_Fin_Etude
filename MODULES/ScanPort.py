import nmap

print('------------------------------------')
print('* Mathis JEANNOT & Paul MASCARILLA *')
print('------------------------------------')


def Nmap(ip):
    ip = str(ip)
    nm = nmap.PortScanner()
    print("Début du scan NMAP, Veuillez patienter")
    nm.scan(ip)
    return nm
def afficheNmap(nm):
    for host in nm.all_hosts():
        displayInfo = f"Hôte : {host} {nm[host].hostname()}\n"
        displayInfo += f"Status : {nm[host].state()}\n"
        for protocol in nm[host].all_protocols():
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

if __name__ == "__Main__":
    cible = str(input("Entrez l'adresse IPv4 cible : "))
    print(afficheNmap(Nmap(cible)))
