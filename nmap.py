import re
import shlex, subprocess

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


file_csv='res.csv'
with open(file_csv, 'w') as file:
    file.write("port;protocol;status;type\n")

if check_ipaddress(host) :
    command_line = 'nmap -T4 -F ' + host
    args = shlex.split(command_line)
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    result = {}

    for line in iter(proc.stdout.readline,''):
        a=line.rstrip()
        if(len(a) > 0):
            if(a[0].isdigit()):
                r=re.match('(\d*)\/(tcp|udp)\s*(open|closed|filtered)\s*(\w*)', a)
                port=r.group(1)
                protocol=r.group(2)
                status=r.group(3)
                type=r.group(4)
                result = {
                    "port": port,
                    "protocol": protocol,
                    "status": status,
                    "type": type,
                }
                print(result)
                csv="%s;%s;%s;%s;\n" % (port, protocol, status, type)
                with open(file_csv, 'a') as file:
                    file.write(csv)

else:
    print('Adresse IP non valide')