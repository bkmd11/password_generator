#! python3

import json
import sys

from cryptography.fernet import Fernet

from unIpass_main import file_writing


def usb_assertion():
    """Makes sure the usb is plugged in with the file on it"""
    try:
        encryption_key = file_writing.json_function('E:key.json', 'rb')

        return encryption_key
    except FileNotFoundError:
        print('Unicorns don\'t exist')
        sys.exit()


def open_unipass():
    """Opens the program and sets variables up"""
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


def close_unipass(account_dict):
    """Saves the state of the program for shut down"""
    # Encrypts my data when I am done
    data = json.dumps(account_dict)

    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(bytes(data, 'utf-8'))

    file_writing.encrypt_function('password_manager.encrypted', 'wb', encrypted)
    file_writing.json_function('E:key.json', 'w', key.decode())



