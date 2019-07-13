#! python3

import json


# TODO: I may not actually need this function
# Loads/Dumps my json file
def json_function(json_file, read_or_write, data=None):
    if data is None:
        with open(json_file, read_or_write) as file:
            data = json.load(file)
        return data
    else:
        with open(json_file, read_or_write) as file:
            json.dump(data, file)


# Handles my encrypted file
def encrypt_function(encrypt_file, read_or_write_binary, data=None):
    if data is None:
        with open(encrypt_file, read_or_write_binary) as file:
            data = file.read()
        return data
    else:
        with open(encrypt_file, read_or_write_binary) as file:
            file.write(data)


# Stores passwords into the dictionary
def store_password(account_name, password, dictionary):
    dictionary[account_name.lower()] = password    # Makes the account_name lower case for ease of use
