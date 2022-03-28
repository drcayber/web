# Lib list for projects

from time import sleep
from whois import whois as ws
from colorama import Fore
from platform import uname as um
from os import system as sys

try: # For Error V,K

    def Page_clear(): # function Clear Data Terminal

        Data_clear = um()[0]

        if Data_clear == 'Linux':
            sys('clear')


    Page_clear() # Run function in Terminal

    def Data_page(): # Show Data Scripts in Terminal

        sys('neofetch')
        print(Fore.GREEN+'\n\n                                      USE DOMIN \n\n')

    Data_page() # Run function Data Script

    def Whois(): # For Whois as WebSite
        print(Fore.YELLOW+'['+Fore.RED+'!'+Fore.YELLOW+']'+Fore.LIGHTCYAN_EX+' Please Do Not Include Https\n\n')
        Dominput = input(Fore.RED+'┌─{'+Fore.GREEN+'INFO-DOMIN'+Fore.YELLOW+'~'+Fore.BLUE+'DOMIN'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        urldata = ws('https://'+Dominput+'/')

        print(urldata)


    Whois() # Run Whois function !

except KeyboardInterrupt: # For Cont + C

    print(Fore.BLUE+'\n\nTanks :)\n\n')

except ValueError: # For ValueError
    print(Fore.BLUE+'\nErore')
    sleep(3)
    sys('python3 webcyber.py') # Reloads File !
