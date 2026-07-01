import paramiko
from getpass import getpass
import time


"""
This segment establishes a connection to a Raspberry Pi using SSH. 
It prompts the user for the username, password and IP address.
"""

host = "192.168.86.113" #IP address of the Raspberry Pi.
username = ("pi") #name of the user on the Raspberry Pi. The default username is "pi".
print (f"username: {username}") #display the username entered by the user.
password = ("1") #prompts the user for password. The defult is "1".
print ("password")


"""
Session is created using the paramiko library, which is used to establish an SSH connection to the Raspberry Pi.
The session is configured to automatically use the inputed password, username and IP of the Raspberry Pi.
Note: No host key is used.
"""
session = paramiko.SSHClient()
session.load_system_host_keys()
session.set_missing_host_key_policy(paramiko.RejectPolicy())
session.connect(
    hostname=host,
    username=username,
    password=password
)




"""
Seprate opperations related to the Raspberry Pi can be added here.
such as executing commands, transferring files or updating the system.
"""

stdin, stdout, stderr = session.exec_command('hostname')
time.sleep (5)
print (f" host name is: {stdout.read().decode()}") #display the hostname of the Raspberry Pi.
session.close()
