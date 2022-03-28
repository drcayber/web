#  Lib list , os , colorama , time , platform

from os import system as sys
from colorama import Fore
from time import sleep
from platform import uname as um



try: # For Error V,K
    def Page_clear(): # function Clear Data Terminal

        clear = um()[0]
        if clear == 'Linux':
            sys('clear')

    Page_clear() # Run clear in Terminal

    def data_tools(): # Banner For Tools


        banner = sys('neofetch')
        sleep(0.15)
        print(Fore.GREEN+'\n\n                                      TYPE OF ATTACKS\n\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'1'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Test Bug Xss\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'2'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Test Sql-Injection\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'3'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' WordPress Brute\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'4'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' WordPress UsenName\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'5'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' WordPress Enum\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'6'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Site Map\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'7'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Dns Brute\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'8'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' System Info\n')
        sleep(0.15)
        print(Fore.RED+'['+Fore.WHITE+'9'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' => '+Fore.YELLOW+' Port Scanner\n')

    data_tools() # Run banner Tools

# function List For type attacks

    def xssBug():
        Page_clear()
        sys('neofetch')
        Dominput = input(Fore.RED+'┌─{'+Fore.GREEN+'DOMIN'+Fore.YELLOW+'~'+Fore.BLUE+'IP'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        xs3 = sys('nmap --script=http-xssed '+str(Dominput))
        print(xs3)

    def sqlinjections():
        Page_clear()
        sys('neofetch')
        Dominput = input(Fore.RED+'┌─{'+Fore.GREEN+'DOMIN'+Fore.YELLOW+'~'+Fore.BLUE+'IP'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        sqlattacks = sys('nmap --script=http-sql-injection '+str(Dominput))
        print(sqlattacks)

    def WordpressBrute():
        Page_clear()
        sys('neofetch')
        Dominput = input(Fore.RED+'┌─{'+Fore.GREEN+'DOMIN'+Fore.YELLOW+'~'+Fore.BLUE+'IP'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        wb = sys('nmap --script=http-wordpress-brute '+str(Dominput))
        print(wb)

    def userName_Wordpress():
        Page_clear()
        sys('neofetch')
        Dominput = input(Fore.RED+'┌─{'+Fore.GREEN+'DOMIN'+Fore.YELLOW+'~'+Fore.BLUE+'IP'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        username_w = sys('nmap --script=http-wordpress-users '+str(Dominput))
        print(username_w)

    def WordpressE():
        Page_clear()
        sys('neofetch')
        Dominput = input(Fore.RED+'┌─{'+Fore.GREEN+'DOMIN'+Fore.YELLOW+'~'+Fore.BLUE+'IP'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        enum = sys('nmap --script=http-wordpress-enum '+str(Dominput))
        print(enum)

    def siteMap():
        Page_clear()
        sys('neofetch')
        Dominput = input(Fore.RED+'┌─{'+Fore.GREEN+'DOMIN'+Fore.YELLOW+'~'+Fore.BLUE+'IP'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        sitemap = sys('nmap --script=http-sitemap-generator '+str(Dominput))
        print(sitemap)

    def DnsB():
        Page_clear()
        sys('neofetch')
        Dominput = input(Fore.RED+'┌─{'+Fore.GREEN+'DOMIN'+Fore.YELLOW+'~'+Fore.BLUE+'IP'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        dnsbrute = sys('nmap --script=dns-brute '+str(Dominput))
        print(dnsbrute)

    def systemInfo():
        Page_clear()
        sys('neofetch')
        Dominput = input(Fore.RED+'┌─{'+Fore.GREEN+'DOMIN'+Fore.YELLOW+'~'+Fore.BLUE+'IP'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        systemI = sys('nmap -A -O -sS -V -v -S -sn -oA -Pn '+str(Dominput))
        print(systemI)

    def Port():
        Page_clear()
        sys('neofetch')
        Dominput = input(Fore.RED+'┌─{'+Fore.GREEN+'DOMIN'+Fore.YELLOW+'~'+Fore.BLUE+'IP'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)
        port = sys('nmap -p- '+str(Dominput))
        print(port)

    def Selects_tools(): # Select the tool in the options displayed

        selects = int(input(Fore.RED+'┌─['+Fore.GREEN+'Webcyber'+Fore.YELLOW+'~'+Fore.BLUE+'SCANNER WEB'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))

        if selects == 1:
            xssBug()

        elif selects == 2:
            sqlinjections()

        elif selects == 3:
            WordpressBrute()

        elif selects == 4:
            userName_Wordpress()

        elif selects == 5:
            WordpressE()

        elif selects == 6:
            siteMap()

        elif selects == 7:
            DnsB()

        elif selects == 8:
            systemInfo()

        elif selects == 9:
            Port()

        else:
             selects < 9
             sys('python3 webcyber.py')

    Selects_tools() # Run selects Tools

except KeyboardInterrupt: # For cont + C

    print(Fore.BLUE+'\n\nTanks :)')

except ValueError: # For ValueError

    print(Fore.BLUE+'\n\nError\nYou had to choose the number of options displayed')
    sleep(6)
    sys('python3 webcyber.py') # Reloads File script