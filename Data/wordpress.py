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
        print(Fore.GREEN+'\n\n                                        WORDPRESS \n\n')

    Data_page() # Run function Data Script

    def ListData(): # function List Number

        print(Fore.RED+'['+Fore.WHITE+'1'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Brute Force Login Page'+Fore.RED+' !\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'2'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Scan WebSite'+Fore.RED+' !\n')
        sleep(0.15)
        print(Fore.YELLOW+'['+Fore.RED+'!'+Fore.YELLOW+']'+Fore.LIGHTCYAN_EX+' Please Add Https\n\n')

    ListData() # For run List Data Scripts

    def BruteForce(): # For brute Force Attacks

        Page_clear() # Reloading For data

        Data_page() # Reloading For data

        Dominput_url = input(Fore.RED+'┌─{'+Fore.GREEN+'WordPress'+Fore.YELLOW+'~'+Fore.BLUE+'BruteForce'+Fore.RED+Fore.YELLOW+'/'+Fore.BLUE+'BruteForce'+Fore.YELLOW+'/'+Fore.LIGHTYELLOW_EX+'Page Login'+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        sleep(0.20)
        passlist = input(Fore.RED+'┌─{'+Fore.GREEN+'WordPress'+Fore.YELLOW+'~'+Fore.BLUE+'BruteForce'+Fore.RED+Fore.YELLOW+'/'+Fore.BLUE+'BruteForce'+Fore.YELLOW+'/'+Fore.LIGHTYELLOW_EX+'PassList'+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        sleep(0.20)
        username = input(Fore.RED+'┌─{'+Fore.GREEN+'WordPress'+Fore.YELLOW+'~'+Fore.BLUE+'BruteForce'+Fore.RED+Fore.YELLOW+'/'+Fore.BLUE+'BruteForce'+Fore.YELLOW+'/'+Fore.LIGHTYELLOW_EX+'UserName'+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        sleep(0.20)
        sys('wpscan --url '+(Dominput_url)+' --passwords '+(passlist)+' --usernames '+(username))

    def ScanNormal(): # For scan web site Wordpress
        Page_clear() # Reloading For data
        Data_page() # Reloading For data
        sleep(0.20)
        Put_url = input(Fore.RED+'┌─['+Fore.GREEN+'WordPress'+Fore.YELLOW+'~'+Fore.BLUE+'BruteForce'+Fore.RED+Fore.YELLOW+'/'+Fore.BLUE+'Scanner'+Fore.YELLOW+'/'+Fore.LIGHTYELLOW_EX+'Domin'+Fore.RED+']'+'\n└──╼> '+Fore.WHITE)
        sys('wpscan --url '+str(Put_url))

    def Selects(): # Selects Number or type attcks


        selects = int(input(Fore.RED+'┌─['+Fore.GREEN+'Webcyber'+Fore.YELLOW+'~'+Fore.BLUE+'WordPress'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))

        if selects == 1:
            BruteForce()

        elif selects == 2:
            ScanNormal()

        else:
            selects < 2
            sys('python3 webcyber.py')

    Selects()

except KeyboardInterrupt: # For Cont + c
    print(Fore.BLUE+'\n\nTanks :)\n\n')

except ValueError: # For ValueError
    print(Fore.MAGENTA+'\n\nError\nYou had to choose the number of options displayed')
    sleep(4)
    sys('python3 webcyber.py') # Reloads File script