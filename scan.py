import nmap
print("-------------------------------------------")
print("Projet de Paul Mascarilla et Mathis Jeannot")
print("-------------------------------------------")
nm = nmap.PortScanner()
host = input("Entrez l'adresse IP de la machine cible : ")
##nm.scan(val)

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))