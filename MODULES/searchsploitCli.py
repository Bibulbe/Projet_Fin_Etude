import os
import re

import requests
import json
import subprocess


def cleanColor(ligne):
    cleaned = re.sub('\x1B\[([0-9]{1,3}(;[0-9]{1,2};?)?)?[mGK]', '', ligne)
    cleaned.replace('  ', '')
    return cleaned


def exploitdbSearch(input_command):
    command = "searchsploit"
    command_run = subprocess.Popen([command, input_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = command_run.communicate()

    command_result = (out.decode())
    Lignes = [cleanColor(character) for character in command_result.split('\n')][3:-1]
    if len(Lignes) > 0:
        Lignes.pop()
        Lignes.pop()

    Lignesindict = [{'titre': Ligne.split(' - ')[0], 'type': (Ligne.split(' - ')[1]).split(' | ')[0],
                     'fichier': ((Ligne.split(' - ')[1]).split('|')[1]).replace(' ', '')} for Ligne in Lignes]

    return (Lignesindict)

print(exploitdbSearch('Vsftpd'))
if "__main__" == __name__:
    samba = exploitdbSearch("samba")
    for s in samba:
        print(s["type"])