#! python3

""" This program can generate, store, and find passwords for various accounts.
It is probably extremely insecure and should be used by no one, ever.

This currently has a lot to be cleaned up to be more pretty, but
overall I am much excitement.

My usb idea to store the hash and key somewhere other than my program makes
this slightly more secure, but is probably still a weakness in my manager.
I am not sure how else I can go about solving that security problem at
this time.

Ideas for Improvement:
Import optparse for my command line arguments
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
    master_password()
    if account_name in dictionary:
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
    # Turns user input into bytes for hashing
    master_pass = master.encode()
    h = hashlib.sha256(master_pass).hexdigest()
    master_hash = json_function('E:hash.json','r')
    if h != master_hash:
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


# Makes sure my usb is plugged in with the file on it
def usb_assertion():
    try:
        encryption_key = json_function('E:key.json', 'rb')

        return encryption_key
    except FileNotFoundError:
        print('Unicorns don\'t exist')
        sys.exit()


# Prints out how this pos works
def usage():
    print('A very shitty password manager')
    print('-M <number> <account name>    Makes a randomly generated password for that account')
    print('-F <account name>    Finds the password for that account, and copies it to the clipboard')
    print('NEVER actually store your passwords in here because you will be hacked')
    print('Consider yourself warned...')


# Obviously this is just a majestic unicorn
def majestic_unicorn():
    print('''
                  ^
                  ^^
                  ^^^
                  ^^^^
                  ^^^^^ $
                UNIPASSUN$$
            UNIPASSUNIPAS$$$
        UNIPASSUN(  )IPASS$$$$
    UNIPASSUNIPASSUNIPASS$$$$$
    UNIPASSUNIPASSUNIPASS$$$$$$
            UNIPASSUNIPAS$$$$$
            UNIPASSUNIPAS$$$$$$
           UNIPASSUNIPASS$$$$$$$$
          UNIPASSUNIPASSU$$$$$$
''')


key = usb_assertion()
encrypted_file = 'password_manager.encrypted'
majestic_unicorn()

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
