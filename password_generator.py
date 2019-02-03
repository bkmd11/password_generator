#! python3

""" This program can generate, store, and find passwords for various accounts.
It is probably extremely insecure and should be used by no one, ever.

Need to set up a way to encrypt the passwords stored in the json file.
Also interested in setting up a master password to make changes and pull
out existing passwords.

Also getting rid of the redundant call for json.load. Could make a function...
"""

import random
import string
import json
import pyperclip
import sys
import getpass

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
    master_pass = getpass.getpass('Enter your password:\n')
    if master_pass != 'spam':
        print('INVALID PASSWORD!!!')
        sys.exit()

# Prints out how this pos works
def usage():
    print('A very shitty password manager')
    print('-M <number> <account name>    Makes a randomly generated password for that account')
    print('-F <account name>    Finds the password for that account, and copies it to the clipboard')
    print('NEVER actually store your passwords in here because you will be hacked')
    print('Consider yourself warned...')

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

        with open('password_manager.json', 'w') as pass_man:
            json.dump(account_dict, pass_man)
            
    # Takes system arguments to call up passwords
    elif sys.argv[1] == '-F':
        account_name = sys.argv[2]

        print(get_password(account_name, account_dict))    
            
except IndexError:
    usage()           
