#! python3

""" This program can generate, store, and find passwords for various accounts.
It is probably extremely insecure and should be used by no one, ever.

I need to encrypt my password list.

Look up how to save encrypted info to a json file. 
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

# Retrieves passwords from the json file
def get_password(account_name, dictionary):
    #return dictionary[account_name]
    master_password()
    if account_name in account_dict:
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

#key = b'U9ERbXPIeJgHxj8BCpc-BQvV2JiXVtYHIGVQLtrWruo='

# Opens the json file to be read
with open('password_manager.json', 'r') as pass_dict:
    account_dict = json.load(pass_dict)

try:
    # Takes system arguments for making the password
    if sys.argv[1] == '-M':
        pass_length = sys.argv[2]
        account = sys.argv[3]

        password = generator(int(pass_length))
        store_password(account, password, account_dict)

        # Turning my dictionary into something I can encrypt
        bytes_dict = json.dumps(account_dict).encode()
        f = Fernet(key)
        token = f.encrypt(bytes_dict)

        ### TypeError: Object of type 'bytes' is not JSON serializable ###

        with open('password_manager.json', 'w') as pass_man:
            json.dump(token, pass_man)
    
    # Takes system arguments to call up passwords
    elif sys.argv[1] == '-F':
        account_name = sys.argv[2]

        print(get_password(account_name, account_dict))    
            
except IndexError:
    usage()           
