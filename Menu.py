from simple_term_menu import TerminalMenu
import sys
from MODULES.ScanPort import Nmap_silent
from MODULES.ScanPort import Nmap_classic
from MODULES.searchsploitCli import exploitdbSearch

def scan_submenu():
    print("Scanning")
    print("1-Scan classic")
    print("2-Scan silencieux")
    print("3-Retour au menu principal")
    choice = input("Choisissez une option : ")
    if choice == "1":
        print("Scan réseau local en cours...")
        target = str(input(">>> Entrez l'IP cible\n>>> "))
        resultat, versions_all = Nmap_classic(target)
        print(resultat)
        for product, version in versions_all.items():
            if product is not None and version is not None:
                exploit = exploitdbSearch(product + " " + version)
                print(exploit)
            else:
                print("Version ou service non trouvé par le scan ")
    elif choice == "2":
        target = str(input(">>> Entrez l'IP cible\n>>> "))
        print(Nmap_silent(target))
    elif choice == "3":
        main_menu()
    else:
        print("Option non valide, veuillez réessayer.")
        scan_submenu()

def exploit_submenu():
    print("Exploit")
    print("1-Exploit vulnérabilité 1")
    print("2-Exploit vulnérabilité 2")
    print("3-Retour au menu principal")
    choice = input("Choisissez une option : ")
    if choice == "1":
        print("Exploitation de la vulnérabilité 1 en cours...")
    elif choice == "2":
        print("Exploitation de la vulnérabilité 2 en cours...")
    elif choice == "3":
        main_menu()
    else:
        print("Option non valide, veuillez réessayer.")
        exploit_submenu()

def main_menu():
    print("Menu principal")
    print("1-Scanning")
    print("2-Exploit")
    print("5-Quit")
    choice = input("Choisissez une option : ")
    if choice == "1":
        scan_submenu()
    elif choice == "2":
        exploit_submenu()
    elif choice == "5":
        sys.exit()
    else:
        print("Option non valide, veuillez réessayer.")
        main_menu()

main_menu()
