"""This is an install/setup feature for when unIpass is used for the first time.
It will set up a master password, an encrypted file for the passwords, and the
json files for the hash and encryption key
"""

import hashlib
import getpass

from unIpass_main import file_writing


# Sets up the master password the first time the program is run
def make_master_password(master_password):
    password = master_password.encode()
    hashed_password = hashlib.sha256(password).hexdigest()

    return hashed_password


# Stores the hash on a thumb drive
def store_hash(hashed_password):
    try:
        file_writing.json_function('E:hash.json', 'w', hashed_password)

    except FileNotFoundError:
        print('Unicorn must be plugged in')


# Makes the necessary files to run unIpass
# TODO: There must be a better way to write files into a given directory. look into os/sys modules.
#  I believe either the asyc or gui real python get into that vaguely...
#  It would make all my file writing more pythonic
#  This also wont currently actually make this directory
def make_files_for_unipass():
    file_writing.encrypt_function('C:Users\\Brian Kendall\\unIpass\\password_manager.encrypted', 'wb', data='')
    file_writing.json_function('E:key.json', 'w', data='')


def main():
    while True:
        password = getpass.getpass('Please enter a strong password for your master password:\n')
        password_2 = getpass.getpass('Please confirm your password:\n')
        if password == password_2:
            hashed_master_password = make_master_password(password)
            store_hash(hashed_master_password)
            make_files_for_unipass()

        else:
            print('The passwords you entered did not match.')


if __name__ == '__main__':
    print('Hello, thank you for choosing unIpass to manage your passwords.\nUnicorns truly are magical creatures.')
    print('Please leave the unIpass usb plugged in for the duration of the install')
    main()
    print('Setup is complete, sleep better knowing unIpass has your passwords safe!')