# Faça um programa que leia o ano de nascimento de um joveme informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se e a hora de se alistar ou seja passou do tempo do alistamento.
# Seu programa tambem devera mostrar o tempo que falta ou que passou so prazo.
  
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} em {}'.format(nasc , idade , atual)) 
if idade == 18 :
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18 :
    saldo = 18 - idade
    print('Ainda faltaram {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera {}'.format(ano))
elif idade > 18 :
    saldo = 18 - idade
    print('Voce ja deveria ter se alistado ha {} anos.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento foi em {}'.format(ano))
