#! python3

""" This program can generate, store, and find passwords for various accounts.
It is probably extremely insecure and should be used by no one, ever.

Through careful research I found out how to encrypt my file.
This currently has a lot to be cleaned up to be more pretty, but
overall I am much excitment.

Known weakness is that my source code has both my hashed master_pass,
and the encryption key in it. So anyone that has a text editor can find
that info and attack me.

But much excitment.

Ideas for Improvment:
USB for ferent key and password hash (assert line for ensuring drive is in)
Have a new ferent key encrypt the file every time it closes (could cause failure)
Import optparse for my command line arguments

I am also going to rename this "unIpass" because why the hell not
With this name change I am going to make a logo that gets displayed
when it starts up
"""

import random
import string
import json
import pyperclip
import sys
import getpass
import hashlib
import send2trash   # Using send2trash to not permantly delete my file yet

from cryptography.fernet import Fernet

# Generates the passwords 
def generator(n):
    all_letters = list(string.ascii_letters + string.digits)
    password = []
    
    master_password()
    for i in range(n):
        character = random.choice(all_letters)
        password.append(character)

    strong_password = ''.join(password)
    return strong_password

# Retrieves passwords from the json file
def get_password(account_name, dictionary):
    if account_name in account_dict:
        master_password()
        password = account_dict[account_name]
        pyperclip.copy(password)
        return 'Password copied to clipboard'
    else:
        return 'No password exists for that account'

# Stores passwords into the file
def store_password(account_name, password, dictionary):
    dictionary[account_name] = password
    print('Password succesfully stored')
    
# Checks a master password for security
def master_password():
    master = getpass.getpass('Enter your password:\n')
    # Turns user input intp bytes for hashing
    master_pass = master.encode()
    h = hashlib.sha256(master_pass).hexdigest()
    
    if h != '4e388ab32b10dc8dbc7e28144f552830adc74787c1e2c0824032078a79f227fb':
        print('INVALID PASSWORD!!!')
        sys.exit()

# Prints out how this pos works
def usage():
    print('A very shitty password manager')
    print('-M <number> <account name>    Makes a randomly generated password for that account')
    print('-F <account name>    Finds the password for that account, and copies it to the clipboard')
    print('NEVER actually store your passwords in here because you will be hacked')
    print('Consider yourself warned...')


# Key to decrypt
key = b'XpvrSWhinFXNycFkFX8DFBFDTWLNJxRYLAQtZFTxG8w='  # I could put this on a flashdrive

encrypted_file = 'password_manager.encrypted'
decrypted_file = 'password_manager.json'

try:
    # Decrypts the file and writes it to a json file
    with open(encrypted_file, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(decrypted_file, 'wb') as read_file:
        read_file.write(decrypted)

    # Opens the json file to be read

    with open(decrypted_file, 'r') as pass_dict:
        account_dict = json.load(pass_dict)
# If the json file doesnt exist
except:
    account_dict = {}
    
try:
    # Takes system arguments for making the password
    if sys.argv[1] == '-M':
        pass_length = sys.argv[2]
        account = sys.argv[3]

        password = generator(int(pass_length))
        store_password(account, password, account_dict)

        with open(decrypted_file, 'w') as pass_man:
            json.dump(account_dict, pass_man)

        with open(decrypted_file, 'rb') as file:
            data = file.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open(encrypted_file, 'wb') as file:
            file.write(encrypted)

    
    # Takes system arguments to call up passwords
    elif sys.argv[1] == '-F':
        account_name = sys.argv[2]

        print(get_password(account_name, account_dict))

    send2trash.send2trash(decrypted_file)
            
except IndexError:
    usage()           
