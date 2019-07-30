#! python3

import json


def json_function(json_file, read_or_write, data=None):
    """Loads/Dumps json file"""
    if data is None:
        with open(json_file, read_or_write) as file:
            data = json.load(file)
        return data
    else:
        with open(json_file, read_or_write) as file:
            json.dump(data, file)


def encrypt_function(encrypt_file, read_or_write_binary, data=None):
    """Reads/Writes the .encrypt file"""
    if data is None:
        with open(encrypt_file, read_or_write_binary) as file:
            data = file.read()
        return data
    else:
        with open(encrypt_file, read_or_write_binary) as file:
            file.write(data)


def store_password(account_name, password, dictionary):
    """Stores password into the dictionary"""
    dictionary[account_name.lower()] = password    # Makes the account_name lower case for ease of use
