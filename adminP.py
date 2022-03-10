# Lib list for projects

from colorama import Fore
from platform import uname as um
from os import system as sys
from time import sleep


try: # For Error V,K

    def Page_clear(): # function Clear Data Terminal

        Data_clear = um()[0]
        if Data_clear == 'Linux':
            sys('clear')


    Page_clear() # Run function in Terminal




    def Data_page(): # Show Data Scripts in Terminal
        sys('neofetch')
        print(Fore.GREEN+'\n\n                                        ADMINPANEL \n\n')



    Data_page()  # Run function Data Script


    sleep(0.15)

    def A_P(): # For DominName
        print(Fore.YELLOW+'['+Fore.RED+'!'+Fore.YELLOW+']'+Fore.LIGHTCYAN_EX+' Please Do Not Include Https\n\n')
        Dominput = input(Fore.RED+'┌─{'+Fore.GREEN+'Panel Admin'+Fore.YELLOW+'~'+Fore.BLUE+'DOMIN'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        urldata = sys('dirb '+'https://'+Dominput+'/')

    A_P()

except KeyboardInterrupt: # Control + c

    print(Fore.MAGENTA+'\n\nTanks :)\n\n')

except ValueError: # type Error in int => str

    print(Fore.MAGENTA+'\n\nError\nYou had to choose the number of options displayed')
    sleep(4)
    sys('python3 webcyber.py') # Reloads File !

