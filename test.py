import tkinter as tk
from tkinter import messagebox
import nmap


# fonction pour valider l'adresse IP saisie
def validate_ip(ip):
  # votre code de validation de l'adresse IP va ici
  # par exemple :
  if ip.count('.') != 3:
    return False
  for octet in ip.split('.'):
    try:
      int_octet = int(octet)
    except ValueError:
      return False
    if not (0 <= int_octet <= 255):
      return False
  return True

# fonction pour afficher les options
def show_options(ip):
  # créer une fenêtre pour afficher les options
  options_window = tk.Toplevel()
  options_window.geometry('400x300')
  options_window.title('ToolBox')

  # ajouter les boutons pour les options
  tk.Button(options_window, text='NMAP', command=option1).pack()
  tk.Button(options_window, text='Option 2', command=option2).pack()
  tk.Button(options_window, text='Option 3', command=option3).pack()

# fonction pour traiter le choix de l'option 1
def option1():
  messagebox.showinfo('Scan NMAP en cours, résultat disponible ici : ')

# fonction pour traiter le choix de l'option 2
def option2():
  messagebox.showinfo('Option 2', 'Vous avez choisi l\'option 2')

# fonction pour traiter le choix de l'option 3
def option3():
  messagebox.showinfo('Option 3', 'Vous avez choisi l\'option 3')

# fonction pour traiter la saisie de l'adresse IP
def process_ip_entry():
  # récupérer la valeur saisie dans l'entrée
  ip = ip_entry.get()
  # valider l'adresse IP
  if validate_ip(ip):
    # si l'adresse IP est valide, afficher les options
    show_options(ip)
  else:
    # si l'adresse IP n'est pas valide, afficher un message d'erreur
    messagebox.showerror('Erreur', 'L\'adresse IP saisie n\'est pas valide')

# créer la fenêtre principale de l'interface graphique
root = tk.Tk()
root.geometry('400x200')
root.title('Saisie d\'adresse IP')


# ajouter un étiquette pour indiquer à l'utilisateur quoi faire
tk.Label(root, text='Veuillez saisir une adresse IP :').pack()

# ajouter une entrée pour la saisie de l'adresse IP
ip_entry = tk.Entry(root)
ip_entry.pack()

# ajouter un bouton pour traiter la saisie de l'adresse IP
tk.Button(root, text='Valider', command=process_ip_entry).pack()

# afficher l'interface graphique
root.mainloop()