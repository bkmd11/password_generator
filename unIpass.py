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

from unIpass_main import password_options
from unIpass_main import start_up
from unIpass_main import shut_down
from unIpass_main import file_writing

from unIpass_main.majestic_unicorn import majestic_unicorn


def main():
    # Makes my argument parser
    parser = argparse.ArgumentParser(description='''A very shitty password manager...
                Please don't actually think your passwords are safe with this thing!''')
    subparser = parser.add_subparsers(dest='command', )

    make = subparser.add_parser('make', help='Makes a password for the specified account')
    make.add_argument('account', help='The account you want a password for')
    make.add_argument('length', type=int, help='the length of the password, >13 recommended')

    find = subparser.add_parser('find', help='Finds the password for a specified account')
    find.add_argument('account', help='Shows all the accounts kept on file')

    stored = subparser.add_parser('stored', help='Allows viewing and maintenance of the accounts stored')
    stored.add_argument('-a', '--all', action='store_true', help='Shows all accounts tracked')

    args = parser.parse_args()

    """ I want to play around with this portion in interactive mode,
        so that I can see what things look like with -m and -f and -l
        get called
        """
    account_dict = start_up.open_unipass()
    majestic_unicorn()

    if args.command == 'make':
        pass_length = args.length
        account = args.account
        password = password_options.generator(pass_length)
        file_writing.store_password(account, password, account_dict)

    elif args.command == 'find':
        account_name = args.account
        print(password_options.get_password(account_name, account_dict))
        time.sleep(10)
        pyperclip.copy('PASSWORD CLEARED')

    elif args.command == 'stored':
        if args.all:
            tracked_accounts = password_options.accounts_stored(account_dict)
            for k in tracked_accounts:
                print(k)

    shut_down.close_unipass(account_dict)


if __name__ == '__main__':
    main()
