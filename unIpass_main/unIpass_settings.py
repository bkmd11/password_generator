# Shows all accounts on file
def accounts_stored(dictionary):
    accounts = dictionary.keys()

    return accounts


# Edits the name of an account in case of a typo
def edit_name(old_account, new_account, dictionary):
    dictionary[new_account] = dictionary.pop(old_account)

    return dictionary


# Deletes an old account to keep everything looking clean
def delete(dictionary, key):
    dictionary.pop(key)

    return dictionary
