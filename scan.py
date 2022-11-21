import os
import ipaddress
host = str(input("Entrez l'adresse IPv4 cible : "))
def check_ip_address(ip_string):
    try:
        ipaddress.ip_address(ip_string)
        print("Adresse IP valide, poursuite du scan")
        nm = os.system('nmap -T4 -F ' + host)
        print(nm)
        return True
    except ValueError:
        print("Adresse IP non valide, format en 192.168.1.1. Veuillez ressaisir ! ")
        return False
check_ip_address(host)

