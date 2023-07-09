# Crie um programa que vai gerar cinco numeros aletorios e colocar em uma tupla. Depois disso, mostre a listagem de numeros gerados e tambem e indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint( 1 , 10), randint( 1 , 10) , randint( 1 , 10) , randint( 1 , 10) , randint( 1 , 10))
print('Os valores sorteados foram : ', end=' ')
for n in numeros :
    print(f'{n} ' , end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')