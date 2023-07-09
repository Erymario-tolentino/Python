# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacento de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = hypot(co , ca)
print('A hipoteusa vai medir {:.2f}'.format(hi))