from colorama import init, Fore, Style


# Obviously this is just a majestic unicorn
def majestic_unicorn():
    init()
    print(Fore.LIGHTRED_EX + '''
                  ^
                  ^^
                  ^^^ ''' + Fore.LIGHTBLUE_EX + '''
                  ^^^^
                  ^^^^^ $
                UNIPASSUN$$''' + Fore.LIGHTGREEN_EX + '''
            UNIPASSUNIPAS$$$
        UNIPASSUN(  )IPASS$$$$
    UNIPASSUNIPASSUNIPASS$$$$$''' + Fore.LIGHTMAGENTA_EX + '''
    UNIPASSUNIPASSUNIPASS$$$$$$
            UNIPASSUNIPAS$$$$$
            UNIPASSUNIPAS$$$$$$''' + Fore.LIGHTYELLOW_EX + '''
           UNIPASSUNIPASS$$$$$$$$
          UNIPASSUNIPASSU$$$$$$
         UNIPASSUNIPASSUN$$$$$$$ 
''' + Style.RESET_ALL)

