#! python3

import json


# Todo: these are all hard to test
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


# Stores passwords into the dictionary
def store_password(account_name, password, dictionary):
    dictionary[account_name.lower()] = password    # Makes the account_name lower case for ease of use
