import nmap
print("-------------------------------------------")
print("Projet de Paul Mascarilla et Mathis Jeannot")
print("-------------------------------------------")
nm = nmap.PortScanner()
val = input("Entrez l'adresse IP de la machine cible : ")
nm.scan(val)
