from time import sleep

from paramiko import SSHClient


def sshSimpleBrutForce(user, passwd):
    client = SSHClient()
    # client.load_system_host_keys()
    # client.load_host_keys('~/.ssh/known_hosts')
    # client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect('127.0.0.1', username='user', password='secret')
    client.close()
