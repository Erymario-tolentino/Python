# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# EX: 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
n = int(input('Digite um numero para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} e {}.'.format(n , f))
