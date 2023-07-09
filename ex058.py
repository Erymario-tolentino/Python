# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um numero entre 0 e 10.So que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios vencer.

from random import randint
computador = randint( 0 , 10 )
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou :
    jogador = int(input('Qual e sua palpite? '))
    palpites += 1
    if jogador == computador :
        acertou = True
    else:
        if jogador < computador :
            print('MAIS... Tente mais uma vez.')
        else:
            print('MENOS...Tente mais uma vez.')
print('Acertou com {} palpites.PARABENS'.format(palpites))
