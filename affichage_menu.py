def displayMenu():
    displayInfo = """\n
    | 1 | Scanning
    | 2 | Exploit
    | 3 | --------
    | 666 | Quit
    """

    print(displayInfo)

def ScanMenu():
    displayInfo = """
  | 1 | Scanning
        a - Nmap classic
        b - Nmap silent
  """
    print(displayInfo)

def ExploitMenu():
    displayInfo = """
  | 2 | Exploit
        a - Recherche de vulnerabilite sur un service
  """
    print(displayInfo)