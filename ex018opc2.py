# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
from math import radians , sin , cos , tan
angulo = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo , seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo , cosseno))
targente = tan(radians(angulo))
print('O angulo de {} tem a TARGENTE de {:.2f}'.format(angulo , targente))
