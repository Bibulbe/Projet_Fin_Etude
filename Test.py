import socket

def is_valid_ip(ip_address):
  if ip_address.count('.') != 3:
    return False
  for octet in ip_address.split('.'):
    try:
      int_octet = int(octet)
    except ValueError:
      return False
    if not (0 <= int_octet <= 255):
      return False
  return True

def is_valid_domain(domain_name):
  try:
    # Vérification de la validité du nom de domaine
    socket.gethostbyname(domain_name)
    return True
  except:
    return False

def run_program1(ip_address):
  # code pour exécuter le premier programme avec l'adresse IP en argument
  return True
def run_program2(ip_address):
  # code pour exécuter le deuxième programme avec l'adresse IP en argument
  return True
def run_program3(ip_address):
  # code pour exécuter le troisième programme avec l'adresse IP en argument
  return True
while True:
  # Demande de l'adresse IP ou du nom de domaine à l'utilisateur
  input_string = input("Entrez une adresse IP ou un nom de domaine : ")

  # Vérification de la validité de l'adresse IP ou du nom de domaine
  if is_valid_ip(input_string):
    # Adresse IP valide, on stocke l'adresse IP dans une variable
    ip_address = input_string
  elif is_valid_domain(input_string):
    # Nom de domaine valide, on résout le nom de domaine en adresse IP
    ip_address = socket.gethostbyname(input_string)
  else:
    print("L'adresse spécifiée n'est ni une adresse IP valide ni un nom de domaine valide")
    continue

  # Demande de sélection de l'option à l'utilisateur
  option = input("Sélectionnez une option (1, 2 ou 3) ou tapez 'q' pour quitter : ")

  # Si l'utilisateur a choisi de quitter, on sort de la boucle
  if option == 'q':
    break

  # Conversion de l'option en entier
  option = int(option)

  # Exécution du programme sélectionné avec l'adresse IP en argument
  if option == 1:
    run_program1(ip_address)
  elif option == 2:
    run_program2(ip_address)
  elif option == 3:
    run_program3(ip_address)
