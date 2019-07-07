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


def main(name_space_object, dictionary):
    if name_space_object.show:
        tracked_accounts = accounts_stored(dictionary)
        for k in tracked_accounts:
            print(k)

    elif name_space_object.edit:

        try:
            dictionary = edit_name(name_space_object.account, name_space_object.change, dictionary)

        except KeyError:
            print('Error: account not found')

    elif name_space_object.delete:
        dictionary = delete(dictionary, name_space_object.account)

    return dictionary
