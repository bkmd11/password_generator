#! python3

import random
import string


def generator(n):
    """Generates the passwords"""
    all_letters = list(string.ascii_letters + string.digits)
    password = []

    for i in range(n):
        character = random.choice(all_letters)
        password.append(character)

    strong_password = ''.join(password)
    return strong_password


def get_password(account_name, dictionary):
    """Retrieves passwords from the dictionary"""
    account_name = account_name.lower()    # Makes it ignore case for ease of use
    if account_name in dictionary:
        password = dictionary[account_name]
        return password
    else:
        return None
