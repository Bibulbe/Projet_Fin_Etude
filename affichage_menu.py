def displayMenu():
    displayInfo = """\n
    | 1 | Scanning
    | 2 | Exploit
    | 3 | --------
    | 11 | Quit
    """

    print(displayInfo)

def ScanMenu():
    displayInfo = """
    | 1 | Scanning
        > a < Nmap classic
        > b < Nmap silent
        > c < Back
  """
    print(displayInfo)

def ExploitMenu():
    displayInfo = """
    | 2 | Exploit
        > a < Recherche de vulnerabilite sur un service
        > b < Recherche de CVE
        > c < Back 
  """
    print(displayInfo)