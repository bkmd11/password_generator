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
salting my hash
"""

import random
import string
import json
import pyperclip
import sys
import getpass
import hashlib
import argparse

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
        password = dictionary[account_name]
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


# This opens the program to set everything up
def open_unipass():
    key = usb_assertion()
    majestic_unicorn()

    # Loads my data and decrypts it, or makes a new dictionary
    try:
        data = encrypt_function('password_manager.encrypted', 'rb')

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)

        account_dict = json.loads(decrypted)
        return account_dict

    except FileNotFoundError:
        account_dict = {}
        return account_dict


# Sets everything up to close the program
def close_unipass(account_dict):
    # Encrypts my data when I am done
    data = json.dumps(account_dict)

    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(bytes(data, 'utf-8'))

    encrypt_function('password_manager.encrypted', 'wb', encrypted)
    json_function('E:key.json', 'w', key.decode())


def main():
    # Makes my argument parser
    parser = argparse.ArgumentParser(description='''A very shitty password manager...
                Please don't actually think your passwords are safe with this thing!''')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-m', '--make', action='store_true',
                       help='Makes a password for the specified account')
    group.add_argument('-f', '--find', action='store_true',
                       help='Finds the password for a specified account')
    parser.add_argument('account', help='Enter the account')
    parser.add_argument('-l', '--length', type=int, metavar='', default=19,
                        help='Specify the length of the password')

    args = parser.parse_args()

    account_dict = open_unipass()

    if args.make:
        pass_length = args.length
        account = args.account
        password = generator(pass_length)
        store_password(account, password, account_dict)

    elif args.find:
        account_name = args.account
        print(get_password(account_name, account_dict))

    else:
        print('You must specify [-m] or [-f]')

    close_unipass(account_dict)


if __name__ == '__main__':
    main()
