import os
import ipaddress
#host = str(input("Entrez l'adresse IPv4 cible : "))
host = '192.168.1.254'
def check_ip_address(ip_string):
    try:
        ipaddress.ip_address(ip_string)
        print("Adresse IP valide, poursuite du scan")
        return True
    except ValueError:
        print("Adresse IP non valide, format en 192.168.1.1. Veuillez ressaisir ! ")
        return False

if True :
    os.system('nmap -T4 -F ' + host + '>> res.txt')
    with open('res.txt', 'r') as file:
        print(file.read())
else:
    check_ip_address(host)