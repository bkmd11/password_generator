"""This is an install/setup feature for when unIpass is used for the first time.
It will set up a master password, an encrypted file for the passwords, and the
json files for the hash and encryption key
"""
# todo: I need to make this actually not suck. Many bugs, no error handling and just generally doesnt work

import hashlib
import getpass
import os

from unIpass_main import file_writing


def make_master_password(master_password):
    """Sets up the master password the first time the program is run"""
    password = master_password.encode()
    hashed_password = hashlib.sha256(password).hexdigest()

    return hashed_password


def store_hash(hashed_password):
    """Stores the hash on a thumb drive"""
    try:
        file_writing.json_function('E:hash.json', 'w', hashed_password)

    except FileNotFoundError:
        print('Unicorn must be plugged in')


def make_files_for_unipass():
    """Makes the necessary files to run unIpass"""
    path = 'C:\\Users\\Brian Kendall\\unIpass'  # todo make this walk directory tree to not just do my username
    os.mkdir(path)
    os.chdir(path)
    file_writing.encrypt_function('password_manager.encrypted', 'wb', data=b'')
    file_writing.json_function('E:key.json', 'w', data='')
    # todo: move unIpass.py and associated files into new directory

def main():

    password_2 = 'spam'
    while True:
        # todo: this works in cmd prompt but not pycharm
        password = getpass.getpass('Please enter a strong password for your master password:\n')
       # password_2 = getpass.getpass('Please confirm your password:\n')
        if password == password_2:
            break

        print('The passwords you entered did not match.')

    hashed_master_password = make_master_password(password)
    store_hash(hashed_master_password)
    make_files_for_unipass()


if __name__ == '__main__':
    print('Hello, thank you for choosing unIpass to manage your passwords.\nUnicorns truly are magical creatures.')
    print('Please leave the unIpass usb plugged in for the duration of the install')
    main()
    print('Setup is complete, sleep better knowing unIpass has your passwords safe!')
