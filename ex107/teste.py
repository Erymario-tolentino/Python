# crie um modulo chamadao moeda.py que tenha as funções incorporadas aumentar(), dimunuir(), dobra() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é  R${moeda.metade(p)}')
print(f'A dobro de {p} é R${moeda.dobro(p)} ')
print(f'Aumentando 10%, temos R${moeda.aumentar(p , 10)}')