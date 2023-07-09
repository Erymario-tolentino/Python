# Escreva um programa um que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentaar descobrir qual foi o numero escolhido pelo computador.O programa devera escrever na tela se o usuario venceu ou perdeu
from random import randint
from time import sleep
print('-=' *30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar')
print('-=' *30)
jogador = int(input('Em que numero entre 0 e .5 Tente adivinhar: '))
computador = randint(0 , 5)
print('processando...')
sleep(3)
if computador == jogador:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e não no {}'.format(computador , jogador))
