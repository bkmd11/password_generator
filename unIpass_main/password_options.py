#! python3

import random
import string
import pyperclip
import time

from unIpass_main import file_writing


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


def main(name_space_object, dictionary):
    if name_space_object.make:
        pass_length = name_space_object.length
        account = name_space_object.account
        password = generator(pass_length)
        file_writing.store_password(account, password, dictionary)
        print('Password successfully stored')

    elif name_space_object.find:
        account_name = name_space_object.account
        password = get_password(account_name, dictionary)
        if password is not None:
            pyperclip.copy(password)
            print('Password copied to clipboard')
            time.sleep(10)
            pyperclip.copy('')
            print('PASSWORD CLEARED')
        else:
            print('No password exists for that account')