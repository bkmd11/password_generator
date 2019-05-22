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
Adding something to keep track of how old passwords are, and suggest changing 
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
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-m', '--make', action='store_true',
                       help='Makes a password for the specified account')
    group.add_argument('-f', '--find', action='store_true',
                       help='Finds the password for a specified account')
    parser.add_argument('account', help='The account you want to use')
    parser.add_argument('-l', '--length', type=int, metavar='int', default=19,
                        help='Specify the length of the password')

    args = parser.parse_args()
    account_dict = start_up.open_unipass()
    majestic_unicorn()

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

    else:
        print('You must specify [-m] or [-f]')

    shut_down.close_unipass(account_dict)


if __name__ == '__main__':
    main()
