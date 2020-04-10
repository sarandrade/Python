# Desafios 114

import requests

try:
    r = requests.get('http://pudim.com.br/')
except:
    print('\033[31mO site Pudim não está acessível no momente.\033[m')
else:
    print('\033[32mO site Pudim está acessível no momente.\033[m')
    print(r.text)