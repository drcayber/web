# Lib list for projects

from time import sleep
from colorama import Fore
from os import system as sys
from platform import uname as um
import requests


try: # For Error V,K

  def Page_clear(): # function Clear Data Terminal

    Data_clear = um()[0]

    if Data_clear == 'Linux':
      sys('clear')

  Page_clear() # Run function in Terminal


  def Data_page(): # Show Data Scripts in Terminal

    sys('neofetch')
    print(Fore.GREEN+'\n\n                                         CYBER VIRTUAL \n\n')

  Data_page() # Run function Data Script

  def Domin(): # function Domin For attacks
    print(Fore.YELLOW+'['+Fore.RED+'!'+Fore.YELLOW+']'+Fore.LIGHTCYAN_EX+' Please Do Not Include Https\n\n')
    DOMINinput = input(Fore.RED+'┌─{'+Fore.GREEN+'VIRTUAL SOURCE'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'DOMIN'+Fore.RED+Fore.RED+'}'+'\n└──╼> '+Fore.WHITE)

    Page_clear() # Reloading For data
    Data_page() # Reloading For data

    for i in range(10):

      url = requests.get('https://'+DOMINinput+'/')



      if url.status_code == 200:

            print(Fore.YELLOW+'{'+Fore.GREEN+'Packet Send '+Fore.RED+'!'+Fore.YELLOW+'}\n')

      if i == 9:
            break

    url = requests.get('https://google.com')
    use = url.text


    file = open('body.html', 'w')
    file.write(use)
    file.close()
    print('')
    print(Fore.RED+'['+Fore.WHITE+'!'+Fore.RED+']'+Fore.LIGHTGREEN_EX+'SAVED FILE CODE HTML\n')

  Domin()

except KeyboardInterrupt: # For Cont + c
  print(Fore.BLUE+'\n\nTanks :)\n\n')
except ValueError: # For ValueError
  print(Fore.MAGENTA+'\n\n[!] You did not enter any data\n\n')
  sleep(4)
  sys('python3 webcyber.py') # Reloads File

