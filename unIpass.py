#! python3
""" This program can generate, store, and find passwords for various accounts.
It is probably extremely insecure and should be used by no one, ever.

This currently has a lot to be cleaned up to be more pretty, but
overall I am much excitement.

My usb idea to store the hash and key somewhere other than my program makes
this slightly more secure, but is probably still a weakness in my manager.
I am not sure how else I can go about solving that security problem at
this time.

Ideas for Improvement:
salting my hash
Something to delete/rename accounts

I am not crazy with how argparse does things...
My old way was better in my opinion
"""
import argparse
import time
import pyperclip
import getpass
import hashlib
import sys


from unIpass_main import password_options
from unIpass_main import system
from unIpass_main import file_writing
from unIpass_main import unIpass_settings

from unIpass_main.majestic_unicorn import majestic_unicorn


# Checks a master password for security
def master_password():
    master = getpass.getpass('Enter your password:\n')
    # Turns user input into bytes for hashing
    master_pass = master.encode()
    h = hashlib.sha256(master_pass).hexdigest()
    master_hash = file_writing.json_function('E:hash.json', 'r')
    if h != master_hash:
        print('INVALID PASSWORD!!!')
        sys.exit()


def main():
    # Makes my argument parser
    parser = argparse.ArgumentParser(description='''A very shitty password manager...
                Please don't actually think your passwords are safe with this thing!''')
    subparser = parser.add_subparsers(dest='command', )

    # Parses for making/finding passwords
    password = subparser.add_parser('password', help='Main use: [find] or [make] a password')
    group = password.add_mutually_exclusive_group()
    group.add_argument('-m', '--make', action='store_true', help='Makes a password of a given length')
    group.add_argument('-f', '--find', action='store_true', help='Finds the password for the specified account')
    password.add_argument('account', help='The account')
    password.add_argument('-l', '--length', type=int, default=19, help='Length of the password')

    # System maintenance like changing/deleting accounts, and showing all stored accounts
    settings = subparser.add_parser('settings', help='Allows viewing and maintenance of the accounts stored')
    group2 = settings.add_mutually_exclusive_group()
    group2.add_argument('-a', '--all', action='store_true', help='Shows all accounts tracked')
    group2.add_argument('-e', '--edit', action='store_true', help='Changes the name of an account')
    group2.add_argument('-d', '--delete', action='store_true', help='Deletes old accounts')
    settings.add_argument('--account', help='The account to be edited')

    args = parser.parse_args()
    account_dict = system.open_unipass()
    majestic_unicorn()
    master_password()

    if args.command == 'password':
        if args.make:
            pass_length = args.length
            account = args.account
            password = password_options.generator(pass_length)
            file_writing.store_password(account, password, account_dict)

        elif args.find:
            account_name = args.account
            print(password_options.get_password(account_name, account_dict))
            time.sleep(10)
            pyperclip.copy('PASSWORD CLEARED')

    elif args.command == 'settings':
        if args.all:
            tracked_accounts = unIpass_settings.accounts_stored(account_dict)
            for k in tracked_accounts:
                print(k)
        elif args.edit:
            key = unIpass_settings.edit_name()
            account_dict[key] = account_dict.pop(args.account)
        elif args.delete:
            account_dict = unIpass_settings.delete(account_dict, args.account)

    system.close_unipass(account_dict)


if __name__ == '__main__':
    main()
