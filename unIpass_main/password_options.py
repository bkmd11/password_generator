#! python3

import random
import string
import pyperclip
import getpass
import hashlib
import sys

from file_writing import json_function


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
        password = dictionary[account_name]
        pyperclip.copy(password)
        return 'Password copied to clipboard'
    else:
        return 'No password exists for that account'
