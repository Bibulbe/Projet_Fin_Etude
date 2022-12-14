import nmap
def Nmap_classic(target):
    print("Début du scan NMAP, Veuillez patienter")
    target = str(target)
    nm = nmap.PortScanner()
    resultat = ""
    versions_all = {}  # Création de la liste qui va stocker les versions
    nm.scan(target)
    for host in nm.all_hosts():
        resultat += f"Host: {host} {nm[host].hostname()}\n"
        resultat += f"State: {nm[host].state()}\n"
        for proto in nm[host].all_protocols():
            resultat += f"PORT\t\tSTATE\t\tPRODUCT\t\tVERSION\n"
            lport = nm[host][proto].keys()
            for port in lport:
                if len(str(port) + str("/") + str(proto)) < 8:
                    space = "\t\t"
                else:
                    space = "\t"
                product = nm[host][proto][port]['product']
                version = nm[host][proto][port]['version']
                state = nm[host][proto][port]['state']
                resultat += f"{port}/{proto}{space}{state}\t\t{product}\t\t{version}\n"
                versions_all[product] = version
    return resultat, versions_all
def Nmap_silent(target):
    print("Début du scan NMAP silencieux, Veuillez patienter")
    target = str(target)
    nm = nmap.PortScanner()
    resultat = ""
    nm.scan(target, arguments='-sS')
    for host in nm.all_hosts():
        resultat += f"Host: {host} {nm[host].hostname()}\n"
        resultat += f"State: {nm[host].state()}\n"
        for proto in nm[host].all_protocols():
            resultat += f"-------------------\n"
            resultat += f"PORT\t\tSTATE\n"
            lport = nm[host][proto].keys()
            for port in lport:
                if len(str(port) + str("/") + str(proto)) < 8:
                    space = "\t\t"
                else:
                    space = "\t"
                state = nm[host][proto][port]['state']
                resultat += f"{port}/{proto}{space}{state}\n"
            resultat += f"-------------------\n"
    return resultat
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
#print(Nmap_classic('192.168.1.94'))