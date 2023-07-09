# A condefederação nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade <= 9 :
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19: 
    print('Classificação: JUNIOR')
elif idade <= 25 :
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
