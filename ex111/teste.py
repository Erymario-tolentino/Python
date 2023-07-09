# Crie um pacote chamado utilidadesceV que tenha dois módulos internos chamados moeda e dado.Transfira todas as funções utilizadas nos desafios 107 , 108 e 109 para o primeiro pacote e mantenha tudo funcionado.


from utilidadesceV import moeda  as md
p = float(input('Digite o preço: R$'))
md.resumo(p , 20 , 12)
