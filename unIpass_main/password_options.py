#! python3

import random
import string


# Generates the passwords
def generator(n):
    all_letters = list(string.ascii_letters + string.digits)
    password = []

    for i in range(n):
        character = random.choice(all_letters)
        password.append(character)

    strong_password = ''.join(password)
    return strong_password


# Retrieves passwords from the dictionary
def get_password(account_name, dictionary):
    account_name = account_name.lower()    # Makes it ignore case for ease of use
    if account_name in dictionary:
        password = dictionary[account_name]
        return password
    else:
        return None

