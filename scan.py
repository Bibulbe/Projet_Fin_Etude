import os
#host = str(input("Entrez l'adresse IPv4 cible : "))
host = '192.168.1.254'
def check_ipaddress(host):
    parts = host.split(".")
    if len(parts) != 4:
        print("L'adresse IP {} n'est pas valide".format(host))
        return False
    for part in parts:
        if not isinstance(int(part), int):
            print("L'adresse IP {} n'est pas valide".format(host))
            return False
        if int(part) < 0 or int(part) > 255:
            print("L'adresse IP {} n'est pas valide".format(host))
            return False
    print("L'adresse IP {} est valide".format(host))
    return True
ip = check_ipaddress(host)
if ip is True:
    os.system('nmap -T4 -F ' + host + '> res.txt')
file = open('res.txt', "r")
lines = file.readlines()
file.close()
print(lines[5:9999])
