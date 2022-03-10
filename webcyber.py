
# Lib list for projects

from os import system
from platform import uname
from time import sleep
from colorama import Fore


try:

    def Page_clear():  # Terminal Clear

        Data_clear = uname()[0]

        if Data_clear == 'Linux':
            system('clear')

    def Developer():
        Page_clear()
        system('neofetch')
        print(Fore.LIGHTGREEN_EX+'\n\nDeveloper : Dr.cyber\n\nTeam : Eagle-Root\n\nMr.HN\n\nVersions : 2.1')
        sleep(5)
        system('python3 webcyber.py')

    Page_clear() # function Run For clear


    def list_tools():  # List tools

        # Due to the fact that if we used other methods to display the list of tools, our code would not be clean, we used the ( print ) method separately.

        BannerBox = system('neofetch')
        sleep(1)
        print(Fore.GREEN+'\n\n                                      SELECTS TOOLS\n\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'1'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Web Scan\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'2'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Info Domin\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'3'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Panel Admin\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'4'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Virtual Source\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'5'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Wordpress\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'6'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Sql Injection\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'99'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ☫ '+Fore.YELLOW+' Developer\n')


    list_tools() # function Run For List tools


    def Selects_tools(): # Select the tool in the options displayed

        selects = int(input(Fore.RED+'┌─['+Fore.GREEN+'Webcyber'+Fore.YELLOW+'~'+Fore.BLUE+'HOME'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))

        if selects == 1:
            system('python3 Data/NScan.py')
        elif selects == 2:
            system('python3 Data/Whois.py')
        elif selects == 3:
            system('python3 Data/adminP.py')
        elif selects == 4:
            system('python3 Data/Virtual.py')
        elif selects == 5:
            system('python3 Data/wordpress.py')
        elif selects == 6:
            system('python3 Data/injections.py')
        elif selects == 99:
            Developer()
        else:
             selects < 6
             system('python3 webcyber.py')



    Selects_tools() # function Run For Tools Run

except KeyboardInterrupt: # Control + c
    print(Fore.MAGENTA+'\n\nTanks :)')

except ValueError: # type Error in int => str

    print(Fore.MAGENTA+'\n\nError\nYou had to choose the number of options displayed')
    sleep(4)
    system('python3 webcyber.py')
