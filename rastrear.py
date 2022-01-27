#modulos
import argparse
import requests, json
import sys
from sys import argv
import os

#argumentos

parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target')
args = parser.parse_args()

#cores
red = '\033[1;31m'
yellow = '\033[1;93m'
lgreen = '\033[1;92m'
clear = '\033[0m'
bold = '\033[1;01m'
cyan = '\033[1;96m'

#baner do script
print (red+ bold + """
█▀▀█ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀ █▀▀█ █▀▀█       ░▀░ ░ █▀▀█
█▄▄▀ █▄▄█ ▀▀█ ░░█░░ █▄▄▀ █▀▀ █▄▄█ █▄▄▀       ▀█▀ ▄ █░░█
▀░▀▀ ▀░░▀ ▀▀▀ ░░▀░░ ▀░▀▀ ▀▀▀ ▀░░▀ ▀░▀▀       ▀▀▀ █ █▀▀▀
                                                          v 1.0
""")
print(red)
print (cyan+bold+"                 <===[[ By: Miguel ]]===> \n"+clear)

ip = args.target
api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[I.P]:", data['query'])
        print(red+"<--------------->"+red)
        print (a, "[Chip]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[Cidade]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Estado]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[Longitude]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[Latitude]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Fuso horário]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[Código de área:]:", data['zip'])
        print (" "+yellow+bold)
        print("ESPERO QUE TENHA GOSTADO!")
except KeyboardInterrupt:
        print ('Terminating, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" Verifique sua internet!"+clear)
sys.exit(1)
