# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por eles vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moedaEx109 
p = float(input('Digite o preço: R$'))
print(f'A metade de {moedaEx109.moeda(p)} é  {moedaEx109.metade(p , True)}')
print(f'A dobro de {moedaEx109.moeda(p)} é {moedaEx109.dobro(p , True)} ')
print(f'Aumentando 10%, temos {moedaEx109.aumentar(p , 10 , True)}')
print(f'Reduzindo 13%, temos {moedaEx109.diminuir(p , 13 , True)}')