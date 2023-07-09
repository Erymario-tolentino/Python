# Crie um programa que leia m numero Real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção interia e {}'.format(num , int(num)))