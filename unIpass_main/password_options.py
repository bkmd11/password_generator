#! python3

import random
import string
import pyperclip


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
    if account_name in dictionary:
        password = dictionary[account_name]
        pyperclip.copy(password)
        return 'Password copied to clipboard'
    else:
        return 'No password exists for that account'

