from simple_term_menu import TerminalMenu
import sys

def scan_submenu():
    print("Sous-menu Scanning")
    print("1-Scan réseau local")
    print("2-Scan IP ciblée")
    print("3-Retour au menu principal")
    choice = input("Choisissez une option : ")
    if choice == "1":
        print("Scan réseau local en cours...")
    elif choice == "2":
        target_ip = input("Entrez l'adresse IP ciblée : ")
        print("Scan de l'IP ciblée", target_ip, "en cours...")
    elif choice == "3":
        main_menu()
    else:
        print("Option non valide, veuillez réessayer.")
        scan_submenu()

def exploit_submenu():
    print("Sous-menu Exploit")
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
