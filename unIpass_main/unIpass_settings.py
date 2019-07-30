def accounts_stored(dictionary):
    """Shows all accounts on file"""
    accounts = dictionary.keys()

    return accounts


def edit_name(old_account, new_account, dictionary):
    """Edits the name of an account in case of a typo"""
    dictionary[new_account] = dictionary.pop(old_account)

    return dictionary


def delete(dictionary, key):
    """Deletes an old account"""
    dictionary.pop(key)

    return dictionary
