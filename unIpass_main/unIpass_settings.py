# Shows all accounts on file
def accounts_stored(dictionary):
    accounts = dictionary.keys()

    return accounts


# Edits the name of an account in case of a typo
def edit_name():
    new_key = input('Enter the new name for the account:\n')
    old_key = new_key

    return old_key


# Deletes an old account to keep everything looking clean
def delete(dictionary, key):
    dictionary.pop(key)

    return dictionary


