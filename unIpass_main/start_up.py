#! python3

import json
import sys

from cryptography.fernet import Fernet

from unIpass_main import file_writing


# Makes sure my usb is plugged in with the file on it
def usb_assertion():
    try:
        encryption_key = file_writing.json_function('E:key.json', 'rb')

        return encryption_key
    except FileNotFoundError:
        print('Unicorns don\'t exist')
        sys.exit()


# This opens the program to set everything up
def open_unipass():
    key = usb_assertion()

    # Loads my data and decrypts it, or makes a new dictionary
    try:
        data = file_writing.encrypt_function('password_manager.encrypted', 'rb')

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)

        account_dict = json.loads(decrypted)
        return account_dict

    except FileNotFoundError:
        account_dict = {}
        return account_dict


