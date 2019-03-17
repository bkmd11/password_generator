#! python3

""" This program can generate, store, and find passwords for various accounts.
It is probably extremely insecure and should be used by no one, ever.

This currently has a lot to be cleaned up to be more pretty, but
overall I am much excitement.

Ideas for Improvement:
USB for ferent key and password hash (assert line for ensuring drive is in)

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


# Retrieves passwords from the dictionary
def get_password(account_name, dictionary):
    if account_name in dictionary:
        master_password()
        password = account_dict[account_name]
        pyperclip.copy(password)
        return 'Password copied to clipboard'
    else:
        return 'No password exists for that account'


# Stores passwords into the dictionary
def store_password(account_name, password, dictionary):
    dictionary[account_name] = password
    print('Password successfully stored')


# Checks a master password for security
def master_password():
    master = getpass.getpass('Enter your password:\n')
    # Turns user input int0 bytes for hashing
    master_pass = master.encode()
    h = hashlib.sha256(master_pass).hexdigest()

    if h != '4e388ab32b10dc8dbc7e28144f552830adc74787c1e2c0824032078a79f227fb':
        print('INVALID PASSWORD!!!')
        sys.exit()


# Loads/Dumps my json file
def json_function(json_file, mode, data=None):
    if data is None:
        with open(json_file, mode) as file:
            data = json.load(file)
        return data
    else:
        with open(json_file, mode) as file:
            json.dump(data, file)


# Handles my encrypted file
def encrypt_function(encrypt_file, mode, data=None):
    if data is None:
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
    key = json_function('E:key.json', 'rb')

except FileNotFoundError:
    print('Unicorns don\'t exist')
    sys.exit()

encrypted_file = 'password_manager.encrypted'

# Loads my data and decrypts it, or makes a new dictionary
try:
    data = encrypt_function(encrypted_file, 'rb')

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    account_dict = json.loads(decrypted)

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

    # Takes system arguments to call up passwords
    elif sys.argv[1] == '-F':
        account_name = sys.argv[2]

        print(get_password(account_name, account_dict))

except IndexError:
    usage()

# Encrypts my data when I am done
data = json.dumps(account_dict)

key = Fernet.generate_key()
fernet = Fernet(key)
encrypted = fernet.encrypt(bytes(data, 'utf-8'))

encrypt_function(encrypted_file, 'wb', encrypted)
json_function('E:key.json', 'w', key.decode())
