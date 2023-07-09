# Crie um código em Python que teste se o site pudim está acessivel pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com/webhp?hl=pt-PT&sa=X&ved=0ahUKEwiB-ZmU1v__AhVF1gIHHSXZCdoQPAgI')
except:
    print('O site GOOGLE não está acessível no momento.')
else:
    print('consegui acessar o site GOOGLE com sucesso!')
    print(site.read())