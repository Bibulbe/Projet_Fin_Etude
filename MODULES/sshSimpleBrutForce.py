import os
from ftplib import FTP, FTP_TLS
from time import sleep

import paramiko
from paramiko import SSHClient


def sshConnection(host, user, passwd):
    client = SSHClient()
    # client.load_system_host_keys()

    # client.load_host_keys('~/.ssh/known_hosts')
    # client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username='user', password='user')
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        return False


def ftpConnection(host, user='', passwd=''):
    host = host
    username = user
    password = passwd
    port = 21

    if not user and not passwd:
        ftp = FTP()
        ftp.connect(host, port)
        ftp.connect()
        ftp.quit()
        return "anonymous", ""
    try:
        ftp = FTP()
        ftp.connect(host, port)
        ftp.login(username, password)
        ftp.quit()
        return username, password

    except ConnectionRefusedError:
        print('ConnectionRefusedError')
        return False


def ftpsConnection(host, user='', passwd=''):
    host = host
    username = user
    password = passwd
    port = 21

    if not user and not passwd:
        ftp = FTP_TLS()
        ftp.connect(host, port)
        ftp.connect()
        ftp.quit()
        return "anonymous", ""
    try:
        ftp = FTP_TLS()
        ftp.connect(host, port)
        ftp.login(username, password)
        ftp.quit()
        return username, password

    except ConnectionRefusedError:
        print('ConnectionRefusedError')
        return False


def sshSimpleBruteForce():
    pass


ftpConnection("192.168.243.129", 'user', 'user')
