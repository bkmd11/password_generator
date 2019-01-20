#! python3

""" This program can generate, store, and find passwords for various accounts.
It is probably extremely insecure and should be used by no one, ever.

Currently my problem with it is my redundant usage() call in the else
statement. But other things I tried cause other bugs.
I will come back to it
"""

import random
import string
import json
import pyperclip
import sys

# Generates the passwords 
def generator(n):
    all_letters = list(string.ascii_letters + string.digits)
    password = []
    
    for i in range(n):
        character = random.choice(all_letters)
        password.append(character)

    strong_password = ''.join(password)
    return strong_password

# Retrieves passwords from the json file
def get_password(account_name, dictionary):
    return dictionary[account_name]

# Stores passwords into the file
def store_password(account_name, password, dictionary):
    dictionary[account_name] = password
    print('Password succesfully stored')

# Prints out how this pos works
def usage():
    print('A very shitty password manager')
    print('-M <number> <account name>    Makes a randomly generated password for that account')
    print('-F <account name>    Finds the password for that account, and copies it to the clipboard')
    print('NEVER actually store your passwords in here because you will be hacked')
    print('Consider yourself warned...')

# Probably a better way to do this. I'm open to suggestions...    
if not len(sys.argv[1:]):
    usage()

elif sys.argv[1] == '-M':
    pass_length = sys.argv[2]
    account = sys.argv[3]
    
    with open('password_manager.json', 'r') as pass_dict:
        account_dict = json.load(pass_dict)

    password = generator(int(pass_length))
    store_password(account, password, account_dict)

    with open('password_manager.json', 'w') as pass_man:
        json.dump(account_dict, pass_man)

elif sys.argv[1] == '-F':
    account_name = sys.argv[2]

    with open('password_manager.json', 'r') as pass_dict:
        account_dict = json.load(pass_dict)

    password = account_dict[account_name]
    pyperclip.copy(password)
    print('Password copied to clipboard')
    
else:
    usage()           
