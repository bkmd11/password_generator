#! python3

""" This program can generate, store, and find passwords for various accounts.
It is probably extremely insecure and should be used by no one, ever.

This currently has a lot to be cleaned up to be more pretty, but
overall I am much excitment.

Ideas for Improvment:
USB for ferent key and password hash (assert line for ensuring drive is in)
Have a new ferent key encrypt the file every time it closes (could cause failure)
Import optparse for my command line arguments
Make a logo that prints on starting
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

# Loads/Dumps my json file
def json_function(json_file, mode, data):
    if data == None:
        with open(json_file, mode) as file:
            data = json.load(file)
        return data
    else:
        with open(json_file, mode) as file:
            json.dump(data, file)

# Handles my encrypted file
def encrypt_function(encrypt_file, mode, data):
    if data == None:
        with open(encrypt_file, mode) as file:
            data = file.read()
        return data
    else:
        with open(encrypt_file, mode) as file:
            file.write(data)

            
# Prints out how this pos works
def usage():
    print('A very shitty password manager')
    print('-M <number> <account name>    Makes a randomly generated password for that account')
    print('-F <account name>    Finds the password for that account, and copies it to the clipboard')
    print('NEVER actually store your passwords in here because you will be hacked')
    print('Consider yourself warned...')

# Makes sure my usb is plugged in with the file on it
try:
    key = json_function('E:key.json', 'rb', None)
        
except FileNotFoundError:
    print('Unicorns don\'t exist')
    sys.exit()
    
encrypted_file = 'password_manager.encrypted'
decrypted_file = 'password_manager.json'

try:
    data = encrypt_function(encrypted_file, 'rb', None)

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    encrypt_function(decrypted_file, 'wb', decrypted)

    account_dict = json_function(decrypted_file, 'r', None)
    
# If the json file doesnt exist
except:
    account_dict = {}


### I can use optparse to do this better maybe ###  
try:
    # Takes system arguments for making the password
    if sys.argv[1] == '-M':
        pass_length = sys.argv[2]
        account = sys.argv[3]

        password = generator(int(pass_length))
        store_password(account, password, account_dict)

        json_function(decrypted_file, 'w', account_dict)
        data = encrypt_function(decrypted_file, 'rb', None)

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        encrypt_function(encrypted_file, 'wb', encrypted)
    
    # Takes system arguments to call up passwords
    elif sys.argv[1] == '-F':
        account_name = sys.argv[2]

        print(get_password(account_name, account_dict))

    send2trash.send2trash(decrypted_file)
            
except IndexError:
    usage()           
